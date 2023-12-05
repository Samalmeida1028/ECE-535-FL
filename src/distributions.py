import matplotlib.pyplot as plt
import os
import json

directory = "distributions"

count = 0
for filename in os.listdir(directory):
    print(count)
    graph_data = {}
    file_path = os.path.join(directory,filename)
    with open(file_path, "r") as f:
        graph_data = json.load(f)
    graphkey = str(list(graph_data)[0])
    print(graph_data[graphkey])
    plt.figure(graph_data[graphkey])
    
    
    plt.bar(graph_data["trained classes"],graph_data["class counts"],width=.7,color='b',)
    plt.title(graph_data[graphkey])
plt.show()