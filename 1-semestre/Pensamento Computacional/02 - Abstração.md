---
materia: "Pensamento Computacional"
modulo: "Abstração"
semestre: 1
unidade: 2
tipo: material-teorico
fonte: "raw/1-semestre/PENSAMENTO COMPUTACIONAL/Unidade II/Abstração.pdf"
tags: [faculdade, pensamento-computacional, semestre-1]
aliases: ["Pensamento Computacional - Unidade 2"]
---

# Abstração

## Tópicos da Unidade

- **Introdução;**

- **Promovendo Abstração na Prática: Jogo de Cartas Binário;**

- **Par ou Ímpar: Criando um Programa no** **_Scratch_.**

## Objetivos de Aprendizado

- Explorar e promover um dos conceitos mais importantes do Pensamento Computacional: **a abstração** , um conceito que ajuda a entender um problema e a planejar uma boa solução;

- Utilizar atividades desplugadas e também Programação de Computadores por meio do _Scratch_.

## Introdução

A abstração é sobre simplificar as coisas, permitindo-nos gerenciar a complexidade e tornar as coisas mais fáceis de fazer. A abstração nos permite criar uma ideia geral de qual é o problema e de como resolvê-lo.

O processo de abstração remove todos os detalhes específicos, e quaisquer padrões que não nos ajudem a resolver nosso problema. Isso nos ajuda a formar nossa ideia do problema que é conhecida como um “modelo”.

Pensamento Abstrato. Acesse: http://bit.ly/2XP1BuH

Se estivéssemos aprendendo/ensinando sobre os países do mundo, por exemplo, utilizaríamos um Mapa Mundial, ou seja, um modelo.

Um Mapa Mundial que mostra os países é uma abstração. É reduzido aos “países do mundo”. Uma outra abstração seria um Mapa com apenas 7 Continentes nomeados.

Mas se estivéssemos andando em São Paulo, um Mapa Mundial não teria detalhes suficientes para nos ajudar. Precisaríamos de um Mapa local que indicasse as ruas, os parques, os bairros etc. Nesse contexto, há muito mais detalhes, porque seria o necessário à situação.

![[pco1-02-fig01.webp]]

*Figura 1 – Mapa Mundi*

*Fonte: Wikimedia Commons*

Na Matemática, quando recorremos a letras e outros símbolos para representar números e quantidades, fórmulas e equações, estamos utilizando o poder da abstração.

Não é mais necessário depender de objetos do mundo real para resolver enigmas matemáticos; graças à abstração, pode-se generalizar procedimentos e aplicar a solução de um problema semelhante a diversas outras situações.

Em Computação, a maioria dos profissionais não precisará utilizar ou conhecer a fundo Álgebra e Estatística; porém a principal lição da Matemática é como abstrair a vasta complexidade do mundo.

Por exemplo, o tratamento de dados de diferentes representações numéricas como:

- Números inteiros;

- Números decimais;

- Números hexadecimais.

Qualquer dado (texto, imagens, vídeo etc.) pode ser expresso como uma lista gigante de números com uma combinação dos elementos acima.

Outro exemplo de abstração em Computação são os números binários. Nos computadores, os dados digitais, o armazenamento, o processamento e as comunicações são gravados e processados como números binários, numa sequência de 0 e 1.

Todos os dados que um computador processa precisam ser convertidos em binário. Os 0 e 1 em binário são usados para representar DESLIGADO ou LIGADO, respectivamente, ou seja, desligar ou ligar um sinal elétrico.

Números binários são importantes porque usá-los em vez do Sistema Decimal simplifica o _design_ de Computadores e Tecnologias relacionadas.

A definição mais simples do Sistema Numérico Binário é um Sistema de Numeração que usa apenas dois dígitos – 0 e 1 – para representar números, em vez de usar os dígitos 1 a 9 mais 0 para representar números.

O que são números binários? Acesse: http://bit.ly/2DyYAas

## Promovendo Abstração na Prática: Jogo de Cartas Binário

Iremos agora explorar uma atividade descrita no livro _Computer Science Unplugged_ , versão traduzida para Português<sup>1</sup> .

A atividade Contando os Pontos – Números Binários trabalha o conceito de abstração, utilizando e exigindo habilidades matemáticas de correlação, soma e ordenação.

> 1 Disponível em: https://classic.csunplugged.org/wp-content/uploads/2014/12/CSUnpluggedTeachers-portuguese-brazil-feb-2011.pdf.

Nessa atividade, o aluno irá converter números decimais em números binários utilizando cinco cartões impressos, cada um contendo uma quantidade específica de pontos.

Esses cartões são apresentados na Figura 2.

![[pco1-02-fig02.webp]]

*Figura 2 – Cartões da Atividade Contando os Pontos*

*Fonte: Adaptado de Bell; Witten e Fellows, 2015, p.11*

No cartão 2, da direita para esquerda, temos a primeira carta com apenas um ponto. Essa carta representa o número DECIMAL 1, a carta seguinte o número decimal 2, e assim por diante até chegarmos à última carta contendo 16 pontos representando o número decimal 16.

Veja a Figura 3.

![[pco1-02-fig03.webp]]

*Figura 3 – Cartas representando os números decimais*

*Fonte: Acervo do Conteudista*

As cartas contêm essas quantidades de pontos especificamente pois, na representação BINÁRIA, os números seguem uma sequência de aumento em potências de 2 (BASE 2).

Veja a Figura 4.

![[pco1-02-fig04.webp]]

*Figura 4 – Cartas representando as potências de 2*

*Fonte: Acervo do Conteudista*

Nessa configuração, podemos representar números binários de 5 posições (5 cartas), porém, em contrapartida, podemos representar, levando em consideração o número 0,32 números decimais.

Em nossa atividade, cada carta representa um _BIT_ e, como ocorre no computador, um _bit_ LIGADO representa o número 1 e o _bit_ DESLIGADO representa o número 0.

Iremos considerar as cartas “viradas para cima”, ou seja, exibindo os pontos, como um bit LIGADO. Cartas viradas para baixo, serão consideradas um _bit_ DESLIGADO.

Vejamos um exemplo na Figura 5.

![[pco1-02-fig05.webp]]

*Figura 5 – Sequência de cartas*

*Fonte: Acervo do Conteudista*

Seguindo a lógica de que cartas para cima representam o número 1 e cartas para baixo representam o número 0, temos a seguinte sequência de número BINÁRIO.

![[pco1-02-fig06.webp]]

*Figura 6*

*Fonte: Acervo do Conteudista*

A configuração de cartas representa o número binário: 01001. Para converter para número DECIMAL, basta somar a quantidade de pontos das cartas viradas. Desse modo, o número DECIMAL é 9 (8+1).

Vejamos o próximo exemplo de conversão de número binário para decimal.

Observe a configuração da Imagem 7.

![[pco1-02-fig07.webp]]

*Figura 7*

*Fonte: Acervo do Conteudista*

Para converter essa sequência em número decimal, devemos primeiro descrever o número 0 para cartas viradas para baixo e o número 1 para cartas viradas para cima.

Desse modo, temos:

![[pco1-02-fig08.webp]]

*Figura 8*

*Fonte: Acervo do Conteudista*

Agora, somamos a quantidade de pontos de cartas viradas para cima (carta com 16 pontos + carta com 2 pontos). Como resultado, a representação DECIMAL de 10010 é 18.

### Convertendo Números Decimais em Números Binários

Seguindo a mesma linha de raciocínio de cartas viradas para cima e de cartas viradas para baixo, podemos converter um número decimal para binário.

Para converter um número decimal para binário, devemos partir com todas as cartas viradas para cima.

No exemplo a seguir, iremos converter o número 28 decimal para sua representação em binário.

![[pco1-02-fig09.webp]]

*Figura 9*

*Fonte: Acervo do Conteudista*

Esse tipo de conversão consiste em distribuir o valor decimal entre as cartas viradas, partindo da esquerda para direita.

Deve-se distribuir o valor que “cabe” em cada carta e a cada distribuição, subtrair o valor total pelo número de pontos da carta e seguir adiante com a distribuição, até chegar a 0.

Para cada carta que conseguimos distribuir o valor, representamos com o número 1; as cartas não utilizadas, com o número 0. Nunca se deve distribuir um valor a uma carta maior que o valor que se deseja distribuir.

Nesse cenário, temos o seguinte resultado:

![[pco1-02-fig10.webp]]

*Figura 10*

*Fonte: Acervo do Conteudista*

Começando da direita para esquerda, distribuímos o primeiro valor (28) na primeira carta (16 pontos). Efetuando a subtração do valor total (28) pelo número de pontos da carta (16), temos como resultado 12. Continuando a sequência, distribuímos o valor 12 na próxima carta (8 pontos), efetuamos novamente a subtração (12-8) e temos agora o valor 4, distribuímos o valor 4 na carta seguinte (4 pontos).

Para essas três primeiras cartas, representamos o número “1”, pois as utilizamos para distribuir o valor decimal; o restante das cartas, como não utilizadas, representam o número 0.

#### Trocando ideias...

**Importante!**

Pode-se fazer o _download_ de imagens dos cartões da atividade: Contando os pontos diretamente do site _CS Unplugged_ . Para isso, acesse o _link_ : http://bit.ly/2W6PSHy.

## Par ou Ímpar: Criando um Programa no Scratch

Tomemos como exemplo a tarefa de identificar se um dado número é par ou ímpar.

Como identificar se um número, qualquer que seja seu tamanho, é par ou ímpar? Como apresentar essa regra a um computador?

Para responder e “ensinar” um computador a identificar se um número é par ou ímpar, podemos utilizar um tipo de abstração matemática chamada Aritmética Modular.

Para identificarmos se um número é par, basta dividi-lo por 2; se o resto da divisão resultar em 0, o número é par; caso contrário, o número é ímpar. Para fazer esse cálculo, podemos utilizar a expressão “A + mod 2”. Por exemplo, se quisermos verificar se o número 5 é par, faríamos: “5 mod 2”, essa expressão resulta em “1”, ou seja, não é par; logo, é ímpar.

Apresentada essa regra, iremos desenvolver um programa de computador utilizando o _Scratch_ .

Para acessar a plataforma _Scratch_ , abra seu navegador _web_ (em nossos exemplos, iremos utilizar o navegador _Google Chrome_ ) e acesse o seguinte _link_ : https://scratch.mit.edu/

A Figura 11 apresenta a tela inicial da plataforma _Scratch_ .

![[pco1-02-fig11.webp]]

*Figura 11 – Página Inicial*

Para traduzir a Plataforma para Língua Portuguesa, desça até o final da página e selecione a opção correspondente ao nosso idioma, conforme apresentado na Figura 12.

![[pco1-02-fig12.webp]]

*Figura 12 – Traduzindo a linguagem da plataforma*

No topo da página inicial, estão posicionados os menus: Criar, Explorar, Ideias, Sobre, Buscar e, por fim, Inscrever-se e Entrar.

Na Tabela a seguir, são descritas as funcionalidades de cada menu.

*Tabela 1 – Funcionalidades de cada Menu*

|**Menu**|**Descrição**|
|---|---|
|Criar|Por meio deste menu, a Plataforma é direcionada para<br>área de criação de Programas do_Scratch_.|
|Explorar|Este menu dá acesso à página com Projetos<br>compartilhadospor usuários da comunidade_Scratch_.|
|Ideias|Estapágina exibe uma série de tutoriais_Scratch_.|
|Sobre|Página sobre a Plataforma_Scratch_.|
|Buscar|Esse menupermite buscar Projetos compartilhados.|
|Inscrever-se|Por meio deste menu é possível criar um usuário de acesso<br>à Plataforma.|
|Entrar|Esse menupermite logar na Plataforma.|

*Fonte: Elaborado pelo autor a partir dos dados obtidos no site _Scratch_*

A Figura 13 destaca os menus superiores, bem como os Projetos compartilhados pela comunidade do _Scratch_ na parte inferior da página.

![[pco1-02-fig13.webp]]

*Figura 13 – Menus da página inicial*

Trocando ideias... **Importante!**

Para criarmos Programas no _Scratch_ , não é necessário logar na Plataforma, porém é muito interessante que você crie uma conta e faça o _login_ , pois dessa maneira todos os seus Projetos ficarão salvos e acessíveis e você também poderá compartilhá-los com outras pessoas.

Para criar Programas no _Scratch_ , basta clicar no menu Criar.

Ao clicar no menu Criar, acessamos a página de criação do _Scratch_ . Na primeira exibição dessa página, poderá ser exibido um tutorial. Para os nossos estudos, devemos fechar esse tutorial.

A Figura 14 destaca o tutorial.

![[pco1-02-fig14.webp]]

*Figura 14 – Tutorial da página de criação*

Antes de começarmos a criar nosso primeiro programa, iremos explorar a página de criação destacada na Figura 15.

![[pco1-02-fig15.webp]]

*Figura 15 – Página de criação*

Podemos observar as áreas identificadas a seguir.

### Área 1

Temos os Blocos de Comando do _Scratch_ ordenados em categorias. Cada categoria possui um conjunto de blocos de comando.

O _Scratch_ disponibiliza 8 categorias: Movimento, Aparência, Som, Eventos, Controle, Sensores, Operacionais e Variáveis.

A categoria Meus Blocos é utilizada quando o usuário cria seus próprios blocos. Ainda na Área 1 temos acesso às configurações de “Fantasias” que são as imagens que utilizamos para os nossos atores (área 3) no _Scratch_ e também configurações de sons que podem ser reproduzidos.

### Área 2

Os Blocos de Comando são arrastados para essa área. A lógica de programação e nosso algoritmo e, desse modo, os programas são criados nessa área.

### Área 3

Os atores (personagens), as saídas de nossos Programas, são exibidos nessa área. Vemos o resultado de nossa programação nessa área.

### Área 4

No _Scratch_ , o Código de Programação, ou seja, os Blocos de Comando, são vinculados ao ator ou ao palco (Plano de Fundo). Nessa área, é possível navegar entre os atores e/ou o palco para criar os Códigos de Programação além de dar acesso às configurações de tamanho e de posicionamento (eixos X e Y) do ator.

Em nosso programa, iremos criar um Código que, ao ser executado, irá solicitar um número, identificar se o número é par ou ímpar e, em seguida, exibir na tela a resposta, ou seja, se o número é par ou ímpar.

Primeiro, devemos configurar um evento que irá disparar a ação que iremos criar com os Códigos do _Scratch_ .

Desse modo, na Área de Blocos de Comando, localize a categoria “Eventos”, clique com o botão esquerdo do mouse sobre o comando e, sem soltar o botão do mouse, arraste para a área de Código, como podemos ver na Figura 16.

![[pco1-02-fig16.webp]]

*Figura 16 – Arrastando um bloco de eventos*

Em seguida, localize a categoria “Sensores” e arraste o bloco (“Pergunte e espere”) para a Área de Código, “encaixe” logo abaixo do Bloco de eventos e altere o texto do Bloco para “Digite um número”, conforme podemos ver na Figura 17.

![[pco1-02-fig17.webp]]

*Figura 17 – Arrastando um bloco pergunte*

Agora, localize a categoria “Controle”, arraste o Bloco representado abaixo (“se então”) para a área de Código e “encaixe” logo abaixo do Bloco “pergunte”, conforme podemos ver na Figura 18.

![[pco1-02-fig18.webp]]

![[pco1-02-fig19.webp]]

*Figura 18 – Arrastando um Bloco condicional*

Até o momento, nosso Programa já consegue solicitar um número, porém ainda não aplicamos a lógica matemática para identificar se um número é par ou ímpar.

Para isso, iremos utilizar um operador de igualdade e a função “resto de” que, no Scratch, calcula e retorna o resto da divisão de um número.

Comece arrastando e encaixando o comando para dentro do encaixe do bloco se então, conforme podemos ver na Figura 19.

![[pco1-02-fig20.webp]]

*Figura 19 – Arrastando um bloco de operador de igualdade*

Em seguida, ainda na categoria Operadores, localize e arraste o comando resto de por para dentro do primeiro encaixe do comando de operação de igualdade, conforme podemos ver na Figura 20.

![[pco1-02-fig21.webp]]

*Figura 20 – Arrastando um Bloco resto de por*

O passo seguinte será vincular o número digitado pelo usuário de nosso Programa à operação matemática. Para isso, na categoria Sensores, localize e arraste o comando resposta para o primeiro encaixe do comando resto de por, conforme podemos ver na Figura 21.

![[pco1-02-fig22.webp]]

*Figura 21 – Arrastando um Bloco resposta*

Retomando a regra para identificar se algum número é par ou ímpar, devemos verificar o resto da divisão por 2: se for igual a zero, esse número é par; caso contrário, o número é ímpar. Para isso, precisamos, agora, digitar o número 2 no espaço em branco do comando resto de por e alterar o número 50 do operador de igualdade por 2.

Podemos ver essa configuração na Figura 22.

*Figura 22 – Alterando valores de operadores*

Nosso programa já consegue identificar se um número digitado pelo usuário é par ou ímpar; porém nosso Programa ainda não exibe uma mensagem de acordo com a resposta. Para isso, na categoria Aparência, localize e arraste um comando diga para dentro da lacuna do comando se então.

Veja a Figura 23: altere o texto do comando dia para “O número é par”.

*Figura 23 – Arrastando um bloco diga*

Por fim, iremos criar a programação que irá exibir uma mensagem caso o número digitado seja um número ímpar. Para isso, arraste um comando diga para dentro da lacuna do comando se então.

Veja a Figura 24.

![[pco1-02-fig23.webp]]

*Figura 24 – Arrastando um bloco diga*

Concluímos nosso Programa, agora devemos testá-lo. Para isso, clique no local indicado na Figura 25.

![[pco1-02-fig24.webp]]

*Figura 25 – Testando o programa*

![[pco1-02-fig25.webp]]

*Figura 26 – Testando o programa*

#### Em Síntese Importante!

Nesta Unidade, exploramos o conceito de abstração utilizando atividades desplugadas e também criando um programa com o _Scratch_ .

Como sugestão, para aprofundamento na utilização do _Scratch_ , é relevante o estudo e o acesso aos tutoriais disponibilizados na Plataforma _Scratch_ . Para isso, acesse o _link_ :

http://bit.ly/2GEPhWZ.
