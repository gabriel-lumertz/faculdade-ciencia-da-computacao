---
materia: "Modelagem de Dados"
modulo: "Ferramenta para Modelagem ER"
semestre: 2
unidade: 6
tipo: material-teorico
fonte: "raw/2-semestre/MODELAGEM DE DADOS/Modelagem de Dados 06.pdf"
tags: [faculdade, modelagem-de-dados, semestre-2]
aliases: ["Modelagem de Dados - Unidade 6"]
---

# Ferramenta para Modelagem ER

## Objetivos da Unidade

- Compreender como um banco de dados relacional é organizado (que estruturas de dados são usadas, como elas estão relacionadas);

- Apresentar os conceitos aplicados ao modelo de dados usado nos sistemas gerenciadores de banco de dados do tipo relacional;

- Estudar um pouco sobre duas ferramentas CASE que auxiliam no desenvolvimento do projeto de Modelagem de dados: BrModelo e MySQL Workbench.

###### VOCÊ SABE RESPONDER?

Para darmos início à unidade, contudo, convidamos você a refletir acerca da questão: você conhece alguma ferramenta para Modelagem ER?

## Introdução

Nesta unidade, estudaremos sobre duas ferramentas CASE que auxiliam no desenvolvimento do projeto de Modelagem de Dados: BrModelo e MySQL _Workbench_ .

##### Reflita

Mas, afinal, o que são ferramentas CASE?

O termo CASE vem do acrônimo _Computer-aided software engineering_ , ou traduzindo, Engenharia de _Software_ Auxiliada por Computador. A utilização de ferramentas CASE permite que os projetistas e outros atores envolvidos no processo de desenvolvimento do projeto de banco de dados compartilhem uma visão comum de cada estágio de desenvolvimento. Ferramentas CASE ajudam a garantir um processo disciplinado além de retratar o progresso (ou falta dele) graficamente.

Alguns dos benefícios que as ferramentas CASE e as abordagens semelhantes trazem, é a possibilidade de fazer com que o cliente faça parte do processo (através de diagramas ou análise de regras de negócios) de uma forma mais dinâmica e assertiva. Tornando, assim, o objeto modelado o mais próximo à necessidade e à realidade do cliente.

Como esse tipo de abordagem enfatiza o teste e o redesenho, o custo de manutenção de um produto ao longo de sua vida útil pode ser reduzido consideravelmente. Uma abordagem organizada para o desenvolvimento incentiva a reutilização de código e design, reduzindo custos e melhorando a qualidade.

No estudo sobre Modelagem de Dados, estudaremos, especificamente, ferramentas que auxiliam na concepção, desenvolvimento e implementação de sistemas de banco de dados.

Uma das grandes vantagens oferecidas pelas ferramentas CASE de banco de dados é a possibilidade de criar scripts SQL a partir de um diagrama de entidade-relacionamento (DER).

O SQL ( _Structure Query Language_ ) é uma linguagem utilizada para armazenar e gerenciar dados no SGBD (MySql, Oracle, SqlServer). SQL foi a primeira linguagem comercial introduzida para o modelo relacional do E. Codd. Hoje, quase todo o SGBD usa o SQL como a linguagem de banco de dados padrão. SQL é usado para criar e excluir tabelas; inserir, atualizar e excluir dados, e selecionar e exibir dados em um SGBD.

Nos exemplos práticos a seguir, demonstraremos como criar diagramas de entidade-relacionamento (DER) e, em seguida, exportar esse esquema em formato SQL, pronto para ser utilizado na criação de tabelas em um banco de dados.

##### Leitura

O que é SQL e por que você deve estudá-lo? Disponível no QR _Code_ .

## BrModelo

A ferramenta BrModelo é uma ferramenta _freeware_ que possibilita o desenvolvimento de diagramas DER, modelo lógico, e exportar esses artefatos em formato de script SQL para criação de tabelas no banco de dados (Cândido, 2007).

##### Site

O software BrModelo 3.0 pode ser baixado e executado apenas nos sistemas operacionais Windows.

### Visão Geral da Ferramenta

A ferramenta BrModelo utiliza o padrão de desenvolvimento _drag_ and _drop_ , ou seja, você arrasta e solta objetos para dentro do palco do _software_ . Abaixo, temos a visão geral da ferramenta:

![[md2-06-fig04.webp]]

*Figura 1 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal, onde estão dispostos os principais objetos do DER - entidade, relacionamento, atributos. No canto direito há um menu vertical, que apresenta as propriedades do objeto E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

Em destaque, temos três áreas da ferramenta:

Área 1

É o palco do _software_ . É nesse espaço que é organizado os objetos do DER.

Área 2

Aqui, estão dispostos os principais objetos do DER (entidade, relacionamento, atributos). Esses objetos são arrastados para o palco do _software_ .

Área 3

Refere-se à tela de propriedades de objeto. Ao selecionar algum objeto no palco, essa tela apresenta as propriedades do objeto.

## Criando um Diagrama de Entidade-Relacionamento (DER)

Nessa sessão, criaremos um DER a partir do seguinte cenário:

- Um funcionário deve possuir no mínimo zero dependente e no máximo muitos dependentes;

- Um dependente deve pertencer, no mínimo, a 1 funcionário e, no máximo, a 1 funcionário.

A partir dessas assertivas, verificamos que existe um relacionamento entre duas entidades: “Funcionário” e “Dependente”, bem como sua cardinalidade.

Nesse contexto, criaremos o DER nos passos a seguir:

Passo 1 – Clique no objeto “Entidade” e, em seguida, selecione Entidade.

![[md2-06-fig05.webp]]

*Figura 2 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo, na parte superior há um menu horizontal, em que se destacam os elementos: Esquema Conceitual - Entidade, Especialização e Atributos. No canto direito há um menu vertical, no qual se apresentam os elementos “Seleção” e “Informações Modelo Conceitual”. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

Passo 2 – Arraste o objeto para o palco e com o objeto selecionado, altere a propriedade nome para: Funcionario (sem acento) e, em seguida, pressione “Enter” no teclado.

![[md2-06-fig06.webp]]

*Figura 3 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical em que se destacam os elementos: “Seleção” - Edição Entidade, Nome, Funcionário. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Entidade 1”. Fim da descrição.

Passo 3 – Clique no objeto “Entidade” e, em seguida, selecione Relação.

![[md2-06-fig07.webp]]

*Figura 4 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal, no qual se destacam os elementos: Entidade - Relação - Criar Relação. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”. Fim da descrição.

Passo 4 – Arraste o objeto para o palco e, com o objeto selecionado, altere a propriedade nome para: possui e, em seguida, pressione “Enter” no teclado.

![[md2-06-fig08.webp]]

*Figura 5 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical, no qual se destacam os elementos: “Nome” - “Possui”. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário” e um losango denominado “Relação 1”. Fim da descrição.

Passo 5 – Adicione um objeto “Entidade” ao palco e altere a propriedade nome para: Dependente e, em seguida, pressione “Enter” no teclado.

![[md2-06-fig09.webp]]

*Figura 6 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal, cujo item “seleção” está ativado. No canto direito há um menu vertical, onde se destacam os elementos: “Nome” - “Dependente”. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, um losango “possui” e um retângulo “Entidade 1”. Fim da descrição.

Para representar os graus de relacionamento e sua as cardinalidades (mínimas e máximas), utilizamos o objeto “Ligar Objetos”, destacado na imagem abaixo:

![[md2-06-fig10.webp]]

*Figura 7 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. Uma das ferramentas do menu está destacada em vermelho “Ligar objetos”. Fim da descrição.

Nos próximos passos, ligaremos os objetos e indicaremos seu grau de relacionamento e suas cardinalidades.

Passo 6 – Selecione o objeto “Ligar Objetos” e, com o objeto selecionado, clique com o botão esquerdo do mouse primeiro no objeto “Funcionário” e, depois, no objeto “possui”. Essa ação irá gerar uma “linha” interligando os dois objetos.

![[md2-06-fig11.webp]]

*Figura 8 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal, cuja ferramenta “ligar objetos” está destacada. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta a um losango “possui” e outro retângulo denominado “Dependente”. Fim da descrição.

Antes de configurar o grau e a cardinalidade do relacionamento. Faça a ligação entre os objetos Dependente e possui.

Passo 7 – Selecione o objeto “Ligar Objetos”, com o objeto selecionado, clique com o botão esquerdo do mouse primeiro no objeto “Dependente” e, depois, no objeto “possui”. Essa ação gerará uma “linha” interligando os dois objetos.

![[md2-06-fig12.webp]]

*Figura 9 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta a um losango “possui”, ligado por uma reta, destacada por uma quadrado laranja, a outro retângulo denominado “Dependente”. Fim da descrição.

O próximo passo será configurar o grau e cardinalidade do relacionamento entre as duas entidades.

Relembrando o cenário:

- Um funcionário deve possuir, no mínimo, zero dependente e, no máximo, muitos dependentes;

- Um dependente deve pertencer, no mínimo, a 1 funcionário e, no máximo, a 1 funcionário.

Devemos também lembrar que a representação das cardinalidades deve ser informada no lado oposto ao da entidade.

![[md2-06-fig13.webp]]

*Figura 10 – Representação das cardinalidades Fonte: Acervo do conteudista*

#ParaTodosVerem: representação das cardinalidades, onde se apresentam dois retângulos: Funcionário, com uma linha reta na cor vermelha sublinhando o nome e Dependente, com uma linha azul sublinhando o nome, entre eles um losango com a palavra “possui”. As formas estão conectadas por linhas retas na cor preta. Fim da descrição.

Passo 8 – Para configurar o grau e a cardinalidade da entidade FUNCIONARIO, selecione a cardinalidade ao lado da entidade DEPENDENTE, com a cardinalidade selecionada, altere a propriedade “Cardinalidade” para “0,n”.

![[md2-06-fig14.webp]]

*Figura 11 – Tela da ferramenta BrModelo Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical, onde se destacam em vermelho o elemento: Cardinalidade. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta a um losango “possui”, ligado por uma reta, destacada por um quadrado vermelho, evidenciando “(0,n), a outro retângulo denominado “Dependente”. Fim da descrição.

Passo 9 – Para configurar o grau e a cardinalidade da entidade DEPENDENTE, selecione a cardinalidade ao lado da entidade FUNCIONARIO, com a cardinalidade selecionada, altere a propriedade “Cardinalidade” para “1,1”.

![[md2-06-fig15.webp]]

*Figura 12 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta, destacada em vermelho, evidenciando “(0,n)”, a um losango “possui”, ligado por uma reta a outro retângulo denominado “Dependente”. Fim da descrição.

Podemos observar o resultado da implementação do cenário de exemplo no DER abaixo:

![[md2-06-fig16.webp]]

*Figura 13  – Representação das cardinalidades*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: representação das cardinalidades, onde se apresentam dois retângulos: Funcionário e Dependente, entre eles um losango com a palavra “possui”. As formas estão conectadas por linhas retas na cor preta, e cada uma delas possui, respectivamente, (1,1) e (0,n), abaixo, organizados horizontalmente, três retângulos verdes: Funcionário (1,1), Possui (0,n), Dependente. Fim da descrição.

###### Onde:

- Um funcionário possui no mínimo zero e no máximo vários dependentes e;

- Um dependente está ligado, no mínimo, a um e, no máximo, a um funcionário.

Antes de criarmos o modelo lógico, devemos adicionar atributos às entidades. Para adicionar atributos, basta clicar no objeto “Atributo”, selecionar o atributo desejado e, em seguida, clicar no objeto no qual queremos adicioná-lo. Em nosso exemplo, utilizaremos os atributos do tipo “Atributo” e “Atributo Identificador”.

![[md2-06-fig17.webp]]

*Figura 14 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal, onde se destacam, em vermelho, os elementos “Atributo” - “Atributo identificador”. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta “(1,1)”, a um losango “possui”, ligado por uma reta (0,n), a outro retângulo denominado “Dependente”. Fim da descrição.

Passo 10 – Clique no objeto “Atributo”, selecione o objeto “Atributo” e, em seguida, clique na entidade FUNCIONARIO. Com o objeto “Atributo” selecionado, altere a propriedade nome para: Nome e pressione “Enter” no teclado.

![[md2-06-fig18.webp]]

*Figura 15 – Tela da ferramenta BrModelo Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical, no qual destaca o elemento “edição: atributo” - “nome”. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta “(1,1)”, a um losango “possui”, ligado por uma reta (0,n),  a outro retângulo denominado “Dependente”. Do retângulo “Funcionário”, parte uma linha que o relaciona com um pequeno círculo acompanhado pela palavra “atributo”. Fim da descrição.

Passo 11 – Clique no objeto “Atributo”, selecione o objeto “Atributo Identificado” e, em seguida, clique na entidade FUNCIONARIO. Com o objeto “Atributo” selecionado, altere a propriedade nome para: Id_Funcionario e pressione “Enter” no teclado.

![[md2-06-fig19.webp]]

*Figura 16 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical, em que se destaca o elemento “edição: atributo” - “nome”. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta “(1,1)”, a um losango “possui”, ligado por uma reta (0,n),  a outro retângulo denominado “Dependente”. Do retângulo “Funcionário”, parte uma linha que o relaciona com um pequeno círculo acompanhado pela palavra “id_Funcionario”, e uma outra linha para “nome”. Fim da descrição.

Passo 12 – Adicione dois atributos à entidade DEPENDENTE, um atributo (não-Identificador) com o nome: Nome_Dependente e um atributo Identificador com o nome: Id_Dependente.

O resultado esperado é o DER exibido abaixo:

![[md2-06-fig20.webp]]

*Figura 17 – DER*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: representação das cardinalidades, onde se apresentam dois retângulos: Funcionário (1,1) e Dependente (0,n), entre eles um losango com a palavra “possui”. As formas estão conectadas por linhas retas na cor preta, abaixo, uma tabela verde e branca: Primeira coluna: Funcionário - id_funcionário campo chave, nome; Segunda coluna: (1,1); Terceira coluna: possui; Quarta coluna: (0,n); Quinta coluna: Dependente - id_dependente campo chave, nome_dependente. Fim da descrição.

### Gerando o esquema Lógico a partir do DER

Para gerar o esquema lógico (modelo lógico) a partir de um DER no BrModelo, basta clicar com o botão direito do mouse sobre um local vazio no palco. Em seguida, clique na opção “Gerar esquema lógico”.

![[md2-06-fig21.webp]]

*Figura 18 – Tela da ferramenta BrModelo*

###### Fonte: Acervo do conteudista

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, um retângulo denominado “Funcionário”, ligado por uma reta “(1,1)”, a um losango “possui”, ligado por uma reta (0,n), a outro retângulo denominado “Dependente”. Do retângulo “Funcionário”, parte uma linha que o relaciona com um pequeno círculo acompanhado pela palavra “id_Funcionario”, e uma outra linha para “nome”. Nessa janela, um menu cujo destaque é “Gerar Esquema Lógico”. Fim da descrição.

Essa ação gerará um esquema lógico que podemos observar na imagem abaixo:

![[md2-06-fig22.webp]]

*Figura 19 – Tela da ferramenta BrModelo*

###### Fonte: Acervo do conteudista

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, duas tabelas conectadas por uma linha preta. Tabela à esquerda: uma coluna e três linhas - Funcionário, Nome: VARCHAR (10), Id_Funcionario: VARCHAR (10); coluna da direita: uma coluna e três linhas - Dependente, Nome_Dependente: VARCHAR, Id_dependente: VARCHAR(10), Id_Funcionário: VARCHAR(10). Fim da descrição.

![[md2-06-fig23.webp]]

*Figura 20 – DER*

#ParaTodosVerem: duas tabelas conectadas por uma linha preta. Tabela à esquerda: uma coluna e três linhas - Funcionário, Nome: VARCHAR (10), Id_Funcionario: VARCHAR (10); coluna da direita: uma coluna e três linhas - Dependente, Nome_Dependente: VARCHAR, Id_dependente: VARCHAR(10), Id_Funcionário: VARCHAR(10). Abaixo uma tabela verde e branca: Primeira coluna: Funcionário - nome: Varchar(65), id_funcionário: Varchar(10) campo chave; Segunda coluna: (1,1); Terceira coluna: possui; Quarta coluna: (0,n); Quinta coluna: Dependente - Nome_dependente: Varchar(65), Id_Dependente: Varchar(10) campo chave, Id_Funcionário: Varchar(10) campo chave estrangeira. Fim da descrição.

Percebam que, ao criar o modelo lógico, o _software_ BrModelo gerou automaticamente a chave estrangeira “Id_Funcionario” na entidade DEPENDENTE, bem como toda a estrutura de dados do modelo físico (nomes das tabelas, nome de campos e tipo de dados).

É, nessa etapa, que no BrModelo, temos a possibilidade de alterar o tipo de dado para determinado Banco de dados.

##### Importante

Caso queira gerar um script para banco de dados Oracle, deve-se alterar os tipos de dados especificamente para Oracle e, assim, por diante.

Para nosso estudo, iremos gerar o script SQL com os tipos de dados da configuração padrão do BrModelo. Esse padrão gera scripts com a sintaxe do banco de dados SQLite.

##### Site

SQLite é o SGBD de código aberto e o mais utilizado nos ambientes mobile.

### Gerando o script SQL

Para gerar o script SQL referente ao DER e o modelo lógico que criamos, até agora, no BrModelo, basta clicar com o botão direito do mouse sobre um local vazio no palco. Em seguida, clique na opção “Gerar esquema Físico”.

![[md2-06-fig26.webp]]

*Figura 21 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na parte superior há um menu horizontal. No canto direito há um menu vertical. E, na parte à esquerda, uma janela onde se apresentam os elementos selecionados no menu, duas tabelas conectadas por uma linha preta. Tabela à esquerda: uma coluna e três linhas - Funcionário, Nome: VARCHAR (10), Id_Funcionario: VARCHAR (10); coluna da direita: uma coluna e três linhas - Dependente, Nome_Dependente: VARCHAR, Id_dependente: VARCHAR(10), Id_Funcionário: VARCHAR(10). Um menu se sobrepõe às tabelas com a opção em destaque vermelho “Gerar Esquema Físico”. Fim da descrição.

Na tela a seguir, clique no botão “Gerar Modelo Físico”.

![[md2-06-fig27.webp]]

*Figura 22 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela do BrModelo, na qual destacam-se as caixas de seleção “Gerar modelo físico”, com traço vermelho ao redor,  e “cancelar”. Fim da descrição.

Essa ação gerará um script SQL, o qual poderá ser salvo em um arquivo do formato

.sql.

```sql
-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.

CREATE TABLE Funcionario (
Nome VARCHAR(10),
Id_Funcionario VARCHAR(10) PRIMARY KEY
)

CREATE TABLE Dependente (
Nome_Dependente VARCHAR(10),
Id_Dependente VARCHAR(10) PRIMARY KEY,
Id_Funcionario VARCHAR(10),
FOREIGN KEY(Id_Funcionario) REFERENCES Funcionario (Id_Funcionario)
)
```

*Figura 23 – Tela da ferramenta BrModelo*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal da ferramenta BrModelo. Na aba Modelo Físico, uma janela branca contendo caracteres verde, azul e preto, demonstrando os códigos inseridos. Parte da janela está demarcada com um retângulo vermelho, abaixo dois botões de comando “salvar” e “fechar”. Fim da descrição.

```sql
CREATE TABLE Funcionario(
```

Nome VARCHAR (65),

Id_Funcionario VARCHAR(10) PRIMARY KEY)

CREATE TABLE Dependente (Nome_Dependente VARCHAR(65),Id_ Dependente VARCHAR(10) PRIMARY KEY,Id_Funcionario VARCHAR(10),

FOREIGN KEY( Id_Funcionario) REFERENCES Funcionario (Id_ Funcionario)

##### Site

Podemos testar o _script_ gerado na plataforma SQLFiddle

```sql
CREATE TABLE Funcionario (
Nome VARCHAR(10),
Id_Funcionario VARCHAR(10) PRIMARY KEY
)
;
CREATE TABLE Dependente (
Nome_Dependente VARCHAR(10),
Id_Dependente VARCHAR(10) PRIMARY KEY,
Id_Funcionario VARCHAR(10),
FOREIGN KEY(Id_Funcionario) REFERENCES Funcionario (Id_Funcionario)
)
```

*Figura 24 – Tela da ferramenta SQL Fiddle Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela, na qual há uma janela branca contendo caracteres roxo, azul e preto, demonstrando os códigos inseridos. Abaixo há quatro botões de comando na cor azul: “Build schema”, “edit fullscreen”, “browser”, “”[;]” . Fim da descrição.

```sql
CREATE TABLE Funcionario (Nome VARCHAR (65),Id_Funcionario VARCHAR(10)
PRIMARY KEY);
CREATE TABLE Dependente (Nome_Dependente VARCHAR(65),
```

Id_Dependente VARCHAR(10) PRIMARY KEY,Id_Funcionario VARCHAR(10),

FOREIGN KEY( Id_Funcionario) REFERENCES Funcionario (Id_ Funcionario)

##### Site

O teste do _script_ pode ser acessado no Qr _Code_ .

## MySQL Workbench

A ferramenta MySQL _Workbench_ é uma ferramenta CASE gratuita, a qual oferece as seguintes funcionalidades:

###### Desenvolvimento SQL

Funcionalidade para consultas MySQL. Permite que o usuário se conecte a um banco de dados existente, edite e execute consultas SQL.

###### Modelagem de Dados

Permite a modelagem visual de banco de dados (criação do modelo lógico e físico).

Administração de Banco de Dados

Funcionalidade de administrador do MySQL. Possui uma interface gráfica para iniciar / parar servidores, criar contas de usuário, editar arquivos de configuração etc.

##### Site

O MySQL _Workbench_ pode ser baixado pelo link a seguir. A ferramenta pode ser instalada nos sistemas operacionais Windows, Mac OS X, e nas principais distribuições Linux.

Disponível no QR _Code_ .

Você pode fazer o download da ferramenta utilizando uma conta Oracle ou apenas clicar em “ _No thanks, just start my download_ ”.

No contexto de nossa disciplina, focaremos no desenvolvimento do modelo lógico/ físico e, em seguida, geraremos um script SQL.

### Visão Geral da Ferramenta

Na tela principal da ferramenta, clique em “ _File/New Model_ ”.

![[md2-06-fig33.webp]]

*Figura 25 – Tela principal MySQL _Workbench_*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal, no qual os elementos “File” - “New model” estão em destaque laranja. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

Na tela a seguir, clique no botão “ _Add Diagram_ ”

![[md2-06-fig34.webp]]

*Figura 26 – Aba “Add Diagram” do MySQL _Workbench_ Fonte: Acervo do conteudista*

```
#ParaTodosVerem: printscreen da tela principal do MySQL Workbench. Na parte superior há um menu horizontal.
```

No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu, o elemento “add diagram” está em destaque vermelho. Fim da descrição.

Essa ação leva à tela principal para o desenvolvimento do modelo lógico.

![[md2-06-fig35.webp]]

*Figura 27 – Tela principal para o desenvolvimento lógico do MySQL _Workbench_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical, no qual estão em destaque amarelo os elementos: “Bird’s eye”, “Catalog Tree”, “Description Editor”. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

Em destaque, temos três áreas da ferramenta:

Área 1

É o palco do _software_ . É nesse espaço que é organizado os objetos do DER.

Área 2

Aqui, estão dispostos os principais objetos do DER (entidade, relacionamento, atributos), esses objetos adicionados ao palco do _software_ .

Área 3

Refere-se à visualização rápida dos diversos objetos e propriedades do modelo em desenvolvimento.

### Criando o Modelo Lógico

Nessa sessão, criaremos um DER levando em consideração o mesmo cenário utilizado anteriormente.

- Um funcionário deve possuir, no mínimo, zero dependente e, no máximo, muitos dependentes;

- Um dependente deve pertencer, no mínimo, a 1 funcionário e, no máximo, 1 funcionário.

Nesse contexto, iremos criar o modelo lógico nos passos a seguir.

Passo 1 – Clique no objeto “ _New Table_ ” e, em seguida, clique em uma área vazia do palco. Essa ação irá adicionar um objeto “ _Table_ ”.

![[md2-06-fig36.webp]]

*Figura 28 – Tela “New Table” do MySQL _Workbench_*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical, no qual se destaca em vermelho a ferramenta “Place a New Table (Quick Key –press T)”. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

![[md2-06-fig37.webp]]

*Figura 29 – Tela “New Table” do MySQL _Workbench_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu, um retângulo com as bordas arredondadas denominada “table1”. Fim da descrição.

Passo 2 – Clique com o botão esquerdo do mouse duas vezes no objeto “ _Table1_ ”. Essa ação irá habilitar uma tela de propriedades, nessa tela, altere o nome da propriedade “ _Table Name_ ” para: Funcionario.

![[md2-06-fig38.webp]]

*Figura 30 –  Tela “Table Name” do MySQL _Workbench_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu, onde se abre uma caixa de ferramentas, cujo destaque indica “table name” - “Funcionário”. Fim da descrição.

Passo 3 – Adicionando um atributo. Na tela de propriedades, logo abaixo da propriedade “ _Table Name_ ”, clique duas vezes com o botão esquerdo do mouse na célula abaixo da coluna “ _Column Name_ ”. Em seguida, altere o nome do atributo para: id_Funcionario.

![[md2-06-fig39.webp]]

*Figura 31 – Tela “Column Name” do MySQL _Workbench_*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu, onde se abre uma caixa de ferramentas, cujo destaque indica “Column name” - “id_Funcionário”. Fim da descrição.

Para cada atributo criado na tabela, existem diversas propriedades, como podemos verificar na imagem abaixo.

![[md2-06-fig40.webp]]

*Figura 32 – Nesta imagem estamos selecionando PK e NN*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Na parte inferior há um menu com caixas de itens a serem selecionados: PK e NN. Fim da descrição.

Cada propriedade, quando selecionada, atribui uma funcionalidade ao atributo. Essas propriedades são:

PK Chave primária (o atributo é uma chave primária);

NN Não nulo (o atributo não pode ficar vazio); UQ Único (o valor do atributo deve ser único em toda a tabela); BIN Binário (o atributo só aceita valores binários); UN _Unsigned_ (não permite valores negativos no atributo);

_Unsigned_ (não permite valores negativos no atributo);

_Zero fill_ (preenche os espaços vazios com zero à esquerda até o ZF tamanho padrão do campo);

Autoincremento (o valor do atributo é gerado automaticamente AI pelo SGBD).

Para concluir, a configuração do atributo “id_Funcionario”, selecione as opções “PK” e “NN”.

Passo 4 – Adicione o atributo “Nome”. Clique duas vezes com o botão esquerdo do mouse na célula abaixo do atributo “id_Funcionario”. Em seguida, altere o nome do atributo para: nome.

![[md2-06-fig41.webp]]

*Figura 33 – Tela de seleção PK e NN*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Na parte inferior há um menu com caixas de itens destacados em vermelho a serem selecionados: “Nome” - “VARCHAR(45)”. Fim da descrição.

O tipo de dado do campo (coluna _Datatype_ ) por padrão é VARCHAR(45), para o nosso exemplo não é preciso alterar. Mas, vale salientar, que é nessa propriedade que se pode alterar o tipo e o tamanho do atributo.

Passo 5 – Adicione a tabela Dependente. Para isso, clique no objeto “ _New Table_ ” e, em seguida, clique em uma área vazia do palco. Essa ação adicionará um objeto “ _Table_ ”.

Em seguida, clique com o botão esquerdo do mouse duas vezes no objeto “ _Table1_ ”. Essa ação habilitará uma tela de propriedades. Nessa tela, altere o nome da propriedade “ _Table Name_ ” para: Dependente.

![[md2-06-fig42.webp]]

*Figura 34 – Tela de alteração do “ _Table name_ ”*

###### Fonte: Acervo do conteudista

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela na qual se apresentam os elementos selecionados no menu. Na parte inferior há um menu com caixas de itens, destacados em vermelho, a serem selecionadas: “table name” - “dependente” . Fim da descrição.

Passo 6 – Adicione o atributo chave. Na tela de propriedades, logo abaixo da propriedade “ _Table Name_ ”. Clique duas vezes com o botão esquerdo do mouse na célula abaixo da coluna “ _Column Name_ ”. Em seguida, altere o nome do atributo para: id_Dependente e selecione as opções “PK” e “NN”.

![[md2-06-fig43.webp]]

*Figura 35 – Tela de alteração do “ _Column name_ ”*

###### Fonte: Acervo do conteudista

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Na parte inferior há um menu com caixas de itens a serem selecionadas: “Column name - id_dependente”, “Datatype - INT”, PK, NN. Fim da descrição.

Passo 7 – Adicione o atributo Nome_Dependente. Clique duas vezes com o botão esquerdo do mouse na célula abaixo do atributo “id_Funcionario”. Em seguida, altere o nome do atributo para: Nome_Dependente.

![[md2-06-fig44.webp]]

*Figura 36 – Nome_Dependente deverá ser VARCHAR (45)*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal. No canto esquerdo há um menu vertical. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Na parte inferior há um menu com caixas de itens, destacados em vermelho, a serem selecionados: “Column name - Nome_Dependente - VARCHHAR (45)”. Fim da descrição.

Passo 8 – Adicionando o grau de relacionamento. A ferramenta dispõe de seis (6) possibilidades para configuração do grau de relacionamento entre tabelas, como destacado na imagem abaixo.

![[md2-06-fig45.webp]]

*Figura 37 – Tela da barra de ferramentas*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ do MySQL _Workbench_ . No canto esquerdo há um menu vertical, na parte à direita, um zoom destacando na cor vermelha as ferramentas para configuração do grau de relacionamento entre tabelas. Fim da descrição.

Na sequência (de cima para baixo), esses relacionamentos significam:

- Relacionamento um-para-um (1:1) sem adicionar atributo chave-composto na entidade fraca;

- Relacionamento um-para-muitos (1:n) sem adicionar atributo chave-composto na entidade fraca;

- Relacionamento um-para-um (1:1) adicionando atributo chave-composto na entidade fraca;

- Relacionamento um-para-muitos (1:n) adicionando atributo chave-composto na entidade fraca;

- Relacionamento muito-para-muitos (n:m).

É importante ressaltar que a notação gráfica utilizada pela ferramenta é a notação Engenharia de Informações ou notação James Martin (Machado, 2014).

Recordando o cenário de nosso exemplo, temos um grau de relacionamento (1:n), no qual um funcionário pode possuir diversos dependentes, mas um dependente deve estar vinculado a somente um funcionário.

Nesse contexto, selecione a relação _one to many identifying relationship_ (Relacionamento um-para-muitos).

![[md2-06-fig46.webp]]

*Figura 38 – Tela da barra de ferramentas*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ do MySQL _Workbench_ . No canto esquerdo há um menu vertical. Na parte à direita, um zoom destacando na cor vermelha as ferramentas para configuração do grau de relacionamento entre tabelas. Fim da descrição.

Com a ferramenta selecionada, clique primeiro na entidade fraca, nesse caso, clique na tabela DEPENDENTE. Em seguida, por último, clique na tabela FUNCIONARIO.

O resultado dessa ação pode ser observado na imagem abaixo.

![[md2-06-fig47.webp]]

*Figura 39 – Tela da barra de ferramentas*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ do MySQL _Workbench_ . No canto esquerdo há um menu vertical. Na parte à direita, dois retângulos onde se organizam as informações, à esquerda: Funcionario - id_Funcionario INT, Nome VARCHAR(45) - Indexes; à direita: Dependentes - id_Dependente INT - Nome_Dependente VARCHAR (45) - Funcionario_id_Funcionario INT - Indexes. Os retângulos estão conectados por uma linha preta. Fim da descrição.

![[md2-06-fig48.webp]]

*Figura 40 – Tabela*

###### Fonte: Acervo do conteudista

#ParaTodosVerem: tabela verde e branca, composta por 4 colunas, nas quais se apresentam os seguintes elementos: Primeira coluna: Funcionário - Id_Funcionario INT chave primária, Nome VARCHAR (45); Segunda coluna: (1,0); Terceira coluna: (1,n); Quarta coluna: Dependente - Id_Dependente INTchave primária, Nome_Dependente VARCHAR (45), Funcionário_id_Funcionário INT chave estrangeira. Fim da descrição.

Percebam que, ao configurar o relacionamento, o _software_ criou automaticamente a chave estrangeira “Funcionario_Id_Funcionario” na entidade DEPENDENTE.

### Gerando o script SQL

Para gerar o script SQL referente ao modelo lógico que criamos, clique no “ _File\ Export\ Forward Enginner SQL CREATE Script ...”_ .

![[md2-06-fig49.webp]]

*Figura 41 – Tela “ _File\ Export\ Forward Enginner SQL CREATE Script …”_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . Na parte superior há um menu horizontal, cuja aba “File” está aberta. No canto esquerdo há um menu vertical, no qual se destaca em vermelho a opção “Export - Forward Engineer SQL Create Script”. E, na parte à direita, uma janela onde se apresentam os elementos selecionados no menu. Fim da descrição.

Na tela seguinte, marque as opções: _Omit Schema Qualifier in Object Names; Do Not Create Users, Only Export Privileges e Don’t create view placeholder tables_ . Avance, clicando no botão “Next”.

![[md2-06-fig50.webp]]

*Figura 42 – Tela SQL _Export Options_*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . No canto esquerdo há um menu vertical verde e azul. Na parte à direita, uma janela na qual apresentam os elementos selecionados no menu e um menu com caixas de itens a serem selecionados, com destaque em vermelho para os elementos: “omit schema qualifier in objects names”, “do not create users. Only export privileges”, “don’t create view placeholder tables”. Fim da descrição.

Na tela seguinte, marque a opção “ _Export MySQL Table Objects_ ” e avance clicando no botão “ _Next_ ”.

![[md2-06-fig51.webp]]

*Figura 43  – Tela SQL _Export Options_*

*Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . No canto esquerdo há um menu vertical verde e azul. Na parte à direita, uma janela na qual se apresentam os elementos a serem selecionados, com destaque em vermelho para: “export MySQL table objects (2 total objects, 2 selected”. Fim da descrição.

Por fim, é gerado um script SQL na sintaxe MySQL para criação das tabelas referente ao modelo lógico criado pela ferramenta. O script gerado poderá ser salvo em um arquivo do formato .sql.

```sql
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Funcionario` (
  `id_Funcionario` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Funcionario`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Dependente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dependente` (
  `id_Dependente` INT NOT NULL,
  `Nome_Dependente` VARCHAR(45) NULL,
  `Funcionario_id_Funcionario` INT NOT NULL,
  PRIMARY KEY (`id_Dependente`, `Funcionario_id_Funcionario`),
  INDEX `fk_Dependente_Funcionario_idx` (`Funcionario_id_Funcionario` ASC),
  CONSTRAINT `fk_Dependente_Funcionario`
    FOREIGN KEY (`Funcionario_id_Funcionario`)
    REFERENCES `Funcionario` (`id_Funcionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
```

*Figura 44 – Tela SQL _Export Options_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela principal do MySQL _Workbench_ . No canto esquerdo há um menu vertical verde e azul. Na parte à direita, uma janela onde se apresentam os elementos selecionados no menu, destaca-se em vermelho os códigos para “CREATE TABLE IF NOT EXISTS”, funcionario, id_funcionario, INT NOT NULL, nome VARCHAR (45) NULL, PRIMARY KEY (id_funcionario), ENGINE=InnoDB. Abaixo desse código, há outro que corresponde à Dependente: CREATE TABLE IF NOT EXISTS, dependentre, id_dependente, INT NOT NULL, nome_dependente VARCHAR (45) NULL, Funcionario_id_funcionario, INT NOT NULL, PRIMARY KEY (id_dependente, funcionario_id_funcionario), INDEX fk_dependente_funcionario_idx (funcionario_id_funcionario ASC), CONSTRAINT fk_dependente_funcionario, FOREIGN KEY (funcionario_id_funcionario), REFERENCES funcionário (id_funcionario), ON DELETE NO ACTION, ON UPDATE NO ACTION, ENGINE = InnoDB. Fim da descrição.

##### Site

Podemos testar o script gerado na plataforma SQLFiddle.

```sql
CREATE TABLE IF NOT EXISTS `Funcionario` (
  `id_Funcionario` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Funcionario`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Dependente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dependente` (
  `id_Dependente` INT NOT NULL,
  `Nome_Dependente` VARCHAR(45) NULL,
  `Funcionario_id_Funcionario` INT NOT NULL,
  PRIMARY KEY (`id_Dependente`, `Funcionario_id_Funcionario`),
```

*Figura 45 – Tela SQL _Fiddle_ Fonte: Acervo do conteudista*

#ParaTodosVerem: _printscreen_ da tela SQL _Fiddle_ . Na parte superior há um menu horizontal, abaixo do menu uma janela branca preenchida por caracteres pretos e azuis, demonstrando os códigos inseridos: “CREATE TABLE IF NOT EXISTS”, funcionario, id_funcionario, INT NOT NULL, nome VARCHAR (45) NULL, PRIMARY KEY (id_funcionario), ENGINE=InnoDB. Abaixo desse código, há outro que corresponde à Dependente: CREATE TABLE IF NOT EXISTS, dependentre, id_dependente, INT NOT NULL, nome_dependente VARCHAR (45) NULL, Funcionario_id_funcionario, INT NOT NULL, PRIMARY KEY (id_dependente, funcionario_id_funcionario). Na parte inferior, quatro caixas de menu na cor azul: “build schema”, “edit fullscreen”, “browser”, “[;]”. Fim da descrição.

##### Site

O teste do script pode ser acessado no QR _Code_ .

## Em Síntese

Compreender a organização de um banco de dados relacional é fundamental para entender as estruturas de dados utilizadas e suas inter-relações. Os conceitos aplicados nos sistemas gerenciadores de banco de dados do tipo relacional são essenciais para a construção e manutenção desses sistemas. A modelagem de dados, por sua vez, é facilitada por ferramentas CASE como o BrModelo e o MySQL _Workbench_ , as quais oferecem recursos e funcionalidades para desenvolver projetos de banco de dados de forma eficiente.

Por meio do entendimento das estruturas de dados empregadas em um banco de dados relacional e da aplicação dos conceitos específicos desses sistemas, é possível criar e gerenciar bases de dados de maneira mais eficaz. As ferramentas CASE, como o BrModelo e o MySQL _Workbench_ , atuam como suporte no processo de modelagem, oferecendo funcionalidades que auxiliam na criação, visualização e implementação de modelos de dados, tornando o desenvolvimento mais preciso e ágil.

Assim, a compreensão profunda desses tópicos proporciona uma base sólida para a construção e manutenção de bancos de dados relacionais. Isso promove uma modelagem de dados mais robusta e eficiente ao utilizar ferramentas especializadas, como o BrModelo e o MySQL _Workbench_ , para o desenvolvimento e gerenciamento desses projetos.
