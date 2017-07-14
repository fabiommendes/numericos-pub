<style>
@media only print {
    body {
        font-size: 0.75em;
        margin-left: 4.5%;
        margin-right: 4.5%;
    }
    h2 {page-break-before: always;}
    h2.first {page-break-before: avoid	;}
}
.wide { 
    height: 50em;
}
</style>


# Segunda Prova de Métodos Numéricos

<center>
Data: 05/07/2017
Professor: Fábio Macêdo Mendes/Turma A
</center>


**Nome:**

**Matrícula:**

***
### Observações

* A prova é **individual e sem consulta**, sendo vedado o uso de telefones celulares.
* A interpretação dos enunciados faz parte da avaliação.
* O computador do laboratório pode ser utilizado **exclusivamente** para acessar o Jupyter ou implementar os programas numéricos necessários para a realização da prova.
***


<h2 class="first">Q1. Matrizes (1,0 pts)</h2>
Considere o sistema matricial abaixo

$$
\begin{bmatrix}
1 & 2\\
2 & 2
\end{bmatrix} 
\times
\begin{bmatrix}
x\\
y
\end{bmatrix} 
=\begin{bmatrix}
0\\
1
\end{bmatrix} 
$$

e responda às questões:

a) (0,5) Resolva este sistema utilizando a eliminação de Gauss *sem* pivoteamento.
## Resposta:
Escalonando a matriz abaixo:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|1  2 = 0|
|2  2 = 1
</pre>
</center>

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|1  2 = 0|
|2  2 = 1|
</pre>
</center>

Obtém-se a seguinte matriz:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|1  2  = 0|
|0 -2  = 1|
</pre>
</center>

Logo, temos o sistema:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
1X + 2Y = 0
0X - 2Y = 1
</pre>
</center>

Isolando y, temos:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
y = -0,5
</pre>
</center>

Sunstituindo Y e Isolando X, temos:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
x = 1
</pre>
</center>

b) (0,5) Resolva este sistema utilizando a eliminação de Gauss *com* pivoteamento.
## Resposta:
Pivoteando a matriz abaixo:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|1  2 = 0|
|2  2 = 1|
</pre>
</center>

Obtém-se:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|2  2 = 0|
|1  2 = 0|
</pre>
</center>

Escalonando a matriz pivoteada, obtém-se:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
|2  2 = 1|
|0 -2 = 1|
</pre>
</center>

Logo, temos o sistema:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
2X + 2Y = 1
0X - 2Y = 1
</pre>
</center>

Isolando y, temos:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
y = -0,5
</pre>
</center>

Sunstituindo Y e Isolando X, temos:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
x = 1
</pre>
</center>

## Q2. Aproximações (3,0 pts)

Considere o conjunto de pontos abaixo e responda às questões

<center>

|   x   | 0   | 1   | 2   |
|:-----:|-----|-----|-----|
|  f(x) | 2   | 1   | 3   |

</center>

a) (1,0) Calcule o polinômio interpolador utilizando o método que achar mais adequado.
## Resposta
Utilizando o método de Lagrange
Sendo:
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
<center>
$${P}_{2}(X) = {Y}_{0}*{L}_{0}(X) + {Y}_{1}*{L}_{1}(X) + {Y}_{2}*{L}_{2}(X)$$
</center>
</pre>

Então temos L0:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{0}(X) = \dfrac{(X-{X}_{1})*(X-{X}_{2})}{({X}_{0}-{X}_{1})*({X}_{0}-{X}_{2})}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{0}(X) = \dfrac{(X-1)*(X-2)}{(0-1)*(0-2)}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{0}(X) = \dfrac{{X}^{2}-3*X+2}{2}$$
</pre>
</center>

L1:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{1}(X) = \dfrac{(X-{X}_{0})*(X-{X}_{2})}{({X}_{1}-{X}_{0})*({X}_{1}-{X}_{2})}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{1}(X) = \dfrac{(X-0)*(X-2)}{(1-0)*(1-2)}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{1}(X) = -{X}^{2}+2*X$$
</pre>
</center>

L2:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{2}(X) = \dfrac{(X-{X}_{0})*(X-{X}_{1})}{({X}_{2}-{X}_{0})*({X}_{2}-{X}_{1})}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{2}(X) = \dfrac{(X-0)*(X-1)}{(2-0)*(2-1)}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
${L}_{2}(X) = \dfrac{{X}^{2}-X}{2}$$
</pre>
</center>

Logo, temos o polinomio:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${P}_{2}(X) = 2*\dfrac{{X}^{2}-3*X+2}{2}+(-{X}^{2}+2*X)+3*\dfrac{{X}^{2}-X}{2}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${P}_{2}(X) = \dfrac{3*{X}^{2}}{2}-\dfrac{5*X}{2} + 2$$
</pre>
</center>


b) (1,0) Utilize a regra de Simpson para encontrar uma aproximação da integral 
da função no intervalo de 0 até 2. O resultado é o mesmo da integral analítica
realizada com o polinômio interpolador?
## Resposta

Resolvendo pela Regra de Simpson, com h=1:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{s} = \dfrac{h}{3}*[f({X}_{0})+4*f({X}_{1})+f({X}_{2})]$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{s} = \dfrac{1}{3}*[2+4+3]$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{s} = 3$$
</pre>
</center>

Resolvendo de forma analítica:
<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$\int_{0}^{2} \dfrac{3*{X}^{2}}{2}-\dfrac{5*X}{2}+2 $$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$\left. \dfrac{3*{X}^{3}}{6} - \dfrac{5*{X}^{2}}{4} + 2*X\right|_{0}^{2}$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$(\dfrac{3*{2}^{3}}{6} - \dfrac{5*{2}^{2}}{4} + 2*2) - \dfrac{3*{0}^{3}}{6} - \dfrac{5*{0}^{2}}{4} + 2*0 = 3$$
</pre>
</center>

Concluindo que tanto analiticamente quanto pela regra de simpson chega-se à 3

c) (1,0) Calcule a aproximação utilizando a regra do trapézio composta nos
pontos dados. O resultado é o mesmo?
## Resposta

Pela regra do trapézio com h=1:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{T} = \dfrac{h}{2}*[f({X}_{0})+f({X}_{1})]+\dfrac{h}{2}*[f({X}_{1})+f({X}_{2})]$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{T} = \dfrac{h}{2}*[f({X}_{0})+2*f({X}_{1})+f({X}_{2})]$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{T} = \dfrac{1}{2}*[2+2+3]$$
</pre>

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${I}_{T} = 3,5$$
</pre>
</center>

O valor, apesar de ser próximo, não é o mesmo que os encontrados na letra B

## Q3. Tableau de Runge Kutta (2,0 pts)

O método RK4 é definido pelo tableau

<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
 0.0 |
 0.5 | 0.5
 0.5 |  0   0.5
 1.0 |  0    0   1.0
-----+--------------------
     | 1/6  1/3  1/3  1/6
</pre>

Considere o problema de segunda ordem 

    $$x''(t) + x'(t) + x(t) = 0$$

de valor inicial $x(0) = 1, x'(0) = 0$

a) (0,5) Converta a EDO acima em um sistema de primeira ordem.

## Resposta

Calculando a derivada da função:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$\dfrac{{d}^{2}X}{d{t}^{2}} + \dfrac{dX}{dt} + X = 0$$
</pre>
</center>

E temos X(0) e X'(0):

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$X(0) = 1$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$X'(0) = 0$$
</pre>
</center>

Então é possível obter o sistema:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$u => \dfrac{dX}{dt} = v$$
$$u => \dfrac{dv}{dt} = -X - v$$
</pre>
</center>

b) (1,5) Realize a primeira iteração do método RK4 para as condições iniciais 
dadas e com um passo temporal de $\tau = 1/3$.

## Resposta

Sabendo que:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$X(0) = 1 => {X}_{0}=1$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$v(0) = 0 => {v}_{0}=0$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$$h = \dfrac{1}{3}$$
</pre>
</center>

Encontramos os K e os L da regra de range kutta:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${K}_{0} = h*F({X}_{0}, {v}_{0}) = \dfrac{1}{3}*0 = 0$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{0} = h*g({X}_{0}, {v}_{0}) = \dfrac{1}{3}*(-1-0) = -\dfrac{1}{3}$$
</pre>
</center>

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${K}_{1} = h*F({X}_{0}+\dfrac{1}{2}*{K}_{0}, {v}_{0}+\dfrac{1}{2}*{L}_{0}) = \dfrac{1}{3}*(0+(-\dfrac{1}{6})) = -\dfrac{1}{18}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{1} = h*g({X}_{0}+\dfrac{1}{2}*{K}_{0}, {v}_{0}+\dfrac{1}{2}*{L}_{0}) = \dfrac{1}{3}*(-1+(\dfrac{1}{6})) = -\dfrac{5}{18}$$
</pre>
</center>

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${K}_{2} = h*F({X}_{0}+\dfrac{1}{2}*{K}_{1}, {v}_{0}+\dfrac{1}{2}*{L}_{1}) = \dfrac{1}{3}*(-\dfrac{5}{36})) = -\dfrac{5}{108}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{2} = h*g({X}_{0}+\dfrac{1}{2}*{K}_{1}, {v}_{0}+\dfrac{1}{2}*{L}_{1}) = \dfrac{1}{3}*(-\dfrac{35}{36}-(-\dfrac{5}{36})) = -\dfrac{5}{18}$$
</pre>
</center>

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${K}_{3} = h*F({X}_{0}+{K}_{2}, {v}_{0}+{L}_{2}) = \dfrac{1}{3}*(-\dfrac{5}{18}) = -\dfrac{5}{54}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${L}_{3} = h*g({X}_{0}+{K}_{2}, {v}_{0}+{L}_{2}) = \dfrac{1}{3}*(-\dfrac{103}{108}+(\dfrac{5}{18})) = -\dfrac{75}{324}$$
</pre>
</center>

Logo, temos:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{1} = {X}_{0}+\dfrac{1}{6}*({k}_{0}+2*{k}_{1}+2*{k}_{2}+{k}_{3}) = \dfrac{77}{81}$$
</pre>
</center>

## Q4. Método de Newton (2,0 pts)

Calcule o máximo da função $f(x) = x exp(x)$ numericamente utilizando o método
de Newton. Você deve começa no ponto inicial $x=0$ e realizar o número de 
iterações necessário para que a solução possua 2 casas de precisão.

## Reposta
Temos o F'(x):
$$f'(X) = -{e}^{-X}*(X-1)$$

E o F''(x):
$$f''(X) = {e}^{-X}*(X-2)$$	

Com X0 = 0, temos X1:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{1} = {X}_{0}-\dfrac{f'({X}_{0})}{f''({X}_{0})}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{1} = 0-\dfrac{1}{-2}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{1} = \dfrac{1}{2}$$
</pre>
</center>

Com X1 = 1/2, temos X2:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{2} = {X}_{1}-\dfrac{f'({X}_{1})}{f''({X}_{1})}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{2} = 0,5-\dfrac{0,30326}{-0,90979}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{2} = 0,8333$$
</pre>
</center>

Com X2 = 0,8333, temos X3:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{3} = {X}_{2}-\dfrac{f'({X}_{2})}{f''({X}_{2})}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{3} = 0,8333-\dfrac{0,07244}{-0,50706}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{3} = 0,9761$$
</pre>
</center>

Com X3 = 0,9761, temos X4:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{4} = {X}_{3}-\dfrac{f'({X}_{3})}{f''({X}_{3})}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{4} = 0,9761-\dfrac{0,00900}{-0,38578}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{4} = 0,9994$$
</pre>
</center>

Com X4 = 0,9994, temos X5:

<center>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{5} = {X}_{4}-\dfrac{f'({X}_{4})}{f''({X}_{4})}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{5} = 0,9994-\dfrac{0,00022}{-0,36832}$$
</pre>
<pre style="padding: 1em; width: 16em; margin: 1em auto; font-size: 1em">
$${X}_{5} = 0,9999$$
</pre>
</center>

Logo, podemos atribuir X = 0.99 com duas casas de precisão


## Q5. Raízes de funções (2,0 pts)

A função $W(x)$ é definida implicitamente pela solução da equação $x = W \exp{W}$. Utilize o método de busca de raízes de funções para obter uma estimativa do valor
de W(1) com 2 casas de precisão.