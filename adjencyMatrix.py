import random
def generateGraph(n, d):
    expected_edges = (d*n*(n-1))/2
    current_edges = n
    matrix = [[0 for i in range(n)] for j in range(n)]
    random_hamilton_cycle = [i for i in range(n)]
    # losowa permutacja zbioru wierzcholkow zeby stworzyc cykl hamiltona w grafie
    random.shuffle(random_hamilton_cycle)
    random_hamilton_cycle.append(random_hamilton_cycle[0])
    for i in range(n):
        matrix[random_hamilton_cycle[i]][random_hamilton_cycle[i+1]] = 1
        matrix[random_hamilton_cycle[i+1]][random_hamilton_cycle[i]] = 1
        
    random_hamilton_cycle.pop()
    while current_edges < expected_edges:
        u, v, w = random.sample(random_hamilton_cycle, 3)
        if not matrix[u][v] and not matrix[u][w] and not matrix[v][w]:
            matrix[u][v] = 1
            matrix[v][u] = 1
            matrix[u][w] = 1
            matrix[w][u] = 1
            matrix[v][w] = 1
            matrix[w][v] = 1
            current_edges += 3
    return matrix