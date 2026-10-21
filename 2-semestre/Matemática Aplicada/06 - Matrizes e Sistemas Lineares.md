---
materia: "Matemática Aplicada"
modulo: "Matrizes e Sistemas Lineares"
semestre: 2
unidade: 6
tipo: material-teorico
fonte: "raw/2-semestre/MATEMÁTICA APLICADA/Matemática Aplicada 06.pdf"
tags: [faculdade, matematica-aplicada, semestre-2]
aliases: ["Matemática Aplicada - Unidade 6"]
---

# Matrizes e Sistemas Lineares

Responsáveis pelo Conteúdo: Profa. Ms. Adriana Domingues Freitas Profa. Dra. Jussara Maria Marins Revisão Textual: Profa. Dra. Selma Aparecida Cesarin

- **Matriz**

- **Elementos das Diagonais**

- **Classificação de Matrizes**

- **Operações Basicas com Matrizes**

- **Sistemas Lineares**

## Objetivos de Aprendizado

- Identificar os diferentes tipos de matriz;

- Realizar operações: soma, subtração e multiplicação entre matrizes;

- Calcular os determinantes de matrizes quadradas de ordem n ≤ 3;

- Reconhecer situações que envolvam sistemas lineares;

- Utilizar os métodos Cramer e Gauss para a resolução de sistemas lineares possíveis e determinados.

### Matriz

Define-se por Matriz de m · n a um conjunto de m · n (lê-se m por n) elementos que são dispostos em m linhas e n colunas.

Os elementos que compõem uma determinada matriz são representados por uma letra minúscula acompanhada dos índices i (que representa a linha na qual o elemento está posicionado) e j (que representa a coluna na qual o elemento está posicionado); a matriz nós representamos por uma letra maiúscula.

Vejamos um exemplo: temos a seguir uma matriz 3 · 3 que denominaremos matriz A.

Veja a estrutura da matriz com os índices i (linhas) e j (colunas):

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

E, na sequência, a matriz já com os valores numéricos que, nesse caso, foram estipulados de forma aleatória, somente para exemplificar uma matriz com valores numéricos:

$$A = \begin{pmatrix} 6 & 2 & 0 \\ -1 & -3 & 1 \\ 3 & 5 & 8 \end{pmatrix}$$

Os elementos da matriz são localizados pelos dois índices: **i** (linha) e **j** (coluna).

A matriz A3x3 possui os seguintes elementos:

a11 = 6; a12 = 2; a13 = 0.

```
a21 = -1; a22 = -3; a23 = 1.
a31 = 3; a32 = 5; a33 = 8.
```

O elemento a32 = 5 é elemento que está localizado na 3ª linha e na 2ª coluna.

### Elementos das Diagonais

Chamamos de Diagonal Principal (P) a diagonal da matriz quadrada composta pelos elementos aij, onde i = j, isto é, no caso de uma matriz quadrada de ordem 3, a diagonal principal será composta pelos elementos de posição: a11, a22 e a33.

Já a Diagonal Secundária (S) é a diagonal composta pelos elementos aij, onde i + j = n + 1; no caso da matriz quadrada de ordem 3, a diagonal secundária será composta pelos elementos a31, a22 e a13.

![[ma2-06-fig05.webp]]

*Figura 1 – Diagonais de uma matriz quadrada 3x3*

Em uma matriz quadrada de ordem 2, as diagonais principais e secundárias serão compostas da seguinte forma:

Diagonal Principal, elementos a11 e a22.

Diagonal Secundária, elementos a12 e a21.

![[ma2-06-fig06.webp]]

*Classificação de Matrizes*

As matrizes são classificadas de acordo com o número de linhas e colunas.

- Matriz linha: quando temos uma matriz m = 1, composta por uma única linha;

- Matriz coluna: quando temos uma matriz n = 1, composta por uma única coluna;

- Matriz nula: quando temos uma matriz cujos elementos são todos iguais a zero;

- Matriz quadrada: trata-se da matriz m · n, na qual m = n, ou seja, igual número de linhas e colunas. Importante destacar que em toda matriz m · n quadrada temos duas diagonais que são chamadas: diagonal principal e diagonal secundária;

- Matriz triangular superior: quando temos uma matriz quadrada n · n, na qual todos os elementos a seguir da diagonal principal são nulos.

Nesta Unidade, o estudo da matriz quadrada é importante, pois a utilizaremos no cálculo do determinante e na solução de sistemas lineares.

### Operações Básicas com Matrizes

#### Soma e Subtração de Matrizes

Considerando duas matrizes A = (aij)mxn e B = (bij)mxn, a matriz C = (cij)mxn será a matriz soma, das matrizes A + B, na qual os elementos cij serão obtidos por cij = aij + bij.

##### Importante!

**Importante!**

Cada elemento cij da matriz soma C será o resultado da soma entre os elementos correspondentes de A e B. Chamamos de correspondentes os termos que possuírem os mesmos índices ij.

Ou seja, associamos, por meio da soma, os elementos que possuem o mesmo índice:

![[ma2-06-fig07.webp]]


**Importante!**

A soma ou subtração de matrizes somente ocorre entre matrizes de mesma ordem, ou seja, o número de linhas de uma matriz deve ser igual ao número de linhas da outra matriz, assim como o número de colunas.

###### Exemplos

$$\begin{aligned} &A = \begin{pmatrix} -2 & 1 & 3 \\ 0 & 2 & 1 \end{pmatrix} \ e \ B = \begin{pmatrix} -1 & 3 & 4 \\ 2 & -2 & 1 \end{pmatrix} \ e \ A + B = \begin{pmatrix} -3 & 4 & 7 \\ 2 & 0 & 2 \end{pmatrix} \\ &C = \begin{pmatrix} 1 & 2 & -3 \\ 4 & 5 & -2 \\ 2 & 4 & 7 \end{pmatrix} \ e \ D = \begin{pmatrix} 0 & 1 & 3 \\ 4 & 3 & 4 \\ -2 & -3 & -5 \end{pmatrix} \ e \ C + D = \begin{pmatrix} 1 & 3 & 0 \\ 8 & 8 & 2 \\ 0 & 1 & 2 \end{pmatrix} \end{aligned}$$

$$A = \begin{pmatrix} -2 & 1 & 3 \\ 0 & 2 & 1 \end{pmatrix} + C = \begin{pmatrix} 1 & 2 & -3 \\ 4 & 5 & -2 \\ 2 & 4 & 7 \end{pmatrix} \ \text{Soma de A + C não é possível}$$

*Multiplicação de Matrizes*

Dadas duas matrizes A = (aij)mxn e B = (bij)mxn,  a multiplicação entre as matrizes A e B gerará uma nova matriz C na qual:

Todo elemento cij é calculado multiplicando-se ordenadamente os elementos da linha i, da matriz A, pelos elementos da coluna j, da matriz B, e somando-se os produtos obtidos.

Para dizer que a matriz C é o produto de A por B, vamos indicá-la por AB.

Só definimos o produto AB de duas matrizes quando o número de colunas da matriz A for igual ao número de linhas de B. Além disso, notamos que a matriz produto AB possui o número de linhas de A e o número de colunas de B.

Assim, se tivermos uma matriz A3x2 e uma matriz B3x3 não teremos o produto AB, visto que o número de colunas de A não é igual ao número de colunas de B. Porém, se tivermos uma matriz A3x3 e uma matriz B3x3, o produto entre as matrizes se dará da forma que se expõe a seguir.

Importante! **Importante!**

A multiplicação entre duas matrizes A e B só ocorre se o número de colunas da matriz A for igual ao número de linhas da matriz B.

Para realizar a multiplicação, associaremos os termos da linha 1 (da primeira matriz) com a coluna 1 (da segunda matriz); posteriormente, os termos da linha 1, com a coluna 2, e na sequência os termos da linha 1 com a coluna 3.

Após finalizar a associação dos termos da linha 1 com todas as colunas, repetiremos o processo com as demais linhas.

![[ma2-06-fig08.webp]]

- **a11* b11** + **a12* b21** + **a13* b31** a11* b12+ a12* b22+a13* b32 a11* b13+ a12* b23+a13* b33

- C= a21* b11+ a22* b21+a23* b31 a21* b12+ a22* b22+a23* b32 a21* b13+ a22* b23+a23* b33 a31* b11+ a32* b21+a33* b31 a31* b12+ a32* b22+a33* b32 a31* b13+ a32* b23+a33* b33

Importante! **Importante!**

Note que cada termo da linha a1n vai multiplicar um termo na coluna bn1, e faremos a soma dos produtos, obtendo o c11 = a11* b11 + a12* b21 + a13* b31.

Para o cálculo de c12, procederemos da mesma forma; porém, cada termo da linha a1j vai multiplicar um termo da coluna bi2 e teremos c12 = a11* b12 + a12* b22 + a13* b32. E assim sucessivamente também para as demais linhas.

###### Exemplo

Dadas duas matrizes A3x3 e B3x2:

$$A = \begin{pmatrix} 2 & 3 & 1 \\ 0 & 1 & 2 \\ 3 & 5 & 1 \end{pmatrix} \ e \ B \begin{pmatrix} 1 & 2 \\ 2 & 3 \\ -1 & 1 \end{pmatrix}$$

Inicialmente, devemos verificar se a multiplicação (produto) entre A*B é possível. Nesse caso, temos que o produto entre A e B é possível, vez que a condição para a existência do produto entre duas matrizes, de que o número de colunas da matriz A é igual ao número de linhas da matriz B, está contemplada.

Assim, a matriz C=A.B será obtida por:

$$A * B = \begin{pmatrix} 2*1 + 3*2 + 1*(-1) & 2*2 + 3*3 + 1*1 \\ 0*1 + 1*2 + 2*(-1) & 0*2 + 1*3 + 2*1 \\ 3*1 + 5*2 + 1*(-1) & 3*2 + 5*3 + 1*1 \end{pmatrix} = C = \begin{pmatrix} 7 & 14 \\ 0 & 5 \\ 12 & 22 \end{pmatrix}$$

*Determinantes de Matrizes Quadradas até Ordem 3*

Uma matriz quadrada tem, associado a ela, um número real chamado determinante da matriz (Det), obtido por meio de operações que envolvem os elementos da matriz.

Nesta Disciplina, estudaremos os determinantes para matrizes de ordem 1, ordem 2 e ordem 3.

###### Determinante de Matriz Quadrada de Ordem 1

Para matriz quadrada de ordem 1, indicada por A = [a11] , por definição, o determinante da matriz será igual ao número do elemento de posição a11.

###### Exemplo

Seja a matriz A = [5], o determinante de A será det A = 5.

Seja a matriz B = [-2], o determinante de B será det B = 2.

###### Determinante da Matriz Quadrada de Ordem 2

Para as matrizes quadradas de ordem 2, calculamos o determinante fazendo o produto dos elementos da diagonal principal menos o produto dos elementos da diagonal secundária.

###### Exemplo

Calcularemos o determinante da matriz $M = \begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}$.

##### Importante!

O determinante será calculado da seguinte forma: do produto da diagonal principal subtraímos o produto da diagonal secundária.

D = produto da diagonal principal: 2*4 = 8

S = produto da diagonal secundária 3*1 = 3

P – S = 8 – 3 = 5. Logo, det(M) = 5

###### Determinante da Matriz Quadrada de Ordem N = 3

Existem alguns procedimentos para o cálculo do determinante das matrizes quadradas de ordem 3. Um deles, chamado de REGRA DE SARRUS, consiste em copiar as duas primeiras colunas da matriz original:

$$A = \begin{pmatrix} 1 & 1 & 5 \\ 1 & 0 & -2 \\ 2 & 4 & -3 \end{pmatrix}$$

Copiando novamente a matriz e incluindo, após a terceira coluna, novamente as duas primeiras colunas, teremos:

$$\begin{matrix} 1 & 1 & 5 & 1 & 1 \\ 1 & 0 & -2 & 1 & 0 \\ 2 & 4 & -3 & 2 & 4 \end{matrix}$$

Da matriz quadrada A3x3, teremos, agora, uma nova matriz que possui três diagonais de três elementos no sentido da diagonal principal e três diagonais no sentido das diagonais secundárias.

A seguir, somamos os produtos obtidos nas três diagonais principais e dessa soma subtrairemos a soma dos três produtos obtidos nas três diagonais secundárias.

![[ma2-06-fig09.webp]]

*Figura 3 – Cálculo do determinante da matriz de ordem 3 – Regra de Sarrus*

Das diagonais principais (P), temos: 0 – 4 + 20 = 16.

Das diagonais secundárias (S), temos: 0 – 8 – 3 = -11.

Logo, da soma dos produtos das diagonais principais, subtrairemos a soma dos produtos das diagonais secundárias, ou seja, P – S:

16 – (-11) = 16 + 11 = 27

Det(A) = 27

O determinante será a soma dos produtos das diagonais principais com o oposto da soma dos produtos das diagonais secundárias.

### Sistemas Lineares

Quando temos um problema que envolve mais de uma variável e mais de uma equação, de modo que estão vinculadas, então temos um sistema de equações. Por exemplo, se temos as equações E1 3x + 2y = 16 e E2 4x − 3y = 20, temos um sistema, que é, usualmente, indicado por chaves no início:

3x + 2y =16

4x -3x = 10

Outro exemplo de sistema de equações, com três variáveis (x, y e z), com três equações, é dado por:

x + y + 3z= 9 -3x +2y -6z = -14 4x – 5z = 11

Um Sistema de Equações Lineares é um conjunto finito de equações, todas elas nas mesmas incógnitas, que devem ser satisfeitas, simultaneamente.

Uma solução de um sistema linear é uma sequência ordenada de números tais que as substituições das variáveis, por esses números, transformem todas as equações do sistema em identidades verdadeiras.

Resolver um sistema é determinar todas as soluções (sistemas possíveis) ou, ainda, provar que não existe nenhuma (sistemas impossíveis).

É importante considerar que, nesta Disciplina, estudaremos os métodos para resolução de “sistemas lineares possíveis e determinados”, ou seja, sistemas que admitem uma única solução; porém, vale observar que em outras situações, que não trataremos aqui, podemos nos deparar com sistemas lineares possíveis e indeterminados, pois apresentam infinitas soluções e ainda sistemas lineares impossíveis, que não admitem soluções.

Os métodos que estudaremos a seguir são: Método de Cramer e Método de Gauss.

#### Método de Cramer

É o método que envolve o cálculo de determinantes para a resolução de sistemas matriciais.

Considere o sistema a seguir:

2x + 1y = 3

$$1x - 3y = -2$$

A partir desse sistema, nós construiremos uma equação matricial, na qual os coeficientes de x e y serão os elementos de uma matriz A e os resultados do sistema serão elementos de outra matriz B, conforme a figura 4. Note que do produto matricial A*X = B nos permite escrever o sistema como uma equação matricial.

$$\begin{aligned} &\begin{cases} 2x + 1y = 3 \\ 1x - 3y = -2 \end{cases} \\ &A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix} \quad X = \begin{bmatrix} x \\ y \end{bmatrix} \quad B = \begin{bmatrix} 3 \\ -2 \end{bmatrix} \end{aligned}$$

*Figura 4 – Equação Matricial*

A seguir, calcularemos os determinantes das matrizes chamados de: det A, det Ax e det Ay.

Para calcular det Ax, basta trocar os elementos da primeira coluna da matriz A (que correspondem aos coeficientes de x), pelos elementos que compõem a matriz B.

Da mesma forma, para calcular o valor do det Ay, basta trocar os elementos da segunda coluna da A (que correspondem aos coeficientes de y) pelos elementos que compõem a coluna da matriz B, como vemos na figura a seguir:

$$\begin{aligned} A &= \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix} \quad \det A = [(2.(-3))] - [1.(1)] = -6 - 1, \ \det A = -7 \\ \text{Det } A_x &= \begin{bmatrix} 3 & 1 \\ -2 & -3 \end{bmatrix} \quad \det A_x = [(3.(-3))] - [1.(-2)] = -9 + 2, \ \det A_x = -7 \\ \text{Det } B_x &= \begin{bmatrix} 2 & 3 \\ 1 & -2 \end{bmatrix} \quad \det A_y = [(2.(-2))] - [3.(1)] = -4 - 3, \ \det A_y = -7 \end{aligned}$$

*Figura 5 – Cálculo dos determinantes*

Os valores de x e y para a solução do sistema serão calculados por:

$$\begin{aligned} x &= \frac{\det A_x}{\det A} \\ y &= \frac{\det A_y}{\det A} \end{aligned}$$

Logo, os valores de x e y serão:

$$\begin{aligned} x &= \frac{\det A_x}{\det A} = \frac{-7}{-7} = 1 \\ y &= \frac{\det A_y}{\det A} = \frac{-7}{-7} = 1 \end{aligned}$$

Portanto, a solução de nosso sistema será x = 1 e y = 1.

Se tivermos um sistema cuja matriz seja quadrada de ordem três, resolveremos det A , det Ax , det Ay e det Az que deverão ser calculados conforme vimos na Regra de Sarrus e os valores de x, y e z será, respectivamente:

$$\begin{aligned} x &= \frac{\det A_x}{\det A} \\ y &= \frac{\det A_y}{\det A} \\ z &= \frac{\det A_z}{\det A} \end{aligned}$$

*Método de Gauss*

Outro método utilizado na resolução de sistemas lineares é o método de Gauss que consiste em transformar o sistema linear original S em um sistema linear equivalente, que chamaremos de S’, mas de forma escalonada, ou com matriz triangular superior.

Os sistemas equivalentes são sistemas que admitem uma mesma solução; por vezes, é mais prático trabalhar com sistemas equivalentes que permitem soluções mais rápidas e menos trabalhosas.

Como vimos, um sistema equivalente ao outro é sobretudo um sistema cuja solução é a mesma do sistema original.

Por exemplo: quando temos a equação 2x + 6 = 18, temos como solução o valor de x = 6. Podemos obter uma equação equivalente a 2x + 6 = 18 realizando qualquer operação nessa equação, desde que façamos a operação para todos os elementos da equação.

Se dividirmos todos os coeficientes da equação 2x + 6 = 18 por 2 , teremos uma nova equação que será x + 3 = 9. Podemos observar que a solução dessa equação continua sendo x = 3, ou seja, 2x + 6 = 18 e x + 3 = 9 são equivalentes.

Importante! **Importante!**

Multiplicando-se os membros de uma equação E qualquer de um sistema linear S por um número K≠0, o novo sistema S’ obtido será equivalente a S.

Por exemplo, o sistema S é equivalente aos sistemas S’ e S’’:

|Sistema S|Sistema S’|Sistema S”|
|---|---|---|
|2x + y = 5|2x + y = 5|6x + 3y = 15|
|-x +3y = 1|-2x+6y = 2|3x - 9y = -3|

Note que a diferença de S’ para S é que a segunda equação E2 em S’ é o dobro da E2 em S. Também devemos notar que em S”, a equação 1, ou seja, a E1, é o triplo da E1 de S, mas são todos sistemas equivalentes, cuja solução é x = 2 e y = 1.

Outra transformação importante: “se substituirmos uma equação E de um sistema linear S, pela soma membro a membro (isto é, de seus respectivos coeficientes e variáveis) dela com outra, o novo sistema obtido S’ será equivalente a S.

Vamos avaliar novamente nosso sistema S e o equivalente S’:

|Sistema S|Sistema S’|
|---|---|
|2x + y = 5|2x + y = 5|
|-x +3y = 1|-2x+6y = 2|

Em S’, podemos substituir a segunda equação E2 pela soma dela mesma com a primeira E1, membro a membro, ou seja:

2x + (-2x) = 0 e também  y + 6y = 7y e por fim  5 + 2 = 7.

Assim, a segunda equação ficará 0x + 7y = 7 e o sistema S” obtido com essa nova equação será equivalente a S e S’:

2x + y = 5

0x +7y = 7

Agora, podemos facilmente determinar o valor de y, pois:

7y = 7 então y = 1 e se y = 1, temos que 2x +(1) = 5.  Então,  x = 2

Essas transformações são extremamente úteis quando resolvemos um sistema linear buscando uma matriz triangular superior, que é a matriz na qual todos os elementos a seguir da diagonal principal são nulos.

Veremos agora um exemplo no qual temos um sistema 3x3, ou seja, um sistema de três equações e três variáveis.

Para resolver esse sistema de equações, chamaremos de pivô o número pelo qual deveremos multiplicar as equações para que, ao somarmos ou subtrairmos duas equações, possamos anular uma das variáveis, e repetiremos o processo até chegarmos à matriz do triangular superior, isto é, devemos anular os coeficientes a seguir da diagonal principal.

###### Exemplo

Resolver o sistema linear S

S= x + 2y + z = 9

2x + y - z = 3

3x - y -2z = -4

O sistema do exemplo é um sistema composto por três equações com as variáveis x, y e z. Para facilitar as transformações e os cálculos, iremos, a partir das equações, construir um modelo chamado de equação matricial, ou seja, uma matriz composta pelos coeficientes das três equações, que chamaremos de E1, E2 e E3, que compõe o sistema:

|E1:|1|2|1|
|---|---|---|---|
|E2|2|1|-1|
|E3|3|-1|-2|

Resolveremos as equações quando obtivermos da matriz original uma matriz triangular superior. Para isso utilizaremos as etapas a seguir:

1ª. etapa: eliminar os elementos que estão em destaque em vermelho, ou seja, os elementos a21, a31 e a32 da matriz A3x3. Para isso executaremos as multiplicações e somas necessárias:

- 1º passo: destacar o elemento pivô da primeira etapa, isto é, o elemento a11, pois é por meio dele que anularemos o elemento a21. Assim, definiremos a partir de a11 e a21 o multiplicador da equação. O elemento pivô é a razão entre os dois elementos (no caso a21 e a11) e, por meio desse número, é que realizaremos a transformação em busca de uma equação equivalente.

Para Equação 1 (E1) e Equação 2 (E2) o pivô será:

$$m_1 = \frac{a_{21}}{a_{11}} = \frac{2}{1} = 2$$

$$m_1 = 2 \quad \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 2 & 1 & -1 & 3 \\ 3 & -1 & -2 & -4 \end{array} \right]$$

- 2º passo: determinar a transformação da segunda equação (E2’), que será dada pela subtração de (E2) com a primeira equação (E1) multiplicada por m1, ou seja, E2’ = E2 – m1 * E1.

Acompanhe a transformação de cada um dos termos da segunda equação E2’:

$$\begin{array}{cccc} \text{novo } a_{21} & \text{novo } a_{22} & \text{novo } a_{23} & \text{novo } a_{24} \\ a_{21} - m_1 * a_{11} & a_{22} - m_1 * a_{12} & a_{23} - m_1 * a_{13} & a_{24} - m_1 * a_{14} \\ 2 - 2(1) & 1 - 2(2) & -1 - 2(1) & 3 - 2(9) \\ 0 & -3 & -3 & -15 \end{array}$$

Assim, o novo sistema com a substituição de E2 por E2’ ficará:

$$\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & -3 & -3 & -15 \\ 3 & -1 & -2 & -4 \end{array} \right]$$

- 3º passo: anular o termo a31. Nesse caso, o pivô será determinado por a11 e o multiplicador (m2), por a11 e a31:

$$m_2 = \frac{a_{31}}{a_{11}} = \frac{3}{1} = 3$$

$$m_2 = 3 \quad \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & -3 & -3 & -15 \\ 3 & -1 & -2 & -4 \end{array} \right]$$

- 4º passo: executar a transformação, mas agora da terceira equação (E3), que será subtraída do triplo da primeira equação (E1).

A nova E3’ será dada por:

$$\begin{array}{cccc} \text{novo } a_{31} & \text{novo } a_{32} & \text{novo } a_{33} & \text{novo } a_{34} \\ a_{31} - m_2 . a_{11} & a_{32} - m_2 . a_{12} & a_{33} - m_2 . a_{13} & a_{34} - m_2 . a_{14} \\ 3 - 3(1) & -1 - 3(2) & -2 - 3(1) & -4 - 3(9) \\ 0 & -7 & -5 & -31 \end{array}$$

O sistema, com a nova equação ficará:

$$\left[ \begin{array}{ccc|c} 1 & 2 & 1 & 9 \\ 0 & -3 & -3 & -15 \\ 0 & -7 & -5 & -31 \end{array} \right]$$

- 5º passo: anular o termo a32. O pivô será determinado por a22 e o multiplicador por a22 e a32:

$$m_3 = \frac{a_{32}}{a_{22}} = \frac{-7}{-3} = \frac{7}{3}$$

![[ma2-06-fig10.webp]]

- 6º passo: executamos a transformação, mas agora da terceira equação (E3) que será subtraída da segunda equação (E2), multiplicada por m3 = 7/3.

A terceira equação E3’ será dada por:

novo a31 novo a32 novo a33 novo a34 a31 – m3. a21 a32 – m3.a22 a33 – m3.a23 a34 – m3.a24 0 – 7/3(0) -7 – 7/3(-3) -5 -7/3(-3) -31 – 7/3(-15) 0 0 -5+7 = 2 -31+35 = 4

Dessa forma, nosso sistema ficará:

$$\left[ \begin{array}{ccc|c} & 2 & 1 & 9 \\ & -3 & -3 & -15 \\ & 0 & 2 & 4 \end{array} \right]$$

Que compõe uma matriz triangular, na qual prosseguiremos com a segunda etapa.

2ª etapa: resolver as equações E1, E2 e E3. Iniciamos por E3: 2z = 4 z = 2 Com o valor de z = -2, resolvemos E2: -3y – 3z = -15 -3y – 3(2) = -15 y = 3 E, por fim, resolvemos E3: x + 2y + z = 9 x + 2(3) + (2) x = 1 Portanto, a solução de nosso sistema será S (1, 3, 2).

Vale considerar que, nesse exemplo, lidamos com números inteiros; porém, podemos encontrar sistemas com números racionais e, por vezes, poderemos encontrar pivôs nulos ou próximos de zero, o que pode conduzir a resultados imprecisos com a ampliação de erros de arredondamento. Assim, para contornar problemas como esse, podemos executar algumas manobras como:

- a)  No início de cada etapa, escolher para pivô o elemento de maior módulo entre os coeficientes;

- b)  Trocar as linhas das equações, se necessário, para obter um pivô mais conveniente;

- c)  Promover transformações, por meio da multiplicação em duas equações, simultaneamente, em busca de um pivô mais conveniente.

Para a solução de sistemas lineares, entre os dois métodos estudados, podemos optar por um deles. Cabe uma análise para verificar qual deles fornece menos etapas e, por consequência, é mais prático.
