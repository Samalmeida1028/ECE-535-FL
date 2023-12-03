import matplotlib.pyplot as plt

plt.figure(1)

with open("results/ur_fall/ablation/rgb_depth/A30_B30_AB0_label_A_test_B/results.txt", 'r') as f:
    data = f.readlines()

timestamp = []
data1 = []
data2 = []
data3 = []
yticksa = []

for line in data:
    linein = line.strip().split(sep=",")
    timestamp.append(float(linein[0]))
    data1.append(float(linein[7]))
    data2.append(float(linein[8]))
    data3.append(float(linein[9]))

plt.plot(timestamp, data1)
plt.plot(timestamp, data2)
plt.plot(timestamp, data3)

plt.xlabel('Training Round')
plt.ylabel('Accuracy')

plt.yticks([0, 0.5, 1.0], ['0', '0.5', '1.0'])
plt.legend(['Class 0', 'Class 1', 'Class 2'])

plt.title('UmFL_A30_B30_LA_TB')
plt.show()