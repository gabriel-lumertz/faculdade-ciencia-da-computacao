---
materia: "Programação Web"
modulo: "Conceitos do HTML"
semestre: 2
unidade: 1
tipo: material-teorico
fonte: "raw/2-semestre/PROGRAMAÇÃO WEB/Programação Web 01.pdf"
tags: [faculdade, programacao-web, semestre-2]
aliases: ["Programação Web - Unidade 1"]
---

# Conceitos do HTML

### OBJETIVOS DA UNIDADE

- Entender que o HTML5 é uma linguagem para criação e publicação de documentos para _web_ ;

- Apresentar os vários recursos disponíveis com a nova versão do HTML;

- Compreender alguns itens que serão de extrema importância para iniciarmos a construção de um formulário.

## Introdução

Houve um grande avanço da versão do HTML 4.01 para o HTML5. Muitas validações e programações que teríamos que fazer utilizando uma linguagem de programação foi incorporado aos elementos HTML, nesta Unidade iremos verificar quais foram esses itens que utilizaremos e que vieram para facilitar nossas vidas.

## Ambiente Cliente/Servidor

Pensando nos elementos básicos para fornecer informação através da _Web_ , temos:

![[pw2-01-fig01.webp]]

**Figura 1 –** Ambiente cliente/servidor

**Fonte:** Adaptada de Freepik

**#ParaTodosVerem:** figura esquemática que apresenta o ambiente cliente/servidor. A figura é composta por três elementos, da direita para a esquerda temos, a figura de um computador que representa o cliente, no meio uma nuvem que representa a conexão e na direita temos servidores que representa o servidor _web_ com protocolo HTTP. Fim da descrição.

O que precisamos saber:

- **Cliente:**

   - HTML;

   - CSS;

   - _Javascript_ ;

   - XML.

- **Servidor:**

   - Banco de dados;
   
   - JSP;
   
   - ASP.NET.

## O que é HTML?

A _World Wide Web (Web)_ é uma rede de recursos e serviços de informação.

Ela serve-se de três mecanismos, de modo a fazer com que esses recursos estejam legivelmente disponíveis à audiência mais vasta possível:

- Um esquema uniforme de atribuição de nomes, de forma a se localizar os recursos na _Web_ (ex.: URIs);

- Protocolos, para o acesso aos recursos nomeados através da _Web_ (ex.: HTTP);

- Hipertexto, para uma navegação mais fácil através dos referidos recursos (ex.: HTML).

Os laços entre os três mecanismos evidenciam-se através desta especificação.

## Introdução aos URIs

Todos os recursos disponíveis na Web possuem um endereço, o qual poderá ser codificado por um Identificador de Recursos Universal, ou “ _URI_ ” ( _Universal Resource Identifier_ ).

Os URIs são de uma forma geral constituídos por três partes:

- O esquema de nomeação do mecanismo usado para se ter acesso ao recurso;

- O nome da máquina de hospedagem desse recurso;

- O nome do próprio recurso, atribuído na qualidade de trajeto ( _path_ ).

#### Exemplos de URIs

- **Página destinada a relatórios técnicos da W3C:** h t t p : / / w w w . w 3 . o r g / T R /

- **URI referente a caixa postal:** <a href=mailto:alexander_gobbato@ yahoo.com.br> Prof. Alexander Gobbato</a>

- **Identificadores de fragmentos:** h t t p : / / s o m e s i t e . c o m / h t m l / t o p . h t m l # s e c t i o n _ 2

No HTML, os URIs são usados para:

- Fazer uma ligação a um outro documento ou recurso, (ver os elementos A e LINK);

- Fazer uma ligação a uma folha de estilo ou _script_ (ver os elementos LINK e SCRIPT);

- Incluir uma imagem, objeto ou _applet_ numa página, (ver os elementos IMG, OBJECT, APPLET e INPUT);

- Criar um mapa de imagens (ver os elementos MAP e AREA);

- Submeter um formulário (ver FORM);

- Criar um documento com molduras (ver os elementos FRAME e IFRAME);

- Citar uma referência externa (ver os elementos Q, BLOCKQUOTE, INS e DEL);

- Fazer referências a convenções de metadados descrevendo um documento (ver o elemento HEAD).

## W3C

A _World Wide Web Consortium_ ( _W3C_ ) é o órgão responsável por recomendar padrões de desenvolvimento para a _internet_ . Por meio destes padrões se pode classificar _web sites_ de acordo com suas características técnicas, indo além do visual e navegadores, de acordo com sua capacidade em atender aos padrões definidos.

Para se publicar informação de distribuição global, é necessário utilizar-se uma linguagem de compreensão universal, uma espécie de Língua de publicação “Mãe”, a qual possa ser potencialmente usada e compreendida por todos os computadores.

O HTML é a linguagem de publicação usada pela _World Wide Web_ (do Inglês: _Hyper Text Markup Language_ ).

O HTML dá aos autores a possibilidade de:

- Publicar documentos _online_ contendo cabeçalhos, texto, quadros e tabelas, listas, fotos etc.;

- Recuperar ou retirar informações _online_ , por intermédio de ligações de hipertexto, clicando num botão;

- Concepção de formulários para efetuar transações com serviços remotos, para o uso na busca de informação, efetuar reservas, encomenda de produtos etc. (W3C, 2018).

## Versões

A versão mais significativa para nossa realidade foi o HTML 4.01 que foi publicado como uma recomendação do W3C em 1999. Ele possui as mesmas versões do HTML 4.0.

A especificação do HTML 5 teve início em 2008 e ainda está em desenvolvimento sendo que sua última publicação foi liberada em 2012.

**Figura 2 –** HTML5 **Fonte:** Wikimedia Commons

Muitos comandos não são compatíveis com todos os Navegadores (isso se aplica principalmente ao CSS3 que veremos mais para frente).

Quando abrimos uma página HTML em um navegador, o navegador irá interpretar as _tags_ , ou seja, irá fazer uma análise sintática, definindo como cada parte do texto será apresentada.

Um problema comum no desenvolvimento de páginas HTML desde o seu surgimento e outras tecnologias como CSS e _Javascript_ , é a compatibilidade entre os navegadores, ou seja, uma página desenvolvida em HTML5 pode rodar somente no _Chrome_ , por exemplo, ou aparecer de um jeito no _Internet Explorer_ e de outro no _Firefox_ , também temos que tomar cuidado quando falamos em dispositivos ou sistemas diferentes, como visualizar nossa página em um celular. Nem todos os aparelhos estão aptos a rodar os códigos atuais.

## Motores de Renderização

É o mecanismo utilizado pelos navegadores para processar o código das páginas _web_ , os principais motores dos principais navegadores são:

- _Webkit_ (é o mais compatível com HTML 5) – _Safari_ , _Chrome_ ;

- _Gecko_ – _Firefox_ ;

- _Trident_ – _Internet Explorer_ .

Devemos sempre procurar deixar nossos códigos compatíveis com esses motores para que possamos atingir o maior número possível de usuários.

## HTML Markup Tag

As marcações de _tags_ HTML são geralmente chamadas de _tags_ HTML.

As palavras chaves estão marcadas entre os símbolos < e > como <html>.

Geralmente em pares como <b> e </b>.

A primeira _tag_ do par é a _tag_ inicial e a segunda _tag_ a _tag_ final.

#### Regras HTML Tag

- _Tags_ HTML consistem em comandos que aparecem entre colchetes angulares (<>);

- _Tags_ HTML não são _case sensitive_ ;

- _Tags_ HTML quase sempre vêm em pares.

Exemplo:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=utf-8" />
<title>Untitled Document</title>
</head>

<body>
    <h1>Meu primeiro cabeçalho</h1>
    <p>Meu primeiro parágrafo</p>
</body>

</html>
```

**Figura 3 –** Exemplo de código HTML **Fonte:** Acervo do Conteudista

- Texto entre ```<html>``` e ```</html>``` descreve a página _web_ ;

- O texto entre ```<body>``` e ```</body>``` é a informação visível na página;

- O texto entre ```<h1>``` e ```</h1>``` é exibido como cabeçalho;

- O texto entre ```<p>``` e ```</p>``` é exibido como parágrafo.

## Document Type

O elemento <!DOCTYPE> especifica o tipo de documento (DTD), como página de uso restrito de HTML e CSS.

- **HTML 4.01** **_Strict_ DTD –** **_adheres_ CSS** **_and_ HTML 4.01** **_standards_ :** <!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 4.01//EN” “ h t t p : / / w w w . w 3 . o r g / T R / h t m l 4 / s t r i c t . d t d ” >

- **HTML 4.01** **_Transitional_ DTD –** **_adheres_ HTML 4.01 s** **_tandards including deprecated_ HTML** **_elements and attributes_ :** <!DOCTYPE html PUBLIC “-// W3C//DTD XHTML 1.0 Transitional//EN” “ h t t p : / / w w w . w 3 . o r g / T R / x h t m l 1 / D T D / x h t m l 1 - t r a n s i t i o n a l . d t d ” >

- **HTML 4.01** **_Frameset_ DTD –** **_adheres_ HTML 4.01** **_standards including deprecated_ HTML** **_elements and attributes and frames._**

O DOCTYPE é a maneira de você dizer para qualquer navegador como ele deve agir ao ler seu código HTML.

Porque cada _browser_ tem um padrão próprio de renderizar o HTML sem DOCTYPE.

O _Strict_ é o “melhor” uma vez que ao dizer para um _browser_ renderizar com ele, você está dizendo que seguirá rigorosamente os padrões.

O Transitional você diz ao _Browser_ que seu código está em transição, não necessariamente seguirá rigorosamente os padrões, mas não fará um “ninho de ratos”.

Já o _Frameset_ , será para renderizar os arcaicos _Frames_ .

## Documento Principal

O <html> é o elemento principal do documento HTML.

Ele contém outros elementos como:

- <head> </head> _tags_ ;

- <title></title> _tags_ ;

- <body></body> _tags_ .

O elemento <title> fornece o título do documento que aparece o topo do _browser_ .

O elemento <body> contém todas as informações do documento, ele vem depois do cabeçalho e deve ser fechado. A lista a seguir contém alguns atributos comuns:

- **BGCOLOR:** define o valor da cor;

- **BACKGROUND:** permite que você especifique um arquivo gráfico para utilizar como imagem de fundo:

   - Fornece um localizador de recursos uniforme (URL) de uma pasta de imagem para ser utilizada como o fundo tela;

   - Se a imagem for salva em outro lugar, você tem que digitar o endereço completo que aponta para a imagem.

- **LINK:** permite que você especifique a cor em que _hiperlinks_ de texto não visitados;

- **VLINK:** permite que você especifique a cor na qual visitou;

- **ALINK:** permite que você especifique a cor enquanto os usuários clicam nos _links_ .

Vejamos alguns elementos HTML.

#### Criação de Links

A _tag_ <a> define um _hiperlink_ que é usado para ligar uma página para outra.

O atributo mais importante do elemento é o atributo href, que indica o destino do _link_ .

```html
<a href="url">Link text</a>
<a href=http://www.uol.com.br>uol</a>
<a href="http://www.uol.com.br" target="_blank">UOL</a>
```

**Figura 4 –** Exemplo de uso da _tag_ <a> com uso do atributo href

**Fonte:** Acervo do Conteudista

#### Criação de Tabelas

A tag <table> define uma tabela em html. A tag <table> consiste em um elemento <tr> para indicar a linha e um elemento <td> para indicar a célula.

```html
<table border="1">
    <tr>
        <td>linha 1, célula 1</td>
        <td>linha 1, célula 2</td>
    </tr>
    <tr>
        <td>linha 2, célula 1</td>
        <td>linha 2, célula 2</td>
    </tr>
</table>
```

###### Figura 5 – Estrutura HTML para criação de tabela

###### Fonte: Acervo do Conteudista

**#ParaTodosVerem:** a figura apresenta um código HTML que utiliza as tags <table>, <tr> e <td> para a criação de uma tabela. Fim da Descrição.

#### Criação de Listas

- <ul> – lista não ordenada;

- <ol> – lista ordenada;

- <li> – item de lista.

```html
Listas
<ul>
    <li>Café</li>
    <li>Leite</li>
</ul>

<ol>
    <li>Café</li>
    <li>Leite</li>
</ol>
```

###### Figura 6 – Estrutura HTML para criação de listas

###### Fonte: Acervo do Conteudista

```html
#ParaTodosVerem: a figura apresenta um código HTML que utiliza as tags <ul> para uma lista não ordenada,
<ol> para uma lista ordenada e <li> que inserir os itens nas listas. Fim da descrição.
```

#### Criação de Campos Textos

A tag ```<input>``` especifica um campo de entrada onde o usuário pode inserir dados. Os ```<input>``` geralmente são utilizados dentro de ```<form>```.

Um campo de entrada pode variar de muitas formas, dependendo do tipo de atributo.

```html
<input type="text" name="firstname" /><br />
<input type="text" name="lastname" />
<input type="password" name="pwd" />
<input type="radio" name="sex" value="home" />Homem<br />
<input type="radio" name="sex" value="mulher" /> Mulher
<input type="checkbox" name="veiculo" value="Moto" /> Eu tenho moto
<input type="checkbox" name="veiculo" value="Carro" /> Eu tenho carro
<input type="submit" value="Submit" />
```

**Figura 7 –** Estrutura HTML com uso da _tag_ ```<input>```

**Fonte:** Acervo do Conteudista

#### Caracteres Especiais

HTML permite que caracteres especiais sejam representados por sequências de escape, indicadas por três partes: um & inicial, um número ou cadeia de caracteres correspondente ao caractere desejado, e um ; final.

Quatro caracteres ASCII – <, >, e & têm significados especiais em HTML, e são usados dentro de documentos seguindo a correspondência:

**Quadro 1**

|**Entidade**|**Caracter**|
|---|---|
|&lt;|<|
|&gt;|>|
|&amp;|&|

Outras sequências de escape suportam caracteres ISO Latin1. Aqui está uma Tabela com os caracteres mais utilizados em português:

|**Entidade**|**Caracter**|**Entidade**|**Caracter**|
|---|---|---|---|
|á|&aacute;|Á|&Aacute;|
|ã|&atilde;|Ã|&Atilde;|
|â|&acirc;|Â|&Acirc;|
|à|&agrave;|À|&Agrave;|
|é|&eacute;|É|&Eacute;|
|ê|&ecirc;|Ê|&Ecirc;|
|í|&iacute;|Í|&Iacute;|
|ó|&oacute;|Ó|&Oacute;|
|õ|&otilde;|Õ|&Otilde;|
|ô|&ocirc;|Ô|&Ocirc;|
|ú|&uacute;|Ú|&Uacute;|
|ü|&uuml;|Ü|&Uuml;|
|ç|&ccedil;|Ç|&Ccedil;|

Como vemos, as sequências de escape são sensíveis à caixa. Os editores de HTML fazem essa tradução automaticamente.

Alguns editores, no entanto, mantêm a acentuação, sem usar as entidades de formatação. Quando isso acontece, deve-se inserir uma indicação do esquema de codificação ISO Latin1, escrevendo:

```html
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;charset=ISO-8859-1">
```

## Alguns Elementos Novos do HTML

#### Section

Representa um documento genérico ou seção da aplicação. Pode ser usado em conjunto com elementos ```<h1>```,``` <h2>```, ```<h3>```, ```<h4>```, ```<h5>``` e ```<h6>``` para indicar a estrutura do documento

Exemplo:

```html
<!DOCTYPE html>
<html>
<body>

<section>
  <h1>WWF</h1>
  <p>The World Wide Fund for Nature (WWF) is an international organization working on
issues regarding the conservation, research and restoration of the environment, formerly
named the World Wildlife Fund. WWF was founded in 1961.</p>
</section>

<section>
  <h1>WWF's Panda symbol</h1>
  <p>The Panda has become the symbol of WWF. The well-known panda logo of WWF originated
from a panda named Chi Chi that was transferred from the Beijing Zoo to the London Zoo in
the same year of the establishment of WWF.</p>
</section>

</body>
</html>
```

**Figura 8 –** Estrutura HTML com uso da _tag_ <section>

**Fonte:** Acervo do Conteudista

#### Article

Representa uma peça independente do conteúdo de um documento, como um blog ou artigo de jornal.

```html
<!DOCTYPE html>
<html>
<body>

<article>
  <h1>Internet Explorer 9</h1>
  <p>Windows Internet Explorer 9 (abbreviated as IE9) was released to
  the  public on March 14, 2011 at 21:00 PDT.....</p>
</article>

</body>
</html>
```

**Figura 9 –** Estrutura HTML com uso da _tag_ <article> **Fonte:** Acervo do Conteudista

#### Aside

Representa uma parte do conteúdo que é pouco relacionado com o resto da página.

```html
<!DOCTYPE html>
<html>
<body>

<p>My family and I visited The Epcot center this summer.</p>

<aside>
<h4>Epcot Center</h4>
<p>The Epcot Center is a theme park in Disney World, Florida.</p>
</aside>

</body>
</html>
```

**Figura 10 –** Estrutura HTML com uso da _tag_ <aside>

**Fonte:** Acervo do Conteudista

#### Footer

Representa um rodapé de uma seção e pode conter informações sobre o autor, direitos autorais etc.

```html
<!DOCTYPE html>
<html>
<body>

<footer>
  <p>Posted by: Hege Refsnes</p>
  <p><time pubdate datetime="2012-03-01"></time></p>
</footer>

</body>
</html>
```

**Figura 11 –** Estrutura HTML com uso da _tag_ <footer> **Fonte:** Acervo do Conteudista

#### Figure

Representa uma parte do conteúdo de fluxo autossuficiente.

Serve para agrupar uma seção de conteúdo independente, como um vídeo ou uma imagem.

```html
<!DOCTYPE html>
<html>
<body>

<p>The Pulpit Rock is a massive cliff 604 metres (1982 feet) above Lysefjorden,
opposite the Kjerag plateau, in Forsand, Ryfylke, Norway. The top of the cliff is
approximately 25 by 25 metres (82 by 82 feet) square and almost flat, and is a famous
tourist attraction in Norway.</p>

<figure>
  <img src="nome_arquivo" alt="" width="304" height="228" />
</figure>

</body>
</html>
```

**Figura 12 –** Estrutura HTML com uso da _tag_ <figure> **Fonte:** Acervo do Conteudista
