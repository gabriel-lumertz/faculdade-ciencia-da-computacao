---
materia: "Modelagem de Dados"
modulo: "Modelo ER – Parte 2"
semestre: 2
unidade: 4
tipo: material-teorico
fonte: "raw/2-semestre/MODELAGEM DE DADOS/Modelagem de Dados 04.pdf"
tags: [faculdade, modelagem-de-dados, semestre-2]
aliases: ["Modelagem de Dados - Unidade 4"]
---

# Modelo ER – Parte 2

## Objetivos da Unidade

- Apresentar os conceitos de relacionamento;

- Discutir os atributos e as notações gráficas;

- Compreender sua aplicação para a representação do MER.

###### VOCÊ SABE RESPONDER?

Para darmos início à unidade, contudo, convidamos você a refletir acerca da questão: você sabe o que é Modelo ER?

## Introdução

Nesta unidade daremos sequência ao estudo do modelo entidade-relacionamento (Modelo-ER), estudaremos os conceitos e características de relacionamentos, atributos e um pouco mais sobre a notação gráfica criada por Peter Chen na década de 1970.

## Relacionamento

Um relacionamento descreve uma associação entre entidades. Isto é, um relacionamento representa a quantidade de instâncias de uma entidade em relação à outra entidade.

Por exemplo, existe uma relação entre clientes e vendedores que pode ser descrita da seguinte forma: um vendedor pode atender muitos clientes e cada cliente pode ser atendido por um vendedor. Em um Diagrama de entidade-relacionamento (DER), representamos um relacionamento por meio de um losango. No diagrama abaixo, podemos observar o relacionamento (atende) entre as entidades Vendedor e Cliente.

![[md2-04-fig01.webp]]

**Figura 1 –** Um vendedor atende vários Clientes **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra vendedor, inteligado por meio de uma linha azul com um losângo azul com a palavra atende, interligado com um retângulo azul com a palavra cliente. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: vendedor, atende, cliente. Fim da descrição.

##### Trocando Ideias

“Relacionamento é um conjunto de associações entre ocorrências de entidades” (Heuser, 2010).

Antes de começar a estabelecer relações entre entidades do projeto de banco de dados, devemos saber quais tipos de relações podem existir entre um determinado par de entidades. Saber identificá-los adequadamente é uma habilidade inestimável para projetar um banco de dados com êxito.

Para entender como representar um relacionamento em um modelo entidade-relacionado, serão apresentados os conceitos de **Grau de Relacionamento** (unário, binário e ternário) e **Cardinalidade** (Máxima e Mínima).

### Grau de Relacionamento

O número de conjuntos de entidades que participam de um relacionamento é chamado de grau de relacionamento. Os três graus mais comuns de um relacionamento em um banco de dados são: unário, binário e ternário.

![[md2-04-fig03.webp]]

**Figura 2 –** Uma relação unária R é uma associação entre duas instâncias do mesmo tipo de entidade (isto é, R Є E1 × E1). Por exemplo, todo empregado em uma determinada empresa possui um supervisor, e todo supervisor é um empregado. **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: retângulo azul com a palavra empregado, interligado por duas linhas retas a um losango com a palavra supervisor, abaixo, três retângulos verdes, alinhados horizontalmente, onde se apresentam as palavras: empregado, supervisiona, empregado. Fim da descrição.

![[md2-04-fig04.webp]]

**Figura 3 –** Uma relação binária R é uma associação entre duas instâncias de dois tipos de entidade diferentes (isto é, R Є E1 × E2). Por exemplo, numa loja, existe uma relação binária entre um vendedor (entidade VENDEDOR) e um cliente (entidade CLIENTE): um vendedor atende um cliente.

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra vendedor, interligado por meio de uma linha azul com um losângo azul com a palavra atende, interligado com um retângulo azul com a palavra cliente. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: vendedor, atende, cliente. Fim da descrição.

![[md2-04-fig05.webp]]

**Figura 4 –** Uma relação ternária R é uma associação entre três instâncias de três diferentes tipos de entidade (isto é, R Є E1 × E2 × E3). Por exemplo, considere um professor que leciona diversas disciplinas em diversas turmas em uma Universidade. Nesse caso, os tipos de entidade PROFESSOR, TURMA e DISCIPLINA se relacionam entre si com relacionamentos ternários: um professor leciona uma disciplina em uma turma. **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama composto por três retângulos azuis: Turma, Professor e Disciplina, ligados por um losango azul: Possui nove retângulos verdes, alinhados em três colunas com três linhas que se relacionam entre si com relacionamentos ternários. Coluna da esquerda: Professor, Professor, Turma; coluna do centro: Possui, Possui, Possui; coluna da direita: Turma, Disciplina, Disciplina. Fim da descrição.

### Cardinalidade

Quando dizemos cardinalidade de um relacionamento, queremos dizer a capacidade de contar o número de entidades envolvidas nesse relacionamento. Por exemplo, se instâncias das entidades A e B estiverem conectadas por uma relação, então a cardinalidade máxima representa o número máximo de instâncias da entidade B que podem ser associadas a qualquer instância da entidade A.

No entanto, não é necessário atribuir um valor de número para cada nível de conexão em um relacionamento. Na verdade, o termo cardinalidade máxima refere-se a apenas dois valores possíveis: um (1) ou muitos (N).

Embora isso possa parecer muito simples, o valor máximo de cardinalidade de uma relação, nos permite definir os três tipos de relações possíveis entre os tipos de entidade A e B: um-para-muitos (1:N), muitos-para-muitos (N:M) e um-para-um (1:1).

##### Trocando Ideias

Cardinalidade é uma propriedade que especifica a quantidade de ocorrências associadas entre duas entidades dentro de uma relação.

##### Relação um-para-muitos (1:N)

Uma relação 1:N descreve que uma instância do conjunto A se relaciona com diversas instâncias do conjunto B; e uma instância do conjunto B se relacionando com apenas uma instância do conjunto A.

**Tabela 1**

|**Conjunto A**|**Conjunto B**|
|---|---|
||Instânica1|
|Instânica1|Instânica2<br>Instânica3|
|Instânica2|Instânica4|
|Instânica3|Instânica5<br>Instânica6|
|Instânica4|Instânica7|

Considere que uma pessoa pode ter registrado em seu nome vários carros, contudo, um carro é registrado apenas em nome de uma pessoa. Desse modo, a pessoa (“um”) está relacionada com carros (“muitos”). Para o seguinte exemplo, descrevemos a relação como “PESSOA possui CARRO” e representamos como 1:N.

![[md2-04-fig07.webp]]

**Figura 5 –** Descrevemos a relação como “PESSOA possui CARRO” e representamos como 1:N **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra pessoa, interligado por meio de uma linha azul com um losango azul com a palavra possui, interligado com um retângulo azul com a palavra carro. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: pessoa, possui, carro. Fim da descrição.

Lemos esse diagrama como: “Uma pessoa pode possuir vários carros e um carro pode ser registrado em nome de uma pessoa”.

Do mesmo modo, em nosso segundo exemplo, um cliente pode possuir vários pedidos em uma loja, contudo, um pedido pertence apenas a um cliente. Para esse exemplo temos o seguinte diagrama:

![[md2-04-fig08.webp]]

**Figura 6 –** Um cliente pode possuir vários pedidos em uma loja, contudo, um pedido pertence apenas a um cliente **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra cliente, interligado por meio de uma linha azul com um losango azul com a palavra possui, interligado com um retângulo azul com a palavra pedido. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: cliente, possui, pedido. Fim da descrição.

Lemos esse diagrama como: “Um cliente pode possuir vários pedidos e um pedido pertence a um cliente”.

##### Relação muitos-para-muitos (N:M)

Uma relação N:M descreve que uma instância do conjunto A se relaciona com diversas instâncias do conjunto B; e uma instância do conjunto B se relaciona com diversas instâncias do conjunto A.

**Tabela 2**

|**Conjunto A**|**Conjunto B**|
|---|---|
||Instânica1|
|Instânica1|Instânica2<br>Instânica3|
||Instânica3|
|Instânica2|Instânica4|
||Instânica5|
||Instânica2|
|Instânica3|Instânica5<br>Instânica6|
||Instânica7|
|Instânica4|Instânica5<br>Instânica7|

Vamos a um exemplo: um autor pode escrever vários livros e um livro pode ser escrito por diversos autores. Assim, o autor (“muitos) está relacionado a livro (“muitos”). Descrevemos esse relacionamento como “AUTOR escreve LIVRO” e representamos como “N:M”.

![[md2-04-fig09.webp]]

**Figura 7 –** Descrevemos esse relacionamento como “AUTOR escreve LIVRO” e representamos como “N:M”

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra autor, interligado por meio de uma linha azul com um losango azul com a palavra escreve, interligado com um retângulo azul com a palavra livro. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: autor, escreve, livro. Fim da descrição.

Vejamos outro exemplo: um empregado pode trabalhar em vários projetos e um projeto pode alocar vários empregados. Podemos descrever esse relacionamento como: “EMPREGADO trabalha PROJETO” e representamos como “N:M”.

![[md2-04-fig10.webp]]

**Figura 8 –** Podemos descrever esse relacionamento como: “EMPREGADO trabalha PROJETO” e representamos como “N:M

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra empregado, interligado por meio de uma linha azul com um losango azul com a palavra trabalha, interligado com um retângulo azul com a palavra projeto. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: empregado, trabalha, projeto. Fim da descrição.

Lemos esse diagrama como “Um empregado pode trabalhar em vários projetos e um projeto pode alocar vários empregados”.

##### Relação um-para-um (1:1)

Uma relação 1:1 descreve que uma instância do conjunto A se relaciona com apenas com uma instância do conjunto B; e uma instância do conjunto B se relaciona apenas com uma instância do conjunto A.

**Tabela 3**

|**Conjunto A**|**Conjunto B**|
|---|---|
|Instânica1|Instânica2|
|Instânica2|Instânica3|
|Instânica3|Instânica4|
|Instânica4|Instânica1|

Vamos a mais um exemplo: uma loja possui um departamento que é gerenciado por apenas um empregado. Diante do cenário, podemos descrever esse relacionamento como: “EMPREGADO gerencia DEPARTAMENTO” e representamos como “1:1”. Veja a representação desse relacionamento no DER abaixo:

![[md2-04-fig11.webp]]

**Figura 9 –** Podemos descrever esse relacionamento como: “EMPREGADO trabalha PROJETO” e representamos como “N:M

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra empregado, interligado por meio de uma linha azul com um losango azul com a palavra gerencia, interligado com um retângulo azul com a palavra departamento. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: empregado, gerencia, departamento. Fim da descrição.

Podemos ler esse diagrama como: “Empregado gerencia um departamento e um departamento é gerenciado por um empregado”.

Outro bom exemplo de um relacionamento um-para-um é entre as entidades Cliente e Login dentro de uma plataforma de vendas on-line. Um cliente possui apenas um login e o login pertence a apenas um cliente. Veja a representação desse relacionamento no DER abaixo:

![[md2-04-fig12.webp]]

**Figura 10 –** Diagrama de relacionamento DER

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra cliente, interligado por meio de uma linha azul com um losango azul com a palavra possui, interligado com um retângulo azul com a palavra login. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: cliente, possui, login. Fim da descrição.

### Cardinalidade Mínima

O termo cardinalidade mínima refere-se ao número mínimo de instâncias de uma entidade que deve estar associada a uma única instância de uma entidade relacionada.

Utilizamos a representação de cardinalidade mínima para expressar as restrições mínimas de uma ocorrência em uma dada entidade. Ou seja, as cardinalidades mínimas representarão a obrigatoriedade ou não de uma ocorrência em uma entidade. As cardinalidades mínimas possuem os seguintes valores possíveis: 0 e 1.

##### Cardinalidade mínima um (0)

Considere a seguinte regra de negócio:

- Um cliente **pode possuir** diversos pedidos, contudo, todo pedido **deve** pertencer à **somente um cliente** .

Nesse cenário, sabemos que esse tipo de relacionamento é do tipo “um-para-muitos”, ou seja, 1:N, porque um (1) cliente pode possuir diversos (N) pedidos. Já temos a informação da cardinalidade máxima de cada entidade. Agora, para obter as informações a respeito das cardinalidades mínimas de cada entidade, devemos nos atentar à regra de negócio e identificar as palavras que denotam restrições, que nesse caso são: “... **pode possuir** ...” e “... **deve** ... **somente um cliente** ”. Essa análise resulta em:

- O cliente pode ou não possuir um pedido (mínimo 0), mas todo pedido deve pertencer a um cliente (mínimo 1).

Veja a representação desse cenário no diagrama DER abaixo:

![[md2-04-fig13.webp]]

**Figura 11 –** O cliente pode ou não possuir um pedido (mínimo 0), mas todo pedido deve pertencer a um cliente (mínimo 1) **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra cliente, interligado por meio de uma linha azul com um losango azul com a palavra possui, interligado com um retângulo azul com a palavra pedido. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: cliente, possui, pedido. Há um traço vermelho que interliga Cliente à (0,N), e um traço azul que interliga Pedido à (1,1). Fim da descrição.

Mais uma vez é preciso lembrar que as cardinalidades máximas e mínimas de uma entidade em relação à outra, são representadas no lado oposto à da entidade. Lemos esse diagrama do seguinte modo:

- Um cliente pode possuir no mínimo zero (0) e no máximo diversos pedidos (N);

- Um pedido deve pertencer à no mínimo um (1) cliente e no máximo a um (1) cliente.

##### Trocando Ideias

O grau da cardinalidade de uma entidade é sempre representado ao lado oposto da entidade.

##### Cardinalidade mínima zero (1)

Considere a seguinte regra de negócio:

- Todo cliente deve possuir um login e um login deve pertencer à somente um cliente.

Sabemos que a cardinalidade (máxima) dessa relação é um-para-um. Contudo, quais são as cardinalidades mínimas? As cardinalidades representam as restrições mínimas de uma ocorrência, então, nesse caso, ao ler a sentença do cenário, podemos perceber que existem restrições mínimas para a ocorrência de LOGIN e USUÁRIO (deve possuir um login... deve pertencer à somente um...). Nesse caso, as cardinalidades representadas são 1:1 e 1:1.

Veja a representação desse cenário no diagrama DER abaixo:

![[md2-04-fig15.webp]]

**Figura 12 –** Diagrama DER

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama onde se apresentam os seguintes elementos: dentro de um retângulo azul a palavra cliente, interligado por meio de uma linha azul com um losango azul com a palavra possui, interligado com um retângulo azul com a palavra login. Abaixo, três retângulos verdes um ao lado do outro, respectivamente: cliente, possui, login. Há um traço vermelho que interliga Cliente à (1,1) e um traço azul que interliga Login à (1,1). Fim da descrição.

As cardinalidades máximas e mínimas de uma entidade em relação à outra, são representadas no lado oposto ao da entidade. Lemos esse diagrama do seguinte modo:

- Um cliente possui no mínimo um (1) login e no máximo um (1) login;

- Um Login pertence a no mínimo um (1) usuário e no máximo a um (1) usuário.

## Atributo

Um atributo é uma propriedade ou característica de uma entidade, ou uma relação. Por exemplo, o atributo Nome na ficha de um aluno é um atributo da entidade ALUNO. Uma entidade pode ter tantos atributos quanto necessário. Em um Diagrama de entidade-relacionamento (DER), representamos um atributo por meio de uma elipse ou um círculo. No diagrama abaixo, temos um exemplo de representação de atributos:

![[md2-04-fig16.webp]]

**Figura 13 –** Podemos representar os atributos de uma entidade também através de uma tabela

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama em que se apresenta: quadrado azul com a palavra Entidade, dele partem quatro linhas azuis indicando para Atributo 1, 2, 3, 4. Abaixo, uma tabela verde e branca composta por cinco linhas e uma coluna, com título Entidade, em que estão listados os atributos. Fim da descrição

Segundo Machado (2014), podemos classificar os atributos em dois tipos: Descritores e Identificadores.

## Atributos Descritores

Todo e qualquer atributo que seja capaz de identificar e representar uma característica de um objeto. Para Cougo (1997), todo atributo pode ser considerado um atributo descritivo. O que faz o atributo ser classificado com outro tipo é a presença de características funcionais adicionais, por exemplo, um atributo identificador.

### Atributos Identificadores

Um identificador (ou atributo-chave) é um único atributo ou uma combinação de atributos que identificam de forma única uma instância individual de um tipo de entidade. Por exemplo, na entidade ALUNO temos o atributo RGM como atributo identificador (ou atributo-chave), pois esse atributo, o RGM é único para cada Aluno (instância). No DER abaixo, vemos a representação desse cenário:

![[md2-04-fig17.webp]]

**Figura 14 –** Diagrama DER

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama em que se apresenta: quadrado azul com a palavra Aluno, dele partem quatro linhas azuis indicando para NrCelular, Endereço, Nome, RGM. Abaixo, uma tabela verde e branca composta por quatro linhas e uma coluna, com título Aluno, em que estão listados os atributos: RGM como campo chave primária, nome, endereço. Fim da descrição.

Na entidade ALUNO temos o atributo RGM como atributo identificador (ou atributo-chave), pois esse atributo, o RGM é único para cada Aluno (instância).

O atributo Nome, por exemplo, não pode ser um identificador porque dois alunos podem ter o mesmo nome.

Às vezes, por meio de um único atributo não é possível identificar, exclusivamente, uma instância de uma entidade. No entanto, nessas circunstâncias, identificamos um conjunto de atributos que, quando combinados, são exclusivos para cada instância da entidade. Nesse caso, o atributo-chave, também conhecido como chave composta, não é um atributo simples, mas um atributo composto que identifica, exclusivamente, cada instância de entidade.

Considere as entidades EMPREGADO e DEPENDENTE, onde um empregado pode possuir vários dependentes e um dependente deve pertencer a apenas um e no máximo um empregado. Nesse cenário, para identificar uma ocorrência única da entidade DEPENDENTE, utilizamos um atributo composto, formado por um atributo-chave de cada uma das entidades. O DER abaixo apresenta esse quadro:

![[md2-04-fig18.webp]]

![[md2-04-fig19.webp]]

**Figura 15 –** Diagrama DER **Fonte:** Acervo do conteudista

**#ParaTodosVerem:** diagrama composto por dois retângulos azuis: Empregado, dele, linhas azuis indicam - nome, id_empregado; e Dependente, dele, linhas azuis indicam - Idade, Nome, Id_Empregado, id_departamento; e um losango azul entre eles, palavra possui. Abaixo, três tabelas: da esquerda - Uma coluna e três linhas - Empregado (id_Empregado campo chave primária, nome); do centro, uma coluna e uma linha -  (1,1), possui, (0,n); da direita, uma coluna e quatro linhas - Dependente (id_Deepartamento campo chave primária, id_Empregado campo chave estrangeira, nome, idade). Fim da descrição.

Utilizamos os atributos “Id_Departamento” e “Id_Empregado” para formar a chave composta da entidade DEPENDENTE.

##### Importante

Ainda sobre o exemplo do relacionamento Empregado x Dependente: o atributo composto servirá para tornar mais rápida e eficiente a busca de informações referentes à entidade Forte, que nesse contexto é a entidade EMPREGADO. Em uma futura pesquisa no banco de dados, podemos nos deparar com a necessidade de buscar informações do Empregado. Contudo, temos inicialmente apenas informações do Dependente, e por meio da chave composta, podemos identificar o Empregado e todas as outras informações necessárias.

## Notações Gráficas ER

As notações gráficas para se desenvolver um Diagrama de entidade-relacionamento mais comumente utilizadas são as notações criadas por Peter Chen (1990). A seguir, apresentamos os principais símbolos utilizados em um DER:

**Tabela 4 –** Símbolos utilizados na DER

|**Símbolo**|**Representa**|
|---|---|
|entidade “retângulo com o nome da entidadeno<br>centro deste retângulo”|Entidade|
|atributo “está representado em bolinha vazia sem<br>preenchimento”|Atributo Descritor|
|atributo identificar “está representado em  bolinha<br>preenchida|Atributo Identificador|
|relação “colocamos sempre um verbo neste símbolo<br>e o mesmo fica descrito dentro de um losângulo”|Relacionamento|

###### Fonte: Acervo do conteudista

**#ParaTodosVerem:** tabela verde e branca, onde se apresentam os seguintes elementos, distribuídos em cinco linhas e duas colunas, na primeira coluna intitulada “Símbolo”, temos: entidade “retângulo com o nome da entidade no centro deste retângulo”, atributo “está representado em bolinha vazia sem preenchimento”, atributo identificador “está representado em bolinha preenchida”, relação “colocamos sempre um verbo neste símbolo e o mesmo fica descrito, dentro de um losângulo”; na segunda coluna intitulada “Representa”, temos: Entidade, Atributo, Descritor, Atributo Identificador, Relacionamento. Fim da descrição.

## Em Síntese

Ao explorar os conceitos de modelagem de dados, mergulhamos nos fundamentos dos relacionamentos, compreendendo sua importância na estruturação de bancos de dados. Os relacionamentos servem como conexões entre entidades, descrevendo como os dados estão interligados e como as entidades se associam.

Além disso, discutimos os atributos, elementos vitais que descrevem as características das entidades. A compreensão detalhada dos atributos, sejam eles simples ou complexos, é crucial para definir e representar corretamente as propriedades das entidades em um Modelo Entidade-Relacionamento (MER).

Exploramos as notações gráficas, como o diagrama Entidade-Relacionamento (DER), que oferecem uma representação visual clara dos relacionamentos, entidades e atributos. A visualização por meio desses diagramas facilita a compreensão da estrutura do banco de dados, permitindo uma comunicação eficaz entre os envolvidos no projeto.

Esses conceitos e suas representações gráficas não apenas constituem a base para a modelagem de dados, mas também fornecem uma linguagem unificada para descrever e documentar as estruturas dos bancos de dados, sendo essenciais para a criação de sistemas robustos e bem organizados.
