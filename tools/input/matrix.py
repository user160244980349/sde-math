

def matrix(n, m, s):
    mat = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        row = input().strip().split(s)
        
        if len(row) > n:
            raise BoundExceedError()
        
        for j in range(n):
            mat[i][j] = int(row[j])

    return mat


class BoundExceedError(Exception):
    pass
