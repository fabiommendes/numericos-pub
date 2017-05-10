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
    e um vetor e retorna a solução x correspondente
    
        Mx = y,
    
    onde M é a matrix fornecida e y é um vetor.
    """
    
    # Cria a matriz extendida, convertendo-a para float
    M =  np.hstack([matrix, y[:, None]]).astype(float)
    
    # Escalona a matriz M modificando-a na função
    escalonate(M)
    
    # Normaliza os pivos para 1, modificando a matriz
    # M na função
    normalize_pivot(M)
    
    # Resolve o sistema triangular superior
    return solve_upper(M[:, 0:-1], M[:, -1])
    
    
def escalonate(M):
    """
    Modifica a matriz M até atingir a forma triangular
    superior. (escalonamento)
    """
    
    n = len(M)
    
    for k in range(0, n - 1):
        # Pivoteamento: reordenar as linhas para que o
        # pivo seja o maior possível em módulo
        m = np.argmax(abs(M[k:, k])) + k
        if m != k:
            M[m], M[k] = M[k].copy(), M[m].copy()            
        
        # Escalonamento: realiza combinaçoes lineares
        # entre as linhas para zerar os termos abaixo
        # do pivo
        pivot = M[k, k]
        for i in range(k + 1, n):
            M[i] = M[i] - (M[i, k] / pivot) * M[k]

def normalize_pivot(M):
    """
    Normaliza os pivos da matriz
    """
    for i in range(len(M)):
        norm = M[i, i]
        if norm == 0:
            raise ValueError('matriz singular')
        M[i] /= norm
    
def solve_upper(M, y):
    """
    Resolve um sistema linear superior normalizado.
    """
    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(M[i] * x)
    return x
    
 
