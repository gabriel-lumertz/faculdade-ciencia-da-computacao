---
materia: "Programação de Computadores"
modulo: "Estruturas de Dados"
semestre: 1
unidade: 4
tipo: material-teorico
fonte: "raw/1-semestre/PROGRAMAÇÃO DE COMPUTADORES/Programação de computadores 04.pdf"
tags: [faculdade, programacao-de-computadores, semestre-1]
aliases: ["Programação de Computadores - Unidade 4"]
---

# Estruturas de Dados

Anteriomente, aprendemos diversos conceitos de programação de computadores: variáveis, uso de operadores, estruturas de decisão e estruturas de repetição. Sempre quando precisamos, utilizamos variáveis, porém, podemos perceber que essas variáveis armazenam apenas um valor por vez. Para cada variável, podemos armazenar somente um valor.

Nesta Unidade, iremos estudar formas para armazenar diversos valores (N valores) em uma mesma variável. Esse conceito permitirá um salto de qualidade e eficiência em nossos códigos de programação. No estudo de algoritmos, chamamos esse conceito de vetores. Na linguagem _Python_ , temos: _Lists_ , _Dictionarys_ e _Tuples_ .

#### Vídeo

**Vetores – Curso de Algoritmos**

Vetores - Curso de Algoritmos #14 - Gustavo Guanabara

##### Listas

Uma lista é uma estrutura de dados em _Python_ que é uma sequência ordenada de elementos e mutável (pode ter seus valores atualizados). Cada elemento corresponde a um valor e é chamado de item e são definidos entre colchetes [ ].

Utilizamos listas quando precisamos trabalhar com muitos valores relacionados, pois elas permitem que se mantenham diversos dados juntos, crie um código mais intuitivo e execute métodos e operações em vários valores de uma só vez.

![[pc1-04-fig01.webp]]

*Figura 1*

**Itens (ou elemento):** são os valores armazenados dentro de cada posição da lista;

**Tamanho:** é o tamanho da lista (quantos itens possui a lista);

**Índice:** é a posição do elemento onde um valor está armazenado.

###### Declarando Listas e Atribuindo Valores

A forma de declaração de uma lista é muito parecida com a declaração de uma variável comum, contudo, os valores são indicados entre colchetes [] separando cada valor por vírgula. Vejamos um exemplo:

```
minhaLista = [1,2,3,4,5]
```

O código acima declara uma lista com o nome de “minhaLista” e atribui os valores 1, 2, 3, 4 e 5.

As regras para nomear listas em _Python_ seguem as mesmas regras de nomeação de variáveis comuns:

As variáveis podem ter letras (A-Z e a-z), dígitos (0-9) e sublinhados (_).

Não podem começar com números;

Não podem conter pontuação, caracteres especiais (!, @, $, #, etc) ou espaços;

Não podem ser utilizadas palavras reservadas da linguagem.

Para atribuição de valores em listas, no _Python_ , diferente de outras linguagens de programação, podemos armazenar tipos de dados diferentes em uma mesma variável.

```
minhaLista2 = [1, "Silva", 4.5]
```

No código acima, atribuímos valores de tipos diferentes, porém para a mesma variável.

Podemos armazenar valores de todos os tipos primitivos de dados do _Python_ : _string_ , _int_ , _float_ e _boolean_ , além de objetivos e outros tipos de dados.

Outra forma de criar uma lista e atribuir valores é criar uma lista vazia e por meio da _append_ , armazenar valores. A função _append_ adiciona um elemento sempre no final da lista.

Vejamos um exemplo:

```python
ListaNomes = []
ListaNomes.append("João")
ListaNomes.append("Maria")
ListaNomes.append("Anna")
ListaNomes.append("Clara")
```

**Figura 2**

*Fonte: Acervo do Conteudista*

##### Explicando o Código

**Linha 1:** declaramos a lista (vazia) com o nome de “ListaNomes”. Utilizamos colchetes para indicar que se trata de uma lista;

**Linha 2:** atribuímos o valor “João” para a lista “ListaNomes”;

**Linhas 3 a 5:** atribuímos valores à lista por meio da função _append_ .

Se desejarmos adicionar mais elementos à lista, bastaria seguir adicionando instruções _append_ .

Vejamos um exemplo onde criamos um programa capaz de armazenar N nomes em uma lista digitada pelo usuário. Damos ao usuário a possibilidade de seguir ou não cadastrando nomes nessa lista. Vamos ao código.

```python
ListaNomes = []

while True:
    nome = input("Digite um nome ")
    ListaNomes.append(nome)

    continuar = input("Deseja continuar? Digite Sim ou Não ")
    if(continuar=="Não" or continuar=="NÃO"):
        break

print(ListaNomes)
```

**Figura 3**

*Fonte: Acervo do Conteudista*

##### Explicando o Código

**Linha 1:** declaramos a lista (vazia) com o nome de “ListaNomes”. Utilizamos colchetes para indicar que se trata de uma lista;

**Linha 2:** assinatura da instrução _while_ . Como condição, declaramos a palavra reservada “ _True_ ”, dessa forma, forçamos o _while_ continuar executando de forma infinita ou até que alguma ação faça o _while_ finalizar;

**Linha 4:** solicitamos ao usuário que digite um nome e atribuímos o valor digitado à variável “nome”;

**Linha 5:** utilizamos a função _append_ para armazenar o valor contido na variável “nome” na lista (“ListaNomes”);

**Linha 7:** a cada repetição, é solicitado ao usuário do programa que digite “Sim” ou “Não”. O valor digitado é atribuído à variável “continuar”;

**Linha 8:** caso o valor contido na variável “continuar” seja igual a “Não” ou “NÃO”, o _while_ será encerrado (instrução _break_ na linha 9);

**Linha 9:** por meio da função _print_ , são exibidos os valores contidos na lista “ListaNomes”.

###### Acessando Elementos em uma Lista

Para acessar um elemento específico em uma lista, é preciso indicar o índice onde o elemento está armazenado. Chamamos de índice o valor inteiro que representa a posição do elemento que desejamos acessar.

Os índices em uma lista (ou vetor) sempre iniciam em zero (0). Isso significa que uma lista de 2 elementos, temos o índice 0 e índice 1. Nesse cenário, se tentarmos acessar o índice “2”, ao executar o programa, retornará um erro de execução, pois estamos tentando acessar um terceiro elemento (que não existe) na lista. Por exemplo, para obter qualquer item de uma lista, basta indicar o índice entre colchetes. Vejamos:

```python
minhaLista = [1,2]
print(minhaLista[0])
```

**Figura 4**

*Fonte: Acervo do Conteudista*

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 7548 kilobyte(s)

1
```

**Figura 5**

*Fonte: Acervo do Conteudista*

Explicando o código, na linha 1, temos a declaração da lista com a atribuição de valores. Na linha 2, dentro da função _print_ , descrevemos o nome da lista e, entre colchetes, indicamos o índice do elemento que desejamos visualizar.

Outra forma para acessar e visualizar os elementos de uma lista é por meio de uma estrutura de repetição **_for_** . Vejamos um exemplo:

```python
minhaLista3 = ["João", "Maria", "Anna", "Silva"]

for elementos in minhaLista3:
    print(elementos)
```

**Figura 6**

*Fonte: Acervo do Conteudista*

Saída **:**

```text
Result
CPU Time: 0.00 sec(s), Memory: 7716 kilobyte(s)

João
Maria
Anna
Silva
```

**Figura 7**

*Fonte: Acervo do Conteudista*

Explicando o código, na linha 1, temos a declaração da lista com a atribuição de valores. Na linha 3, declaramos o **_for_** , criamos a variável de iteração chamada “elementos” e em seguida, a cláusula **_in_** e a descrição da lista que desejamos visualizar. Dessa forma, a cada repetição do **_for_** , o valor contido no elemento da lista será atribuído para a variável de iteração.

É importante ressaltar que a quantidade de repetições que o **_for_** irá executar é igual à quantidade de elementos existentes na lista.

###### Atualizando Elementos em uma Lista

Podemos atualizar um elemento específico em uma lista, indicando entre colchetes o índice onde o item está armazenado. Vamos a um exemplo:

```python
minhaLista2 = [1, "Silva", 4.5 ]
minhaLista2[0] = 2
minhaLista2[1] = "João da Silva"
```

**Figura 8**

*Fonte: Acervo do Conteudista*

No código acima, na linha 1 declaramos uma lista e atribuímos 3 valores. Na linha 2, atualizamos o valor contido no item armazenado no índice zero (0), o valor original que era “1”, passa agora a ser “2”. Na linha 3, atualizamos o valor contido no item armazenado no índice um (1), o valor original que era “Silva”, passa agora a ser “João da Silva”.

###### Removendo Elementos de uma Lista

No contexto de listas, no _Python_ , podemos remover elementos específicos ou elementos no final de uma lista. Para remover um elemento no final da lista, utilizamos a função _pop_ . Vejamos um exemplo.

```python
minhaLista3 = ["João", "Maria", "Anna", "Silva"]
minhaLista3.pop()
```

**Figura 9** Fonte: Reprodução

Na linha 2, descrevemos o nome da lista e, em seguida, logo após o sinal de ponto final, descrevemos a função **_pop()_** . Essa função remove o elemento contido no **final da lista** . Nesse exemplo, a lista removerá o valor “Silva”.

Pode-se utilizar a função **_pop()_** quantas vezes forem necessárias ao seu algoritmo.

```python
minhaLista3 = ["João", "Maria", "Anna", "Silva"]
minhaLista3.pop()
minhaLista3.pop()
minhaLista3.pop()
print(minhaLista3)
```

**Figura 10**

*Fonte: Reprodução*

No código acima, a cada vez que a função **_pop()_** é executada, é removido o elemento contido no final da lista. Desse modo, ao final da execução, restará apenas o elemento contendo o valor “João”.

Outra maneira para remover um elemento de uma lista é por meio da função **_remove()_** tendo como parâmetro o valor desejado. A função **_remove()_** permite remover a primeira ocorrência de

```python
minhaLista3 = ["João", "Maria", "Anna", "Silva"]
minhaLista3.remove("Maria")
print(minhaLista3)
```

**Figura 11** Fonte: Reprodução

Na linha 2, descrevemos o nome da lista e em seguida, logo após o sinal de ponto final, descrevemos a função **_remove()_** . Essa instrução irá remover o primeiro elemento cujo valor seja igual à “Maria”. Caso o valor indicado na função **_remove()_** não exista na lista, ocorrerá um erro de execução.

#### Site

**_Jdoodle – Online Python_ 3 IDE**

**Pode-se sempre utilizar um bloco de exceções (** **_Try Except_ ) para tratar exceções em seu código. No cenário da função remove, veja um exemplo a seguir de um código contendo o bloco de exceção** **_Try Except_ .**

**Leitura Tratamento de Exceções**

**ACESSE**

Funções de listas podem ser executadas diversas vezes ao longo do código. Vejamos um exemplo onde utilizamos a funções para adicionar e remover elementos.

```python
minhaLista3 = ["João", "Maria", "Anna", "Silva"]
minhaLista3.pop()
minhaLista3.pop()
minhaLista3.append("Fernanda")
print(minhaLista3)
```

**Figura 12** Fonte: Reprodução

Ao final da execução do programa, a lista irá conter 3 elementos com os seguintes valores: “João”, “Maria” e “Fernanda”.

#### Leitura

**Como trabalhar com listas em** **_Python_**

**ACESSE**

## Tuplas

A tupla é uma estrutura de dados em _Python_ que é uma sequência ordenada de elementos e imutável (os valores contidos em seus elementos não podem ser atualizados ou excluídos). Tuplas são similares às listas quanto às regras para nomeação e tipos de dados que podem ser armazenados. Cada elemento dentro de uma tupla é chamado de item, porém, seus valores são definidos entre parênteses (). Por sua característica imutável, tuplas podem ser utilizadas, por exemplo, em cenários onde é preciso garantir que dados sejam protegidos contra gravação ao longo da execução do programa.

###### Declarando Listas e Atribuindo Valores

A forma de declaração de uma tupla é muito parecida com a declaração de uma lista, contudo, os valores são indicados entre parênteses () separando cada valor por vírgula. Vejamos um exemplo:

```
minhaTupla = (1,2,3,4,5)
```

O código acima declara uma lista com o nome de “minhaTupla” e atribui os valores 1, 2, 3, 4 e 5.

###### Acessando Elementos em uma Lista

Para acessar um elemento específico em uma tupla, é preciso indicar o índice onde o elemento está armazenado. Vejamos um exemplo.

```python
minhaTupla = ("João","Anna","Silva")
print(minhaTupla[1])
```

**Figura 13** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 7708 kilobyte(s)

Anna
```

**Figura 14** Fonte: Reprodução

Explicando o código, na linha 1, temos a declaração da tupla com a atribuição de valores. Na linha 2, dentro da função _print_ , descrevemos o nome da lista e, entre colchetes, indicamos o índice do elemento que desejamos visualizar.

Similar à lista, outra forma para acessar e visualizar os elementos de uma tupla é por meio de uma estrutura de repetição **_for_** . Vejamos um exemplo:

```python
minhaTupla = ("João","Anna","Silva")

for elemento in minhaTupla:
    print(elemento)
```

**Figura 15** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.00 sec(s), Memory: 7612 kilobyte(s)

João
Anna
Silva
```

**Figura 16** Fonte: Reprodução

Explicando o código: na linha 1, temos a declaração da lista com a atribuição de valores. Na linha 3, declaramos o **_for_** , criamos a variável de iteração chamada “elemento” e em seguida, a cláusula **_in_** e a descrição da lista que desejamos visualizar. Dessa forma, a cada repetição do **_for_** , o valor contido no elemento da lista será atribuído para a variável de iteração.

É importante ressaltar que a quantidade de repetições que o for irá executar é igual à quantidade de elementos existentes na lista.

###### Atualizando Elementos em uma Lista

Conforme vimos, tuplas não podem ser atualizadas, dessa forma, caso necessário atualizar elementos de um tupla, deve-se declarar novamente a tupla.

###### Removendo Elementos de uma Lista

Do mesmo modo que não se pode atualizar um elemento em um tupla, também não se pode excluir. Caso seja necessário, é permitida a exclusão completa da tupla por meio da instrução **_del_** .

```python
minhaTupla = ("João","Anna","Silva")
del minhaTupla
print(minhaTupla)
```

**Figura 17** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 8128 kilobyte(s)

Traceback (most recent call last):
  File "/home/jdoodle.py", line 3, in <module>
    print(minhaTupla)
NameError: name 'minhaTupla' is not defined
```

**Figura 18** Fonte: Reprodução

Explicando o código: na linha 1, temos a declaração da lista com a atribuição de valores. Na linha 2, descrevemos a cláusula **_del_** e, em seguida, descrevemos o nome da tupla que desejamos excluir.

Na linha 3, ao executar a função _print_ , tendo como parâmetro a tupla criada na linha 1, o programa retornará um erro de execução, pois a tupla foi excluída na linha anterior (linha 2).

#### Leitura

**Entenda o que é e quais as Diferenças entre Listas,** **_Sets_ , Tuplas e Dicionários no** **_Python_**

**ACESSE**

## Dicionários

Um dicionário é uma estrutura de dados em _Python_ que é uma sequência não ordenada de elementos e mutável. Cada item um dicionário possui um par de chave/valor. As regras para nomeação de dicionários seguem as mesmas utilizadas para tuplas e listas.

###### Declarando Dicionários e Atribuindo Valores

A forma de declaração de um dicionário é similar à declaração de uma lista ou tupla. Os valores são indicados entre o símbolo de chaves {} separando cada valor por vírgula. Como dito, todo item dentro de um dicionário é composto pelo conjunto de chave/valor. Embora os valores possam ser de qualquer tipo de dados e possam se repetir, as chaves devem ser do tipo imutável ( _string_ , número ou tupla com elementos imutáveis) e devem ser exclusivas.

Vejamos a sintaxe de declaração de um dicionário:

![[pc1-04-fig19.webp]]

**Figura 19**

Em _Python_ temos:

```
meuDicionario = {"nome": "João da Silva", "idade":25}
```

O código acima declara um dicionário com o nome de “meuDicionario” e atribui o valor “João da Silva” para a chave “nome” e o valor “25” para a chave “idade”. As chaves declaradas nesse dicionário são únicas (não se repetem) e são do tipo _string_ .

###### Acessando Elementos em uma Lista

Para acessar um elemento específico em um dicionário, basta indicar a chave do elemento entre colchetes. Vejamos um exemplo:

```python
meuDicionario = {"nome": "João da Silva", "idade":25}
print(meuDicionario["nome"])
```

**Figura 20** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.00 sec(s), Memory: 7800 kilobyte(s)

João da Silva
```

**Figura 21** Fonte: Reprodução

###### Atualizando e Adicionando Elementos em um Dicionário

Podemos atualizar um elemento específico em um dicionário, basta indicar a chave do elemento entre colchetes. Vamos a um exemplo:

```python
meuDicionario = {"nome": "João da Silva", "idade":25}
meuDicionario["idade"] = 38

print(meuDicionario["idade"])
```

**Figura 22** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 7664 kilobyte(s)

38
```

**Figura 23** Fonte: Reprodução

No código acima, na linha 1, declaramos um dicionário a e atribuímos seus valores. Na linha 2, atualizamos o valor referente à chave “idade” para “38”.

Para adicionar um elemento ao dicionário, deve-se declarar a nova chave do dicionário e atribuir seu valor. Vejamos um exemplo:

```python
meuDicionario = {"nome": "João da Silva", "idade":25}

meuDicionario["email"] = "joao@gmail.com"

print(meuDicionario)
```

**Figura 24** Fonte: Reprodução

No código acima, na linha 1, declaramos um dicionário a e atribuímos seus valores. Na linha 2, adicionamos uma nova chave com o nome de “ _email_ ” e atribuímos o valor “joao@gmail.com”. Na linha 3, por meio da função _print_ , visualizamos todos os dados contidos no dicionário.

###### Removendo Elementos de um Dicionário

Em um dicionário, podemos remover elementos específicos, um elemento contido no final do dicionário ou apagar todos os elementos. Para remover um elemento no final da lista, utilizamos a função _popitem()_ . Vejamos um exemplo:

```python
meuDicionario = {"nome": "João da Silva", "idade":25, "email":'joão@msn.com'}
meuDicionario.popitem()
```

**Figura 25**

*Fonte: Reprodução*

Na linha 2, descrevemos o nome do dicionário e, em seguida, logo após o sinal de ponto final, descrevemos a função **_popitem()_** . Essa função remove o elemento contido no **final do dicionário** . Nesse exemplo, o dicionário removerá a chave “ _email_ ” e seu valor.

Pode-se utilizar a função **_popitem()_** quantas vezes forem necessárias ao seu algoritmo.

Para remover um elemento específico, basta indicar o nome da chave como parâmetro na função _pop()_ . Vejamos um exemplo:

```python
meuDicionario = {"nome": "João da Silva", "idade":25, "email":'joão@msn.com'}
meuDicionario.pop("nome")
```

**Figura 26**

*Fonte: Reprodução*

Na linha 2, descrevemos o nome do dicionário e, em seguida, logo após o sinal de ponto final, descrevemos a função **_pop()_** e, como parâmetro, descrevemos a chave “nome”. Dessa forma, o elemento removerá a chave “nome” e seu valor.

Por fim, para excluir todos os elementos do dicionário, basta descrever a cláusula **_del_** seguida do nome do dicionário.

```
del meuDicionario
```

#### Leitura

**Dicionários no** **_Python_**

**ACESSE**

## Manipulação de Strings

Em _Python_ , uma _string_ é uma sequência de caracteres _Unicode_ . _Strings_ podem ser criadas colocando caracteres entre aspas simples ou aspas duplas. Mesmo aspas triplas podem ser usadas em _Python_ , mas geralmente usadas para representar _strings_ de várias linhas.

```python
minhaString = 'Olá'
print(minhaString)

minhaString = "Olá"
print(minhaString)

minhaString = '''Olá'''
print(minhaString)

# 3 aspas duplas para suportar textos com múltiplas linhas
minhaString = """Olá, bem vindo
            ao mundo do Python"""
print(minhaString)
```

**Figura 27** Fonte: Reprodução

```text
Result
CPU Time: 0.01 sec(s), Memory: 7892 kilobyte(s)

Olá
Olá
Olá
Olá, bem vindo ao mundo do Python
```

**Figura 28** Fonte: Reprodução

É possível acessar caracteres específicos em uma _string_ . Para isso, basta indicar o número do índice desejado.

```python
minhaString = 'São Paulo'
print(minhaString[0])
```

**Figura 29** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.01 sec(s), Memory: 7688 kilobyte(s)

S
```

**Figura 30** Fonte: Reprodução

É possível concatenar (juntar) duas ou mais _strings_ utilizando o sinal de adição (+).

```python
minhaString = 'São Paulo' + ' é um estado ' + 'do Brasil'
print(minhaString)
```

**Figura 31** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.00 sec(s), Memory: 7864 kilobyte(s)

São Paulo é um estado do Brasil
```

**Figura 32** Fonte: Reprodução

Também é possível identificar um caractere específico ou uma sequência de caracteres contida em uma _string_ . Para isso, utilizamos a cláusula **_in_** .

```python
minhaString = 'São Paulo' + ' é um estado ' + 'do Brasil'

if 'São Paulo' in minhaString:
    print("Sequência encontrada")
else:
    print("Sequência não encontrada")
```

**Figura 33** Fonte: Reprodução

Saída:

```text
Result
CPU Time: 0.00 sec(s), Memory: 7752 kilobyte(s)

Sequência encontrada
```

**Figura 34** Fonte: Reprodução

É importante o aprofundamento nos estudos acerca de _strings_ , pois essas possibilitam uma infinidade de funções e instruções para sua manipulação.

#### Em Síntese

**Nesta Unidade, estudamos os conceitos introdutórios acercada das principais estruturas de dados e** **_strings_ do** **_Python_ . É importante que assista à videoaula desta unidade e que leia os livros e materiais complementares indicados nesta Unidade de estudo. É fundamental que, além dos estudos em** **_Python_ , busque estudar ou retomar conceitos de desenvolvimento de algoritmos, em especial, o tema desta Unidade.**
