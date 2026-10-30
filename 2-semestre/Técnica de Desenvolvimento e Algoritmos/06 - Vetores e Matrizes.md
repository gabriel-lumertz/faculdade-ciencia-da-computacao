---
materia: "Técnica de Desenvolvimento e Algoritmos"
modulo: "Vetores e Matrizes"
semestre: 2
unidade: 6
tipo: material-teorico
fonte: "raw/2-semestre/TÉCNICA DE DESENVOLVIMENTO E ALGORITMOS/TDA 06.pdf"
tags: [faculdade, tecnica-de-desenvolvimento-e-algoritmos, semestre-2]
aliases: ["Técnica de Desenvolvimento e Algoritmos - Unidade 6"]
---

# Vetores e Matrizes

## Objetivos de Aprendizado

- Desenvolver algoritmos em pseudocódigo que utilizem as estruturas de dados do tipo vetores e matrizes.

## Conceito de Vetor e Matriz

Nesta Unidade VI, continuaremos conhecendo um pouco mais sobre as estruturas que compõem os algoritmos. Salientamos que a implementação dos algoritmos utilizando qualquer Linguagem de Programação permite o teste efetivo desres. Neste curso, os testes serão realizados na ferramenta VisualG.

Na Unidade I, abordamos as definições de algoritmos e as três técnicas mais utilizadas para o desenvolvimento destes. Na Unidade II, foram abordados alguns algoritmos que utilizam apenas estrutura sequencial, ou seja, entrada dos dados, processamento e saída. Na Unidade III. abordamos alguns algoritmos que utilizam estruturas condicionais, também conhecidas como desvios. Na Unidade IV, abordamos alguns algoritmos que utilizam estruturas de repetição, em que um ou vários comandos podem ser repetidos várias vezes. Na unidade V, abordamos as sub-rotinas, ou seja, a modularização dos algoritmos.

A partir desta unidade, abordaremos dois novos tipos de dados, conhecidos como vetores e matrizes.

Um vetor é também conhecido como variável composta homogênea unidimensional. Isto quer dizer que se trata de um conjunto de variáveis de mesmo tipo, que possuem o mesmo identificador (nome) e são alocadas sequencialmente na memória. Como as variáveis têm o mesmo nome, o que as distingue é um índice que referencia sua localização dentro da estrutura. (ASCENCIO; CAMPOS,  2012, p. 151)

O vetor é declarado juntamente com as outras variáveis, conforme sintaxe a seguir:

```javascript
  var nome_da_variável: vetor[posição_inicial..posição_final] de tipo_dos_dados
```

A seguir, alguns exemplos de vetores:

![[tda2-06-fig01.webp]]

Acima, podemos ver a criação de um vetor chamado vet, que possui cinco posições. Ou seja, foram alocadas cinco porções de memória para armazenamento de números inteiros. Estas porções de memória são contíguas, isto é, seus endereços são sequenciais.

![[tda2-06-fig02.webp]]

Acima, é possível ver a criação de um vetor chamado y, que possui três posições. Ou seja, foram alocadas três porções de memória para armazenamento de números reais. Essas porções de memória são contíguas, isto é, seus endereços são sequenciais.

Para atribuir valores às posições dos vetores, é necessário colocar o nome do vetor e a posição entre colchetes, conforme exemplos abaixo:

![[tda2-06-fig03.webp]]

É possível utilizar a estrutura de repetição com variável de controle para carregar todas as posições de um vetor, conforme exemplo a seguir:

```
para i <- 1 até 5 faça [passo 1]
   escreval ("Digite o ",i," º número")
   leia (x[i])
fimpara
```

Nesse exemplo, a estrutura de repetição PARA foi utilizada para garantir que a variável i assuma todos os valores possíveis entre 1 e 5 (posições válidas para o vetor X). Assim, para cada execução da repetição, será utilizada uma posição diferente do vetor.

*Quadro 1 - Simulação*

![[tda2-06-fig04.webp]]

*Fonte: Ascencio e Campos (2012, p. 152)*

Da mesma forma que utilizamos a estrutura de repetição para passar por todas as posições de um vetor, a fim de carregá-las com dados digitados pelo usuário, usamos a estrutura de repetição para mostrar os dados armazenados no vetor, conforme exemplo abaixo:

```
para i <- 1 até 5 faça [passo 1]
escreval ("Conteúdo da posição ",i," do vetor ")
escreval (x[i])
fimpara
```

Os vetores são conhecidos como variáveis homogêneas unidimensionais, ou seja, são variáveis com o mesmo nome e o mesmo tipo, mas diferenciadas por um único índice. Assim, não podemos usar um vetor para armazenar os dados de um produto, pois os dados de um produto são: código do tipo inteiro, descrição do tipo literal e preço do tipo real.

A seguir, há um exemplo de algoritmo utilizando vetor. O algoritmo deve receber dez números digitados pelo usuário e mostrar qual o menor.

![[tda2-06-fig05.webp]]

*Figura 1 - Fluxograma do algoritmo exemplo de vetor*

A seguir, temos um algoritmo exemplo em pseudocódigo:

```javascript
algoritmo "exemplo1"
// Função: receber 10 números e mostrar o menor
// Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
// Data: 24/12/2018 /*07/02/2020
// seção de declarações de variáveis e constantes
var num: vetor[1..10] de inteiro
i, menor: inteiro
inicio
      para i <- 1 até 10 faça [passo 1]
           leia (num[i])
      fimpara
      menor <- num[1]
      para i <- 1 até 10 faça [passo 1]
           se (num[i] < menor) entao
              menor <- num[i]
           fimse
      fimpara
      escreval (menor)
fimalgoritmo
```

Quando falamos em vetores em algoritmos e em programação de computadores, estamos falando de uma variável capaz de armazenar uma quantidade finita de variáveis, todas com o mesmo nome e do mesmo tipo, diferenciadas apenas por um índice. Não estamos falando dos vetores da GEOMETRIA ANALÍTICA.

Uma matriz é uma variável composta homogênea multidimensional. Ela é formada por uma sequência de variáveis, todas do mesmo tipo, com o mesmo identificador (mesmo nome), e alocadas sequencialmente na memória. Uma vez que as variáveis têm o mesmo nome, o que as distingue são índices que referenciam sua localização dentro da estrutura. Uma variável do tipo matriz precisa de um índice para cada uma de suas dimensões. (ASCENCIO; CAMPOS, 2012, p. 194)

A matriz é declarada juntamente com as outras variáveis, conforme sintaxe a seguir:

```javascript
  var nome_da_variável: vetor[posição_inicial..posição_final, posição_inicial..posição_final] de tipo_dos_dados
```

A seguir alguns exemplos de matrizes:

![[tda2-06-fig06.webp]]

Acima, podemos ver a criação de uma matriz chamada mat, que possui 15 posições, ou seja, possui 3 linhas e 5 colunas.

![[tda2-06-fig07.webp]]

Acima, podemos ver a criação de uma matriz chamada X, que possui 4 posições, ou seja, possui 2 linhas e 2 colunas.

Para atribuir valores às posições das matrizes, é necessário colocar o nome da matriz e suas posições (linha e coluna) entre colchetes, conforme exemplos abaixo:

![[tda2-06-fig08.webp]]

É possível utilizar estruturas de repetição aninhadas com variável de controle para carregar todas as posições de uma matriz, conforme exemplo a seguir:

```
  // a variável i será utilizada como primeiro índice, ou
seja, linha
  // a variável j será utilizada como segundo índice, ou
seja, coluna
  para i <- 1 até 3 faça [passo 1]
      para j <- 1 até 5 faça [passo 1]
      escreval ("Digite o número da linha",i," coluna ",j)
      leia (mat[i,j])
      fimpara
  fimpara
```

Os valores assumidos pela variável i estão dentro do intervalo de 1 a 3, ou seja, exatamente o número das linhas da matriz. Por esta razão, a variável i é utilizada para indicar a primeira dimensão, dentro dos colchetes. Para cada valor assumido por i, a variável j assume os valores no intervalo de 1 a 5, ou seja, exatamente o número das colunas. Por esta razão, a variável j é utilizada para indicar a segunda dimensão, dentro dos colchetes. (ASCENCIO; CAMPOS, 2012, p. 196)

*Quadro 2 - Simulação das estruturas de repetição para carregar uma matriz*

|**MEMÓRIA**|**TELA**|
|---|---|---|
|i<br>j|||
|1<br>1|Digite  o  número  da  linha  1  e  coluna|1:  12|
|2|Digite  o  número  da  linha  1  e  coluna|2:  9|
|3|Digite  o  número  da  linha  1  e  coluna|3:  3|
|4|Digite  o  número  da  linha  1  e  coluna|4:  7|
|5|Digite  o  número  da  linha  1  e  coluna|5:  -23|
|2<br>1|Digite  o  número  da  linha  2  e  coluna|1:  15|
|2|Digite  o  número  da  linha  2  e  coluna|2:  4|
|3|Digite  o  número  da  linha  2  e  coluna|3:  2|

|**MEMÓRIA**|**TELA**|
|---|---|---|
|4|Digite  o  número  da  linha  2  e  coluna|4:  34|
|5|Digite  o  número  da  linha  2  e  coluna|5:  -4|
|3<br>1|Digite  o  número  da  linha  3  e  coluna|1: 3|
|2|Digite  o  número  da  linha  3  e  coluna|2: 45|
|3|Digite  o  número  da  linha  3  e  coluna|3: 3|
|4|Digite  o  número  da  linha  3  e  coluna|4:  0|
|5|Digite  o  número  da  linha  3  e  coluna|5:  -3|
||Fonte: Ascencio e Campos (2012, p. 196)||

Assim, podemos imaginar os elementos dispostos em uma estrutura bidimensional, como uma tabela.

| 1              | 12  | 9   | 3   | 7   | -23 |     |
| -------------- | --- | --- | --- | --- | --- | --- |
| **Matriz mat** | 2   | 15  | 4   | 2   | 34  | -4  |
|                | 3   | 3   | 45  | 3   | 0   | -3  |
|                |     | 1   | 2   | 3   | 4   | 5   |

Da mesma forma que utilizamos estruturas de repetição aninhadas para passar por todas as posições de uma matriz para carregá-las com dados digitados pelo usuário, usamos estruturas de repetição aninhadas para mostrar os dados armazenados na matriz, conforme exemplo abaixo:

```
para i <- 1 até 3 faça [passo 1]
   para j <- 1 até 5 faça [passo 1]
   escreval ("Conteúdo da linha ",i," coluna ",j)
   escreval (mat[i,j])
   fimpara
fimpara
```

As matrizes são conhecidas como variáveis homogêneas multidimensionais, ou seja, são variáveis com o mesmo nome e o mesmo tipo, mas diferenciadas por seus índices. Assim, não podemos usar uma matriz para armazenar os dados de um aluno, pois os dados de um aluno são: código do inteiro e nome do tipo literal.

A seguir, há um exemplo de algoritmo utilizando matriz. O algoritmo deve receber 6 números digitados pelo usuário, armazenando-os em uma matriz 3 X 2. Em seguida, deve mostrar qual o maior número digitado.

![[tda2-06-fig09.webp]]

*Figura 2 - Fluxograma do algoritmo exemplo de matriz*

A seguir, há um algoritmo exemplo em pseudocódigo:

```javascript
algoritmo "exemplo2"
// Função: receber 6 números, armazenar em uma matriz
// mostrar o maior
// Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
// Data: 24/12/2018 /*07/02/2020
// seção de declarações de variáveis e constantes
var m: vetor[1..3, 1..2] de inteiro
i, j, maior: inteiro
inicio
para i <- 1 até 3 faça [passo 1]
     para j <- 1 até 2 faça [passo 1]
          leia (m[i,j])
     fimparafimparamaior <- m[1,1]
para i <- 1 até 3 faça [passo 1]
     para j <- 1 até 2 faça [passo 1]
          se (m[i,j] > maior) então
             maior <- m[i,j]
          fimse
     fimparafimparaescreval (maior)
fimalgoritmo
```

Quando falamos em matrizes em algoritmos e em programação de computadores, estamos falando de uma variável capaz de armazenar uma quantidade finita de variáveis, todas com o mesmo nome e do mesmo tipo, diferenciadas apenas por seus  índices. Não estamos falando das matrizes da GEOMETRIA ANALÍTICA, apesar de ambas apresentarem a mesma estrutura de armazenamento.

Observe a Figura 3, a seguir, que representa as duas estruturas estudadas nesta Unidade VI, ou seja, vetores e matrizes.

![[tda2-06-fig10.webp]]

*Figura 3 - Vetores e Matrizes*

*Fonte: sn333g / 123RF*

Com a utilização das estruturas do tipo vetores e matrizes, podemos desenvolver algoritmos que necessitem do armazenamento, mesmo que temporário, de conjuntos de dados, sem a necessidade de declarar uma variável específica para cada elemento do conjunto.
