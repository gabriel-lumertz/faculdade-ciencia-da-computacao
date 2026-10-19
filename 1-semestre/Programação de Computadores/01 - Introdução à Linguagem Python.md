---
materia: "Programação de Computadores"
modulo: "Introdução à Linguagem Python"
semestre: 1
unidade: 1
tipo: material-teorico
fonte: "raw/1-semestre/PROGRAMAÇÃO DE COMPUTADORES/Programação de computadores 01.pdf"
tags: [faculdade, programacao-de-computadores, semestre-1]
aliases: ["Programação de Computadores - Unidade 1"]
---

# Introdução à Linguagem Python

_Python_ é uma linguagem de programação de alto nível interpretada, interativa, orientada a objetos. Foi criado por Guido van Rossum no final da década de 1980. Como o Perl, o códigofonte do _Python_ também está disponível sob a GNU _General Public License_ ( _GPL_ ). _Python_ tem seu nome inspirado um programa de TV inglês chamado “ _Flying Circus de Monty Python_ ” e não na espécie de cobra.

_Python_ é uma linguagem de programação de aplicação geral e possui uma sintaxe simples e fácil de usar. Isso torna o _Python_ uma excelente linguagem para aprender a programar, destacamos algumas características:

**Interpretado:** _Python_ é processado em tempo de execução pelo interpretador. Não é preciso compilar o programa antes de executá-lo;

**Orientado a objetos:** _Python_ suporta estilo ou técnica de programação orientada a objetos que encapsula código dentro de objetos;

**Uso geral:** _Python_ pode ser usado para quase tudo. É aplicável a quase todos os campos para uma variedade de tarefas. Seja a execução de tarefas de curto prazo como teste de _software_ ou desenvolvimento de _software_ para uso ao longo prazo;

**Fácil de aprender:** _Python_ é extremamente fácil de começar. _Python_ possui uma sintaxe muito simples;

**Livre e de código aberto:** _Python_ é um exemplo de _Software_ Livre e Código Aberto. Em linhas gerais, você pode distribuir gratuitamente cópias deste _software_ , ler seu

código-fonte, fazer alterações nele, usar partes dele em novos programas gratuitos. Seu uso é totalmente gratuito, mesmo para fins comerciais;

**Portátil:** Devido à sua natureza de código aberto, programas _Python_ podem funcionar em diversas plataformas;

**_Case-sensitive:_** _Python_ diferencia letras maiúsculas de minúsculas em sua codificação;

**Linguagem com tipagem dinâmica (** **_Duck typing_ ):** Em _Python_ , não é preciso declarar o tipo de dados ao declarar uma variável. O interpretador determina o tipo de dados em tempo de execução.

### Leitura

**_Duck Typing_ com** **_Python_**

**ACESSE**

Como exemplos de aplicações desenvolvidas com _Python_ , podemos destacar:

**Desenvolvimento** **_Web_ :** _Python_ oferece diferentes _Frameworks_ para desenvolvimento _web_ como _Django_ , _Pyramid_ , _Flask_ . Esses _Frameworks_ são conhecidos pela segurança, flexibilidade e escalabilidade;

**Desenvolvimento de jogos:** _PySoy_ e _PyGame_ são duas bibliotecas _Python_ usadas para desenvolvimento de jogos;

**Inteligência Artificial e Aprendizado de Máquina:** Há um grande número de bibliotecas de código aberto que podem ser usadas durante o desenvolvimento de aplicações de Inteligência Artificial e Aprendizado de Máquina;

**Desenvolvimento de aplicações para** **_Desktop_ :** O _Python_ possui diversos _Frameworks_ com as quais podemos construir aplicativos de área de trabalho. PyQt, PyGtk, PyGUI são alguns exemplos.

**Leitura**

**_Framework_ : Saiba como Usar e quais são os Mais Populares**

**ACESSE**

Nas próximas etapas de nossa Unidade de estudo, iremos aprender como baixar o _Python_ , criar nossos primeiros códigos e estudar sobre conceitos de variáveis. Ao longo dos estudos, será proveitoso visitar em paralelo, conceitos de desenvolvimento de algoritmos.

**Instalando o Ambiente de Desenvolvimento**

Nessa etapa, iremos instalar o _Python_ em um ambiente com sistema operacional _Windows_ . Serão instalados bibliotecas padrão do _Python_ , compilador, interpretador e o editor de _scripts_ IDLE.

- 1 Faça o _download_ do instalador do _Python_ 3 com a versão mais recente por meio do _site;_

**_Site Download Python_**

**ACESSE**

![[pc1-01-fig01.webp]]

**Figura 1 – Página de** **_download_ do** **_Python_** Fonte: Adaptada python.org

- 2 Localize o arquivo de instalação e o execute. Na tela inicial, na parte inferior, selecione a opção “ _Add Python_ 3.10 _to PATH_ ”, essa opção fará com que o instalador crie as variáveis de sistema no _Windows;_

Em seguida, clique em “ _Install Now_ ”;

![[pc1-01-fig02.webp]]

**Figura 2 –** **_Software_ de instalação do** **_Python_** Fonte: Reprodução

- 4 Caso seu _Windows_ solicite permissão para seguir a instalação, clique em SIM;

- 5 Aguarde o final da instalação. Na tela a seguir, clique no botão “ _Close_ ”.

![[pc1-01-fig03.webp]]

**Figura 3 –** **_Software_ de instalação do** **_Python_** Fonte: Reprodução

### Sites

**Caso não consiga instalar o** **_Python_ , os estudos poderão seguir utilizando ferramentas** **_online_ de compilação. Como sugestão, pode-se utilizar as ferramentas indicadas a seguir.**

**_Jdoodle – Online Python 3 IDE_** Clique no botão para conferir o conteúdo.

**ACESSE**

**_Replit – Python (with Turtle) Online Compiler & Interpreter_** Clique no botão para conferir o conteúdo.

**ACESSE**

#### Criando Programas em Python

Na etapa anterior, instalamos o _Python_ em nosso sistema operacional e junto com ele, foi instalado também a ferramenta para desenvolvimento de programas em _Python_ , o IDLE, um editor de _scripts_ que iremos utilizar a partir de agora para executar e criar nossos programas em _Python_ .

### Leitura

**IDLE – Modo Interativo do** **_Python_**

**ACESSE**

Nessa etapa, iremos aprender como criar e executar nossos códigos em _Python_ .

Para criar códigos em _Python_ , iremos utilizar o IDLE, para isso, localize-o em seu sistema operacional e execute o programa.

Ao iniciar o IDLE, a tela aberta será o interpretador _Python_ . Essa aplicação será a responsável por executar nossos programas em _Python_ .

Para criar um programa, clique no botão “ _File_ ” e em seguida “ _New File_ ”.

![[pc1-01-fig04.webp]]

*Figura 4 – Tela do interpretador Python*

*Fonte: Acervo do Conteudista*

Para o nosso primeiro programa, iremos criar o tradicional “olá, mundo”. Para isso, usaremos a função “ _print_ ” do _Python_ . Utilizamos essa função para apresentar alguma informação na tela, para isso, entre os parênteses da função _print_ e entre aspas duplas, digitamos o que queremos que seja visualizado na tela. Assim, digite na tela de digitação de _scripts_ :

```python
print("Ola, Mundo!!")
```

**Figura 5 – Tela de digitação de** **_scripts_**

*Fonte: Acervo do Conteudista*

Em seguida, para executar o programa, clique no botão “ _Run_ ”, opção _Run Module_ . Você pode também pressionar a tecla F5 de seu teclado.

![[pc1-01-fig06.webp]]

Como o arquivo não foi salvo, a ferramenta solicita que se salve o programa. Clique no botão “ _OK_ ” e em seguida escolha um local em seu computador e salve seu programa.

![[pc1-01-fig07.webp]]

**Figura 7 – Tela de digitação de** **_scripts_ – Salvando** **_scripts_** Fonte: Acervo do Conteudista

Ao concluir, o programa será executado por meio do interpretador _Python_ do IDLE.

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo1.py
Ola, Mundo!!
>>> 
```

###### Figura 8 – Tela do interpretador Python

*Fonte: Acervo do Conteudista*

Agora em diante, qualquer alteração no programa, ao executar, o programa o interpretador _Python_ do IDLE será aberto.

#### Conceito e Uso de Variáveis no Python

Inicialmente, para seguir com os estudos de conceitos de variáveis, precisamos entender o conceito de **identificadores** . Identificadores em _Python_ são os nomes utilizados para identificar variáveis, funções, classes, módulos ou outros objetos.

Vale lembrar que a linguagem _Python_ é _Case-sensitive_ , ou seja, diferencia letras maiúsculas de minúsculas em sua codificação. Assim, por exemplo, o identificador “pessoa” é diferente de “Pessoa”.

Afinal, o que são variáveis? Uma variável é uma área de armazenamento que nossos programas podem manipular, são localizações de memória reservadas para armazenar valores, desse modo, ao criar uma variável, é reservado algum espaço na memória do computador que está executando o programa.

Por conta da característica de tipagem dinâmica, ao declarar uma variável, não é preciso indicar de forma explícita o tipo de dados que serão armazenados. A declaração ocorre automaticamente quando você atribui um valor a uma variável.

O sinal de igual (=) é usado para atribuir valores às variáveis. A descrição à esquerda do operador = é o nome da variável e a descrição à direita do operador = é o valor armazenado na variável.

![[pc1-01-fig09.webp]]

*Figura 9*

Para nomear variáveis no _Python_ , devemos seguir algumas regras:

As variáveis podem ter letras (A-Z e a-z), dígitos (0-9) e sublinhados (_);

Não podem começar com números;

Não podem conter pontuação, caracteres especiais (!, @, $, # etc.) ou espaços;

Não podem ser utilizadas palavras reservadas da linguagem.

A lista a seguir mostra as palavras-chave _Python_ . Estas são palavras reservadas e você não pode usá-las como constantes, variáveis ou qualquer outro nome de identificador. Todas as palavraschave _Python_ contêm apenas letras minúsculas.

###### Tabela 1

|_and_|_as_|_assert_|_break_|_class_|
|---|---|---|---|---|
|_continue_|_def_|_del_|_elif_|_else_|
|_except_|_False_|_finally_|_for_|_from_|
|_global_|_if_|_import_|_in_|_is_|
|_lambda_|_None_|_nonlocal_|_not_|_or_|
|_pass_|_raise_|_return_|_true_|_try_|
|_while_|_with_|_yield_|||

Os tipos de dados armazenados em uma variável podem ser:

Números (inteiros, reais e complexos);

_String_ (cadeia de caracteres que representam um texto);

_Boolean_ ;

_List_ ; _Tuple_ ;

_Dicitonary_ .

##### Exemplos Práticos: Atribuindo e Manipulando Valores para Variáveis

Em nosso primeiro exemplo, vamos criar um programa que seja capaz de armazenar o nome de uma pessoa, sua idade e _e-mail_ . Nosso programa irá exibir na tela os valores armazenados.

Digite o seguinte código no editor de _scripts_ do IDLE:

```python
nome = "João da Silva"
idade = 20
email = "joao@gmail.com"
print("nome " + nome, " idade ", idade)
```

```python
nome = "João da Silva"
idade = 20
email = "joao@gmail.com"
print("nome " + nome, " idade ", idade)
```

**Figura 10** Fonte: Acervo do Conteudista

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
nome João da Silva  idade  20
>>> 
```

###### Figura 11

*Fonte: Acervo do Conteudista*

##### Explicando o Código

**Na linha 1:** atribuímos o valor “João da Silva” à variável **nome** . Quando desejamos armazenar um valor de sequência de caracteres ( **_string_** ), devemos digitar o valor entre aspas duplas;

**Na linha 2:** Atribuímos o valor “20” à variável **idade** . Diferentemente da atribuição anterior, por se tratar de um número, não precisamos digitar o número entre aspas duplas. Quando desejarmos armazenar um valor, precisamos apenas digitar os números (utilize ponto ao invés de vírgula para separar casas decimais);

**Na linha 3** : Atribuímos o valor “joao@gmail.com” a variável **_email_** _;_

**Na linha 4** : Por meio da função “ _print_ ”, exibimos os valores armazenados nas variáveis (impresso na tela). Concatenamos os valores das variáveis e rótulos.

### Leitura

**Guia Básico da Função** **_print_ () em** **_Python_**

**ACESSE**

Podemos atribuir valores em uma mesma linha a múltiplas variáveis. Para isso, basta digitar os valores separados por vírgula.

```python
nome,idade,email = "João da Silva",20,"joao@gmail.com"

print("nome " + nome, " idade ", idade, " email ",email )
```

**Figura 12**

*Fonte: Acervo do Conteudista*

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
nome João da Silva  idade  20 email joao@gmail.com
>>> 
```

###### Figura 13

*Fonte: Acervo do Conteudista*

Podemos também atribuir valores às variáveis de acordo com o valor armazenado em outra variável. Por exemplo:

```python
a = 5
b = 6
c = a

print(a)
print(c)
```

###### Figura 14

*Fonte: Acervo do Conteudista*

**Na linha 3:** Atribuímos para a variável c o valor contido na variável a, ou seja, o valor armazenado na variável c será 5, o mesmo valor armazenado na variável a.

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
5
5
>>> 
```

**Figura 15** Fonte: Acervo do Conteudista

É importante ressaltar que a cada vez que é utilizado o sinal de = para atribuir um valor a uma variável, caso tenha nessa variável algum valor atual, o valor será atualizado. Por exemplo:

```python
a = 5
b = 6
c = a
a = 1
print(a)
print(c)
```

**Figura 16**

*Fonte: Acervo do Conteudista*

O valor que será exibido para a variável “a” será 1, pois embora na linha 1 tenha sido atribuído o valor 5, na linha 4 foi atribuído o valor 1, uma vez que o _Python_ executa linha a linha suas instruções. Já o valor da variável “c” será 5, pois no momento que foi atribuído o valor para a variável “c”, o valor da variável “a” ainda era 5.

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
1
5
>>> 
```

**Figura 17** Fonte: Acervo do Conteudista

Vejamos o mesmo exemplo, porém exibindo os resultados antes e depois da nova atribuição para a variável “a”.

```python
a = 5
b = 6
c = a
print("variável a antes de ter um novo valor atribuído ", a)
a = 1
print("valor atribuído para a variável c ",c)
print("variável a DEPOIS de ter um novo valor atribuído ", a)
```

**Figura 18**

*Fonte: Acervo do Conteudista*

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
variável a antes de ter um novo valor atribuído  5
valor atribuído para a variável c  5
variável a DEPOIS de ter um novo valor atribuído  1
>>> 
```

**Figura 19** Fonte: Acervo do Conteudista

Por conta da característica de tipagem dinâmica, uma mesma variável pode ter diversos tipos diferentes de dados atribuídos no mesmo programa. Vejamos um exemplo:

```python
a = 5
b = 6
c = a
print("variável a antes de ter um novo valor atribuído ", a)
a = "texto"
print("valor atribuído para a variável c ",c)
print("agora o valor armazenado na variável a é um tipo texto ", a)
```

**Figura 20**

*Fonte: Acervo do Conteudista*

**Na linha 1:** Atribuímos o valor **5** do tipo número inteiro para a variável “a”;

**Na linha 5:** Atribuímos o valor **texto** do tipo cadeia de caracteres ( _string_ ) para a variável “a”.

O último valor de saída (impresso na tela) para a variável “a” será o valor “texto”.

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo2.py
variável a antes de ter um novo valor atribuído  5
valor atribuído para a variável c  5
agora o valor armazenado na variável a é um tipo texto  texto
>>> 
```

**Figura 21**

*Fonte: Acervo do Conteudista*

**Exemplos Práticos: Comandos de Entrada de Dados**

#### Exemplo 1

Em muitas soluções, devemos solicitar dados ao usuário do programa. Para isso, a partir de agora iremos utilizar a função “ _input_ ” em nossos programas sempre que desejarmos que o usuário insira um dado.

A sintaxe dessa função é:

![[pc1-01-fig22.webp]]

*Figura 22*

Por exemplo, vamos criar um programa que solicita o nome do usuário e exibe na tela uma saudação com seu nome.

Digite o seguinte código no editor de _scripts_ do IDLE:

```python
nome = input("digite seu nome")
print("Olá, ", nome, " tudo bem?")
```

```python
nome = input("digite seu nome")
print("Olá, ", nome, " tudo bem?")
```

Saída:

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo3.py
digite seu nome João
Olá,   João  tudo bem?
>>> 
```

**Figura 24**

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Na linha 1:** Atribuímos o valor que será informado pelo usuário do programa à variável nome. A função _input_ sempre retorna um tipo cadeia de caracteres ( **_string_** );

**Na linha 2:** Por meio da função “ _print_ ”, exibimos (impresso na tela) os valores armazenados na variável nome. Concatenamos o valor da variável com os valores fixos digitados (“olá e tudo bem?”).

**Exemplo 2**

Em muitos cenários, como quando precisamos manipular números para efetuar operações aritméticas, precisamos de alguma forma armazenar esses dados como um tipo número. Sabemos que a função “ _input_ ” sempre retorna um tipo _string_ . A estratégia será converter o valor vindo da função “ _input_ ”.

Em nosso segundo exemplo, iremos desenvolver um programa que irá solicitar ao usuário seu nome, idade e altura. Para cada variável, iremos armazenar como tipos diferentes: _string_ , inteiro e real.

Digite o seguinte código no editor de _scripts_ do IDLE:

```python
nome = input("digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print("O nome digitado é", nome)
print("A idade digitada é", idade)
print("O peso digitado é", peso)
```

```python
nome = input("digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print("O nome digitado é", nome)
print("A idade digitada é", idade)
print("O peso digitado é", peso)
```

**Figura 25** Fonte: Acervo do Conteudista

```text
Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Home/AppData/Local/Programs/Python/Python310/u1_exemplo4.py
digite seu nome: João
Digite sua idade: 37
Digite seu peso: 84
O nome digitado é João
A idade digitada é 37
O peso digitado é 84.0
>>> 
```

**Figura 26**

*Fonte: Acervo do Conteudista*

#### Explicando o Código

**Na linha 1:** Atribuímos o valor que será informado pelo usuário do programa à variável **nome** . A função _input_ sempre retorna um tipo cadeia de caracteres ( **_string_** );

**Na linha 2:** Atribuímos o valor que será informado pelo usuário do programa à variável **idade** . Porém, diferentemente da primeira linha, convertemos o resultado da função _input_ para o tipo inteiro por meio da cláusula _int_ ();

**Na linha 3:** Atribuímos o valor que será informado pelo usuário do programa à variável **idade** . Convertemos o resultado da função _input_ para o tipo real ( _float_ ) por meio da cláusula _float_ ().

A sintaxe para a conversão dos dados da função _input_ para os tipos de número inteiro e real, é:

![[pc1-01-fig27.webp]]

*Figura 27*

![[pc1-01-fig28.webp]]

*Figura 28*

É importante ressaltar que se o usuário digitar um número real (um número com casas decimais, por exemplo) para um _input_ convertendo em _int_ , o número digitado com casas decimais será armazenado como um inteiro.

Destaca-se também que a tentativa de se converter uma cadeia de caracteres em algum tipo de número acarretará erro de execução do programa.

### Em Síntese

**Nesta Unidade, além de aprendermos a instalar o ambiente de desenvolvimento** **_Python_ , estudamos os conceitos de identificadores, uso e atribuição de valores de variáveis e comandos de entrada (** **_input_ ) e saída (** **_print_ ). É importante que assista à videoaula da Unidade e que leia os livros e materiais complementares indicados.**
