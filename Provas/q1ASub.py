# -*- coding: utf-8 -*-
''' Questão 1 - Considere o sistema matricial abaixo

        |1  2|*|X| = |0|
        |2  2| |Y| = |1|

a) Resolva este sistema utilizando a eliminação de Gauss sem pivoteamento.
'''
import numpy as np

matriz = np.array([[1,2],[2,2]])
vetor = np.array([0,1])

def resolver_gauss(M, v):    
    m = len(M)
    
    #Cria Matriz extendida de floats
    v = np.asarray(v, dtype='float')
    M = np.hstack([M, v[:, None]])
    
    #Escalona matriz
    for k in range(m - 1):
        pivo = M[k, k]
        for i in range(k + 1, m):
            M[i] = M[i] - M[i, k] / pivo * M[k]

    #Normaliza pivos
    for k in range(m):
        M[k] = M[k] / M[k, k]
        
    #Resolve sistema triangular superior
    x = np.zeros(m)
    for k in reversed(range(m)):
        x[k] = M[k, m] - sum(M[k, 0:m] * x)
    return x

resposta = resolver_gauss(matriz, vetor)

print('X = '+str(resposta[0]))
print('Y = '+str(resposta[1]))