import adjencyMatrix, adjencyList, eulerian_cycle, hamilton_first
import time, sys
from copy import deepcopy
sys.setrecursionlimit(100_000_000)


print("Podaj ilosc wierzcholkow ")
wierzcholki = int(input())
graph = [[0 for i in range(wierzcholki)] for j in range(wierzcholki)]
print("Podaj ilosc krawedzi ")
krawedzie = int(input())
for i in range(krawedzie):
    print("Podaj krawedz ")
    u = int(input())
    v = int(input())
    graph[u][v] = 1
    graph[v][u] = 1

[print(g) for g in graph]

adj_list = adjencyList.matrixToAdjList(graph)
eulerian_cycle.find_euler_cycle(deepcopy(adj_list), 0, [])


print(hamilton_first.findFirstHamiltonianPath(adj_list, wierzcholki))