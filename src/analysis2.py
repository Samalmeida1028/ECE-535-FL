import matplotlib.pyplot as plt
import os
import json

directory = "C:/Users/expre/OneDrive/Desktop/ece535 project/ECE-535-SLAM/acc_results"



for filename in os.listdir(directory):
    print(filename)
    plt.figure(filename)
    file_path = os.path.join(directory,filename)
    with open(file_path, "r") as f:
        graph_data = json.load(f)
    classes = graph_data[list(graph_data)[0]]
    run_num = []
    for i in range(len(classes[list(classes)[0]])):
        run_num.append((2*i)-1)
        legend = []
    for key in classes:
        datac = classes[key]
        legend.append(key)
        plt.plot(run_num,datac)
    plt.xlabel('Training Round')
    plt.ylabel('Accuracy')
    plt.yticks([0, 0.5, 1.0], ['0', '0.5', '1.0'])
    plt.legend(legend)
    plt.title(filename[8:-4])
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