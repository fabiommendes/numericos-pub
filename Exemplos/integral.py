import numpy as np

# Alguns integrandos
def f1(x):
    return np.exp(x)

def f2(x):
    return 2 * np.sqrt(1 - x**2 + 1e-15)
    

# Salvamos o resultado analitico como um atributo 
# da funcao
f1.resp = np.exp(1) - np.exp(-1)
f2.resp = np.pi


# Regras de quadratura
def midpoint(f, i):
    return f(a + dx/2 + i * dx) * dx

def trapezio(f, i):
    xi = a + i * dx
    xf = xi + dx
    return dx * (f(xi) + f(xf)) / 2

def simpson(f, i):
    x1 = a + i * dx
    x2 = x1 + dx / 2
    x3 = x1 + dx
    return dx * (f(x1) + 4 * f(x2) + f(x3)) / 6


# Intervalo de integraçao e regra de quadratura
f = f2
a, b = -1, 1
quad = simpson


# Avalia a precisao das integrais para varios
# valores de N
for N in [2, 4, 10, 20, 50, 100, 1000, 10000]:
    dx = (b - a) / N
    S1 = sum(quad(f1, i) for i in range(N))
    S2 = sum(quad(f2, i) for i in range(N))
    err1 = abs(S1 - f1.resp)
    err2 = abs(S2 - f2.resp)
    print('%5s) Erro: %.2e/%.2e' % (N, err1, err2))



