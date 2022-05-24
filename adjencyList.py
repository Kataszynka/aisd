def matrixToAdjList(matrix):
    """
    Transform adjency matrix to adjency list
    """
    n = dict()
    for i in range(0, len(matrix)):
        r = []
        for j in range(0, len(matrix)):
            if(matrix[i][j] == 1):
                r.append(j)
        n[i]= r
    return n
