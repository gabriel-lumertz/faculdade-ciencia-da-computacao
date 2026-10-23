---
materia: "Modelagem de Dados"
modulo: "Banco de Dados"
semestre: 2
unidade: 1
tipo: material-teorico
fonte: "raw/2-semestre/MODELAGEM DE DADOS/Modelagem de Dados 01.pdf"
tags: [faculdade, modelagem-de-dados, semestre-2]
aliases: ["Modelagem de Dados - Unidade 1"]
---

# Banco de Dados

## Objetivos da Unidade

- Apresentar o histórico e a evolução dos bancos de dados;

- Conhecer suas utilizações e modelos;

- Compreender os principais bancos de dados em uso no mercado.

###### VOCÊ SABE RESPONDER?

Para darmos início à unidade, convidamos você a refletir acerca da questão: você conhece a aplicação de Banco de Dados?

## Evolução Histórica de Banco de Dados

Os seres humanos começaram a armazenar informações há muito tempo. Há décadas, elaborados sistemas de banco de dados foram desenvolvidos por escritórios governamentais, bibliotecas, hospitais e organizações empresariais, e alguns dos princípios básicos desses sistemas ainda são usados hoje.

A seguir, apresentaremos, de maneira cronológica, os principais destaques ocorridos na evolução dos bancos de dados eletrônicos.

###### 1960

Foi marcada pela criação de banco de dados eletrônicos. O desenvolvimento do IMS (um banco de dados hierárquico criado pela IBM) e o aparecimento dos primeiros sistemas de banco de dados de redes.

###### 1970

Surgimento do Modelo de dados relacional e a implementação de sistemas de banco de dados relacionais.

###### 1980

SQL ( _Structured Query Language_ ) torna-se um padrão mundial para os modelos relacionais. Sistemas de banco de dados orientados às aplicações (espacial, científico, de engenharia etc.).

###### 1990

_Data mining, data warehousing_ , bancos de dados multimídia e bases de dados Web e os primeiros protótipos dos modelos orientados a objetos.

###### Anos 2000

Gerenciamento de dados de fluxo e mineração:

- Mineração de dados e suas aplicações;

- Tecnologia da Web;

- XML;

- Integração de dados;

- Redes Sociais;

- Computação em nuvem;

- Sistemas de informação globais.

## O que é um Banco de Dados

Um banco de dados é uma coleção de dados. Essa definição pode parecer muito simples, não é mesmo? Mas, resume muito bem o que qualquer banco de dados é. Os bancos de dados suportam armazenamento e manipulação de dados, sejam eles eletrônicos ou não.

Um banco de dados pode ser tão simples quanto um arquivo de texto com uma lista de nomes. Ou podem ser tão complexos quanto um grande sistema de gerenciamento de banco de dados relacional, com ferramentas embutidas para ajudá-los a manter os dados.

Em nosso cotidiano, interagimos com bancos de dados em muitos momentos. Uma lista de telefones on-line, por exemplo, definitivamente usaria banco de dados para armazenar dados relativos a pessoas, números de telefone, outros detalhes de contato etc. Sua prestadora de serviços de eletricidade utiliza um banco de dados para gerenciar o faturamento, problemas relacionados com o cliente, para lidar com dados de panes etc.

Consideremos também o Facebook. Ele precisa armazenar, manipular e apresentar dados relacionados a usuários, seus amigos, mensagens, anúncios e muito mais.

##### Site

Qual é o Banco de Dados mais utilizado no mundo?

## O que é um Sistema Gerenciador de Banco de Dados

Sistema de Gerenciamento de Banco de Dados (SGBD) é um conjunto de programas que permitem aos seus usuários controlar o acesso ao banco de dados, manipular dados, relatórios / representação de dados.

A seguir serão apresentados os quatro principais modelos ou tipos de SGBD.

##### Importante

SGBD é o nome dado aos _softwares_ que gerenciam bancos de dados, e não o tipo do banco de dados.

### Hierárquico

O modelo hierárquico foi desenvolvido nos anos 60 para gerenciar grandes quantidades de dados para projetos de fabricação complexos. Sua estrutura lógica básica é representada por uma árvore de cabeça para baixo. A estrutura hierárquica contém níveis ou segmentos.

Um segmento é o equivalente ao tipo de registro de um sistema de arquivos. Dentro da hierarquia, uma camada superior é percebida como o pai do segmento diretamente abaixo dele, que é chamado de filho. O modelo hierárquico descreve um conjunto de relações um-para-muitos (1: M) entre um pai e seus segmentos filhos. (Cada pai pode ter muitos filhos, mas cada filho tem apenas um pai.).

O editor de registro do Windows (figura 1) é um exemplo de um banco de dados hierárquico.

![[md2-01-fig03.webp]]

**Figura 1 –** Mostra a imagem da janela do Editor de Registro do Windows. Uma forma de organizar os arquivos hierarquicamente

*Fonte: Acervo do conteudista*

**#ParaTodosVerem:** _printscreen_ da janela do editor de registro do windows, onde se apresentam ao lado esquerdo, na vertical, arquivos na cor amarela e ao lado direito um espaço branco onde o conteúdo das pastas se apresentam.

Na parte superior, há uma barra de ferramentas, e na parte inferior, uma barra de rolagem. Fim da descrição.

Um SGBD nesse modelo possui as seguintes vantagens:

- Simplicidade conceitual;

- Segurança de banco de dados;

- Independência dos dados;

- Integridade do banco de dados;

- Eficiência em lidar com uma grande base de dados.

Quanto às desvantagens:

- Implementação complexa;

- Difícil gerenciamento;

- Falta de independência estrutural;

- Limitações de implementação;

- Falta de normas e padrões bem definidos.

Exemplos de sistemas de gerenciamento de banco de dados hierárquico incluem os bancos de dados _Information Management System_ (IMS) e o _SYSTEM_ 2000.

### Rede

Consideramos o SGBD um modelo em rede, quando este organiza os dados em uma estrutura de rede. Isso geralmente resulta em complexas estruturas de banco de dados. Comparando como o modelo hierárquico, no modelo em Rede, o registro-filho pode possuir diversos pais, pois em uma rede os nós podem ter o máximo de conexões possíveis.

![[md2-01-fig04.webp]]

**Figura 2 –** Modelo de Rede em nós Fonte: Pixabay.com

**#ParaTodosVerem:** ilustração que representa o modelo de rede em nós, com várias conexões e esferas interligadas formando uma pirâmide. As esferas e as hastes que as interligam são cinzase no centro da pirâmide há uma esfera verde. Fim da descrição.

Embora o modelo de banco de dados de rede seja pouco utilizado atualmente, as definições de conceitos de banco de dados que surgiram com esse modelo ainda são utilizadas por modelos de dados mais modernos. Alguns conceitos importantes que foram definidos nesse momento são:

###### O esquema

É a organização conceitual de todo o banco de dados visto pelo administrador do banco de dados.

###### O subesquema

Define a parte do banco de dados “visível” pelos programas aplicativos, os quais produzem as informações desejadas a partir dos dados contidos no banco de dados.

**_O Data Manipulation Language_ (DML)**

É a linguagem que define o ambiente no qual os dados podem ser gerenciados e para trabalhar com os dados no banco de dados.

**O** **_Data Definition Language_ (DDL)**

Linguagem de definição de dados de esquema, a qual permite ao administrador do banco de dados definir os componentes do esquema.

Um SGDB de Rede possui as seguintes vantagens:

- Simplicidade conceitual;

- Permite gerenciar uma grande quantidade de relações;

- Possibilita a flexibilidade de acesso a dados;

- Promove a integridade do banco de dados;

- Favorece a independência dos dados;

- Possui normas e padrões bem definidos.

Quanto às desvantagens:

- Complexidade do sistema;

- Falta de independência estrutural.

O _RDM Server_ , _IDMS_ e _TOTAL_ são exemplos de sistemas de gerenciamento de banco de dados que implementam o modelo de rede.

### Relacional

Esse tipo de SGBD define relações de banco de dados em forma de tabelas, também conhecidas como relações. Ao contrário do SGBD de rede, o tipo relacional não suporta relacionamentos do tipo muitos para muitos.

Criado na década de 1970 por Edgar Frank Codd, pesquisador da IBM, a base do modelo relacional é um conceito matemático conhecido como relação. O modelo de dados relacional executa as mesmas funções básicas fornecidas pelos SGBDs dos tipos hierárquico e de rede, além de uma série de outras funções que tornam o modelo de dados relacional mais fácil de entender e implementar. Esse é o tipo de SGBD mais popular no mercado.

##### Site

_Site_ 1: Conceito de relação matemática.

_Site_ 2: As regras de Codd para Bancos de Dados Relacionais.

_Site_ 1 _Site_ 2

Uma das grandes vantagens desse modelo (SGBD-R) é a sua capacidade de ocultar as complexidades do modelo relacional do usuário. O SGBD-R gerencia todos os detalhes físicos, enquanto o usuário vê o banco de dados relacional como uma coleção de tabelas nas quais os dados são armazenados. O usuário pode manipular e consultar os dados de uma forma que parece intuitiva e lógica.

Uma tabela relacional armazena uma coleção de dados relacionados. A esse respeito, a tabela de banco de dados relacional se assemelha a um arquivo, disposta em linhas e colunas.

|**Id**|**Nome**|**Rgm**|**Sexo**|**Dt Nasc**|
|---|---|---|---|---|
|123|João|42315|M|13/03/1985|
|124|Maria|42888|F|21/08/1990|

Outra grande vantagem é a sua linguagem de consulta poderosa e flexível, o _Structured Query Language_ (SQL), a qual permite ao usuário especificar o que deve ser feito sem especificar como deve ser feito. O SGBD-R usa o SQL para traduzir consultas de usuários em instruções para recuperar os dados solicitados. O SQL torna possível recuperar dados com muito menos esforço do que qualquer outro banco de dados ou ambiente de arquivos.

O SGBD-Relacional possui as seguintes vantagens:

- A independência estrutural;

- Melhor simplicidade conceitual;

- Projeto, implementação, gerenciamento e uso mais simples de banco de dados;

- Sistema de gerenciamento de banco de dados poderoso.

Quanto às desvantagens, temos:

- Sobrecarga substancial de _hardware_ e _software_ de sistema;

- Possibilidade de má concepção e implementação.

Exemplos de sistemas de gerenciamento de banco de dados relacional incluem banco de dados _MySQL, Oracle e Microsoft SQL Server_ .

### Orientado a Objetos

No SGBD orientado a objetos (SGBD-OO), tanto os dados como suas relações estão contidos em uma única estrutura conhecida como objeto. Esse modelo de dados é outro método de representar objetos do mundo real. Considera cada objeto no mundo como objetos e os isola uns dos outros.

O SGBD-OO baseia-se nos seguintes componentes:

- Um objeto é uma abstração de uma entidade do mundo real. Em termos gerais, um objeto pode ser considerado equivalente a uma tabela do SGBD Relacional. Mais precisamente, um objeto representa apenas uma ocorrência de uma entidade;

- Atributos descrevem as propriedades de um objeto. Por exemplo, um objeto PESSOA inclui os atributos Nome, Número de Segurança Social e Data de Nascimento;

- Objetos que compartilham características semelhantes são agrupados em classes. Uma classe é uma coleção de objetos semelhantes com estrutura compartilhada (atributos) e comportamento (métodos). O método de uma classe representa uma ação no mundo real, como encontrar o nome de uma pessoa selecionada, alterar o nome de uma pessoa ou imprimir o endereço de uma

pessoa. Em outras palavras, os métodos são o equivalente a procedimentos em linguagens de programação tradicionais. Em termos orientados a objetos, os métodos definem o comportamento de um objeto;

- As classes são organizadas em uma hierarquia de classes. A hierarquia de classe se assemelha a uma árvore invertida na qual cada classe tem apenas um pai. Por exemplo, a classe CLIENTE e a classe EMPREGADO compartilham uma classe pai PESSOA, o que chamamos de herança;

- A herança é a capacidade de um objeto dentro da hierarquia de classe herdar os atributos e métodos das classes acima dele. Por exemplo, duas classes, CLIENTE e EMPREGADO, podem ser criadas como subclasses da classe PESSOA. Nesse caso, CLIENTE e EMPREGADO herdarão todos os atributos e métodos de PESSOA.

![[md2-01-fig06.webp]]

**Figura 3 –** Organograma

###### Fonte: Acervo do conteudista

**#ParaTodosVerem:** organograma composto pelos sequintes elementos: Pessoa - ID + Nome + E-mail + Telefone + ImprimeDados(), abaixo: Cliente - +endereçoEntrega + imprimeEndereço() + cadastraCliente(pessoa:Pessoa), ao lado: Empregado - +endereçoEntrega + setor + cargo + salário + cadastraEmpregado(pessoa:Pessoa). Fim da descrição.

![[md2-01-fig07.webp]]

A Figura 3 apresenta a classe de objeto PESSOA como classe pai e as classes de objetos CLIENTE E EMPREGADO como subclasses ou classes-filho da classe de objeto PESSOA. Para complementar a classe PESSOA possui os atributos:

- Id, nome, email e telefone;

- E o método ImprimeDados();

- A sublasse CLIENTE possui o atributo endereçoEntrega();

- E os métodos imprimeEndereço() e cadastraCliente este último que utiliza um objeto do tipo pessoa;

- A subclasse EMPREGADO possui os atributos endereço, entrega, setor, cargo e salário;

- E o método cadastraEmpregado() que utiliza um objeto do tipo pessoa.

As vantagens oferecidas por esse modelo são as seguintes:

- Apresentação visual inclui conteúdo significativo;

- Alta integridade do banco de dados;

- Independência estrutural e de dados.

Quanto às desvantagens:

- Falta de normas e padrões bem definidos;

- Acesso completo aos dados de navegação;

- Curva de aprendizagem íngreme.

Exemplos de sistemas de gerenciamento de banco de dados orientados a objetos incluem os bancos de dados CACHÉ, DB4Objects, VERSANT, JASMIN e MATISSE.

##### Site

SGBD-OO – Banco de Dados Orientado a Objetos: Uma Realidade.

## A Importância dos Bancos de Dados

As informações são úteis para relatar a uma organização os resultados de suas operações atuais e colaborar com a gestão de estratégias para os negócios.

As informações organizacionais são armazenadas em um banco de dados. Aplicativos e programas, como sistemas de gerenciamento da cadeia de suprimentos e sistemas de gerenciamento de relacionamento com o cliente, acessam os dados no banco de dados para que o programa possa consultá-lo e exibir, de maneira intuitiva, o que está acontecendo com o negócio.

O valor da informação reside não apenas na própria informação, mas nas ações que surgem da informação. Por exemplo, se as informações o alertarem para a má satisfação do cliente, isso só será útil se isso criar uma mudança na forma como o negócio lida com os clientes. Assim, o processo de informação deve fazer parte de um processo de revisão mais amplo dentro do negócio para obter os melhores resultados.

Nesse contexto, um banco de dados se faz importante, pois gerencia e possibilita o acesso à informação. Elaborar como os dados serão armazenados e de qual forma, é parte extremamente relevante para o sucesso do gerenciamento e manutenção do banco de dados, tão vital e essencial para a organização. Nos capítulos seguintes, iniciaremos nossos estudos sobre a modelagem de dados.

Até breve.

## Em Síntese

Após analisar o histórico e a evolução dos bancos de dados, assim como suas utilizações e modelos ao longo do tempo, torna-se evidente a significativa transformação dessas ferramentas. Desde seus primórdios, quando os dados eram armazenados de maneira rudimentar, até os modernos e complexos sistemas atuais, os bancos de dados passaram por um notável processo de aprimoramento e adaptação.

Essas bases de dados, inicialmente voltadas para o armazenamento de informações de forma estática, tornaram-se centrais para uma ampla gama de aplicações. Por meio de modelos relacionais, orientados a objetos, NoSQL e outros, esses sistemas se diversificaram para atender a diferentes necessidades de armazenamento e manipulação de dados em ambientes empresariais, científicos e pessoais.

No mercado contemporâneo, os bancos de dados tornaram-se essenciais para a gestão eficiente de informações em empresas, oferecendo não apenas armazenamento, mas também ferramentas analíticas e de inteligência artificial para suportar a tomada de decisões estratégicas. Os principais modelos, como bancos de dados relacionais, documentais, de colunas e gráficos, têm sido amplamente adotados, cada um com suas características específicas, para atender a diferentes contextos e necessidades.

Dessa forma, a compreensão do histórico, evolução e utilização dos bancos de dados é crucial para profissionais e organizações que buscam aproveitar ao máximo o potencial dessas ferramentas na era da informação, na qual a gestão e análise de dados se tornaram pilares fundamentais para o sucesso e a inovação nos negócios e na pesquisa.
