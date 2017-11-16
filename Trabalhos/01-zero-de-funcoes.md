# Zero de funções

Teste 1: 16/11

A função de Lambert W(x) é definida implicitamente pela equação:

    x = W exp W
    
onde apenas valores x > 0 são aceitos. Implemente a função W(x) em Python 
tratando-a como a solução de um problema de zero de funções.

Instruções:

1. Dado um x, o valor de W é obtido resolvendo um problema de zero de funções.
2. A sua função deve recusar valores de x negativos (você pode levantar um erro 
   com `raise ValueError` para sinalizar entradas inválidas).
3. Sua função deve **retornar** o resultado de W(x) e não imprimí-lo na tela
   (use `return W` ao invés de `print(W)`).
4. Você pode utilizar o método numérico que achar mais adequado.
5. Existe uma implementação da W de Lambert em `scipy.special.lambertw` e você
   pode utilizá-la para testar seu código. Obviamente a sua resposta não
   pode utilizar esta implementação!
6. O valor de W(x) está sempre entre 0 e x.
7. Consiga um resultado com pelo menos 2 casas decimais de precisão.
