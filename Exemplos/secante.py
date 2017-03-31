# Pede informações para o usuário
print('Método de Secante: cálculo da raiz quadrada')
z = float(input('Valor do argumento: '))
n_iter = int(input('Número de iterações: '))


# Executa o método de Newton
x_prev = 0.5
x = 2.5
y_prev = x_prev**2 - z
y = x**2 - z
for i in range(n_iter):
    x_prox = (x_prev * y - x * y_prev) / (y - y_prev)
    y_prox = x_prox**2 - z
    x, x_prev = x_prox, x
    y, y_prev = y_prox, y
    
    
# Imprime o resultado
print('Raiz quadrada:', x)

