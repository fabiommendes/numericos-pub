# Minimização

Entrega: 16/11

(Este teste será entregue no mesmo dia da aplicação do teste 01, que será 
realizado de forma presencial).


A série de dados abaixo foi gerada por uma função senoidal do tipo `sin(w t)`,
onde o valor da frequência angular w é desconhecido: 

    ys = [ 0.2493938 ,  0.72091586,  1.08935177,  0.82557285,  0.15184373,
          -0.55819513, -0.84832015, -1.13075724, -0.66132559, -0.37482053,
           0.49910671,  0.99533713,  0.97493417,  0.56770796, -0.59740919,
          -0.76333201, -1.05362856, -0.8085086 , -0.32029816,  0.4021104 ]

Estes dados foram obtidos nos valores de tempo abaixo:

    ts = [   0.        ,    5.26315789,   10.52631579,   15.78947368,
            21.05263158,   26.31578947,   31.57894737,   36.84210526,
            42.10526316,   47.36842105,   52.63157895,   57.89473684,
            63.15789474,   68.42105263,   73.68421053,   78.94736842,
            84.21052632,   89.47368421,   94.73684211,  100.        ]

A função de erro quadrático é dada pelo somatório de 
    
    $$EQ(w) = \sum_i \left( \sin(w t_i) - y_i \right)^2$$

Podemos propor o melhor valor de w como aquele que minimiza o erro quadrático
EQ(w). Você deve criar um problema de mínimo de funções que encontre o melhor 
valor para w. 

Instruções:


1. Utilize um método para encontrar o mínimo de funções para obter uma 
   estimativa para  a constante w. Você pode escolher o método que achar mais 
   apropriado (Newton, Busca ternária, Tangente, etc)
2. Você deve implementar o método de minimização e não pode utilizar funções já 
   prontas no scipy. É lógico que estas funções podem ser úteis para conferir
   se a a sua implementação está correta.
3. Este é um problema de minimização não-linear e portanto pode fornecer vários
   valores de mínimos locais. Rode o programa várias vezes com diferentes chutes 
   iniciais e escolha a resposta que forneça o menor valor de EQ(w)
4. É sempre interessante fazer um gráfico da solução para verificar se a 
   resposta obtida faz algum sentido. Utilize o gráfico para tentar encontrar
   um "chute" inicial adequado para w0.
5. O valor de EQ(w) para o mínimo global está próximo de 0.
