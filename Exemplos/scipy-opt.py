import numpy as np


def newton(f, x0, e=1e-6, derivada=None):
    """
    Calcula o extremo da função f(x) utilizando o método
    de Newton.
    
    Args:
        f: função objetivo
        x0: chute inicial
        derivada (opcional): derivada de f(x)
    """
    
    # Define derivada 1a
    if derivada is None:
        def f_(x):
            return (f(x + e) - f(x)) / e
    else:
        f_ = derivada
        
    # Define derivada 2a
    def f__(x):
        return (f_(x + e) - f_(x)) / e
    
    x = x0
    for i in range(20):
        x = x - f_(x) / f__(x)
    return x


# Mostra o resultado
r = newton(np.sin, -1, derivada=np.cos)
print('   r:', r)
print('f(r):', np.sin(r))
