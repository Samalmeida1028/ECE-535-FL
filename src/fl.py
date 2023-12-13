import os
import copy
import torch
import math
import numpy as np
import json
import re

from server import Server
from client import Client
from utils import load_data, split_server_train, client_idxs
from pathlib import Path


class FL:
    def __init__(self, config, is_mpi=False, rank=0):
        self.config = config
        self.is_mpi = is_mpi
        self.rank = rank
        self.num_clients_A = int(self.config["FL"]["num_clients_A"])
        self.num_clients_B = int(self.config["FL"]["num_clients_B"])
        self.num_clients_AB = int(self.config["FL"]["num_clients_AB"])
        self.results_path = self.config["SIMULATION"]["results_path"]
        self.rounds = int(self.config["FL"]["rounds"])
        self.eval_interval = int(self.config["FL"]["eval_interval"])

    def start(self):
        """Starts the FL communication rounds between the server and clients."""

        # Loads the training and testing data of the FL simumation
        data_name, data_train, data_test = load_data(self.config)

        client_train = data_train
        server_test = data_test

        y_samples = np.expand_dims(data_test["y"], axis=0) # true labels for classes
        y_samples_train = np.expand_dims(data_train["y"], axis=0) # true labels for classes
        extra_length = len(np.unique(y_samples))

        y_dist= np.unique(y_samples, return_counts=True)
        y_dist_train = np.unique(y_samples_train, return_counts=True)
        last_slash_index = self.results_path.find("/")
        typemodle = self.results_path[last_slash_index+1:]
        typemodle = re.sub('/','_',typemodle)
        data_name+=typemodle

        test_dist = {"name": data_name ,"trained classes": y_dist[0].tolist(),"class counts" : y_dist[1].tolist()}
        train_dist = {"name": data_name,"trained classes": y_dist_train[0].tolist(),"class counts" : y_dist_train[1].tolist()}
        run_acc = {}

        try:
            with open("/media/sf_ece535_project/ECE-535-SLAM/distributions/test_dist_" + data_name + ".txt", 'w') as f:
                f.write(json.dumps(test_dist))
        except Exception as e:
            print(e, "creating file")
            with open("/media/sf_ece535_project/ECE-535-SLAM/distributions/test_dist_" + data_name + ".txt", 'x') as f:
                f.write(json.dumps(test_dist))

        try:
            with open("/media/sf_ece535_project/ECE-535-SLAM/distributions/train_dist_" + data_name + ".txt", 'w') as f:
                f.write(json.dumps(train_dist))
        except Exception as e:
            print(e, "creating file")
            with open("/media/sf_ece535_project/ECE-535-SLAM/distributions/train_dist_" + data_name + ".txt", 'x') as f:
                f.write(json.dumps(train_dist))

        # There is a small chance that the labels in the generated server_train are fewer than the labels in server_test.
        # If that happens, regenerate the server_train again until the sets of lables between them are the same.
        while True:
            server_train_A = split_server_train(data_train, self.config)
            if set(server_train_A["y"]) == set(server_test["y"]):
                break
        while True:
            server_train_B = split_server_train(data_train, self.config)
            if set(server_train_B["y"]) == set(server_test["y"]):
                break

        server = Server(server_train_A, server_train_B, self.config)
        server.init_models()

        # Generates sample indices for each client
        client_train_idxs = client_idxs(client_train, self.config)
        n_clients = len(client_train_idxs)
        clients = []

        modalities = ["A" for _ in range(self.num_clients_A)] + ["B" for _ in range(
            self.num_clients_B)] + ["AB" for _ in range(self.num_clients_AB)]
        for i in range(n_clients):
            clients.append(
                Client(client_train, client_train_idxs[i], modalities[i], self.config))

        n_eval_point = math.ceil(self.rounds / self.eval_interval)
        # result table: round, local_ae_loss, train_loss, train_accuracy, test_loss, test_accuracy, test_f1
        result_table = np.zeros((n_eval_point, 7 + extra_length))
        result_table[:, 0] = np.arange(1, self.rounds+1, self.eval_interval)
        row = 0

        for t in range(self.rounds):
            print(f"Round {t+1} starts")
            selected_clients = server.select_clients(clients)
            local_models = []

            # Local update on each selected client
            for client in selected_clients:
                local_model, client_weight, local_ae_loss = client.update(
                    copy.deepcopy(server.global_ae))
                local_models.append(
                    (copy.deepcopy(local_model), client.modality, client_weight))

            # Cloud update on the server
            train_loss, train_accuracy = server.update(local_models)

            # Cloud evaluation
            if t % self.eval_interval != 0:
                continue
            else:
                with torch.no_grad():
                    test_loss, test_accuracy, test_f1, perclassaccuracy = server.eval(
                        server_test,data_name)
                    
                result_table[row, 0:7] = np.array(
                    (t+1, local_ae_loss, train_loss, train_accuracy, test_loss, test_accuracy, test_f1))

                row += 1
                dataset_name = str(list(perclassaccuracy)[0])

                if not len(run_acc):
                    run_acc = perclassaccuracy
                    #print(run_acc)
                else:
                    for key in run_acc[dataset_name]:
                        values = run_acc[dataset_name][key]
                        if(type(values) is list):
                            values.append(perclassaccuracy[key])
                        else:
                            values = [values] + [perclassaccuracy[key]]
                        run_acc[dataset_name].update({key:values})
                #print(run_acc)
                try:
                    with open("/media/sf_ece535_project/ECE-535-SLAM/acc_results/result_" + data_name + ".txt", 'w') as f:
                        f.write(json.dumps(run_acc))
                except Exception as e:
                    print(e, "creating file")
                    with open("/media/sf_ece535_project/ECE-535-SLAM/acc_results/result_" + data_name + ".txt", 'x') as f:
                        f.write(json.dumps(run_acc))
                        
                self.write_result(result_table)

    def write_result(self, result_table):
        """ Writes simulation results into a result.txt file

        Args:
            result_table: a 2-d numpy array contraining rows of simulation results
        """
        if self.is_mpi:
            results_path = os.path.join(self.results_path, f"rep_{self.rank}")
        else:
            results_path = self.results_path
        Path(results_path).mkdir(parents=True, exist_ok=True)
        np.savetxt(os.path.join(results_path, "results.txt"),
                   result_table, delimiter=",", fmt="%1.4e")
