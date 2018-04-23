#Implementation of Bellman-Ford Algoritm
import sys
def bellManFord(source_node, nodes, edges):
	inf, num_vert = sys.maxsize, len(nodes)
	nodeCosts = {node:inf for node in nodes}
	prevNodes = {node:None for node in nodes}
	nodeCosts[source_node] = 0
	for i in range(num_vert):
		for from_v, to_v, cost in edges:
			if nodeCosts[from_v] + cost < nodeCosts[to_v]:
				prevNodes[to_v] = from_v
				nodeCosts[to_v] = nodeCosts[from_v] + cost
				if(i == num_vert - 1):
					print("Negative Cycle!")
					break
	return nodeCosts, prevNodes

#Example Usage
source_node = "S"
nodes = ["S","A","B","C","D","E"]
edges = [("S","E",8), ("E","D",1), ("D","C",-1), ("C","B",-2),
			("B","A",1), ("S","A",10), ("D","A",-4), ("A","C",-2)]
print(bellManFord(source_node, nodes, edges))