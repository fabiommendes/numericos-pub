import numpy as np

pi = np.pi
V = 350

# Define função e derivadas
def f(r):
    return 2*pi*r * (r + V / (pi*r**2)) 

def f_(r):
    return 4*pi*r - 2*V/r**2
    
def f__(r):
    return 4*pi + 4*V/r**3
    
# Executa método de newton
r = 100
for i in range(20):
    r = r - f_(r) / f__(r)
    
# Mostra o resultado
print('   r:', r)
print('f(r):', f(r))
