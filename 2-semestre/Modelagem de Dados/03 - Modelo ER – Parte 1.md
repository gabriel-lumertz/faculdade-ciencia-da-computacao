---
materia: "Modelagem de Dados"
modulo: "Modelo ER – Parte 1"
semestre: 2
unidade: 3
tipo: material-teorico
fonte: "raw/2-semestre/MODELAGEM DE DADOS/Modelagem de Dados 03.pdf"
tags: [faculdade, modelagem-de-dados, semestre-2]
aliases: ["Modelagem de Dados - Unidade 3"]
---

# Modelo ER – Parte 1

## Objetivos da Unidade

- Mapear os seguintes conceitos: entidades, atributos simples, atributos complexos, atributos chaves a atributos multivalorados;

- Transformar do Modelo Entidade Relacionamento (ER) para o Modelo Relacional (MR);

- Estudar o Modelo de Entidade Relacional, o modelo de dados mais utilizado no mercado. Nessa primeira parte veremos os conceitos de entidades, entidades fortes e fracas.

###### VOCÊ SABE RESPONDER?

Para darmos início à unidade, contudo, convidamos você a refletir acerca da questão: você sabe o que é Modelo ER?

## Introdução ao Modelo-ER

O Modelo entidade-relacionamento (Modelo-ER) é a técnica mais difundida e utilizada para modelagem de dados (Heuser, 2010). O modelo ER foi proposto pela primeira vez por Peter Pin-Shan Chen, do Instituto de Tecnologia de Massachusetts (MIT), na década de 1970, e descreve o modelo conceitual de um banco de dados, apoiando-se principalmente na representação de entidades do mundo real e as associações entre elas.

##### Importante

Segundo Heuser (2010) podemos definir entidade como um “conjunto de objetos da realidade modelada sobre os quais se deseja manter informações no banco de dados”.

Como é mais fácil analisar as estruturas graficamente do que descrevê-las em um texto, os projetistas de bancos de dados preferem usar uma ferramenta gráfica na qual as entidades e seus relacionamentos são retratados. Assim, o Modelo-ER, tornou-se um padrão amplamente aceito para modelagem de dados.

No modelo ER, a estrutura de um banco de dados é retratada como um diagrama, chamado de diagrama de entidade-relacionamento (DER).

Embora sejam capazes de descrever qualquer sistema, os diagramas de entidade-relacionamento são mais frequentemente associados a bancos de dados. Em particular, os diagramas de entidade-relacionamento são comumente utilizados durante a fase de concepção de um processo de desenvolvimento, a fim de identificar diferentes elementos do sistema e as suas relações uns com os outros.

Os principais elementos em um DER são:

###### Entidade

Uma classe de objetos do mundo real com características e propriedades comuns sobre as quais desejamos registrar informações.

###### Relacionamento

Uma associação entre duas ou mais entidades.

###### Atributo

Uma característica de uma entidade ou relacionamento.

No DER, as entidades são representadas por retângulos, os relacionamentos são representados por losangos e atributos por círculos.

![[md2-03-fig02.webp]]

**Figura 1 –** Os principais elementos em um DER

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** esquema em que se apresenta os símbolos que identificam as Entidades por retângulos, os Relacionamentos por Losangos e cada um dos Atributos por círculos pequenos. São três atributos que se relacionam com Entidade, abaixo de Relacionamento e quatro atributos que se relacionam com Entidade ao lado de Relacionamento.  Fim da descrição.

O DER promove aos analistas um auxílio inestimável no que diz respeito à concepção, otimização e o desenvolvimento de um projeto de Banco de dados.

Entre as vantagens do modelo-ER, podemos destacar:

- Excepcional simplicidade conceitual;

- Representação visual;

- Ferramenta de comunicação eficaz;

- Integrado com o modelo de banco de dados relacional.

Em contrapartida, podemos destacar as seguintes desvantagens:

- Representação limitada de restrições;

- Representação limitada de relacionamento.

Diagramas de entidade-relacionamento (DER) constituem um quadro muito útil para a criação e manipulação de bases de dados. Primeiramente, esses diagramas são fáceis de compreender e não requer treinamento extensivo para poder trabalhar com ele eficientemente. Isso significa que os projetistas podem usar diagramas de entidade-relacionamento para se comunicar facilmente com desenvolvedores, clientes e usuários finais, independentemente de sua proficiência em TI. Em segundo lugar, os diagramas de entidade-relacionamento são prontamente traduzíveis em tabelas relacionais que podem ser usadas para construir bases de dados rapidamente. Além disso, podem ser usados diretamente pelos desenvolvedores de banco de dados como o modelo para a implementação de dados em aplicativos de software específicos.

Por fim, os diagramas de entidade-relacionamento podem ser aplicados em outros contextos, como descrever as diferentes relações e operações dentro de uma organização.

##### Site

Softwares livres para modelagem ER.

_Site_ 1 _Site_ 2

## Entidades, Entidades Fortes e Fracas

Uma Entidade é um objeto de interesse para o usuário final e refere-se realmente ao conjunto de entidades e não a uma única entidade. Em outras palavras, a entidade no MER corresponde a uma tabela.

Uma entidade pode ser uma pessoa, lugar, evento, objeto ou um conceito que é relevante para um determinado sistema para o qual estamos modelando o projeto de banco de dados. Por exemplo:

**Pessoa**

Estudante, Empregado, Cliente.

**Lugar**

Cidade, Sala, Armazém.

**Evento**

Festa, Casamento, Exposição, Feira.

**Objeto**

Carro, Navio, Máquina, Produto.

###### Conceito

Projeto, Conta, Curso.

Essas entidades são representadas no DER por um retângulo e nomeadas, usando substantivos singulares. Por exemplo, em um sistema escolar podemos ter as seguintes entidades:

![[md2-03-fig04.webp]]

**Figura 2 –** Entidades representadas no DER

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** ilustração em que há a representação de entidades. Cada uma delas com um retângulo de traço rosa e seu nome dentro. Da esquerda para a direita temos: Aluno, Professor, Curso, Turma e Histórico. Fim da descrição.

É importante entender a distinção entre **entidade** , uma **instância de entidade** e um **conjunto de entidades** . Uma entidade define uma coleção de entidades que possuem os mesmos atributos. Uma instância de entidade é um único item nesta coleção. Um conjunto de entidades é um conjunto de instâncias de entidade.

Por exemplo: ALUNO é um tipo de entidade; um aluno com o número de RGM “151623” é uma instância de entidade; uma coleção de todos os alunos é um conjunto de entidades.

Existem três tipos de entidades: Fortes; Fracas e Associativas.

### Entidade Forte

Se uma entidade pode existir separadamente de todas as suas entidades relacionadas, então essa entidade é classificada como uma Entidade Forte. Como destaca Barbiere (1994), “além de independência de existência, normalmente possuem independência de identificação dada por um ou mais atributos próprios”.

##### Importante

Segundo Barbiere (1994), as entidades fortes comumente são as primeiras a serem identificadas no processo inicial de análise do projeto de modelagem de dados.

Por exemplo, a entidade EMPREGADO é uma entidade forte, pois não depende de outra entidade para que exista uma instância.

**Tabela 1 –** Entidade Empregado

**Empregado** Id_empregado atributo chave nome_empregado

**Fonte:** Acervo do conteudista

**#ParaTodosVerem:** representação da entidade empregado dentro de um retângulo e os atributos id_Empregado e nomeEmpregado. Fim da descrição.

### Entidade Fraca

Uma entidade fraca é uma entidade que depende da existência de outra entidade. Em termos mais técnicos, ela pode ser definida como uma entidade que não pode ser identificada por seus próprios atributos. Uma entidade fraca é aquela que atende a duas condições:

- A entidade fraca é dependente da existência de uma instância da entidade com a qual tem um relacionamento;

- A entidade fraca tem uma chave primária que é parcial ou totalmente derivada da entidade-mãe no relacionamento.

Por exemplo, temos a seguinte regra de negócio:

- Todo dependente deve estar **vinculado** a um empregado.

Nossa regra de negócio diz que um DEPENDENTE só pode existir/ser cadastrado se ele estiver vinculado a um EMPREGADO, ou seja, não podemos cadastrar um DEPENDENTE sem indicar à qual EMPREGADO esse dependente está vinculado.

Vejamos o exemplo na Tabela 2, temos a entidade DEPENDENTE, podemos definir essa entidade como fraca, pois conforme nossa regra de negócio, para existir uma instância da entidade DEPENDENTE, deve-se existir primeiro uma instância de EMPREGADO.

**Tabela 2 Empregado (1,1) Possui (0,n) Dependente** Id_empregado atributo chave Id_dependente atributo chave nome_empregado Id_empregado atributo chave Nome_dependente

Vejamos o exemplo da Tabela 3 abaixo:

**Tabela 3 Pedido (0,n) Possui (1,1) Dependente** Id_Pedido atributo chave Id_Pedido atributo chave nome_Dependente Id_Produto ValorPedido Id_ItemPedido atributo chave

A entidade Itens_Pedido é uma entidade fraca, pois sua existência depende da existência de uma instância da entidade Pedido, ou seja, para termos Itens de pedidos devemos antes ter dados do Pedido.

### Entidade Associativa

Onde a entidade descreve uma conexão entre duas entidades com uma relação de muitos para muitos, por exemplo, atribuição de Empregado a Projeto (um Empregado pode ser atribuído a mais de um Projeto, e um Projeto pode ser atribuído a mais de um Empregado).

###### Tabela 4

**(1,n) Possui (1,n) Projeto**

###### Empregado

Id_Projeto atributo chave

Id_Empregado atributo chave

Se houver informações sobre o relacionamento, essas informações serão mantidas em uma entidade associativa, por exemplo, o número de horas em que o Empregado trabalhou em um Projeto específico é um atributo da relação entre Empregado e Projeto, não de Empregado ou de Projeto.

![[md2-03-fig06.webp]]

Uma entidade associativa é identificada unicamente por concatenação das chaves primárias das duas entidades que ele conecta.

##### Livro

PUGA, S.; FRANÇA, E.; GOYA, M. **Banco de Dados:** Implementação em SQL, PL SQL e Oracle 11g. 1.ed. São Paulo: Pearson Universidades, 2013.

## Em Síntese

Ao explorar os fundamentos da modelagem de dados, foi possível compreender os conceitos essenciais que regem a estrutura de um banco de dados. Inicialmente, foi feito o mapeamento detalhado de elementos vitais, como entidades, atributos simples, atributos complexos, atributos-chave e atributos multivalorados. A compreensão desses elementos proporciona uma base sólida para a construção e organização dos dados.

A transição do Modelo Entidade-Relacionamento (ER) para o Modelo Relacional (MR) foi outro ponto de destaque. Esse processo de conversão permitiu entender como representar os relacionamentos entre entidades por meio de tabelas no Modelo Relacional, traduzindo efetivamente a estrutura visual do ER em um formato prático e operacional.

Nesta etapa introdutória, nos concentramos no Modelo de Entidade Relacional, o qual é amplamente utilizado no mercado. Exploramos as nuances entre entidades fortes e fracas, compreendendo suas distinções e aplicabilidades no contexto da modelagem de dados.

Essa imersão inicial nos conceitos fundamentais e na transição entre modelos serviu como alicerce para a compreensão mais profunda da organização e estruturação dos dados, aspecto crucial para o desenvolvimento e gestão eficaz de bancos de dados no ambiente profissional.
