---
materia: "Circuitos Lógicos"
modulo: "Circuitos Combinacionais"
semestre: 2
unidade: 3
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 03.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 3"]
---

# Circuitos Combinacionais

## Tópicos da Unidade

- **Introdução**

- **Teoremas da Álgebra Booleana**

- **Simplificação de Circuitos Lógicos**

- **Circuitos Combinacionais**

- **Mapa de Karnough**

## Objetivos de Aprendizado

Nesta Unidade, objetiva-se que o aluno tenha conhecimento sobre Minimização de funções e Circuitos Combinacionais a fim de que esteja apto a realizar trabalhos com redes de circuitos e interpretação de Mapas de Karnaugh.

## Contextualização

Para entendermos os circuitos combinacionais, precisamos estudar a simplificação de circuitos lógicos, começando por um aprofundamento na simplificação de circuitos lógicos. Dois métodos serão usados: o primeiro utilizará os teoremas da álgebra booleana e o segundo, uma técnica de mapeamento.

Além disso, vale lembrar que estudaremos técnicas simples para projetar circuitos lógicos que satisfaçam um dado conjunto de requisitos.

## Introdução Soma de Produtos

Para trabalharmos com simplificação de expressões, temos que lembrar que a simplificação exige que a expressão trabalhada esteja na forma de soma de produtos, como exemplificado:

$$\begin{aligned} &A \times B \times C + \bar{A} \times B \times \bar{C} \\ &A \times B + \bar{A} \times B \times \bar{C} + \bar{C} \times \bar{D} + D \end{aligned}$$

Cada uma dessas expressões no formato “soma de produtos” consiste em dois ou mais termos AND (que são os produtos), os quais, por sua vez, estão conectados a uma porta OR. Cada termo AND consiste em uma ou mais variáveis que aparecem individualmente na sua forma complementada ou não. Se tomarmos como exemplo a expressão A B C A B C, o primeiro produto AND contém as variáveis A, B e C na sua forma não complementar ou não invertida, já no segundo produto, há as variáveis A e C na sua forma complementada ou invertida. Podemos observar que, em uma expressão do tipo “soma de produtos”, um sinal de inversão não pode cobrir mais do que uma variável em um termo, ou seja, não poderíamos ter algo como A·B·C.

### Produto de Somas

Uma segunda forma para os projetos de circuitos lógicos é o produto de somas, que consiste em dois ou mais termos OR (somas) que são conectados às entradas de uma porta AND. Cada termo OR contém uma ou mais variáveis na sua forma complementada ou não, conforme exemplos:

$$\begin{aligned} &(A + \bar{B} + C) \times (A + C) \\ &(A + \bar{B}) \times (\bar{C} + D) \times F \end{aligned}$$

O mais utilizado e, portanto, o mais exemplificado aqui é de “soma de produtos”, ficando o método de “produto das somas” reservado para circuitos especiais.

## Teoremas da Álgebra Booleana

Antes de falarmos das simplificações, devemos nos atentar a alguns teoremas de extrema importância, uma vez que são muito utilizados durante os cálculos de simplificação.

Os teoremas booleanos nos ajudam a simplificar expressões de circuitos lógicos e serão listados os oito primeiros na figura a seguir. Em cada um deles, (X) é uma variável lógica que pode ser igual a 0 ou 1 e para exemplificar a circuitaria, há um pequeno circuito lógico que o representa.

### Teoremas para variável única

##### Teorema 01

Esse teorema mostra que o resultado de uma operação AND, que possui como entrada de sinal uma variável X qualquer e outro sinal de valor 0, tem uma saída de sinal igual a 0. A saída de uma porta AND sempre será 0 toda vez que um de seus sinais de entrada for igual a 0, independente da outra fonte de sinal.

##### Teorema 02

Teorema de fácil compreensão matemática, uma vez que qualquer elemento multiplicado por 1 tem como resposta o próprio elemento.

##### Teorema 03

Pode ser provado verificando o resultado para cada valor possível de entrada. Se _x_ = 0; então, 0 × 0 = 0; se _x_ = 1; então, 1 × 1 = 1; logo, _x_ × _x_ = _x_ .

##### Teorema 04

Pode ser provado do mesmo modo. Entretanto, podemos raciocinar que, em qualquer instante, _x_ ou seu inverso _~~x~~_ deve ser igual a 0 e, então, uma operação AND de _x_ com seu inverso será sempre igual a 0.

##### Teorema 05

A soma de 0 a qualquer valor não altera esse valor, seja na adição ordinária ou na operação OR.

##### Teorema 06

O teorema 6 diz que uma operação com a porta OR possui como entradas uma variável qualquer _x_ e 1 será sempre igual a 1. É possível fazer a verificação desse teorema para os dois valores possíveis ele _x_ ; 0 + 1 = 1 e 1 + 1 = 1. De modo equivalente, podemos lembrar que a saída de uma porta OR de duas entradas será igual a 1, quando qualquer uma das entradas for igual a 1, não importando o valor da outra entrada.

##### Teorema 07

Mais um teorema de fácil prova: para ambos os valores da variável, basta fazer o cálculo de x; 0 + 0 = 0 e 1 + 1 = 1.

##### Teorema 08

Pode ser provado raciocinando que, em qualquer instante, _x_ ou seu inverso _~~x~~_ estará em nível lógico 1; então, sempre teremos a operação OR de 0 e 1, cujo resultado será sempre 1.

![[cl2-03-fig01.webp]]

*Figura 1 – Teoremas para variável única*

### Teoremas para variável única

##### Teoremas 09 e 10 – Leis da Comutatividade

Estas leis determinam que a ordem, na qual realizamos as operações AND e OR não é importante, pois o resultado será sempre o mesmo.

##### Teoremas 11 e 12 – Leis da Associatividade

Estas leis determinam que podemos agrupar as variáveis de expressões do tipo AND ou OR do modo que desejarmos.

##### Teorema 13 – Leis da Distributividade

Esse teorema afirma que uma expressão pode ser expandida quando se multiplicam os termos um a um, igual na álgebra comum. Também é regra, por esse teorema, que é permitido fatorar uma expressão, caso tenhamos a soma de dois ou mais termos, cada um contendo uma variável comum, podemos fatorar essa variável como fazemos na álgebra comum, conforme mostra o exemplo:

Assumindo a expressão:

$$z = A \times \bar{B} \times C + \bar{A} \times \bar{B} \times \bar{C}$$

Nessa equação, é possível fatorar a variável :

$$z = \bar{B} \times (A \times C + \bar{A} \times \bar{C})$$

$$z = A \times B \times C + A \times B \times D$$

$$z = A \times B \times (C + D)$$

*Teorema 14*

O teorema 14 não possui nenhum correspondente na álgebra comum. Nele, você deve se atentar aos valores através do estudo dos casos a seguir:

Caso 1 – para _x_ = 0 e _y_ = 0 _x_ + _x_ × _y_ = _x_ 0 + 0 × 0 = 0 0 = 0

Caso 2 – para _x_ = 0 e _y_ = 1 _x_ + _x_ × _y_ = _x_ 0 + 0 × 1 = 0 0 = 0

Caso 3 – para x = 1 e y = 0 _x_ + _x_ × _y_ = _x_ 1 + 1 × 0 = 1 1 = 1

Caso 4 – para x = 1 e y = 1 _x_ + _x_ × _y_ = _x_

1 + 1 × 1 = 1 1 = 1

O teorema 14 também pode ser demonstrado através de fatoração e do uso dos teoremas 6 e 12:

$$\begin{aligned} x + x \times y &= x \times (1 + y) \\ x + x \times y &= x \times 1 && \text{uso do teorema 6} \\ x + x \times y &= x && \text{uso do teorema 2} \end{aligned}$$

*Teorema 15*

Vamos usar como explicação um exemplo de simplificação da expressão:

$$x = A \times C \times D + \bar{A} \times B \times C \times D$$

Fatorando as variáveis comuns _C_ × _D_ , temos:

$$x = C \times D \times (A + \bar{A} \times B)$$

Esse teorema diz que podemos substituir A A B por A + B. Assim, temos:

$$\begin{aligned} x &= C \times D \times (A + B) \\ x &= A \times C \times D + B \times C \times D \end{aligned}$$

*Teoremas de DeMorgan (Redes NAND-NAND e NOR-NOR)*

Os teoremas de DeMorgan são extremamente úteis para simplificar expressões, nas quais o produto (AND) ou a soma (OR) das variáveis são invertidos. Os dois teoremas são:

##### Teorema 16

O complemento da soma é igual ao produto dos complementos.

$$\left(\overline{x + y}\right) = \bar{x} \times \bar{y}$$

*Teorema 17*

O complemento do produto é igual à soma dos complementos.

$$\left(\overline{x \times y}\right) = \bar{x} + \bar{y}$$

Vamos utilizar um exemplo conjunto, onde ambos os teoremas (16 e 17) são aplicados na mesma simplificação.

Como simplificar a expressão a seguir para outra que contenha apenas variáveis simples invertidas?

$$z = \left(\overline{(\bar{A} + C) \times (B + \bar{D})}\right)$$

Utilizando o teorema 17, podemos reescrever a expressão anterior como:

$$z = \left(\overline{\bar{A} + C}\right) + \left(\overline{B + \bar{D}}\right)$$

Agora que a inversão foi separada, podemos tratar os termos utilizando o teorema 16 para sua simplificação:

$$z = \left(\bar{\bar{A}} \times \bar{C}\right) + \left(\bar{B} \times \bar{\bar{D}}\right)$$

Nessa simplificação, partimos o sinal de inversão ao meio e trocamos os sinais (+) por (–) e, então, cancelamos as inversões duplas e temos finalmente:

$$z = A \times \bar{C} + \bar{B} \times D$$

Nesse exemplo de simplificação com teoremas de DeMorgan, vimos que quando utilizamos seus teoremas, o que fazemos é partir o sinal de inversão em qualquer ponto na expressão e, então, mudamos o sinal do operador que estiver neste ponto (simplificando, trocamos (+) por (–) e (–) por (+)), procedimento este que pode ser feito até a redução máxima da expressão a variáveis simples.

Exemplo1:

$$\begin{aligned} z &= \overline{A + \bar{B} \times C} \\ z &= \bar{A} \times \left(\overline{\bar{B} \times C}\right) \\ z &= \bar{A} \times \left(\bar{\bar{B}} + \bar{C}\right) \\ z &= \bar{A} \times \left(B + \bar{C}\right) \end{aligned}$$

Exemplo 2:

$$\begin{aligned} z &= \overline{(A + B \times C) \times (D + E \times F)} \\ z &= \left(\overline{A + B \times C}\right) + \left(\overline{D + E \times F}\right) \\ z &= \left(\bar{A} \times \overline{B \times C}\right) + \left(\bar{D} \times \overline{E \times F}\right) \\ z &= \left[\bar{A} \times (\bar{B} + \bar{C})\right] + \left[\bar{D} \times (\bar{E} + \bar{F})\right] \\ z &= \bar{A} \times \bar{B} + \bar{A} \times \bar{C} + \bar{D} \times \bar{E} + \bar{D} \times \bar{F} \end{aligned}$$

*Simplificação de Circuitos Lógicos*

Uma vez obtida a expressão de um circuito lógico, é comum optarmos por reduzi-la a uma forma mais simples, que contenha um menor número de termos ou variáveis em um ou mais termos da expressão. Esta nova expressão pode ser usada para implementar um circuito equivalente ao circuito original, mas que contém um menor número de portas e conexões.

![[cl2-03-fig02.webp]]

*Figura 2 – Simplicação de circuito lógico. (A) Circuito original e (B) Circuito simplificado.*

É sempre preferível um circuito mais simples para se trabalhar, contando-se que tenha a mesma lógica que o circuito original, uma vez que no circuito simplificado há um número menor  de portas e, portanto, será menor e mais barato do que o circuito original. Além disso, a confiabilidade será melhorada porque existe um menor número de ligações, diminuindo, assim, uma das causas potenciais de falhas no circuito.

### Método Algébrico de Simplificação

Para a simplificação algébrica, usam-se os teoremas da álgebra booleana, porém nem sempre é simples de se identificar qual teorema deve ser aplicado para se ter obter o circuito mais simples possível. Não existe um modo fácil de constatar se a expressão obtida está em sua forma mais simples ou se poderia ser ainda mais simplificada. Portanto, a simplificação algébrica, frequentemente, torna-se um processo de tentativa e erro. Com a experiência, no entanto, pode-se ficar perito e obter resultados razoavelmente bons.

Para explicar como fazer a simplificação pelo metodo algébrico, vamos trabalhar direto com os exemplos.

Vamos simplificar o circuio lógico a seguir:

![[cl2-03-fig03.webp]]

*Figura 3 – Circuito Lógico Original*

Antes de mais nada, é preciso identificar cada expressão de cada porta lógica individual ou agrupada (aquela que entra na última porta lógica), o que nos dá a seguinte expressão:

O próximo passo é desfazer os grandes sinais de inversão ou inversão dupla, conforme os teoremas de DeMorgan (encontrados no material complementar) e, então, multiplicar os termos. Assim, temos:

z A B C A B A C; conforme teorema 17 de De Morgan. z A B C A B A C; cancelamento de inversões duplas. z A B C A B A A B C; multiplicação. z A B C A B A B C; regra A × A = A

Com a expressão, agora, sob a forma de soma-de-produtos, devemos procurar por variáveis comuns dentre os vários termos com a intenção de fatorar. O primeiro e terceiro termos têm AC em comum, que pode ser fatorado:

$$z = A \times C \times (B + \bar{B}) + A \times \bar{B}$$

Aplicando a regra B B 1, teremos:

$$\begin{aligned} z &= A \times C \times (1) + A \times \bar{B} \\ z &= A \times C + A \times \bar{B} \end{aligned}$$

O fator comum, agora, é o A que pode ser fatorado, nos dando:

$$z = A \times (C + \bar{B})$$

Este resultado não pode mais ser simplificado, dando- nos, então, a expressão final que pode ser implementada, agora, em um novo circuito lógico mais simples, conforme a figura a seguir:

![[cl2-03-026.webp]]

*Figura 4 – Circuito Lógico Simplificado*

É possível ser mais simples ou há outras formas? Vamos tentar outros dois métodos no exemplo a seguir. Suponha a seguinte expressão:

z A B C A B C A B C

##### Método 1

Se prestarmos atenção, veremos que a expressão possui o produto _A_ × _B_ nos primeiros dois termos:

$$z = A \times B \times C + A \times B \times \bar{C} + A \times \bar{B} \times C$$

Logo, podemos isolar esse termo:

$$z = A \times B \times (C + \bar{C}) + A \times \bar{B} \times C$$

Aplicando a regra _C_

$+ \bar{C} = 1$, teremos:

$$\begin{aligned} z &= A \times B \times (1) + A \times \bar{B} \times C \\ z &= A \times B + A \times \bar{B} \times C \end{aligned}$$

O fator comum, agora, é o A que pode ser fatorado, dando-nos:

$$z = A \times (B + \bar{B} \times C)$$

Aplicando o teorema 15, temos:

$$z = A \times (B + C)$$

*Método 2*

Lembrando a expressão original:

$$z = A \times B \times C + A \times B \times \bar{C} + A \times \bar{B} \times C$$

Podemos observar que há duas semelhanças, o primeiro e o segundo termos possuem AB em comum e o primeiro e o terceiro termos possuem AC em comum. Mas como saber se devemos fatorar AB dos primeiros dois termos ou AC dos dois termos extremos? Na verdade, podemos fazer ambos usando o termo ABC duas vezes. Veja como fica:

$$z = A \times B \times C + A \times B \times \bar{C} + A \times \bar{B} \times C + A \times B \times C$$

Isso somente é permitido lembrando que A B C A B C A B C , como visto no teorema 7. Agora, sim, podemos fatorar AB dos dois primeiros termos e AC dos últimos termos:

$$z = A \times B \times (C + \bar{C}) + A \times C \times (\bar{B} + B)$$

Aplicando a regra $C + \bar{C} = 1$ e $B + \bar{B} = 1$, teremos:

$$\begin{aligned} z &= A \times B \times (1) + A \times C \times (1) \\ z &= A \times B + A \times C \\ z &= A \times (B + C) \end{aligned}$$

Este é, naturalmente, o mesmo resultado obtido com o método 1. Esse artifício de usar o mesmo termo duas vezes sempre pode ser usado. De fato, o mesmo termo pode ser usado mais de duas vezes, se for necessário.

Vamos ver mais alguns exemplos? Quanto mais exemplos estudados, maior a gama de teoremas aplicados.

Vamos simplificar a seguinte expressão:

$$z = \bar{A} \times C \times \left(\overline{\bar{A} \times B \times D}\right) + \bar{A} \times B \times \bar{C} \times \bar{D} + A \times \bar{B} \times C$$

Pode parecer complicado, mas vamos lá! A primeira coisa a se fazer é usarmos os teoremas de De Morgan no primeiro termo:

$$z = \bar{A} \times C \times (A + \bar{B} + \bar{D}) + \bar{A} \times B \times \bar{C} \times \bar{D} + A \times \bar{B} \times C$$

Com isso, podemos realizar a multiplicação do primeiro termo:

z A C A A C B A C D A B C D A B C

Aplicando a regra A A 0 , teremos:

z A C B A C D A B C D A B C

Chegamos, agora, na forma de “soma de produtos” que queríamos. O próximo passo é o mesmo de sempre, procurar por fatores comuns dentre os vários termos “produto”. Se prestar atenção, identificará que os termos dos extremos da expressão têm o produto _BC_ em comum e os termos do meio possuem o produto _AD_ em comum.

Esses elementos podem ser fatorados, dando-nos a seguinte expressão:

$$z = B \times C \times (\bar{A} + A) + \bar{A} \times \bar{D} \times (C + B \times \bar{C})$$

Aplicando o teorema 15, que diz que:

A A 1 e C BC C B , teremos:

$$z = \bar{B} \times C + \bar{A} \times \bar{D} \times (B + C)$$

Você deve estar se perguntando: Mas e se eu tivesse fatorado o C presente no primeiro, segundo e quarto termos do produto ao invés dos produtos _BC_ e _AD_ , quando chegamos anteriormente na equação:

z A C A A C B A C D A B C D A B C

Tudo bem, você pode fazer isso se quiser!  Então, chegará à seguinte equação:

$$z = C \times (\bar{A} \times \bar{B} + \bar{A} \times \bar{D} + A \times \bar{B}) + \bar{A} \times B \times \bar{C} \times \bar{D}$$

Nessa etapa, você perceberá que ainda poderá fatorar o valor dentro dos parênteses, tendo:

$$z = C \times \left(\bar{B} \times [\bar{A} + A] + \bar{A} \times \bar{D}\right) + \bar{A} \times B \times \bar{C} \times \bar{D}$$

Lembrando da regra que $\bar{A} + A = 1$, temos:

$$z = C \times (\bar{B} + \bar{A} \times \bar{D}) + \bar{A} \times B \times \bar{C} \times \bar{D}$$

Agora, vem a multiplicação:

z B C A C D A B C D

Nesse ponto, você observa que voltamos à fatoração do produto _AD_ , do segundo e terceiro termos:

$$z = \bar{B} \times C + \bar{A} \times \bar{D} \times (C + B \times \bar{C})$$

Agora, devemos usar o teorema 15 na expressão dentro dos parênteses para obter:

$$z = \bar{B} \times C + \bar{A} \times \bar{D} \times (B + C)$$

Que é a mesma resposta, mas por um caminho mais longo, o que nos prova que sempre devemos procurar pelos maiores fatores comuns para fatorar, tornando a reposta mais simples de ser obtida.

Já vimos anteriormente que, quando temos um circuito lógico, os resultados dos circuitos podem ser listados em uma tabela-verdade, mas também podemos obter a expressão do circuito lógico, observando a tabela-verdade criada por ele. Veja o exemplo:

|A|B|x|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|0|
|1|1|0|

*Figura5 – Tabela Verdade do exemplo de Circuitos Combinatórios*

Na tabela verdade da figura 5, temos um exemplo de onde a saída X apenas terá o valor 1 quando A = 0 e B = 1. Dessa forma, podemos determinar quais portas lógicas geram tal processo e, assim, identificar como ficaria a expressão desse circuito, conforme a figura 6:

![[cl2-03-fig04.webp]]

*Figura 6 – Circuito Lógico do exemplo de Circuitos Combinatórios*

Como esse exemplo é mais simples, notamos facilmente que a porta lógica AND pede que os dois sinais de entrada tenham o valor 1 para que sua saída seja 1, mas por se tratar de um sinal invertido, temos de considerar também uma porta lógica inversora anterior em um dos sinais de entrada, o que exige um sinal de entrada com valor 0 para que possua uma saída invertida de valor 1. Dessa forma, chegamos à conclusão da expressão de saída.

Vamos ver, agora, um exemplo um pouco mais complexo, observe a tabelaverdade da figura 7:

|A|B|x|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

*Figura 7 – Tabela Verdade do exemplo de Circuitos Combinatórios Complexos*

Essa tabela nos informa que a saída X será 1 apenas para dois casos específicos, quando A = 0, B = 1 e A = 1 e B = 0. Já sabemos que o termo A B 1 quando A = 0, B = 1; sabemos também que o termo A B 1 quando A = 1 B = 0. Isso nos leva à conclusão que o sinal apenas será ALTO para uma ou outra das condições analisadas; logo, fica mais fácil de entender que esses termos devem ser unidos com a porta lógica OR para produzirem a saída desejada.

Graficamente, teremos, então:

![[cl2-03-fig05.webp]]

*Figuea 8 – Representação lógica dos pré-circuitos*

Uma porta AND é adicionada a cada exemplo, onde a saída na tabela-verdade é 1 e, então, as saídas das portas AND são unidas em ua porta OR para produzir a saída X que terá o valor 1 quando um dos termos AND for 1, gerando o seguinte circuito lógico:

![[cl2-03-fig06.webp]]

![[cl2-03-fig07.webp]]

![[cl2-03-fig08.webp]]

![[cl2-03-fig09.webp]]

![[cl2-03-fig10.webp]]

![[cl2-03-fig11.webp]]

*Figura 9 – Representação lógica do Circuito Lógico Final*

Que tal colocarmos em prática um exemplo de projeto de um conversor? Vemos, na figura 10, uma representação de um conversor analógico-digital que monitora a tensão de uma bateria de 12V; a saída desse conversor gera um número binário de 4bits (ABCD) que corresponde à tensão da bateria com incrementos de 1V, sendo A o MSB (Most Significant Bit ou Bit Mais Significante) e D o LSB (Least Significant Bit ou Bit Menos Significante). As saídas binárias do conversor são ligadas em um circuito digital que deve produzir uma saída em ALTO sempre que o valor binário for maior que 01102 = 610, ou seja, quando a tensão da bateria for maior que 6V. E, agora, como projetar esse circuito?

![[cl2-03-fig12.webp]]

*Figura 10 – Conversor Analógico-Digital*

| | A | B | C | D | z | |
|---|---|---|---|---|---|---|
| (0) | 0 | 0 | 0 | 0 | 0 | |
| (1) | 0 | 0 | 0 | 1 | 0 | |
| (2) | 0 | 0 | 1 | 0 | 0 | |
| (3) | 0 | 0 | 1 | 1 | 0 | |
| (4) | 0 | 1 | 0 | 0 | 0 | |
| (5) | 0 | 1 | 0 | 1 | 0 | |
| (6) | 1 | 0 | 0 | 1 | 0 | |
| (7) | 0 | 1 | 1 | 1 | 1 | $\to\ \overline{A}\,B\,C\,D$ |
| (8) | 1 | 0 | 0 | 0 | 1 | $\to\ A\,\overline{B}\,\overline{C}\,\overline{D}$ |
| (9) | 1 | 0 | 0 | 1 | 1 | $\to\ A\,\overline{B}\,\overline{C}\,D$ |
| (10) | 1 | 0 | 1 | 0 | 1 | $\to\ A\,\overline{B}\,C\,\overline{D}$ |
| (11) | 1 | 0 | 1 | 1 | 1 | $\to\ A\,\overline{B}\,C\,D$ |
| (12) | 1 | 1 | 0 | 0 | 1 | $\to\ A\,B\,\overline{C}\,\overline{D}$ |
| (13) | 1 | 1 | 0 | 1 | 1 | $\to\ A\,B\,\overline{C}\,D$ |
| (14) | 1 | 1 | 1 | 0 | 1 | $\to\ A\,B\,C\,\overline{D}$ |
| (15) | 1 | 1 | 1 | 1 | 1 | $\to\ A\,B\,C\,D$ |

*Figura 11 – Tabela-Verdade do Conversor Analógico-Digital*

Primeiramente, deve-se avaliar a tabela-verdade fornecida, onde podemos notar que a saída Z apenas será 1 para os casos, em que o número binário fornecido pelo conversor for maior que 1001, para todos os outros casos, a saída será o. Logo, podemos montar a seguinte equação:

z A B C D A B C D A B C D A B C D A B C D A B C D A B C D A B C D A B C D

A simplificação dessa equação exige um pouco de atenção e paciência, mas vamos lá! Note que, do segundo produto em diante, há a repetição do termo D+ D e esse será o foco da fatoração dessa equação, o que nos dará:

z A B C D A B C D D A B C (D D) A B C D D A B C D D z A B C D A B C A B C A B C A B C z A B C D A B C C A B C C z A B C D A B A B z A B C D A B B z A B C D A

Se você lembrar do teorema 15, perceberá que podemos aplicá-lo. O Teorema 15 nos diz que x x y x y, que no nosso caso seria x = A ey = BCD, logo:

$$\begin{aligned} z &= \bar{A} \times B \times C \times D + A \\ z &= B \times C \times D + A \end{aligned}$$

Assim, chegamos ao circuito lógico final, conforme a figura 12, que é o circuito representativo do nosso conversor analógico-digital.

![[cl2-03-fig13.webp]]

*Figura 12 – Circuito Lógico do Conversor Analógico-Digital*

## Mapa de Karnough

O método gráfico conhecido como Mapa de Karnough é uma ferramenta que facilita o processo de simplicação de uma equação lógica ou mesmo pode ser usado para converter uma tabela verdade no seu circuito lógico correspondente. O Mapa de Karnough pode ser usado, conceitualmente, para qualquer quantidade de sinais de entrada, mas claro que há um limite prático de 6 sinais de entrada.

O mapa de Karnough é um meio de mostrar a relação entre as entradas lógicas e a saída desejada do circuito. Na figura 13, você encontra três exemplos de mapa para duas, três e quatro sinais de entrada.

![[cl2-03-fig14.webp]]

![[cl2-03-fig15.webp]]

*Figura 13 – Mapa de Karnough para duas (A), três (B) e quatro (C) variáveis*

Na figura 13, há quatro pontos importantes que devemos observar e guardar, pois são de extrema importância.

###### Observação 1

A tabela verdade fornece o valor da saída X para cada combinação de valores da entrada e o mapa de Karnough dá a mesma informação em um formato diferente. Para cada linha na tabela verdade há uma correspondência em um quadrado do mapa de Karnough. Na figura 13.A, a condição  na tabela verdade, tem como correspondência o quadrado _AB_ no mapa de Karnough. Como a tabela verdade mostra _X_ = 1 para esse caso, o valor 1 é colocado no quadrado _AB_ do mapa.

De forma semelhante, a condição _A_ = 1, _B_ = 1 na tabela verdade tem correspondência no quadrado  no mapa de Karnough, e como _X_ = 1 para esse caso também, o valor 1 também é colocado no quadrado _AB_ . Os demais quadrados, para onde _X_ = 0 na tabela verdade, são preenchidos com o valor 0. Os exemplos das figuras 13.B e 13.C são preenchidos seguindo a mesma regra.

###### Observação 2

Os quadrados que aparecem no mapa de Karnough possuem uma identificação, onde os quadrados no sentido horizontal diferem apenas em uma variável. Se tomarmos como exemplo o quadrado posicionado no canto superior esquerdo em um mapa de Karnough de quatro variáveis com denominação _ABCD_ , tem como adjacente, imediatamente, à sua direita, um quadrado denominado _ABCD_ .

De maneira semelhante, os quadrados verticais diferem apenas uma variável, por vez, com seus adjacentes, ou seja, o quadrado no canto superior esquerdo recebe a denominação _ABCD_ e o logo abaixo recebe _ABCD_ .

###### Observação 3

Para que os quadrados adjacentes, seja na horizontal ou na vertical, possuam a diferenciação correta de apenas uma variável, eles devem ser organizados na ordem mostrada _AB_ , _AB_ , _AB_ e _AB_ , e de mesma forma da esquerda para a direita.

###### Observação 4

Preenchido o Mapa de Karnough com os valores de 0 e 1 nos locais corretos, a expressão na forma de soma de produtos para a saída X pode ser obtida juntando cada quadrado com o valor 1 utilizando a função da porta lógica OR. Tomando como exemplo o Mapa de Karnough de três variáveis com os quadrados ABC , ABC , ABC e ABC que possuem valor 1 geram a expressão x ABC ABC ABC ABC .

### Agrupamento de Termos do Mapa de Karnough

O agrupamento de termos é a forma simplificado extraída do mapa de Karnough, o agrupamento é obtido combinando os quadrados do mapa de Karnough que contenham o valor 1. Vamos usar como exemplo os seguintes mapas:

![[cl2-03-fig16.webp]]

*Figura 14 – Agrupamentos de pares de quadrados com valor 1*

A figura 14.A apresenta um mapa de Karnough para uma tabela verdade de três variáveis. Você pode observar que há um par de quadrados com valor 1 que são adjacentes na vertical, o primeiro representando _ABC_ e o segundo _ABC_ .

Nesses dois termos, apenas a variável A aparece tanto na forma normal ( _A_ ), quanto na forma complementar ( _A_ ) e as variáveis _B C_ permanecem inalteradas. Sendo assim, eles podem ser agrupados ou combinados, para que seja possível eliminar a variável A, conforme a expressão:

$$\begin{aligned} x &= \bar{A} \times B \times \bar{C} + A \times B \times \bar{C} \\ x &= B \times \bar{C} \times (\bar{A} + A) \\ x &= B \times \bar{C} \times (1) \\ x &= B \times \bar{C} \end{aligned}$$

Como segundo exemplo, na figura 14.B, você encontra um exemplo com dois quadrados de valor 1 horizontalmente adjacentes; logo, podem ser combinados eliminando a variável C comum a ambos quadrados. De mesma forma na figura 14.C, os quadrados esquerdo superior e esquerdo inferior, que são adjacentes, podem ser agrupados eliminando a variável A. A figura 14.D mostra um exemplo um pouco mais completo com dois grupos de semelhanças de variáveis que podem ser eliminadas da mesma forma que os demais.

Esses foram exemplos de agrupamentos de dois termos, mas também podemos ter o agrupamento de 4 termos, conforme a figura a seguir:

![[cl2-03-fig17.webp]]

*Figura 15 – Agrupamentos de quartetos de quadrados com valor 1*

Quando um quarteto é agrupado, o termo resultante contém apenas as variáveis que não mudam de forma para todos os quadrados do quarteto.

Há também o agrupamento de oito termos ou octetos, onde um grupo de quadrados adjacentes que contenham o valor 1 podem ser combinados, quando um octeto é agrupado num mapa de quatro variáveis, três das quatro variáveis são eliminadas, porque apenas uma variável permanece inalterada, conforme no exemplo da figura 16:

![[cl2-03-fig18.webp]]

*Figura 16 – Agrupamentos de quartetos de octetos com valor 1*

Quando uma variável aparece nas formas complementada e não complementada dentro de um grupo, essa variável é eliminada da expressão. Importante salientar que variáveis que não mudam para todos os quadrados do grupo devem aparecer na expressão final.

Resumidamente, para simplificar uma expressão através do mapa de Karnough, você deve seguir os passos a seguir:

- Passo 1: Construa o mapa de Karnough e coloque valores 1 nos quadrados que correspondem aos valores 1 da tabela-verdade. Em seguida, preencha os demais quadrados com valores 0.

- Passo 2: Examine o mapa de Karnough para detectar valores 1 adjacentes e agrupe aqueles com valor 1 que não são adjacentes a quaisquer outros valores 1. Estes são denominados valores 1 isolados.

- Passo 3: Procure por valores 1 que são adjacentes a somente um outro valor 1. Agrupe todo par que contenha o valor 1.

- Passo 4: Agrupe qualquer octeto, mesmo que ele contenha algum valor 1 que já tenha sido combinado.

- Passo 5: Agrupe qualquer quarteto que contenha um ou mais valores 1 que ainda não tenham sido combinados, certificando-se de usar o número mínimo de agrupamentos.

- Passo 6: Agrupe quaisquer pares necessários para incluir quaisquer valores 1 que ainda não tenham sido combinados, certificando-se de usar o número mínimo de agrupamentos.

- Passo 7: Forme a soma OR de todos os termos gerados por cada agrupamento.

Visitando o endereço abaixo, você encontrará um programa gratuito que poderá fazer download na língua inglesa e espanhola. Então, leia o manual e utilize o programa para aprofundar seus conhecimentos e aprender como fazer as dezenas de cálculos via software. Acesse, explore, conheça e experimente para se familiarizar com as ferramentas mais adequadas a cada situação:

Sistemas Lógicos e Digitais – Software de Simulação, Simplificação e Conversão https://goo.gl/AVhUyG

Nas próximas unidades, vamos explorar mais profundamente os conceitos de instrução e CPU, os quais vão necessitar dos conhecimentos aqui estudados. Por isso, não deixe de exercitar e participar dos fóruns para sanar todas suas dúvidas. Até lá! Abraços!
