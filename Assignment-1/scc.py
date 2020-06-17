
#########--------------- Code to find strongly connected components in a graph --------------#########

# Importing required modules

from datetime import datetime

# Importing data from the file

startTime = datetime.now()

with open("SCC.txt") as scc:
    vertices = []
    connections = []
    for line in scc:
        data = line.split()
        if len(data) > 1:
            vertices.append(data[0])
            connections.append(data[1])

print(len(vertices))
print(len(connections))

print(f"Total time taken to load file = {datetime.now() - startTime}")