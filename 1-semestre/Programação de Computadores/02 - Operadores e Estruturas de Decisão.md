---
materia: "Programação de Computadores"
modulo: "Operadores e Estruturas de Decisão"
semestre: 1
unidade: 2
tipo: material-teorico
fonte: "raw/1-semestre/PROGRAMAÇÃO DE COMPUTADORES/Programação de computadores 02.pdf"
tags: [faculdade, programacao-de-computadores, semestre-1]
aliases: ["Programação de Computadores - Unidade 2"]
---

# Operadores e Estruturas de Decisão

#### Operadores

Um operador é um símbolo que informa ao programa, quais manipulações matemáticas ou lógicas o programa deve executar. A linguagem _Python_ é rica em operadores e fornece o seguinte tipo de operadores: operadores aritméticos; relacionais; lógicos e de concatenação:

##### Operadores Aritméticos

Operadores aritméticos são utilizados para elaboração e execução de cálculos matemáticos. Em _Python_ , temos os seguintes operadores:

**Quadro 1**

|**Operador**|**Descrição**|**Exemplo**|
|---|---|---|
|+|Operador de adição|MinhaVariavel = 2 + 4|
|-|Operador de subtração|MinhaVariavel = 2 - 4|
|*|Operador de multiplicação|MinhaVariavel = 2 x 4|
|/|Operador de divisão|MinhaVariavel = 4 / 2|

|**Operador**|**Descrição**|**Exemplo**|
|---|---|---|
|%|Operador Módulo. Calcula o<br>resto da divisão|Minha Variavel = 8%2|
|**|Operador de exponenciação|MinhaVariavel = 2**4|
|//|Operador divisão de<br>números inteiros. Resulta<br>somente na parte inteira da<br>divisão|MinhaVariavel = 9//2|

```python
#atribuindo valores para variáveis a e b
a = 2
b = 3

#operação de adição
resultado = a + b
print(resultado)

#operação de subtração
resultado = a - b
print(resultado)

#operação de multiplicação
resultado = a * b
print(resultado)

#operação de divisão
resultado = a / b
print(resultado)

#operação de exponenciação
resultado = a ** b
print(resultado)

#operação de divisão de inteiros
resultado = a // b
print(resultado)
```

**Figura 1 – Código exemplo 1** Fonte: Acervo do Conteudista

### Site

**_Jdoodle –Online Python_ 3 IDE O código acima pode ser acessado e testado a seguir.**

**ACESSE**

### Explicando o Código

**Linha 2** : declaramos uma variável com o nome de “a” e atribuímos, por meio do sinal de “igual” o valor “2”;

**Linha 3** : declaramos uma variável com o nome de “b” e atribuímos, por meio do sinal de “igual” o valor “3”;

**Linha 6** : efetuamos a operação aritmética de soma entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 7** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (5);

**Linha 10** : efetuamos a operação aritmética de subtração entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 11** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (-1);

**Linha 14** : efetuamos a operação aritmética de multiplicação entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 15** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (6);

**Linha 18** : efetuamos a operação aritmética de divisão entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 19** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (0,6666);

**Linha 22** : efetuamos a operação aritmética de exponenciação entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 23** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (8);

**Linha 26** : efetuamos a operação aritmética de divisão de inteiros entre os termos representados pelas variáveis a e b, em seguida, é atribuído o resultado dessa operação à variável “resultado”;

**Linha 27** : utilizamos a função “ _print_ ” para imprimir na tela o valor contido na variável “resultado” (0).

#### Precedência de Operadores Aritméticos

Como na matemática, em _Python_ , uma expressão numérica é avaliada de acordo com a ordem dos operadores aritméticos, essa regra é chamada de precedência. A precedência do operador determina o agrupamento de termos em uma expressão e afeta a forma como uma expressão é avaliada. A prioridade de avaliação da expressão está ligada diretamente à precedência do operador. É válido ressaltar que a utilização de parênteses é empregada para a alteração da precedência de uma expressão.

Abaixo temos um exemplo de precedência entre operadores.

**Quadro 2**

|**Ordem de**<br>**Prioridade**|**Operação**|**Símbolo**|
|---|---|---|
|1º|Parênteses|()|
|2º|Inversão de sinal|-|
|3º|Exponenciação|**|
|4º|Multiplicação, Divisão, Resto<br>da divisão (módulo)|*, /, %, //|
|3º|Adição e Subtração|+, -|

Em uma expressão com operadores da mesma prioridade, as operações serão executadas da esquerda para a direita.

De acordo com o exposto, podemos destacar, por exemplo, um cenário como: _a_ = 8 + 1 * 9.

Seguindo a ordem de precedência, a variável “a” resulta em 17, e não 81, pois o operador * tem precedência **mais alta** do que +, assim, efetua-se primeiro a multiplicação 1 * 9 e, depois, a adição por 8.

```
a = 20
b = 10
c = 15
d = 5
e = (a + b) * c / d
```

Para resolver essa expressão, é preciso primeiro efetuar o cálculo da expressão entre parênteses, em seguida, a multiplicação e, por fim, a divisão. Seguindo essa ordem, temos:

```
e = (20+10) * 15 / 5
e = 30 * 15 / 5
e = 450 / 5
e = 90
```

### Operadores Relacionais

Operadores relacionais são utilizados para comparar valores entre termos. O resultado dessa comparação sempre irá retornar um valor booleano, ou seja, _true_ ou _false_ . Em _Python_ , temos os seguintes operadores.

|**Operador**|**Nome**|**Descrição**|**Exemplo**|
|---|---|---|---|
|==|Igualdade|Verifica se os valores<br>de dois operandos<br>são iguais ou não, se<br>a resposta for**sim**, a<br>condição torna-se<br>verdadeira (_true_).|_if_(a==b):<br>_print_(“a é igual a<br>b”)|
|!=|Diferente|Verifica se os valores<br>de dois operandos<br>são iguais ou**não**, se<br>a resposta for não, a<br>condição torna-se<br>verdadeira (_true_).|_if_(a!=b):<br>_print_(“a não é<br>igual a b”)|
|>|Maior que|Verifica se o valor do<br>operando esquerdo é<br>maior que o valor do<br>operando à direita,<br>se**sim**, a condição<br>torna-se verdadeira<br>(_true_).|_if_(a>b):<br>_print_(“a é maior<br>que b”)|
|<|Menor<br>que|Verifica se o valor do<br>operando esquerdo é<br>menor que o valor do<br>operando à direita,<br>se**sim**, a condição<br>torna-se verdadeira<br>(_true_).|_if_(a>b):<br>_print_(“a é menor<br>que b”)|

|**Operador**|**Nome**|**Descrição**|**Exemplo**|
|---|---|---|---|
|>=|Maior<br>igual|Verifica se o valor do<br>operando à esquerda<br>é maior ou igual ao<br>valor do operando à<br>direita, se**sim**, a<br>condição torna-se<br>verdadeira (_true_).|_if_(a>=b):<br>_print_(“a é maior<br>ou igual que b”)|
|<=|Menor<br>igual|Verifica se o valor do<br>operando à esquerda<br>é menor ou igual ao<br>valor do operando à<br>direita, se**sim**, a<br>condição torna-se<br>verdadeira (_true_).|_if_(a>=b):<br> _print_(“a é<br>menor ou igual<br>que b”)|

### Site

**_Jdoodle – Online Python_ 3 IDE**

**Podemos verificar esses operadores em execução com o código criado e compartilhado por meio do seguinte** **_link_ :**

##### Operadores Lógicos

Um operador lógico é um operador que retorna um resultado booleano ( _true_ ou _false_ ) baseado no resultado booleano de uma ou duas outras expressões. O conceito de operadores lógicos é simples. Eles permitem que um programa tome uma decisão com base em múltiplas condições. Cada operando é considerado uma condição que pode ser avaliada de acordo com o valor (verdadeiro ou falso).

Os operadores lógicos em _Python_ são **_and_** , **_or_** e **_not_** .

###### Quadro 3

|**Operador**|**Descrição**|**Exemplo**|
|---|---|---|
|**_and_**|Retorna verdadeiro se ambas as<br>expressões resultarem como<br>verdadeira. Todas as expressões<br>são avaliadas antes que o<br>operador**_and_**seja aplicado.|_if_(a>=b)**_and_**(c>d):<br>_print_(“a é maior ou<br>igual que b**e**c é<br>maior que d)|
|**_or_**|Retorna verdadeiro se pelo<br>menos uma das expressões<br>resultarem como verdadeira.<br>Caso a primeira expressão<br>retorne como verdadeiro, o<br>restante das expressões não é<br>avaliado.|_if_(a>=b) **_or_**(c>d):<br>_print_(“a é maior ou<br>igual que b**ou**c é<br>maior que d)|

|**Operador**|**Descrição**|**Exemplo**|
|---|---|---|
|**_not_**|Retorna verdadeiro se a<br>expressão à direita for avaliada<br>como falsa. Retorna falso se a<br>expressão à direita for|a,b=10,5<br>_if not_(a<b):<br>_print_(“a é menor|
||verdadeiro.|que b”)|

**_Site Jdoodle – Online Python_ 2 IDE Podemos verificar esses operadores em execução com o código criado e compartilhado por meio do seguinte** **_link_ :**

**ACESSE**

##### Operadores de Concatenação

O operador de concatenação de **_string_** em _Python_ é representado por dois pontos ("+"). Utilizase esse operador quando é necessária a junção de dois operandos que contenham um texto.

```python
a= "João"
b= " Silva"

print(a+b)
```

###### Figura 2

*Fonte: Acervo do Conteudista*

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/teste.py ===
João Silva
>>> 
```

###### Figura 3

Acervo do Conteudista

### Leitura

**Operadores e Expressões em** **_Python_**

**ACESSE**

#### Estrutura de Decisão

Em muitos momentos, nosso aplicativo deve tomar decisões de acordo com as **condições** préestabelecidas. As estruturas de decisão exigem que o programador especifique uma ou mais condições a serem avaliadas ou testadas pelo programa, juntamente com uma declaração ou instruções a serem executadas.

![[pc1-02-fig04.webp]]

*Figura 4*

A Figura acima representa um fluxograma onde temos uma estrutura de decisão, e de acordo com a resposta do teste da **condição** , **falso** ou **verdadeiro** , o programa executa um bloco de instruções e segue para a finalização do algoritmo.

### Leitura

**Explicando Algoritmos e Fluxogramas com Exemplos**

**ACESSE**

A linguagem _Python_ fornece os seguintes tipos de declarações de tomada de decisão: _if_ ...; _if ._ .. _else_ e _if_ ... _elif_ .

##### Estrutura if ...

A estrutura _if_ ... é utilizada para testar uma condição e caso retorne verdadeiro, executa um bloco de instruções. Toda declaração **_if_** segue a sintaxe padrão: teste uma condição e, se for verdade, execute uma ação.

![[pc1-02-fig05.webp]]

**Figura 5**

### Leitura

**Indentação do Código** **_Python_ Clique no botão para conferir o conteúdo.**

**ACESSE**

Vejamos o seguinte cenário. Um programa deve obter as notas A e B de um aluno, somar as notas e em seguida, verificar se a nota do aluno é maior que seis (6), se sim, o programa exibe na tela a mensagem “Aluno aprovado”. A seguir, temos um fluxograma descrevendo esse algoritmo.

![[pc1-02-fig06.webp]]

**Leitura Desvio Condicional Simples (SE…ENTÃO) Clique no botão para conferir o conteúdo. ACESSE**

Qual é a condição para que o aluno possa ser aprovado?

A condição é que a soma das notas A e B deve ser maior que seis (6), caso o teste dessa condição retorne verdadeiro, o programa executa as instruções previstas para essa situação.

Implementando o seguinte algoritmo em _Python_ , temos:

```python
a=3
b=4
soma = a+b
if (soma > 6):
    print("Aluno aprovado")
```

**Figura 7**

*Fonte: Acervo do Conteudista*

**_Site_**

**_Jdoodle – Online Python_ 2 IDE**

**ACESSE**

#### Explicando o Código

**Linhas 1 e 2** : declaramos uma variável com o nome de “a” e “b” e em seguida, atribuímos os valores 3 para “a” e 4 para “b”;

**Linha 3** : efetuamos uma operação de adição entre as variáveis “a” e “b” e atribuímos o resultado para a variável “soma”;

**Linha 4** : descrevemos a estrutura condicional **_if_** testando a condição “soma > 6”. Caso o teste retorne verdadeiro, o programa executará a linha 5, do contrário, o programa será finalizado;

**Linha 5** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno aprovado”.

##### Estrutura if ... else

Na estrutura **_if ... else_** , além de testar uma condição e executar um bloco de instruções no caso de retorno do teste ser verdadeiro, também é descrito as instruções para quando o retorno for falso. Utilizamos essa estrutura quando o programa deve tomar duas decisões.

Toda declaração **_if ... else_** . Segue sintaxe padrão: teste uma condição e, se for verdade, execute o bloco de instrução 1; caso contrário, execute o bloco de instrução 2.

![[pc1-02-fig09.webp]]

*Figura 8*

**Leitura Estrutura de Decisão SE-ENTÃO-SENÃO Clique no botão para conferir o conteúdo. ACESSE**

Partindo do exemplo anterior, onde nosso programa recebe duas notas e, em seguida. efetua a soma entre as duas, iremos complementar com mais uma decisão. Caso a condição retorne falsa, o programa irá imprimir na tela o texto “Aluno reprovado”. A seguir, temos um fluxograma descrevendo esse algoritmo.

![[pc1-02-fig10.webp]]

**Figura 9**

Do mesmo modo que o algoritmo anterior, a condição para o aluno ser aprovado é possuir uma nota maior que seis (6). Contudo, nesse novo algoritmo, temos previsto também instruções em caso de um retorno ser falso, ou seja, caso o aluno possua nota menor ou igual a seis (6).

Implementando o seguinte algoritmo em _Python_ , temos:

```python
a=3
b=2
soma = a+b

if (soma > 6):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
```

**Figura 10** Fonte: Acervo do Conteudista

**_Site_**

**_Jdoodle – Online Python_ IDE Podemos visualizar esse código por meio do seguinte** **_link_ :**

#### Explicando o Código

**Linhas 1 e 2** : declaramos uma variável com o nome de “a” e “b” e em seguida, atribuímos os valores 3 para “a” e 2 para “b”;

**Linha 3** : efetuamos uma operação de adição entre as variáveis “a” e “b” e atribuímos o resultado para a variável “soma”;

**Linha 5** : descrevemos a estrutura condicional **_if_** testando a condição “soma > 6”. Caso o teste retorne verdadeiro, o programa executará a linha 6. Caso contrário, o programa executará a linha 8;

**Linha 6** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno aprovado”;

**Linha 8** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno reprovado”.

##### Estrutura if ... elif

Utilizamos a estrutura _if_ ... _elif_ quando o programa deve testar uma condição quando a primeira condição testada retorna falso.

![[pc1-02-fig12.webp]]

**Figura 11**

**Leitura Desvio Condicional Aninhado (SE...ENTÃO...SENÃO...SE)**

**ACESSE**

Vejamos o seguinte cenário. Um programa deve obter as notas A e B de um aluno, somar as notas e, em seguida, verificar se a nota do aluno é maior que seis (6), se sim, o programa exibe na tela a mensagem “Aluno aprovado”. Caso o aluno não possua uma nota maior que seis (6), porém, possua uma nota maior que dois (2), o aluno poderá realizar uma prova de recuperação. A seguir, temos um fluxograma descrevendo esse algoritmo.

![[pc1-02-fig13.webp]]

**Figura 12**

Implementando o seguinte algoritmo em _Python_ , temos:

```python
a=1
b=3
soma = a+b

if (soma > 6):
    print("Aluno aprovado")
elif (soma > 2):
    print("Aluno pode realizar prova de recuperação")
```

###### Figura 13

*Fonte: Acervo do Conteudista*

**_Site_**

**_Jdoodle – Online Python_ IDE Podemos visualizar esse código por meio do seguinte** **_link_ :**

**ACESSE**

#### Explicando o Código

**Linhas 1 e 2** : declaramos uma variável com o nome de “a” e “b” e, em seguida, atribuímos os valores 1 para “a” e 3 para “b”;

**Linha 3** : efetuamos uma operação de adição entre as variáveis “a” e “b” e atribuímos o resultado para a variável “soma”;

**Linha 5** : descrevemos a estrutura condicional **_if_** testando a condição “soma > 6”. Caso o teste retorne verdadeiro, o programa executará a linha 6. Caso contrário, o programa executará a linha 7;

**Linha 6** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno aprovado”;

**Linha 7** : testamos a condição “soma > 2”. Caso o teste retorne verdadeiro, o programa executará a linha 8. Caso contrário, o programa será finalizado;

**Linha 8** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno pode realizar prova de recuperação”.

##### Estruturas de Decisão Encadeadas

Em alguns cenários de nossos algoritmos, devem-se realizar diversos testes e condições para se atingir um objetivo. Em cenários onde é preciso verificar diversas condições, podemos escrever sequências de instruções de estruturas de decisão. Esse cenário comumente é chamado de estruturas de decisão aninhadas ou encadeadas.

Abaixo, temos exemplos de estruturas de decisão encadeadas.

```python
if(condição):
         bloco de instrução 1
         elif(condição):
                 bloco de instrução 2
        else:
                bloco de instrução 3
else:
        bloco de instrução 4
if(condição):
        if(condição):
                bloco de instrução 1
        else:
                if(condição):
                        bloco de instrução 2
                else:
                        bloco de instrução 3
else:
        bloco de instrução 4
```

Vejamos o seguinte cenário. Um programa deve obter as notas A e B e a frequência de um aluno. Para ser considerado aprovado, o aluno deve possuir frequência maior que 75% e nota maior que 6.

Caso o aluno não possua frequência maior que 75%, será considerado reprovado de forma direta.

O aluno que possuir a frequência mínima, porém, nota menor ou igual a 6 e maior que 2, poderá realizar uma prova de recuperação, caso contrário, será reprovado. A seguir, temos um fluxograma descrevendo esse algoritmo.

![[pc1-02-fig15.webp]]

**Figura 14**

Implementando o seguinte algoritmo em _Python_ , temos:

```python
a=1
b=5
frequencia = 80

if (frequencia > 75):
    soma = a+b
    if(soma > 6):
        print("Aluno aprovado")
    elif(soma > 2):
        print("Aluno pode realizar prova de recuperação")
    else:
        print("Aluno reprovado")
else:
    print("Aluno reprovado direto")
```

**Figura 15** Fonte: Acervo do Conteudista

### Site

**_Jdoodle – Online Python_ IDE**

**Podemos visualizar esse código por meio do seguinte** **_link_ :**

**ACESSE**

#### Explicando o Código

**Linhas 1 e 2** : declaramos uma variável com o nome de “a” e “b” e, em seguida, atribuímos os valores 1 para “a” e 5 para “b”;

**Linha 5** : descrevemos a estrutura condicional **_if_** _t_ estando a condição “frequencia > 75”. Caso o teste retorne verdadeiro, o programa executará o bloco a partir da linha 6. Caso contrário, o programa executará o bloco de instruções a partir da linha 13 e finalizará a execução do programa;

**Linha 6** : efetuamos uma operação de adição entre as variáveis “a” e “b” e atribuímos o resultado para a variável “soma”;

**Linha 7** : descrevemos a estrutura condicional **_if_** testando a condição “soma > 6”. Caso o teste retorne verdadeiro, o programa executará a linha 8. Caso contrário, o programa executará a linha 9;

**Linha 8** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno aprovado”;

**Linha 9** : testamos a condição “soma > 2”. Caso o teste retorne verdadeiro, o programa executará a linha 10. Caso contrário, o programa irá executar o bloco de instruções a partir da linha 12;

**Linha 10** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno pode realizar prova de recuperação”;

**Linha 12** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno reprovado”;

**Linha 13** : utilizamos a função “ _print_ ” para imprimir na tela o texto “Aluno reprovado direto”.

**Em Síntese Nesta Unidade, estudamos a aplicação de operadores (aritméticos, relacionais, lógicos e de concatenação), bem como os conceitos de estruturas de decisão.  É importante que assista à videoaula e que leia os livros e materiais complementares indicados nesta unidade de estudo. É fundamental que, além dos estudos em** **_Python_ , busque estudar ou retomar conceitos de desenvolvimento de algoritmos, ter**

**uma boa noção desse tema o ajudará na jornada de estudos de programação de computadores.**

**Até a próxima!**

_2 / 3_
