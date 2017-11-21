# Álgebra linear + EDOs

Teste 1: 16/11

Existem várias aplicações numéricas que podem ser mapeadas em problemas de 
álgebra linear com matrizes muito grandes e dominantes na diagonal. Considere,
por exemplo, a equação diferencial abaixo

    y''(x) - y(x) = sqrt(x)

pode ser transformada no problema de álgebra linear abaixo:

    | b0   1    0    0    0    0    0  |   | y1 |   | sqrt(x0) - y0 |
    | 1    b1   1    0    0    0    0  |   | y2 |   | sqrt(x1)      |
    | 0    1    b2   1    0    0    0  |   | y3 |   | sqrt(x2)      |
    | 0    0    1    b3   1    0    0  | x | y4 | = | sqrt(x3)      |
    |                  ...             |   | .. |   |      ...      |
    |                       ...        |   | .. |   |      ...      |
    | 0    0    0    0    0    1    bn |   | yn |   | sqrt(x6) - yf |


(não se preocupem com os detalhes de como é feito)


Onde definimos `x_i = h * i`, `b = -2 - h**2` e y0 e yf são os valores iniciais e
finais de y(x). h é o passo da simulação e determina a resolução da solução. 

Instruções:

1. Crie a lista de x's partindo de x0 = 0 até xf = 10 com h = 1e-3 (consulte a 
   função arange() do numpy.)
2. Crie a matriz M acima
3. Crie o vetor b do lado direito do sistema linear
4. Utilize um método iterativo para resolver o sistema linear
5. Faça um gráfico do resultado (vetor y como função do vetor x)