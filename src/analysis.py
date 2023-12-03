import matplotlib.pyplot as plt

with open("results/ur_fall/ablation/rgb_depth/A30_B30_AB0_label_A_test_B/results.txt", 'r') as f:
    datas1 = f.readlines()
with open("results/opp/dccae/acce_gyro/A10_B0_AB30_label_A_test_B/results.txt", 'r') as f:
    datas2 = f.readlines()
with open("results/mhealth/ablation/gyro_mage/A30_B30_AB0_label_A_test_B/results.txt", 'r') as f:
    datas3 = f.readlines()

sets = [('UmFL_URFall_A30_B30_AB0_LA_TB',datas1),('MmFL_Opp_A10_B0_AB30_LA_TB',datas2),('UmFL_mHealth_A30_B30_AB0_LA_TB',datas3)]
timestamp = []
data1 = []
data2 = []
data3 = []
yticksa = []

for data in sets:
    plt.figure(data[0])

    for line in data[1]:
        linein = line.strip().split(sep=",")
        timestamp.append(float(linein[0]))
        data1.append(linein[7:])

    for j in range(len(data1[0])):
        plot_data = []
        for i in data1:
            plot_data.append(float(i[j]))
        plt.plot(timestamp,plot_data)

    plt.xlabel('Training Round')
    plt.ylabel('Accuracy')

    plt.yticks([0, 0.5, 1.0], ['0', '0.5', '1.0'])
    plt.legend(['Class 0', 'Class 1', 'Class 2'])

    plt.title(data[0])

    timestamp.clear()
    data1.clear()
    data2.clear()
    data3.clear()

plt.show()