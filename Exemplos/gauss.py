"""
Eliminação de Gauss.

1) Cria matriz estendida
2) Converte matriz estendida em triangular superior
3) Normaliza os pivôs para 1 
4) Resolve a matriz triangular normalizada

"""
import numpy as np


def solve(matrix, y):
    """
    Resolve um sistema linear dado por uma matriz
    e um vetor.
    """
    M = extended_matrix(matrix, y).astype(float)
    print('extendida')
    print(M)
    upper_triangular(M)
    print('escalonamento')
    print(M)
    normalize_pivot(M)
    print('normalizacao')
    print(M)
    return solve_upper(M[:, 0:-1], M[:, -1])
    
def extended_matrix(matrix, y):
    """
    Retorna a matriz extendida pelo vetor v.
    """
    return np.hstack([matrix, y[:, None]])
    
def upper_triangular(M):
    """
    Modifica a matriz M até atingir a forma triangular
    superior. (escalonamento)
    """
    # só para matrizes 2 x 2!
    pivot = M[0, 0]
    M[1] = M[1] - (M[1, 0] / pivot) * M[0]

def normalize_pivot(M):
    """
    Normaliza os pivos da matriz
    """
    for i in range(len(M)):
        M[i] /= M[i, i]
    
def solve_upper(M, y):
    """
    Resolve um sistema linear superior normalizado.
    """
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(M[i] * x)
    return x
    
        
### testa funcoes
matrix = np.array([
    [2, 1, 0], 
    [0, 0, 2],
    [3, 1, 0],
])
y = np.array([0, 84, 1])
  
print(solve(matrix, y))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
