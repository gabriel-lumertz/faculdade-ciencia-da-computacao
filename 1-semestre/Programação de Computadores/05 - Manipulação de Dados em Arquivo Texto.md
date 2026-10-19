---
materia: "Programação de Computadores"
modulo: "Manipulação de Dados em Arquivo Texto"
semestre: 1
unidade: 5
tipo: material-teorico
fonte: "raw/1-semestre/PROGRAMAÇÃO DE COMPUTADORES/Programação de computadores 05.pdf"
tags: [faculdade, programacao-de-computadores, semestre-1]
aliases: ["Programação de Computadores - Unidade 5"]
---

# Manipulação de Dados em Arquivo Texto

#### Introdução

A busca pelo conhecimento sempre foi a força motriz no avanço da humanidade. Vivemos em uma era tecnológica, na qual a informação digital predomina sobre a humanidade. É notório que, atualmente, a tecnologia desempenha um importante papel na vida da humanidade, ela permite impulsionar o progresso e que nações estejam conectadas, melhora a qualidade de vida e abre novas oportunidades em diversos setores. Podemos facilmente observar também que a tecnologia molda e transforma a maneira de como vivemos, trabalhamos e nos relacionamos. Sua importância é inegável e abrange praticamente todos os aspectos da sociedade moderna.

Hoje, realizamos os mais diversos serviços através de nossos _smartphones_ . Isso porque cada dia mais surgem novos aplicativos poderosos que trazem muitos benefícios para as pessoas. Não só os aplicativos, mas, também, todo e qualquer tipo de _software_ ( _Web_ , _Desktop_ , _Mobile_ etc.) traz inúmeros benefícios para a população

A utilização desses _softwares_ só é possível porque “Programadores” com bastante _expertises_ os desenvolveram com as mais atuais tecnologias. Cada dia mais a programação vem se tornando uma habilidade essencial para pessoas que queiram ingressar na área de tecnologia. Na verdade, a importância da programação vai além do desenvolvimento de _softwares_ e sistemas complexos. A verdadeira importância da programação consiste na capacidade das pessoas em resolver problemas e impulsionarem a inovação.

Para você ser um excelente programador, você precisa ter bom raciocínio lógico, conseguir resolver problemas, dominar uma linguagem de programação, conhecer IDEs eficientes, bem como técnicas de programações avançadas que permitirão a você criar algoritmos eficientes e elegantes.

O principal objetivo desta Unidade é apresentar técnicas e ferramentas para a manipulação de arquivo texto na programação. Todo _software_ manipula dados, sejam dados de entrada, ou de saídas (CORMEN, 2012). Muitas vezes, é necessário armazenar tais dados em banco de dados, ou até mesmo, em arquivos de texto. Imagine que você precisa desenvolver um _software_ que mantenha um registro em “Log” que armazena o horário de _login_ no sistema. Geralmente, arquivos de “log” utilizam arquivo “.txt” para armazenar os dados.

Assim, é visto a grande importância de aprender manipulação de dados em arquivos textos. Nesta Unidade de ensino, focamos na leitura, processamento e escrita em arquivos textos. Utilizaremos a linguagem _Python_ e IDE _Colab_ . Entretanto, você pode ficar à vontade para usar a IDE que mais goste. Usamos o _Colab_ porque é uma eficiente IDE e é _on-line_ , assim não precisamos nos preocupar com instalações e configurações. Apenas praticar os conceitos apresentados aqui. Bons estudos.

#### Colab

Uma IDE é uma plataforma de desenvolvimento que permite aos seus usuários criarem _software_ em determinadas linguagens de programação. Nesta apostila, iremos adotar a IDE _Colab_ para apresentarmos técnicas de manipulação de arquivo texto. Utilizaremos, também, a linguagem de programação _Python_ . Escolhemos o Colaboratório ( _Colaboratory_ ) ou abreviadamente, _Colab_ , para ser a nossa IDE porque ela possui grande facilidade de uso. O _Colab_ é uma IDE _on_ - _line_ , assim não será necessária a instalação de nada.

O _Colab_ é uma IDE desenvolvida e mantida pelo _Google_ , esse ambiente possui diversas bibliotecas de funções previamente instaladas que facilitarão nosso trabalho. A IDE _Colab_ é um serviço de nuvem gratuito hospedado pelo _Google_ para incentivar a programação em _Python_ , que permite que você escreva e execute _Python_ em seu navegador sem necessidade alguma de configuração, acesso gratuito à aceleração da GPU e recursos de colaboração. Além disso, tem pré-instalado uma série de bibliotecas de nosso interesse.

É importante observar também que o _Google Colab_ é constituído de máquinas virtuais. Na verdade, o _Google_ disponibiliza uma máquina virtual para que possamos programar e executar os nossos códigos.

### Leitura

**_Colab_**

**ACESSE**

Depois que acessar o _link_ anterior, você será direcionado para a tela inicial do _Google Colab_ , onde constará a seguir com a **opção “Recente”** selecionada. Note que no menu superior você possui as opções conforme a Figura 1.

![[pc1-05-fig01.webp]]

*Figura 1 – Tela inicial do Colab*

*Fonte: Reprodução*

**#ParaTodosVerem:** foto ilustrando a tela inicial do _Colab_ . Foto com fundo em branco e letras em cinza e detalhes em laranja. Ilustrando as opções que existem no _Google Colab_ . Fim da descrição.

Observe que na Figura 1, na parte laranja, há algumas opções, tais como:

**Exemplos:** nessa opção, você encontra vários exemplos de utilização dos recursos do _Google Colab;_

**Recente:** essa opção mostra os _Notebooks_ que você criou recentemente;

**_Google Drive_ :** já essa opção possibilita o armazenamento do seu _notebook_ virtual no seu _Google Drive_ ;

**_GitHub_ :** agora, essa opção permite que você utilize o _GitHub_ como repositório;

**_Upload_ :** essa última opção permite que você faça _upload_ de arquivos _Python_ para dentro do seu _notebook_ .

Como mencionado anteriormente, os _Notebooks Colab_ são máquinas virtuais e são _Notebooks Jupyter_ , que são armazenados no _Google Drive_ que permitem combinar código executável e texto em um único documento, junto com imagens, HTML e muito mais.

É importante observar que, para poder instalar um _notebook_ , você precisa fazer _login_ na sua conta _Google_ . Isso permitirá que todos os _notebooks_ criados no _Colab_ sejam armazenados no seu _Google Drive_ .

O _Google Colab_ é uma IDE fantástica, ela permite compartilhar _notebooks_ com seus amigos. Além do acesso compartilhado, seus amigos poderão editar, alterar e fazer comentários no seu código.

Agora, vamos para a nossa primeira missão, ela consiste na criação de um _Notebook Colab_ . Para isso, você deve clicar em “Novo _Notebook_ ” que se encontra na parte inferior da telinha laranja do _Colab_ .

![[pc1-05-fig02.webp]]

*Figura 2 – Criando um novo notebook*

*Fonte: Reprodução*

**#ParaTodosVerem:** foto ilustrando a abertura de um novo _notebook_ no _Colab_ . Foto com fundo em branco e letras em cinza. A foto possui um menu superior na cor laranja com algumas opções que podem ser acessadas. Fim da descrição.

Após criar um _notebook_ , você será direcionado para a tela principal do _Google Colab_ . Nela, podemos codificar e executar códigos em _Python_ . Aqui, você pode codificar o seu código e vê-lo executando logo em seguida.

![[pc1-05-fig03.webp]]

*Figura 3 – Tela de programação do Colab*

*Fonte: Reprodução*

**#ParaTodosVerem:** figura ilustrando a tela de programação do _Colab_ . Foto com fundo em preto e letras em brancos. A figura contém célula para codificação, que é representado por um retângulo, contém também mecanismos de execução que é representado por um triângulo dentro de um círculo. Fim da descrição.

Opções são exibidas quando passamos o mouse abaixo da célula, essas opções permitem adicionar uma nova célula, ou ainda, adicionar um texto, isto é, um comentário na célula. Tal situação, é ilustrada a seguir:

![[pc1-05-fig04.webp]]

**Figura 4 – Célula de programação do** **_Colab_** Fonte: Reprodução

**#ParaTodosVerem:** figura ilustrando a Célula de programação do _Colab_ . Foto com fundo em preto e letras em branco. A figura contém um retângulo em vermelho alertando a área de programação. Contém, também, dois retângulos vermelhos apresentando as opções onde criar células e inserir textos. Fim da descrição.

A criação de células permite você ir criando e testando códigos e inserindo comentários sobre o código criado.

A segunda missão que devemos completar consiste em executar um “ _Hello World_ ” no _Colab_ para se familiarizar com o ambiente que iremos trabalhar ao longo desta Unidade de ensino. Para isso, basta colocar o seguinte código:

```python
print("Hello World")
```

Dentro da célula criada e, depois, clicar na seta dentro de um círculo no lado esquerdo para executar.

Para executar, você também pode pressionar as teclas “Ctrl + _Enter_ ” que o programa será executado.

```python
print("Hello World")
```

**Figura 5 –** **_Hello World_ no** **_Colab_**

*Fonte: Reprodução*

**#ParaTodosVerem:** figura ilustrando um _Hello World_ no _Colab_ . Foto com fundo em preto e letras em brancos. A Figura contém, também, o _print_ “ _Hello World_ ”. Fim da descrição.

A seguir, mostrando o resultado do comando “print(“Hello World”)”:

```python
print("Hello World")
```

```text
Hello World
```

**Figura 6 – Resultado do** **_Hello World_ no** **_Colab_**

*Fonte: Reprodução*

**#ParaTodosVerem:** figura ilustrando o resultado do _Hello World_ no _Colab_ . Figura com fundo em preto e letras em branco. A Figura contém também um retângulo em vermelho mostrando o resultado do “print(“Hello World”)”. Fim da descrição.

Dessa forma é que iremos executar todos os códigos apresentados aqui.

Vamos, ainda, apresentar mais um recurso interessante do _Google Colab_ , o _Colab_ permite que você altere o nome do seu _notebook_ , isso permite que você organize melhor as suas aplicações.

![[pc1-05-fig07.webp]]

**Figura 7 – Alteração do nome do** **_notebook_ no** **_Colab_** Fonte: Reprodução

**#ParaTodosVerem:** figura ilustrando a alteração de nome no _Google Colab_ . Figura com o fundo em preto e com as letras em brancos. Figura contém, também, um retângulo em vermelho que apresenta onde trocar o nome do _notebook_ . Fim da descrição.

#### Lendo um Arquivo em Texto

O primeiro passo é criar um arquivo “.txt”. Crie um arquivo “txt” com o nome de “dados.txt”. Conforme ilustrado na Figura a seguir:

![[pc1-05-fig08.webp]]

**Figura 8 – Criação do arquivo “txt”** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo azul demonstrando uma área do _Desktop_ , onde tem o arquivo “dado.txt” e uma lixeira. A figura também possui um menu abaixo. Fim da descrição.

Agora, abra o arquivo “dados.txt” e escreva a seguinte frase: “Meu primeiro arquivo txt”. Salve e feche o arquivo.

Após criar o arquivo “dados.txt”, precisamos enviá-lo para o _notebook_ . Isto porque o _Google Colab_ é uma IDE _on_ - _line_ que está na nuvem, assim, precisamos enviar o arquivo “dados.txt” para a nuvem.

Clique no ícone de uma pasta do lado esquerdo, conforme ilustrado na Figura a seguir:

![[pc1-05-fig09.webp]]

**Figura 9 – Pasta de upload de arquivos no** **_Colab_** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo preto demonstrando o ícone da pasta para fazer _upload_ do arquivo “txt”. A Figura ainda contém um retângulo em vermelho demonstrando onde está o ícone. Fim da descrição.

Após clicar no ícone da pasta, clique em “ _upload_ ” conforme ilustrado na Figura a seguir:

![[pc1-05-fig10.webp]]

**Figura 10 – Ícone de** **_upload_ de arquivo** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo preto demonstrando o ícone de _upload_ para fazer _upload_ do arquivo “txt”. A Figura ainda contém um retângulo em vermelho demonstrando onde está o ícone. Fim da descrição.

Após fazer o _upload_ do arquivo, ele aparecerá no diretório, conforme a Figura a seguir.

![[pc1-05-fig11.webp]]

**Figura 11 – Arquivo dado no** **_Colab_** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo preto demonstrando onde o arquivo “dados.txt” fica após ser feito o _upload_ . A Figura ainda contém um retângulo em vermelho demonstrando onde está o arquivo. Fim da descrição.

##### Lendo um Arquivo Texto

Agora, vamos à programação. O primeiro passo na programação consiste em ler o arquivo e carregá-lo na memória. Para ler um arquivo em “txt” no _Python_ , utilizaremos a função “open()”. A função “open()” recebe dois parâmetros, o primeiro é o nome do arquivo e o segundo parâmetro consiste na ação que iremos fazer com o arquivo. Como iremos abrir o arquivo para uma leitura, precisamos usar a opção “r” de _read_ .

```python
dados = open("dados.txt", "r")
```

Após a execução do código anterior, a variável “dados” será uma referência para o arquivo “dados.txt” que está sendo carregado na memória.

Após, é necessário ler o conteúdo do arquivo. Realizamos essa operação com a função “read”. Escreva o seguinte trecho de código no _Colab_ :

```python
conteudo = dados.read()
```

Agora, a variável “conteudo” contém todos os dados que estavam dentro de “dados.txt”. Para imprimir os dados que estão em “conteudo”, utilize a função “print”.

```python
print(conteudo)
```

E por último, devemos fechar o arquivo com o seguinte código:

```python
dados.close()
```

Neste momento, o seu código deve estar parecido com o código a seguir:

```python
1. # Abertura do arquivo
2. dados = open("dados.txt", "r")
3. # Leia o conteúdo do arquivo
4. conteudo = dados.read()
5. #Imprimindo o arquivo txt
6. print(conteudo)
7. #Fechando o arquivo
8. dados.close()
```

Agora, execute o código clicando na seta de execução. A saída do seu programa deve ser igual ao ilustrado na Figura a seguir:

```python
# Abertura do arquivo
dados = open("dados.txt", "r")
# Leia o conteúdo do arquivo
conteudo = dados.read()
#Imprimindo o arquivo txt
print(conteudo)
#Fechando o arquivo
dados.close()
```

```text
Meu primeiro arquivo txt
```

###### Figura 12 – Saída da execução do código

*Fonte: Reprodução*

**#ParaTodosVerem:** figura com o fundo preto demonstrando a saída do código. Os comentários possuem a cor verde, e o código está na cor branca. A Figura

ainda contém um retângulo em vermelho demonstrando a saída. Fim da descrição.

##### Escrevendo em um Arquivo txt

Para escrever em um arquivo texto, devemos abri-lo com o parâmetro “w” de _write_ , ao invés de “r”. Dessa forma:

```python
dados = open("dados.txt", "w")
```

Dessa forma, o arquivo será aberto para escrita. Para escrever dados no arquivo, podemos usar a função “write()”. Da seguinte maneira:

```python
dados.write("\n Escrevendo no arquivo texto \n")
```

A frase dentro das aspas será escrita no arquivo texto. Após, podemos fechar o arquivo, com a função “close()”.

```python
dados.close()
1. # Abertura do arquivo
2. dados = open("dados.txt", "w")
3. # Escrevendo o conteúdo do arquivo
4. dados.write("\n Escrevendo no arquivo texto \n")
5. #Fechando o arquivo
6. dados.close()
```

Para visualizar o que foi escrito no arquivo, devemos abri-lo. Entretanto, como o arquivo está na nuvem, devemos fazer o _download_ dele. Para isso, clique novamente no ícone da pasta, depois clique nos três pontinhos à direita do arquivo e selecione “ _Download_ ”. Assim, o seu arquivo texto será baixado para o seu computador e você poderá ver o que foi escrito no arquivo. A Figura a seguir ilustra esse procedimento.

![[pc1-05-fig13.webp]]

**Figura 13 –** **_Download_ do arquivo alterado** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo preto demonstrando as opções de _download_ do arquivo alterado. A Figura ainda contém um retângulo em vermelho demonstrando os passos que devem ser feitos. Fim da descrição.

##### Lendo Apenas uma Linha do Arquivo

Como visto anteriormente, a função “read()” lê o conteúdo todo do arquivo. Entretanto, muitas vezes, é interessante que você faça a leitura de apenas uma linha do arquivo. Podemos ler apenas uma linha do arquivo usando a função:

```
arquivo.readline()
```

onde “arquivo” é o nome da variável de referência para o arquivo texto no seu código.

Agora, crie um novo arquivo texto e nomeie esse arquivo como  “segundoArquivoTexto.txt”. Agora, abra esse arquivo e coloque as seguintes frases: “Este é meu segundo exemplo de arquivo texto e _Python_ .

_Python_ é uma linguagem fantástica!

É uma linguagem muito simples de programar.

É importante que você digite as frases em linhas separadas. Agora, feche o arquivo e realize o mesmo procedimento anterior para subi-lo para a nuvem.

![[pc1-05-fig14.webp]]

**Figura 14 –** **_Upload_ do arquivo** Fonte: Reprodução

**#ParaTodosVerem:** figura com o fundo preto demonstrando o _upload_ do arquivo alterado. A Figura ainda contém um retângulo em vermelho demonstrando onde o arquivo está. Fim da descrição.

Agora crie uma nova célula para programar.

Antes, é importante observar que existe a função “readline()” que lê apenas uma única linha do arquivo e existe, também, a função “readlines()” que lê todas as linhas do arquivo e o concatena em uma única variável. Neste exemplo, vamos usar o readline().

Digite o seguinte código na nova célula:

```python
1. segundoArquivo = open("segundoArquivoTexto.txt", "r")
2. linha = segundoArquivo.readline();
3. #Imprimindo a linha
4. print(linha)
```

A saída desta execução será semelhante a apresentada na Figura a seguir:

```python
segundoArquivo = open("segundoArquivoTexto.txt", "r")
linha = segundoArquivo.readline();
#Imprimindo a linha
print(linha)
```

```text
Este é meu segundo exemplo de arquivo texto e Python
```

**Figura 15 – Saída do Código**

*Fonte: Reprodução*

**#ParaTodosVerem:** figura com o fundo preto demonstrando a saída do código. A Figura ainda contém um retângulo em vermelho demonstrando a saída. São apresentados, ainda, códigos que estão na cor branca e comentários na cor verde. Fim da descrição.

Perceba que foi impresso apenas a primeira linha, isso porque a função “readline()” lê apenas uma linha por vez. Se você deseja ler apenas uma linha por vez e imprimi-las cada uma separada, também, você utiliza a função “readline()” dentro de um for, ou ainda, usa a função “readlines()”.

No código a seguir, usamos a função “readlines()”.

```python
1. #Abrindo o arquivo
2. segundoArquivo = open("segundoArquivoTexto.txt", "r")
3. #lendo e concatenando as linhas em uma única variável
4. linhas = segundoArquivo.readlines();
5. #imprimindo as linhas separadamente
6. for linha in linhas:
7. print(linha)
```

A saída desse programa será:

```python
#Abrindo o arquivo
segundoArquivo = open("segundoArquivoTexto.txt", "r")
#lendo e concatenando as linhas em uma única variável
linhas = segundoArquivo.readlines();
#imprimindo as linhas separadamente
for linha in linhas:
    print(linha)
```

```text
Este é meu segundo exemplo de arquivo texto e Python

Python é uma linguagem fantástica

É uma linguagem muito simples de programar
```

###### Figura 16 – Saída do Código 2

*Fonte: Reprodução*

**#ParaTodosVerem:** figura com o fundo preto demonstrando a saída do código com o comando “readlines()”. A Figura ainda contém um retângulo em vermelho demonstrando a saída. São apresentados, ainda, códigos que estão na cor branca e comentários na cor verde. Fim da descrição.

##### Abrindo um Arquivo para Leitura e Escrita ao Mesmo Tempo

Para abrir um arquivo para leitura e escrita ao mesmo tempo, devemos abri-lo com “r+”. Assim, podemos abrir um arquivo, ler e depois escrever nele, no mesmo código. Observe o código a seguir:

```python
1. # Abertura do arquivo
2. dados = open("dados.txt", "r+")
3. # Leia o conteúdo do arquivo
4. conteudo = dados.read()
5. # Imprimindo o conteudo
6. print(conteudo)
7. # Escrevendo no arquivo
8. dados.write("\n Phyton s2 \n")
9. #Fechando o arquivo
10. dados.close()
```

No código anterior, abrimos o arquivo, lemos o seu conteúdo e logo em seguida, imprimimos o conteúdo que estava no arquivo. Posteriormente, escrevemos mais conteúdo no arquivo e depois o fechamos. É interessante observar que o conteúdo escrito será escrito abaixo do conteúdo lido anteriormente, isso porque como lemos todo o conteúdo do arquivo primeiro, o cursor está no final do arquivo e, assim, irá adicionar o conteúdo da linha oito no arquivo. Dependendo da ordem que lemos e escrevemos no arquivo, o conteúdo pode ser sobreposto.

##### Como Criar um Arquivo “txt” em Python

Em muitas situações, o programa desenvolvido terá que criar um arquivo texto, ao invés de abrir um arquivo já existente. Para criar um arquivo do zero e adicionar conteúdo nele, você pode usar o seguinte código:

```python
1.
        def criar_arquivo_txt(nome_arquivo, conteudo):
2.
            try:
3.
               with open(nome_arquivo, 'w') as arquivo:
4.
               arquivo.write(conteudo)
5.
           print(f"O arquivo '{nome_arquivo}' foi criado com sucesso!")
6.
          except Exception as e:
7.
           print(f"Erro ao criar o arquivo: {e}")
8.
9.
        nome_arquivo = "MeuArquivo.txt"
10.
        conteudo = "Python s2."
11.
12.
        criar_arquivo_txt(nome_arquivo, conteudo)
```

No código anterior, criamos um método chamado de “criar_arquivo_txt()”. Esse método será responsável por criar o arquivo “txt”. Posteriormente, na linha 12, chamamos o método e ele criará o nosso arquivo. Para você verificar se o arquivo realmente foi criado, vá no ícone da pasta ao lado esquerdo.

![[pc1-05-fig17.webp]]

**Figura 17 – Saída do Código 3**

*Fonte: Reprodução*

**#ParaTodosVerem:** figura com o fundo preto demonstrando a criação do arquivo. A Figura ainda contém um retângulo em vermelho demonstrando onde o arquivo foi criado. São apresentados, ainda, códigos que estão na cor branca e comentários na cor verde. Fim da descrição.

### Em Síntese

**Já está mais do que comprovado que a tecnologia possui um papel importante na sociedade. Com a tecnologia podemos ir mais longe na busca do conhecimento e obter ideias inovadoras. Atualmente, a tecnologia traz muitos benefícios e conforto para as pessoas. Hoje realizamos quase todas as nossas rotinas na palma da mão com os nossos** **_smartphones_ . Isso só é possível porque algum desenvolvedor criou excelentes aplicativos através da programação. A programação possibilita a criação de diversos** **_softwares_ , seja** **_mobile_ ,** **_web_ ou** **_desktop_ .**

**Na programação, muitas vezes, é necessário a manipulação de dados, sejam dados de entrada ou de saída. Esta Unidade de ensino traz um estudo sobre manipulação de arquivo texto em** **_Python_ . Aqui, estudamos os principais recursos sobre a criação, leitura e escrita em arquivo texto.**
