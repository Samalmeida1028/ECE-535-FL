import matplotlib.pyplot as plt

fig,ax = plt.subplots()

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
    data1.append(linein[7])
    data2.append(linein[8])
    data3.append(linein[9])

# for i in range((3*len(data1))):
#     yticksa.append(round(i/(3*len(data1)),2))

ax.plot(timestamp, data1)
ax.plot(timestamp, data2)
ax.plot(timestamp, data3)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.yticks(['0','0.5','1.0'])
# plt.ylim(ymax=1)
# ax.set_yticks(['0', '.5', '1.0'])
# ax.set_yscale('linear')
# ax.set_yticklabels(['0','.5','1.0'],fontsize=5)
plt.autoscale('both')
# ax.set_yt
# ax.set_autoscaley_on(True)
plt.title('Graph from text file')
plt.show()