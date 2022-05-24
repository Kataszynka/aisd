def findFirstHamiltonianPath(adj_list, n):
    
    def hamiltonianPaths(adj_list, v, visited, path, n):
        if len(path) == n:
            return True
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                path.append(w)
                
                if hamiltonianPaths(adj_list, w, visited, path, n):
                    return True
                
                visited[w] = False
                path.pop()

    start = 0
    path = [start]
    visited = [False] * n
    visited[start] = True
    hamiltonianPaths(adj_list, start, visited, path, n)
    path.append(start)
    return path