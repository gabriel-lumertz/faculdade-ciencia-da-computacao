---
materia: "Técnica de Desenvolvimento e Algoritmos"
modulo: "Conceito de Lógica Aplicada a Programas"
semestre: 2
unidade: 1
tipo: material-teorico
fonte: "raw/2-semestre/TÉCNICA DE DESENVOLVIMENTO E ALGORITMOS/TDA 01.pdf"
tags: [faculdade, tecnica-de-desenvolvimento-e-algoritmos, semestre-2]
aliases: ["Técnica de Desenvolvimento e Algoritmos - Unidade 1"]
---

# Conceito de Lógica Aplicada a Programas

## Tópicos da Unidade

- **Definição de Algoritmo;**

- **Técnicas para o Desenvolvimento de Algoritmos.**

## Objetivos de Aprendizado

- Conceituar ALGORITMO, descrever os três tipos mais utilizados de ALGORITMOS e mostrar alguns exemplos de ALGORITMOS utilizando esses três tipos.

## Definição de Algoritmo

O computador é um dispositivo eletrônico importante e muito útil nos dias atuais, pois tem a finalidade de receber, manipular e armazenar dados.

A finalidade de um computador é realizar o PROCESSAMENTO DE DADOS, ou seja, receber dados por um dispositivo de entrada (por exemplo, teclado, mouse, scanner, entre outros), realizar operações com esses dados e gerar uma resposta que será exibida em um dispositivo de saída (por exemplo, impressora, monitor de vídeo, entre outros). (ASCENCIO, 1999, p. 1)

Portanto, para realizar o PROCESSAMENTO DE DADOS, o computador precisa de duas partes diferentes que trabalham juntas: o _hardware_ , composto pelas partes físicas, e o _software_ , composto pelos programas.

Quando existe a necessidade de execução de um determinado tipo de PROCESSAMENTO DE DADOS, será preciso desenvolver um software e, para que o computador compreenda e execute esse software, devemos escrevê-lo utilizando uma linguagem entendível pelo computador e pelo desenvolvedor, ou seja, devemos usar as chamadas LINGUAGENS DE PROGRAMAÇÃO.

Segundo Ascencio e Campos (2012, p. 1), as etapas para o desenvolvimento de um programa são: análise, algoritmo e codificação.

- Análise – Nesta etapa, estuda-se o enunciado do problema para definir os dados de entrada, o processamento e os dados de saída;

- Algoritmo – Ferramentas do tipo descrição narrativa, fluxograma ou português estruturado são utilizadas para descrever o problema com suas soluções;

- Codificação – O algoritmo é transformado em códigos da linguagem de programação escolhida para se trabalhar.

Portanto, um programa é a codificação de um algoritmo em uma linguagem de programação. (ASCENCIO; CAMPOS, 2012, p. 1)

O texto a seguir apresenta a definição de algoritmos, segundo alguns autores consagrados na área de programação de computadores.

“Algoritmo é uma sequência de passos que visa atingir um objetivo bem definido” (FORBELLONE, 2005, p. 3).

“Algoritmo é a descrição de uma sequência de passos que deve ser seguida para a realização de uma tarefa” (ASCENCIO, 1999, p. 2).

“Um algoritmo representa um conjunto de regras para a solução de um problema” (FURLAN DE SOUZA et al., 2011, p. 4).

“Algoritmo é um processo de cálculo matemático ou de resolução de um grupo de problemas semelhantes” (MANZANO, 2004, p. 6).

Ação é um acontecimento que, a partir de um estado inicial, após um período de tempo finito, produz um estado final previsível e bem definido. Portanto, um algoritmo é a descrição de um conjunto de comandos que, obedecidos, resultam numa sucessão finita de ações (FARRER, 1999, p. 3).

Neste ponto, você deve estar pensando: já vi isso em outro momento da minha vida escolar! Então, é importante salientar que estamos falando de ALGORITMO, e não de LOGARITMO.

Analisando as definições anteriores, podemos perceber que executamos, no dia a dia, vários algoritmos, como se pode observar nos exemplos a seguir, extraídos de Ascencio e Campos (2012, p. 2).

ALGORITMO 1 –  FAZER UM SANDUÍCHE

Passo 1 – PEGAR  O  PÃO E A FACA.

Passo 2 – CORTAR  O  PÃO  AO  MEIO.

Passo 3 – PEGAR  A  MAIONESE.

Passo 4 – PASSAR  A  MAIONESE, COM O AUXÍLIO DA FACA,  NO  PÃO.

Passo 5 – PEGAR  E  CORTAR  ALFACE  E  TOMATE.

Passo 6 – COLOCAR  ALFACE  E  TOMATE  NO  PÃO.

Passo 7 – PEGAR  O  HAMBÚRGUER.

Passo 8 – FRITAR  O  HAMBÚRGUER.

Passo 9 – COLOCAR  O  HAMBÚRGUER  NO  PÃO.

ALGORITMO 2 – TROCAR UMA LÂMPADA

Passo 1 – PEGAR  UMA  LÂMPADA  NOVA.

Passo 2 – PEGAR  UMA  ESCADA.

Passo 3 – POSICIONAR  A  ESCADA  EMBAIXO  DA  LÂMPADA  QUEIMADA. Passo 4 – SUBIR  NA  ESCADA  COM  A  LÂMPADA  NOVA  NA  MÃO.

Passo 5 – RETIRAR  A  LÂMPADA  QUEIMADA.

Passo 6 – COLOCAR  A  LÂMPADA  NOVA.

Passo 7 – DESCER  DA  ESCADA.

Passo 8 – TESTAR  O  INTERRUPTOR.

Passo 9 – GUARDAR  A  ESCADA.

Passo 10 – JOGAR  A  LÂMPADA  VELHA  NO  LIXO.

ALGORITMO 3 – IR PARA A ESCOLA

Passo 1 – ACORDAR  CEDO.

Passo 2 – IR  AO  BANHEIRO.

Passo 3 – ABRIR  O  ARMÁRIO  PARA  ESCOLHER  UMA  ROUPA.

Passo 4 – SE  O  TEMPO  ESTIVER  QUENTE,  PEGAR  UMA  CAMISETA E  UMA  CALÇA JEANS;  CASO  CONTRÁRIO,  PEGAR  UM  AGASALHO  E UMA  CALÇA  JEANS.

Passo 5 – VESTIR  A  ROUPA  ESCOLHIDA.

Passo 6 – TOMAR  CAFÉ.

Passo 7 – PEGAR  UMA  CONDUÇÃO.

Passo 8 – DESCER  PRÓXIMO  À  ESCOLA.

##### ALGORITMO 4 – SACAR DINHEIRO NO BANCO 24 HORAS

Passo 1 – IR  ATÉ  UM  BANCO  24  HORAS.

Passo 2 – COLOCAR  O  CARTÃO.

Passo 3 – DIGITAR  A  SENHA.

Passo 4 – SOLICITAR  A  QUANTIA  DESEJADA.

Passo 5 – SE  O  SALDO  FOR  MAIOR  OU  IGUAL  À  QUANTIA  DESEJADA,  SACAR;  CASO  CONTRÁRIO,  MOSTRAR  MENSAGEM  DE  IMPOSSIBILIDADE  DE  SAQUE.

Passo 6 – RETIRAR  O  CARTÃO.

Você pode estar pensando: “Mas eu realizo essas atividades de maneira diferente!”. Esse pensamento está correto, pois, às vezes, um problema pode ser resolvido de diversas maneiras, porém gerando a mesma resposta, ou seja, podem existir vários algoritmos para solucionar o mesmo problema.

Para Ascencio e Campos (2012, p. 3), a construção de qualquer tipo de algoritmo exige as etapas descritas a seguir:

Compreender completamente o problema a ser resolvido, destacando os pontos mais importantes e os objetos que o compõem.

Definir os dados de entrada, ou seja, quais dados serão fornecidos e quais objetos fazem parte desse cenário problema.

Definir o processamento, ou seja, quais cálculos serão efetuados e quais as restrições para esses cálculos. O processamento é responsável pela transformação dos dados de entrada em dados de saída. Além disso, deve-se verificar quais objetos são responsáveis pelas atividades.

Definir os dados de saída, ou seja, quais dados serão gerados depois do processamento.

Construir o algoritmo utilizando um dos tipos descritos na próxima seção.

Testar o algoritmo realizando simulações.

## Técnicas para o Desenvolvimento de Algoritmos

Na literatura, estão descritas algumas técnicas utilizadas para o desenvolvimento de algoritmos e as três mais conhecidas e utilizadas são: descrição narrativa, fluxograma e pseudocódigo, também conhecido como portugol.

A DESCRIÇÃO NARRATIVA é a técnica que analisa o enunciado do problema e escreve, utilizando uma linguagem natural (por exemplo, a língua portuguesa), os passos a serem seguidos para sua resolução. A vantagem da descrição narrativa é que, por utilizar uma linguagem natural, não é preciso aprender nenhuma outra nova linguagem. Em compensação, tem-se a desvantagem de que as linguagens naturais permitem várias interpretações, além de serem muito diferentes das linguagens de programação, o que dificulta a transcrição de um algoritmo para um programa.

O fluxograma consiste em analisar o enunciado do problema e escrever, utilizando símbolos gráficos pré-definidos na Tabela 1, os passos a serem seguidos para sua resolução. A vantagem do fluxograma é que a utilização de elementos gráficos permite a fácil compreensão dos elementos que compõem o Processamento de Dados, ou seja, são facilmente identificadas as entradas, o processamento e as saídas. Em compensação, tem-se a desvantagem  de ter de aprender a simbologia dos fluxogramas e, normalmente, a falta de detalhes dificulta a transcrição para um programa utilizando uma linguagem de programação.

*Tabela 1 - Conjunto  de  símbolos  utilizados  no  fluxograma*

![[tda2-01-fig01.webp]]

![[tda2-01-fig02.webp]]

![[tda2-01-fig03.webp]]

*Fonte: Ascencio e Campos (2012)*

O pseudocódigo ou portugol é a técnica mais utilizada e analisa o enunciado do problema escrevendo, por meio de regras predefinidas, também conhecidas como códigos, os passos a serem seguidos para sua resolução. A vantagem da utilização do pseudocódigo é que a passagem do algoritmo para uma linguagem de programação é quase direta, consistindo, na grande maioria das vezes, em uma espécie de tradução. Em compensação, a desvantagem está na necessidade de se aprender as regras do pseudocódigo.

Observe o infográfico a seguir.

![[tda2-01-fig04.webp]]

![[tda2-01-fig05.webp]]

![[tda2-01-fig06.webp]]

*Figura 1 - Técnicas para o desenvolvimento de algoritmos Fonte: Viktor Bondar / 123RF*

O objetivo do algoritmo é estruturar a solução de um problema, assim, não há tipo mais apropriado, pois cabe, ao desenvolvedor, definir o tipo mais adequado para o seu entendimento. Neste material, utilizaremos os fluxograma e o português estruturado. O fluxograma, por utilizar elementos gráficos, o que facilita o entendimento, bem como o português estruturado, porque permite utilizar uma ferramenta denominada VisualG e, com essa ferramenta, é possível verificar a corretude das soluções adotadas.

Os exemplos a seguir mostram alguns algoritmos desenvolvidos com os três tipos citados anteriormente em Ascencio e Campos (2012, p. 4).

ALGORITMO 1 - Faça um algoritmo para mostrar o resultado da multiplicação de dois números.

Algoritmo em descrição narrativa:

Passo 1 – RECEBER  OS  DOIS  NÚMEROS QUE SERÃO MULTIPLICADOS. Passo 2 – MULTIPLICAR OS  NÚMEROS.

Passo 3 – MOSTRAR  O  RESULTADO  OBTIDO.

Algoritmo em fluxograma:

![[tda2-01-fig07.webp]]

*Figura 2 - Fluxograma do algoritmo que multiplica dois números*

##### Algoritmo em pseudocódigo:

```javascript
algoritmo "exemplo1"
// Função: multiplicar dois números
// Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
// Data: 24/12/2018 /*07/02/2020
// seção de declarações de variáveis e constantes
var n1, n2, m: real
inicio
      escreval ("digite dois números")
      leia (n1)
      leia (n2)
      m <- n1 * n2
      escreva ("Multiplicação = ",m)
fimalgoritmo
```

ALGORITMO 2 - Faça um algoritmo para mostrar o resultado da divisão de dois números.

Algoritmo em descrição narrativa:

Passo 1 – Receber os dois números que serão divididos.

Passo 2 – Se o segundo número for igual a zero, não poderá haver divisão, pois não existe divisão por zero, caso contrário, dividir os números e mostrar o resultado da divisão.

##### Algoritmo em fluxograma:

![[tda2-01-fig08.webp]]

*Figura 3 - Fluxograma do algoritmo para calcular a divisão entre dois números*

##### Algoritmo em pseudocódigo:

```javascript
algoritmo "exemplo2"
// Função: calcular a divisão de dois números
// Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
// Data: 24/12/2018 /*07/02/2020
// seção de declarações de variáveis e constantes
var n1, n2, d: real
inicio
      escreval ("digite dois números")
      leia (n1)
      leia (n2)
      se n2 = 0 entao
         escreva ("impossível dividir")
         senao
         d <- n1 / n2
      escreva (d)
      fimsefimalgoritmo
```

ALGORITMO 3 - Faça um algoritmo para calcular a média aritmética entre duas notas de um aluno e mostrar sua situação, sendo este aluno aprovado ou reprovado.

Algoritmo em descrição narrativa:

Passo 1 – Receber as duas notas.

Passo 2 – Calcular a média aritmética.

Passo 3 – Mostrar a média aritmética.

Passo 4 – Se a média aritmética for maior ou igual a sete, então, a situação do aluno é aprovado, caso contrário, a situação é reprovado.

##### Algoritmo em fluxograma:

![[tda2-01-fig09.webp]]

*Figura 4 - Fluxograma para calcular a média aritmética*

##### Algoritmo em pseudocódigo:

```javascript
  algoritmo "exemplo3"
  // Função: calcular a média aritmética entre duas notas e
mostrar a
  // Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
  // Data: 24/12/2018 /*07/02/2020
  // Data: 24/12/2018
  // seção de declarações de variáveis e constantes
  var nota1, nota2, m: real
  inicio
        escreval ("digite as duas notas")
        leia (nota1)
        leia (nota2)
  m <- (nota1+nota2)/2
  escreval("media = ",m)
  se (m >= 7) entao
     escreval ("Aprovado")
  senao
     escreval ("Reprovado")
  fimse
  fimalgoritmo
```

ALGORITMO 4 - Faça um algoritmo para calcular o novo salário de um funcionário. Sabe-se que os funcionários que possuem salário atual até R$ 500,00 terão aumento de 20%; os demais terão aumento de 10%.

Algoritmo em descrição narrativa:

Passo 1 – Receber o salário atual do funcionário.

Passo 2 – Se o salário atual do funcionário for até R$ 500,00, então, calcular o novo salário com percentual de aumento de 20%, caso contrário, calcular o novo salário com percentual de aumento de 10%.

Passo 3 – Mostrar o novo salário.

Algoritmo em fluxograma:

![[tda2-01-fig10.webp]]

*Figura 5 - Fluxograma para calcular o salário reajustado*

##### Algoritmo em pseudocódigo:

```javascript
algoritmo "exemplo4"
// Função: calcular o salário reajustado
// Autor: Ana Fernanda /*revisão Margarete E. S. Almendro
// Data: 24/12/2018 /*07/02/2020
// seção de declarações de variáveis e constantes
var sal_atual, novo_sal: real
inicio
      escreval ("digite o salário atual")
      leia (sal_atual)
      se (sal_atual <= 500) entao
         novo_sal <- sal_atual * 1.20
      senao
         novo_sal <- sal_atual * 1.10
      fimse
      escreval("novo salário = ",novo_sal)
fimalgoritmo
```

Os exemplos acima, tente fazer um algoritmo para calcular a diferença entre dois números e mostrar a mensagem de resultado POSITIVO, NEGATIVO ou ZERO.
