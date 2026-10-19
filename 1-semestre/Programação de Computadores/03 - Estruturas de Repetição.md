---
materia: "Programação de Computadores"
modulo: "Estruturas de Repetição"
semestre: 1
unidade: 3
tipo: material-teorico
fonte: "raw/1-semestre/PROGRAMAÇÃO DE COMPUTADORES/Programação de computadores 03.pdf"
tags: [faculdade, programacao-de-computadores, semestre-1]
aliases: ["Programação de Computadores - Unidade 3"]
---

# Estruturas de Repetição

#### Estruturas de Repetição ( Loop )

Em programação de computadores, uma estrutura de repetição ( _loop_ ) é uma sequência de instruções que é continuamente repetida até que uma determinada condição seja alcançada. _Loops_ estão entre os mais básicos e poderosos conceitos de programação.

Os programadores usam _loops_ para percorrer valores, somar números, repetir funções ou instruções de códigos e muitas outras coisas.

Estruturas de repetição ( _loop_ ) são semelhantes às estruturas condicionais ( _if, else_ etc.), contudo, ao contrário de uma instrução _if_ , que apenas avalia uma condição uma única vez, um _loop_ será executado várias vezes até que a condição retorne um valor falso.

_Loops_ são suportados por todas as linguagens de programação modernas, embora suas implementações e sintaxe possam ser diferentes. Em Python temos dois tipos de estruturas de repetição: _for_ e _while_ .

**_for_** _:_ é um loop que é executado por um número predefinido de vezes;

**_while_** _:_ é um loop que é repetido enquanto uma expressão for verdadeira.

### Leitura

**_Loop for_ – Estruturas de Repetição em** **_Python_**

**ACESSE**

#### Estrutura de Repetição for

Estruturas de repetição do tipo **_for_** são excelentes quando temos um número predefinido de repetições, ou seja, quando temos um número finito de repetições a serem executadas.

A sintaxe para a estrutura _for_ é:

![[pc1-03-fig01.webp]]

**Figura 1**

**Variável** : refere-se à variável de iteração. É por meio dessa variável que identificamos a sequência de repetição durante a execução do _Loop_ . Essa variável irá iterar de acordo com a faixa de valores declarada;

**Faixa de valores** : esse parâmetro corresponde à faixa de valores ou quantidade de repetições que a estrutura irá executar. Esse parâmetro pode ser uma _string_ , uma lista, um dicionário, uma tupla ou um objeto que permita iterações.

Por exemplo, imaginemos um cenário onde desejamos que nosso programa faça uma sequência progressiva de cinco (5) adições, acrescentando sempre 3 ao resultado da soma anterior. Em Python temos algo do tipo:

**Código:**

```python
soma = 0
for i in (0,1,2,3,4):
    soma = soma +3
    print(soma)
```

**Figura 2**

*Fonte: Acervo do Conteudista*

**Saída:**

```text
3
6
9
12
15
```

**Figura 3** Fonte: Acervo do Conteudista

#### Explicando o Código

**Linhas 1** : declaramos uma variável com o nome de “soma” e atribuímos o valor “0” para ela;

**Linha 2** : assinatura da instrução for. Como variável para iteração, declaramos a variável “i”, em seguida declaramos a cláusula obrigatória **_in_** e por fim, declaramos a sequência numérica a ser percorrida. Nesse caso, entre 0 e 4;

**Linha 3** : a cada repetição, a variável “soma” acumulará o valor contido

anteriormente mais (+) o valor 3. Dessa forma, ao final de 5 repetições, teremos uma progressão aritmética;

**Linha 4** : após atualização do valor contido na variável “soma”, utilizamos a função _print_ para exibir o resultado na tela.

É importante ressaltar que a instrução _for_ , no Python, irá percorrer por todos a sequência declarada no parâmetro de faixa de valores, assim, uma _string_ com 5 caracteres fará com que nosso for seja executado 5 vezes, em uma sequência com 10 números, o _for_ será executado 10 vezes, e assim por diante. Vejamos o exemplo a seguir, onde temos como parâmetro para a faixa de valores, 6 valores aleatórios.

```python
for i in (2,5,9,56,4,58):
    print(i)
```

**Figura 4** Fonte: Acervo do Conteudista

Saída:

```text
2
5
9
56
4
58
```

**Figura 5**

*Fonte: Acervo do Conteudista*

**Linha 1** : assinatura da instrução _for_ . Como variável para iteração, declaramos a variável “i”, em seguida declaramos a cláusula obrigatória **_in_** e por fim, declaramos a sequência numérica de seis números (aleatória) a ser percorrida;

**Linha 2** : a cada repetição, utilizamos a função _print_ para exibir na tela o valor contido na variável de iteração “i”. É importante ressaltar que como a faixa de valores possui 6 números, o _for_ executará 6 repetições.

Comumente, para uma sequência finita, é utilizado em _Python_ a função _range_ , uma função que gera uma sequência numérica. A sintaxe dessa função é:

![[pc1-03-fig06.webp]]

**Figura 6**

A seguir, temos um código que exibe na tela uma contagem progressiva de 5 números entre 0 e 4.

**Código:**

```python
for i in range(5):
    print(i)
```

###### Figura 7

*Fonte: Acervo do Conteudista*

**Saída:**

```text
0
1
2
3
4
```

###### Figura 8

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Linha 1** : assinatura da instrução _for_ . Como variável para iteração, declaramos a variável “i”. Para a função “ _range_ ”, declaramos que o fim da sequência será o número 5, contudo, como explicado, esse número não é incluso na sequência;

**Linha 2** : a cada repetição, utilizamos a função _print_ para exibir na tela o valor contido na variável de iteração “i”. É importante ressaltar que conforme o parâmetro da função “ _range_ ” (5), será criada uma sequência entre 0 e 4 e assim, o _for_ executará 5 repetições.

Vejamos outro exemplo, criaremos agora um programa que exibirá uma progressão numérica de zero (0) à quinze (15) tendo como incremento o valor 2. Ou seja, nosso programa irá exibir uma progressão aritmética de razão 2. Para tanto, iremos usar a estrutura **_for_** com a cláusula _range_ configurando o parâmetro de incremento para 2.

Codigo:

```python
for i in range(0,15,2):
    print(i)
```

**Figura 9**

*Fonte: Acervo do Conteudista*

Saída:

```text
Result
CPU Time: 0.02 sec(s), Memory: 7800 kilobyte(s)

0
2
4
6
8
10
12
14
```

**Figura 10** Fonte: Acervo do Conteudista

#### Explicando o Código

**Linha 1** : assinatura da instrução _for_ . Como variável para iteração, declaramos a variável “i”. Para a função “ _range_ ”, declaramos que o fim da sequência será o número 15 (segundo parâmetro), contudo, como explicado, esse número não é incluso na sequência. Diferente do exemplo anterior, configuramos o incremento (terceiro parâmetro) para o valor 2. Assim, a cada repetição do _for_ , o valor de “i” será somado com o valor +2;

**Linha 2** : a cada repetição, utilizamos a função _print_ para exibir na tela o valor contido na variável de iteração “i”. É importante ressaltar que conforme o parâmetro da função “ _range_ ” (15), será criada uma sequência entre 0 e 14, porém, como o

incremento está configurado para somar o valor +2 a cada repetição, serão executadas a quantidade de repetições possíveis entre 0 e 14 em uma progressão de múltiplos de 2. Assim, temos 8 repetições, que é a quantidade de números múltiplos de 2 dentro da sequência de 0 a 14.

**Leitura Progressão Aritmética**

**ACESSE**

É importante destacar que dentro de um bloco de instruções em uma estrutura de repetição, podemos, por exemplo, utilizar estruturas de decisão. Vejamos um exemplo. Devemos criar um programa que dado uma sequência numérica progressiva (de 0 a 30), identifique quais números dessa sequência são múltiplos de 3.

Código:

```python
qtdMultiplos = 0
for i in range(1,30):
    if(i%3==0):
        qtdMultiplos+=1
        print(i)

print("A quantidade de números divisíveis por 3 na sequência de 1 a 30 é",qtdMultiplos )
```

**Figura 11** Fonte: Acervo do Conteudista

Saída:

```text
3
6
9
12
15
18
21
24
27
A quantidade de números divisíveis por 3 na sequência de 1 a 30 é 9
```

**Figura 12**

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “qtdMultiplos” e atribuímos o valor “0” para ela;

**Linha 2** : assinatura da instrução for. Como variável para iteração, declaramos a variável “i”, em seguida, por meio da função “ _range_ ”, configuramos uma sequência numérica até o número 30 a partir do número 1;

**Linha 3** : a cada repetição, essa linha é executada, e dessa forma, é testada a condição. Se o número atual da sequência (contido na variável “i”) dividido por três, resultar seu **resto** (por isso o operador de módulo) em zero, o número é divisível por 3 e assim, as linhas 4 e 5 serão executadas;

**Linha 4** : ao ser executada, essa linha adiciona “+1” para o valor atribuído à variável “qtdMultiplos”;

**Linha 5** : utilizamos a função _print_ para exibir na tela o valor contido na variável de iteração “i”;

**Linha 7** : ao final do _for_ , ou seja, após concluir todas as repetições da estrutura, essa linha será executada. Utilizamos a função _print_ para exibir na tela o valor contido na variável “qtdMultiplos”.

Por meio da estrutura _for_ , podemos, por exemplo, percorrer todos os caracteres contidos em uma variável com valor do tipo _string_ . Vejamos um exemplo.

Código:

```python
minhaString = "ABCDEFGH"

for x in minhaString:
    print(x)
```

**Figura 13**

*Fonte: Acervo do Conteudista*

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 7716 kilobyte(s)

A
B
C
D
E
F
G
H
```

**Figura 14** Fonte: Acervo do Conteudista

#### Explicando o Código

Temos na linha 1 a declaração da variável e a atribuição de um valor do tipo _string_ . Na linha 3, temos a assinatura da instrução _for_ , como variável para iteração, declaramos a variável “x”, em seguida, logo após a cláusula **_in_** , descrevemos a variável “minhaString”. Por ser um tipo _string_ , a estrutura _for_ é capaz de percorrer toda a cadeia de caracteres que formam o valor _string_ e dessa forma, um a um, cada caractere é acessado e visualizado na tela por meio da função _print_ .

### Leitura

**Estrutura de repetição PARA (** **_For_ )**

**ACESSE**

#### Estrutura de Repetição while

Estruturas de repetição do tipo _while_ são utilizadas quando em nosso código devemos repetir um trecho de código ou instruções. Estruturas de repetição _while_ são criadas escrevendo a palavrachave _while_ , seguida de uma condição (como em uma instrução _if_ ) e, em seguida, do código que deseja executar.

### Leitura

**Estrutura de repetição ENQUANTO (** **_While_ )**

**ACESSE**

A sintaxe para a estrutura _while_ é:

![[pc1-03-fig15.webp]]

**Figura 15** Fonte: Acervo do Conteudista

Para o início de nossos estudos com a estrutura _while_ , vamos criar um programa que exibe na tela uma contagem progressiva de 1 a 5. Assim, temos o seguinte código.

Código:

```python
contador = 0
while (contador < 5):
    contador+=1
    print(contador)
```

**Figura 16** Fonte: Acervo do Conteudista

Saída:

```text
1
2
3
4
5
```

**Figura 17**

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “contador” e atribuímos o valor “0” para ela. Essa será a variável para iteração, será utilizada como **variável de controle** ;

**Linha 2** : assinatura da instrução _while_ . Declaramos a condição (contador < 5). Essa condição faz com que a instrução _while_ continue a executar enquanto o valor contido na variável “contador” seja um número menor que 5;

**Linha 3** : a cada repetição, a variável “contador” acumulará o valor contido anteriormente mais (+) o valor 1. Dessa forma, ao final de 5 repetições, teremos uma progressão aritmética;

**Linha 4** : após atualização do valor contido na variável “contador”, utilizamos a função _print_ para exibir o resultado na tela.

Em muitos cenários, o algoritmo exige que se repita um certo trecho de código, contudo sem a informação sobre em qual momento a repetição será finalizada. Desse modo, é escrito um código onde dada uma condição, o processo de repetição é finalizado. Vejamos um exemplo. Temos um cenário onde nosso programa deve solicitar que o usuário digite um nome até que seja digitado o número zero (0). Seguimos com o código em _Python_ .

Código:

```python
nome = ""
while True:
    texto = input("Digite um nome ou '0' para encerrar o programa ")

    if(texto == "0"):
        print("Programa finalizado")
        break
    else:
        nome = nome + texto +"\n"

print(nome)
```

**Figura 18**

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “nome” e atribuímos o valor “ ”, ou seja, vazio. Essa será a variável que irá armazenar os nomes digitados pelo usuário do programa;

**Linha 2** : assinatura da instrução _while_ . Diferente do _while_ anterior, não é declarada uma condição com algum operador lógico, apenas a palavra reservada “ _True_ ”, dessa forma, forçamos o _while_ a continuar executando de forma infinita ou até que alguma ação faça o _while_ finalizar;

**Linha 3** : a cada repetição, é solicitado ao usuário do programa que digite um nome ou o número zero. O valor digitado é atribuído para a variável “texto”;

**Linha 5** : caso o valor contido na variável “texto” seja igual a zero (0), as linhas 6 e 7 serão executadas. Ressaltamos aqui que a instrução “ **_break_** ” quando executada em um _while_ , executará a parada desse _loop;_

**Linha 9** : essa linha será executada enquanto o usuário do programa digitar textos diferentes de zero (0). Ao ser executada, essa linha armazenará na variável “nome” o valor digitado adicionando com o valor contido nessa variável anteriormente. Por fim, adiciona um caractere de quebra de linha “\n”;

**Linha 11** : essa linha será executada quando o _while_ encerrar, ou seja, quando o usuário digitar zero (0). Utilizamos a função _print_ para exibir na tela os valores contidos na variável “nome”.

Podemos criar uma outra solução para o problema anterior utilizando uma variável do tipo _Boolean_ como condição do _While_ , mas diferente do código anterior, essa variável pode mudar de estado (de verdadeiro para falso), assim, quando diferente de verdadeiro, irá encerrar o programa.

Código:

```python
nome = ""
continuar = True
while continuar:
    nome = nome + input("Digite um nome ") + "\n"

    x = input("Deseja continuar? Digite 'Sim' ou 'Não' ")

    if(x.upper() =="SIM"):
        continuar = True
    else:
        continuar = False

print(nome)
```

**Figura 19** Fonte: Acervo do Conteudista

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “nome” e atribuímos o valor “ ”, ou seja, vazio. Essa será a variável que irá armazenar os nomes digitados pelo usuário do programa;

**Linha 2** : declaramos uma variável com o nome de “continuar” e atribuímos o valor “ _True_ ”. Essa será a variável que iremos utilizar como condição para que a estrutura _while_ continue a executar repetições;

**Linha 3** : assinatura da instrução _while_ . Utilizamos a variável “continuar” como condição. Enquanto o valor dessa variável for verdadeiro ( _True_ ), o _while_ irá executar repetições;

**Linha 4** : a cada repetição, é solicitado ao usuário do programa que digite um nome. Ao ser executada, essa linha armazenará na variável “nome” o valor digitado juntando com o valor contido nessa variável anteriormente. Por fim, adiciona um caractere de quebra de linha “\n”;

**Linha 6** : é solicitado ao usuário do programa que digite “Sim” ou “Não” para expressar o desejo de continuar a executar o programa;

**Linha 8** : com a estrutura de decisão, testamos a condição: Se o valor contido na variável “x” for igual à “SIM” (note o texto como um valor em maiúsculo), será atribuído o valor “ _True_ ” para a variável “continuar”, caso contrário, será atribuído o valor “ _False_ ”. É importante ressaltar que garantimos que o valor contido em “x” seja um texto em maiúsculo utilizando a função “ _upper_ ()”. Por meio dessa sequência de instruções mudamos (ou mantemos) o estado da variável “continuar” e dessa forma, controlamos o _while_ acerca de sua execução;

**Linha 13** : essa linha será executada quando o _while_ encerrar, ou seja, quando o usuário digitar um valor diferente de “SIM”. Utilizamos a função _print_ para exibir na tela os valores contidos na variável “nome”.

### Leitura

**Funções Básicas com** **_Strings_ com** **_Upper Lower Title_**

**ACESSE**

Em alguns cenários é preciso não permitir que alguns trechos de código dentro da estrutura de repetição sejam executados. Porém, garantindo que a estrutura continue sendo executada, assim temos a cláusula _continue_ . Dentro de uma estrutura de repetição, ao ser executada, essa cláusula fará com que seja executada a primeira linha da estrutura de repetição, ignorando as demais linhas de códigos seguintes.

Vejamos um exemplo. Criaremos um programa que exibe uma sequência de números entre zero (0) e nove (9), porém, nosso programa não deve exibir os números 1 e 3.

Código:

```python
contador = 0

while contador < 10:
    if(contador == 1 or contador == 3):
        contador+=1
        continue

    print(contador)
    contador+=1
```

**Figura 20**

*Fonte: Acervo do Conteudista*

```text
Result
executed in 0.838 sec(s)

0
2
4
5
6
7
8
9
```

**Figura 21** Fonte: Acervo do Conteudista

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “contador” e atribuímos o valor “0” para ela. Essa será a variável para iteração, será utilizada como **variável de controle;**

**Linha 2** : assinatura da instrução _while._ Declaramos a condição (contador < 10). Essa condição faz com que a instrução _while_ continue a executar enquanto o valor contido na variável “contador” seja um número menor que 10;

**Linha 4** : por meio da estrutura de decisão, o programa verifica se o valor contido na variável “contador” é igual a “1” ou “3”. Caso verdadeiro, para essas duas situações, serão executadas as linhas 5 e 6;

**Linha 5** : cada vez que essa linha é executada é adicionando +1 ao valor contido na variável “contador”;

**Linha 6** : cada vez que essa linha é executada, a cláusula continue executa a primeira linha da estrutura de repetição. Assim, as linhas 8 e 9 não serão executadas;

**Linha 8** : ao ser executada, essa linha exibe por meio da função _print_ , o valor contido na variável “contador”;

**Linha 9** : é adicionando +1 ao valor contido na variável “contador”.

### Vídeo

**Repetição com** **_While_ +** **_Break_ e** **_Continue_**

Curso Python 3 | Aula 13 - Repetição com while + break e continue

### Exercício

**Escreva um programa que leia um grupo de valores (não sabemos quantos são) para calcular e visualizar a média desses valores e, também, determinar e visualizar o maior deles. Utilize uma estrutura de repetição** **_while_ ou** **_for_ .**

**Importante! Antes que leia a resposta para o desafio proposto, tente criar sua própria solução. Como sugestão, desenvolva primeiro o algoritmo, pode ser em pseudocódigo ou um fluxograma, o importante aqui é pensar no passo a passo para a resolução do problema, em seguida, implemente seu algoritmo na linguagem Python.**

##### Resolução

Seguimos com o seguinte código em _Python_ para a solução do desafio proposto.

```python
qtdvalores = int(input("Digite a quantidade de números que serão calculados "))
contador = 0
valor = 0
while contador < qtdvalores:
    valor += float(input("Digite um valor "))
    contador+=1

media = valor/ contador
print(media)
```

**Figura 22** Fonte: Acervo do Conteudista

### Leitura

**_Jdoodle – Online Python 3 IDE_**

**O código anterior pode ser visualizado por meio do** **_link_ a seguir.**

**ACESSE**

#### Explicando o Código

**Linha 1** : declaramos uma variável com o nome de “qtdvalores” e utilizamos a instrução **_input_** para solicitar ao usuário do programa a quantidade de números que serão calculados. Utilizamos a instrução **_int_** para converter o tipo _string_ para inteiro;

**Linha 2** : declaramos uma variável com o nome de “contador” e atribuímos o valor “0” para ela. Essa será a variável para iteração, será utilizada como **variável de controle;**

**Linha 3** : declaramos uma variável com o nome de “valor” e atribuímos o valor “0” para ela. Iremos utilizar essa variável para armazenar os valores digitados pelo usuário do programa;

**Linha 4** : assinatura da instrução _while_ . A condição para continuar a repetir a instrução _while_ é de que o valor contido na variável “contador” seja menor que o valor contido na variável “qtdvalores”, enquanto essa proposição for verdadeira, o _while_ continuará a executar;

**Linha 5** : a cada repetição, é solicitado ao usuário do programa que digite um valor. O valor digitado é atribuído para a variável “valor” adicionando (operação aritmética de adição +) com o valor contido anteriormente. Utilizamos a instrução _float_ para converter _string_ em _float;_

**Linha 6** : a cada repetição, a variável “contador” acumulará o valor contido anteriormente mais (+) o valor 1;

**Linha 8** : ao encerrar o _while_ , é realizado o cálculo da média. Para isso é realizado a divisão entre o valor contido na variável “valor” e a variável “contador”;

**Linha 9** : utilizamos a função _print_ para exibir na tela o valor contido na variável “media”.

### Leitura

**_Jdoodle – Online Python 3 IDE_ Segue também a solução do desafio utilizando a estruturar** **_for_ . Clique no botão para conferir o conteúdo.**

**ACESSE**

#### Em Síntese

Nesta Unidade, estudamos os conceitos e a implementação de estruturas de repetição. É importante que assista a videoaula desta unidade e que leia os livros e materiais complementares indicados nesta Unidade de estudo. É fundamental que além dos estudos em _Python_ , busque estudar ou retomar conceitos de desenvolvimento de algoritmos, em especial, o tema desta unidade.

Até a próxima.
