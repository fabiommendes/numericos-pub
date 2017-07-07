# -*- coding: utf-8 -*-
''' Questão 1 - Considere o sistema matricial abaixo

        |1  2|*|X| = |0|
        |2  2| |Y| = |1|

b) Resolva este sistema utilizando a eliminação de Gauss com pivoteamento.
'''
import numpy as np

matriz = np.array([[1,2],[2,2]])
vetor = np.array([0,1])

def pivoteamento(matriz, posicaoPivo):
    #recebe a matriz a ser realizado o pivoteamento e qual coluna deve ser analisada
    #Retorna matriz com o maior índice da coluna no pivo
    indiceMaior = 0
    indice = 0

    #procura o maior e menor pivo para serem trocados
    for i in matriz:
        if abs(i[posicaoPivo]) > abs(indiceMaior):
            indiceMaior = indice
        indice += 1
        
    #verifica se o maior módulo encontrado na coluna já não é o pivô, caso contrário troca as linhas
    if indiceMaior > posicaoPivo:
        aux = np.copy(matriz[indiceMaior])
        matriz[indiceMaior] = np.copy(matriz[posicaoPivo])
        matriz[posicaoPivo] = np.copy(aux)
    
    return matriz



def resolver_gauss(M, v):    
    m = len(M)
    
    #Cria Matriz extendida de floats
    v = np.asarray(v, dtype='float')
    M = np.hstack([M, v[:, None]])
    
    #Realizar pivoteamento de M
    M = pivoteamento(M, 0)

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