"""
Code Python de décomposition LU
Zakaria Choukri
Algèbre 2
UM6P-CS

"""

"""
exemple 1:   n = 2

[4  3]  =  [1    0] [4   3  ]
[6  3]     [1.5  1] [0  -1.5]

"""

"""
exemple 2:   n = 3

[2  -3  1 ]     [ 1  0  0] [2  -3   1]
[-2  2  -3]  =  [-1  1  0] [0  -1  -2]
[4  -9  -2]     [ 2  3  1] [0   0   2]

"""
# A = [[4, 3], [6, 3]]                            # exemple de matrice A d'ordre 2
A = [[2, -3, 1], [-2, 2, -3], [4, -9, -2]]      # exemple de matrice A d'ordre 3
n = len(A)                                      # ordre des matrices
L = [[0 for i in range(n)] for i in range(n)]   # la matrice L (initialisée à 0)
U = [[0 for i in range(n)] for i in range(n)]   # la matrice U (initialisée à 0)

for i in range(n):
    for k in range(n):
        
        if i == k == 0:
            U[i][k] = A[i][k]
        
        elif i == 0 and k != 0:
            U[i][k] = A[i][k]
        
        elif i != 0 and k == 0:
            L[i][k] = A[i][k]/U[0][0]

for i in range(n):
    for k in range(n):
        for m in range(1,n):
            
            if k >= m:
                temp = 0
                for j in range(m):
                    temp += L[m][j] * U[j][k]
                U[m][k] = A[m][k] - temp
            
            elif i >= m:
                temp = 0
                for j in range(m):
                    temp += L[i][j] * U[j][m]
                L[i][m] = (A[i][m] - temp)/U[m][m]

for i in range(n):
    L[i][i] = 1

print("A =", A)
print("L =", L)
print("U =", U)