# Pede informações para o usuário
print('Método de Newton: cálculo da raiz quadrada')
z = float(input('Valor do argumento: '))
n_iter = int(input('Número de iterações: '))


# Executa o método de Newton
x = 1
for i in range(n_iter):
    x = x - (x**2 - z) / (2 * x)
    
# Imprime o resultado
print('Raiz quadrada:', x)

