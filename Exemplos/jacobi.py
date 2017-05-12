import numpy as np


def rmatrix(n, A=0):
    M = np.matrix(np.random.normal(size=[n,n]))
    return M + np.diag(A * np.ones(n))
    

def alphas(M):
    alphas = []
    for k, linha in enumerate(M):
        linha = abs(linha) 
        diag = linha[0, k]
        alpha_k = (np.sum(linha) - diag) / diag
        alphas.append(alpha_k)
    return np.array(alphas)
        
N = 3   
M = rmatrix(N, 10)
alpha_max = alphas(M).max()
print('alpha_max:', alpha_max)

if alpha_max > 1:
    raise SystemExit('Matriz diverge!')

D = np.matrix(np.diag(np.diag(M)))
Dinv = np.matrix(np.diag(1.0 / np.diag(M)))
R = M - D
x = np.matrix([[.0]] * N)
x_ok = np.matrix(np.random.normal(size=[N, 1]))
y = M * x_ok

for i in range(10):
    x = Dinv * (y - R * x)
    print(abs(x - x_ok).sum())
    












