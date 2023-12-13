import matplotlib.pyplot as plt
import os
import json

directory = "acc_results"
dist_directory = "distributions"

for filename in os.listdir(directory):
    # plt.figure(filename)
    fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(15, 5))
    test_path = os.path.join(dist_directory,"test_dist_"+filename[7:])
    train_path = os.path.join(dist_directory,"train_dist_"+filename[7:])
    perclass_path = os.path.join(directory,filename)
    with open(perclass_path, "r") as f:
        graph_data = json.load(f)
    classes = graph_data[list(graph_data)[0]]
    run_num = []
    for i in range(len(classes[list(classes)[0]])):
        run_num.append((2*i)-1)
        legend = []
    count = 0
    for key in classes:
        datac = classes[key]
        legend.append(key)
        line, = ax1.plot(run_num,datac)
        graph_data = {}
        with open(test_path, "r") as f:
            graph_data = json.load(f)
        graphkey = str(list(graph_data)[0])
        # print(graph_data[graphkey])
        ax2.bar(graph_data["trained classes"][count],graph_data["class counts"][count],width=.7,label=graph_data[graphkey],color = line.get_color())


        graph_data = {}
        with open(train_path, "r") as f:
            graph_data = json.load(f)
        graphkey = str(list(graph_data)[0])
        # print(graph_data[graphkey])
        ax3.bar(graph_data["trained classes"][count],graph_data["class counts"][count],width=.7,label=graph_data[graphkey],color = line.get_color())
        count += 1

    ax1.set_title("Per Class Accuracy")
    ax2.set_title("Test Distribution")
    ax3.set_title("Train Distribution")
    fig.suptitle(graph_data[graphkey])
    # ax1.legend(legend,loc="center right")
    # ax2.legend(legend, loc="center right")
    # ax3.legend(legend, loc="center right")
    fig.legend(legend,loc="right")
    fig.savefig("acc_plots/"+filename+".png")
    
    

plt.show()



# sets = [('UmFL_URFall_A30_B30_AB0_LA_TB',datas1),('MmFL_Opp_A10_B0_AB30_LA_TB',datas2),('UmFL_mHealth_A30_B30_AB0_LA_TB',datas3)]
# timestamp = []
# data1 = []
# data2 = []
# data3 = []
# yticksa = []

# for data in sets:
#     plt.figure(data[0])

#     for line in data[1]:
#         linein = line.strip().split(sep=",")
#         timestamp.append(float(linein[0]))
#         data1.append(linein[7:])

#     for j in range(len(data1[0])):
#         plot_data = []
#         for i in data1:
#             plot_data.append(float(i[j]))
#         plt.plot(timestamp,plot_data)

#     plt.xlabel('Training Round')
#     plt.ylabel('Accuracy')

#     plt.yticks([0, 0.5, 1.0], ['0', '0.5', '1.0'])
#     plt.legend(['Class 0', 'Class 1', 'Class 2'])

#     plt.title(data[0])

#     timestamp.clear()
#     data1.clear()
#     data2.clear()
#     data3.clear()

# plt.show()