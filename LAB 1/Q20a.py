#Representing graph by using a dictionary

Btree={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
for node in Btree:
    print(f"{node} -> {Btree[node]}")