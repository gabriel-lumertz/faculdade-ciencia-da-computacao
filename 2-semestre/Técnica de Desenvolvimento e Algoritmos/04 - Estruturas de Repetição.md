---
materia: "Técnica de Desenvolvimento e Algoritmos"
modulo: "Estruturas de Repetição"
semestre: 2
unidade: 4
tipo: material-teorico
fonte: "raw/2-semestre/TÉCNICA DE DESENVOLVIMENTO E ALGORITMOS/TDA 04.pdf"
tags: [faculdade, tecnica-de-desenvolvimento-e-algoritmos, semestre-2]
aliases: ["Técnica de Desenvolvimento e Algoritmos - Unidade 4"]
---

# Estruturas de Repetição

## Objetivos de Aprendizado

- Desenvolver algoritmos em fluxograma e em pseudocódigo com estruturas de repetição.

## Estruturas de Repetição em Algoritmos

Nesta Unidade IV, continuaremos conhecendo um pouco mais sobre as estruturas que compõem os algoritmos. Salientamos que a implementação dos algoritmos utilizando qualquer Linguagem de Programação permite o teste efetivo destes. Neste curso, os testes serão realizados na ferramenta VisualG.

Na Unidade I, abordamos as definições de algoritmos e as três técnicas mais utilizadas para o desenvolvimento dos mesmos. Na Unidade II, foram abordados alguns algoritmos que utilizam apenas estrutura sequencial, ou seja, entrada dos dados, processamento e saída. Na Unidade III, abordamos alguns algoritmos que utilizam estruturas condicionais, também conhecidas como desvios. E a partir desta Unidade IV, abordaremos algoritmos que apresentam comandos que são repetidos várias vezes, assim, a estrutura que permite essa execução repetitiva é denominada Estrutura de Repetição.

“Uma estrutura de repetição é utilizada quando um trecho do algoritmo, ou até mesmo o algoritmo inteiro, precisa ser repetido. O número de repetições pode ser fixo ou estar atrelado a uma condição”. (ASCENCIO; CAMPOS, 2012, p. 95)

As estruturas de repetição estão divididas em: Estrutura de repetição com variável de controle, Estrutura de repetição condicional com teste no início e Estrutura de repetição condicional com teste no final. As estruturas de repetição são também conhecidas como laços ou loops, e estes podem se repetir por um número definido ou indefinido de vezes.

A primeira estrutura de repetição a ser abordada é a estrutura de repetição com variável de controle e é utilizada quando se sabe o número de vezes em que um trecho do algoritmo deve ser repetido.

*Quadro 1 - Estrutura de repetição com variável de controle em fluxograma e em pseudocódigo*

|**Fluxograma**|**Pseudocódigo**|
|---|---|
||para VARIÁVEL_DE_CONTROLE<br>de VALOR_INICIAL ate VALOR_<br>FINAL faca<br>comandos<br>fimpara|

Na estrutura de repetição com variável de controle, a variável de controle recebe o valor inicial e os comandos são repetidos até que a variável de controle receba o valor final. A instrução ```PASSO n``` indicada como a variável será incrementada ou decrementada.

```
Exemplo 1 da estrutura de repetição com variável de controle em pseudocódigo

para i de 0 ate 5 passo 1 faca
   escreva ("Estudar")
fimpara
```

Exemplo 1 da estrutura de repetição com variável de controle em fluxograma

![[tda2-04-fig01.webp]]

*Figura 1 - Estrutura de repetição com variável de controle em fluxograma do Exemplo 1*

No exemplo acima, a variável de controle, identificada por i, receberá, inicialmente, o valor 0 e este será incrementado em 1, devido à instrução ```PASSO 1```, até atingir o valor 5, logo, o comando escreval (“estudar”) será repetido seis vezes.

Teste de mesa ou simulação da estrutura definida no Exemplo 1:

*Quadro 2 - Teste de mesa do Exemplo 1*

|**Memória**|**Tela**|
|---|---|---|
|i|||
|0|estudar||
|1|estudar||
|2|estudar||
|3|estudar||
|4|estudar||
|5|estudar||

Exemplo 2 da estrutura de repetição com variável de controle em pseudocódigo

```
para x de 5 ate 1 passo -1 faca
   escreva ("Valor de x= ",x)
fimpara
```

Exemplo 2 da estrutura de repetição com variável de controle em fluxograma

![[tda2-04-fig02.webp]]

*Figura 2 - Estrutura de repetição com variável de controle em fluxograma do Exemplo 2*

No exemplo acima, a variável de controle, identificada por x, receberá, inicialmente, o valor 5 e este será decrementado em 1, devido à instrução ```PASSO -1```, até atingir o valor 1, logo, o comando escreval (“valor de x = ”,x) será repetido cinco vezes.

Teste de mesa ou simulação da estrutura definida no Exemplo 2:

*Quadro 3 - Teste de mesa do Exemplo 2*

|**Memória**|**Tela**|
|---|---|---|---|
|x||||
|5|valor de x = 5|
|4|valor de x = 4|
|3|valor de x = 3|
|2|valor de x = 2|
|1|valor de x = 1|

Exemplo 3 da estrutura de repetição com variável de controle em pseudocódigo

```
para m de 0 ate 100 passo 20 faca
se (m <> 0) então
escreval ("Múltiplo de 20 = ", m)
fimse
fimpara
```

Exemplo 3 da estrutura de repetição com variável de controle em fluxograma

![[tda2-04-fig03.webp]]

![[tda2-04-fig04.webp]]

*Figura 3 - Estrutura de repetição com variável de controle em fluxograma do Exemplo 3*

```
algoritmo "exemplo3"
// Autor: Margarete E. S. Almendro
// 07/02/2020
// utilizando laços de repetição
Var
num, m, idade:inteiro
soma:real;
nome:caractere;
Inicio
      para m de 0 ate 100 passo 20 faca
      se (m <> 0) então
         escreval ("Múltiplo de 20 = ", m)
      fimse
      fimpara
fimalgoritmo
```

No exemplo acima a variável de controle, identificada por m, receberá, inicialmente, o valor 0 e este será incrementado em 20, devido à instrução [PASSO 20], até atingir o valor 100, logo, o comando se (m <> 0), então, escreval (“Múltiplo de 20 = ”,m), fimse, será testado seis vezes, e o comando escreval (“Múltiplo de 20 = ”, m) será executado cinco vezes.

Teste de mesa ou simulação da estrutura definida no Exemplo 3:

*Quadro 4 - Teste de mesa do Exemplo 3*

|**Memória**|**Tela**|
|---|---|---|
|m||
|0||
|20|múltiplo de 20 = 20|
|40|múltiplo de 20 = 40|
|60|múltiplo de 20 = 60|
|80|múltiplo de 20 = 80|
|100|múltiplo de 20 = 100|

```
Exemplo 4 da estrutura de repetição com variável de controle em pseudocódigo
escreva("Números de 250 a 25")
para m de 250 ate 25 passo -25 faca
      escreval ("Número = ", m)
fimpara
```

Exemplo 4 da estrutura de repetição com variável de controle em fluxograma

![[tda2-04-fig05.webp]]

*Figura 4 - Estrutura de repetição com variável de controle em fluxograma do Exemplo 4*

No exemplo acima, a variável de controle, identificada por num, receberá inicialmente o valor 250 e este será decrementado em 25, devido à instrução [PASSO -25], até atingir o valor 25, logo, o comando escreval (“Número = “, m) será repetido dez vezes.

Teste de mesa ou simulação da estrutura definida no Exemplo 4:

*Quadro 5 - Teste de mesa do Exemplo 4*

|**Memória**|**Tela**|
|---|---|
|num||
|250|Número = 250|

|**Memória**|**Tela**|
|---|---|---|
|225|Número =|225|
|200|Número =|200|
|175|Número =|175|
|150|Número =|150|
|125|Número =|125|
|100|Número =|100|
|75|Número =|75|
|50|Número =|50|
|25|Número =|25|

Existem duas situações em que os comandos da estrutura de repetição com variável de controle não são repetidos, ou seja, não são executados nenhuma vez.

Quais situações seriam estas?

Situação 1:

```
para i de 10 ate 20 passo -1 faca
           escreval ("Número = ", i)
fimpara
```

Na situação 1, o comando escreval (i) não será executado nenhuma vez porque o valor inicial da variável de controle i é 10 e deveria ir até 20, mas como  o passo é -1, então, a variável de controle vai decrementar em uma unidade, logo, a condição para execução que seria i <= 20 não seria respeitada.

Situação 2:

```
para i de 10 ate 0 passo 1 faca
escreval ("Número = ", i)
fimpara
```

Na situação 2, o comando escreval (i) não será executado nenhuma vez porque o valor inicial da variável de controle i é 10 e deveria ir até 0, mas como  o passo é 1, então, a variável de controle vai incrementar em uma unidade, logo, a condição para execução que seria i >= 0 não seria respeitada.

A segunda estrutura de repetição a ser abordada é a estrutura de repetição condicional com teste no início, mais utilizada quando NÃO se sabe o número de vezes em que um trecho do algoritmo deve ser repetido.

Embora a indicação de sua utilização seja para quando NÃO se sabe o número de repetições necessário, essa estrutura também pode ser utilizada quando se sabe o número de repetições.

*Quadro 6 - Estrutura de repetição condicional com teste no início em fluxograma e em pseudocódigo*

```text
enquanto (Condição) faca
    comandos
fimenquanto
```

![[tda2-04-fig06.webp]]

Na estrutura de repetição condicional com teste no início, os comandos serão repetidos enquanto a condição for verdadeira.

Nos exemplos, a seguir, exploraremos a estrutura de repetição condicional com teste no início.

Exemplo 1  da estrutura de repetição condicional com teste no início em pseudocódigo

```
i <- 0
enquanto (i <= 5) faca
   escreval("Estudar")
    i <- i + 1
fimenquanto
```

Exemplo 1  da estrutura de repetição condicional com teste no início em fluxograma

![[tda2-04-fig07.webp]]

*Figura 5 - Estrutura de repetição condicional com teste no início em fluxograma do Exemplo 1*

No exemplo acima, a variável identificada por i, receberá, inicialmente, o valor 0, enquanto a condição i <= 5 for verdadeira, os comandos escreval (“estudar”) e i <- i + 1 serão repetidos.

Teste de mesa ou simulação da estrutura definida no Exemplo 1:

*Quadro 7 - Teste de mesa do Exemplo 1*

|**Memória**|**Tela**|
|---|---|---|
|i||
|0|estudar|
|1|estudar|
|2|estudar|
|3|estudar|
|4|estudar|
|5|estudar|
|6||

Exemplo 2 da estrutura  de repetição condicional com teste no início em pseudocódigo

```
i <- 10
j <-100
cont <- 0
enquanto i < j faca
   i <- i + 10
   j <-j - 10
   cont <- cont + 1
fimenquanto
escreval ("Repeticoes = ", cont)
```

Exemplo 2 da estrutura  repetição condicional com teste no início  em fluxograma:

![[tda2-04-fig08.webp]]

*Figura 6 - Estrutura de repetição condicional com teste no início em fluxograma do Exemplo 2*

No exemplo acima, a variável identificada por i, receberá, inicialmente, o valor 10; a variável identificada por j, receberá, inicialmente, o valor 100; a variável identificada por cont, receberá, inicialmente, o valor 0. Enquanto a condição i < j for verdadeira, os comandos i ← i + 10, j ← j - 10 e cont ← cont + 1 serão repetidos.

Teste de mesa ou simulação da estrutura definida no Exemplo 2:

*Quadro 8 - Teste de mesa do Exemplo 2*

|**Memória**|**Tela**|
|---|---|---|---|
|i|j|cont||
|10|100|0||
|20|90|1||
|30|80|2||
|40|70|3||
|50|60|4||
|60|50|||
||||Repetições = 5|

Existe uma situação em que os comandos da estrutura de repetição condicional com teste no início não são repetidos, ou seja, não são executados nenhuma vez. Qual situação será esta?

```
i<- 0
enquanto i > 0 faça
escreva(i)
i<- i + 1
```

Na situação acima, os comandos escreval (i) e i <- i + 1 não serão executados nenhuma vez porque o valor inicial da variável i é 0 o que torna a condição i > 0 falsa.

A terceira estrutura de repetição a ser abordada é a estrutura de repetição condicional com teste no final, mais utilizada quando NÃO se sabe o número de vezes em que um trecho do algoritmo deve ser repetido.

Embora a indicação de sua utilização seja para quando NÃO se sabe o número de repetições necessário, essa estrutura também pode ser utilizada quando se sabe o número de repetições.

*Quadro 9 - Estrutura de repetição condicional com teste no final em fluxograma e em pseudocódigo*

```text
repita
    comandos
até condição
```

![[tda2-04-fig09.webp]]

Na estrutura de repetição condicional com teste no final, os comandos serão repetidos pelo menos uma vez e até a condição se tornar verdadeira.

Nos exemplos, a seguir, vamos explorar a estrutura de repetição condicional com teste no final.

Exemplo 1  da estrutura de repetição condicional com teste no final em pseudocódigo

```
i<-10
repita
   escreval ("valor de i = •",i)
   i<-i + 10
 ate i > 50
```

Exemplo 1 da estrutura de repetição condicional com teste no final em fluxograma:

![[tda2-04-fig10.webp]]

*Figura 7 - Estrutura de repetição condicional com teste no final em fluxograma do exemplo 1*

No exemplo acima, a variável identificada por i, receberá, inicialmente, o valor 10, os comandos escreval (“valor de i = ”,i) e i ← i + 10 serão executados até a condição se tornar verdadeira, ou seja, até i > 50.

Teste de mesa ou simulação da estrutura definida no Exemplo 1:

*Quadro 10 - Teste de mesa do Exemplo 1*

|**Memória**|**Tela**|
|---|---|---|
|i||
|10|valor de i = 10|
|20|valor de i = 20|
|30|valor de i = 30|
|40|valor de i = 40|
|50|valor de i = 50|
|60||

Exemplo 2 da estrutura de repetição condicional com teste no final em pseudocódigo i ← 1

```
repita
escreval ("valor de i = ",i)
i ← i + 1
até i > 5
```

Exemplo 2 da estrutura de repetição condicional com teste no final em fluxograma:

![[tda2-04-fig11.webp]]

*Figura 8 - Estrutura de repetição condicional com teste no final em fluxograma do Exemplo 2*

No exemplo acima, a variável identificada por i, receberá, inicialmente, o valor 1, os comandos escreval (“valor de i = “,i) e i <- i + 1 serão executados até a condição se tornar verdadeira, ou seja, até i > 5.

Teste de mesa ou simulação da estrutura definida no Exemplo 2:

*Quadro 11 - Teste de mesa do Exemplo 2*

|**Memória**|**Tela**|
|---|---|---|
|i||
|1|valor de i = 1|

|**Memória**|**Tela**|
|---|---|---|---|
|2|valor de i = 2|
|3|valor de i = 3|
|4|valor de i = 4|
|5|valor de i = 5|
|6||

Quando utilizamos a estrutura de repetição condicional com teste no final, os comandos serão repetidos PELO MENOS UMA VEZ, pois a condição se encontra após o comandos.

Em quais estruturas de repetição podemos gerar um laço também conhecido como loop, ou seja, uma estrutura de repetição infinita, o que trava a execução do algoritmo?

As duas estruturas de repetição condicionais, com teste no início e com teste no final, podem causar um laço, conforme exemplos abaixo:

##### Exemplo 1:

```
i <- 1
enquanto i > 0 faça
escreval ("valor de i = ",i)
i <-i + 1
fimenquanto
```

No exemplo 1 a variável i é inicializada com 1 e dentro da estrutura de repetição ela é incrementada em 1. Como a estrutura enquanto será executada enquanto a condição for verdadeira (i > 0) e a condição nunca se tornará falsa, teremos um laço infinito.

Exemplo 2:

```
i <- 1
repita
escreval ("valor de i = ",i)
i <- i + 1
até i < 0
```

No Exemplo 2, a variável i é inicializada com 1 e, dentro da estrutura de repetição, ela é incrementada em 1. Como a estrutura repita será executada até a condição se tornar verdadeira (i < 0) e a condição nunca se tornará verdadeira, teremos um laço infinito.

Observe a Figura 9, a seguir:

![[tda2-04-fig12.webp]]

*Figura 9 - Estruturas de repetição em algoritmos em algoritmos Fonte:  yasnaten / 123RF*

Como se pode ver, as estruturas de repetição permitem que um ou vários comandos sejam executados repetidas vezes.
