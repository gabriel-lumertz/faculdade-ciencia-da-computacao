---
materia: "Programação Web"
modulo: "Fundamentos de CSS"
semestre: 2
unidade: 2
tipo: material-teorico
fonte: "raw/2-semestre/PROGRAMAÇÃO WEB/Programação Web 02.pdf"
tags: [faculdade, programacao-web, semestre-2]
aliases: ["Programação Web - Unidade 2"]
---

# Fundamentos de CSS

### OBJETIVOS DA UNIDADE

- Entender as regras e a função do CSS na programação _web_ ;

- Compreender como as folhas de estilo organizam o conteúdo de uma página _web_ , aplicando os conhecimentos adquiridos na construção de _layouts_ .

## O Que é CSS?

A finalidade do HTML, desde sua criação, sempre foi lidar somente com a marcação e a estruturação de conteúdo. Entretanto, quando abrimos nosso navegador, vemos páginas atraentes e agradáveis, que extrapolam uma simples marcação de _tags_ HTML.

No início do HTML, recorria-se a elementos e atributos específicos da própria Linguagem para definir a formatação das páginas. Por exemplo, o elemento ```<font>``` foi introduzido na versão 3.2 do HTML para definir fonte, tamanho e cor de texto.

A partir da versão 4.0 do HTML, o _World Wide Web Consortium_ ( _W3C_ ) incorporou o _CSS_ ( _Cascading Style Sheet_ , ou Folha de Estilo em Cascatas), com a finalidade de se encarregar de toda a apresentação visual de um _site_ , alterar elementos como fonte, cor e tamanho de textos, espaçamento entre blocos, enfim, todo o aspecto estético de uma página _web_ .

A utilização do CSS trouxe vários benefícios e, entre eles, podemos citar:

- Garantir flexibilidade e controle dos elementos na página;

- Simplificar a criação de páginas _web_ ;

- Permitir que a aparência e o _layout_ de todas as páginas de um _site_ sejam alteradas editando-se, com isso, um único arquivo (folhas de estilo externas);

- Garantir maior flexibilidade e controle nas especificações do _site_ , entre outros.

#### Sintaxe CSS

O CSS utiliza uma estrutura de sintaxe simples, na qual a regra é a unidade básica de uma folha de estilo e é composta de duas partes principais: um seletor e uma ou mais declarações, como apresentado na Figura 1.

![[pw2-02-fig01.webp]]

*Figura 1 – Regra CSS*

**#ParaTodosVerem:** imagem que descreve a utilização de uma Regra CSS. Da esquerda para a direita, são especificados o Seletor e as declarações. Na parte superior da imagem, há o título “Regra CSS”. A parte inferior da imagem contém textos destacando a Propriedade e o valor de cada uma das declarações. O seletor utilizado é o h1 e as declarações são “color: blue” e “font-size: 12px”. Fim da descrição.

Nessa definição dos componentes de uma regra CSS, temos:

- **Seletor:** é o elemento HTML que se deseja criar o estilo;

- **Declaração:** determina os parâmetros do estilo e consiste em uma **propriedade** e um **valor** ;

- **Propriedade:** define a característica do seletor que será alterada;

- **Valor:** refere-se à quantificação ou qualificação da propriedade.

Uma regra pode conter várias declarações separadas por ponto e vírgula. Veja o exemplo a seguir:

```html
h1{color: _red_ ; font-size: 36px}
```

#### Seletores Válidos

Os seletores são componentes HTML que desejamos modificar e estilizar, por meio do uso do CSS. Dentre os vários existentes, o Quadro 1 apresenta três dos principais seletores utilizados para criar estilos para um elemento do HTML.

| **Tipo de seletor**     | **Descrição**                                                                                                                                               | **Exemplo**                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Seletor de elemento** | Seleciona um elemento<br>do HTML.                                                                                                                           | **p**<br>Seleciona apenas<br>os elementos **p**<br>da página.                           |
| **Seletor de id**       | Usado para especificar<br>um estilo para um<br>elemento único e<br>seleciona apenas um<br>elemento que possui o<br>valor atribuído id.                      | **_main_**<br>Seleciona apenas<br>o elemento com<br>o **id “_main_”**.                  |
| **Seletor de classe**   | Usado para especificar<br>um estilo para um<br>grupo de elementos,<br>permitindo criar um<br>estilo para vários<br>elementos do HTML com<br>a mesma classe. | **_main_**<br>Seleciona apenas<br>os elementos<br>que possuem a<br>classe **_“main”_**. |

Vejamos, a seguir, um exemplo contendo o uso desses seletores:

```html
<html>
<head>
<style>
       #main {
               text-align: center;
               color: red;
       }
       .cor {color: blue;}
       p {font-size: 28px;}
       /*Efeito de sombra no texto*/
       h1{text-shadow: 5px 5px 5px #FF0000;}
       /*Efeito quebra de linha*/
       p {word-wrap:break-word;}
       @import url('https://fonts.googleapis.com/css2?family=Shan-
       tell');
       p{font-family: 'Shantell Sans', cursive;}
       div{
               transform: rotate(20deg);
       }
</style>
</head>
<body>
       <h1 id="main">Texto alinhado ao centro na cor vermelha</
       h1>
       <h2 class="cor">Texto alinhado à esquerda na cor azul</h2>
       <p>Texto alinhado à esquerda no tamanho 28px</p>
</body>
</html>
```

##### Site

O CSS _Validation Service_ é uma ferramenta indispensável para verificar se o seu CSS é válido.

## Vinculando Folhas de Estilo a Documentos

Não basta que você defina uma regra CSS. É preciso informar ao documento onde ela se encontra. As folhas de estilo podem ser utilizadas de três maneiras diferentes:

- Estilo externo;

- Estilo interno;

- Estilo _inline_ .

O estilo externo é ideal quando a formatação deve ser aplicada a várias páginas. Com um arquivo externo, você pode alterar um formato e ele será aplicado automaticamente em todo o projeto.

Um estilo externo pode ser escrito por qualquer editor e não deve conter nenhuma _tag_ HTML. O arquivo deve ser salvo com a extensão .css e pode ser vinculado a um documento HTML usando o elemento _link_ , que deve estar contido na da seção _head_ .

Veja o exemplo a seguir:

```html
<head>
       <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
```

Lembre-se de que o atributo href deve apontar exatamente o endereço no qual se encontra o arquivo que contém a folha de estilo criada. Veja a seguir um exemplo de uma folha de estilo salva no arquivo **estilo.css** :

```css
hr {color: _sienna_ ;} p {margin-left:20px;} body {background-image:url(“images/back40.gif”);}
```

O estilo interno é usado na própria página HTML, sendo definido na seção _head_ com o emprego do elemento _style_ . As regras de estilo são definidas dentro das _tags_ ```<style></style>```, como mostra o exemplo a seguir:

```html
<head>
	<style type=”text/css”>
		hr {color: _sienna_ ;}
		p {margin-left:20px;}
		body {background-image:url(“images/back40.gif”);}
	</style>
</head>
```

O estilo _inline_ é o método mais simples e direto de aplicar formatação a um elemento HTML. Ele é usado diretamente no elemento que se quer alterar, dentro das _tags_ de abertura e fechamento do elemento, por meio do emprego do atributo _style_ .

Veja um exemplo a seguir:

```html
<p style="color:sienna; margin-left:20px">
Este é um parágrafo formatado
</p>
```

## Estilizando Documentos

Como vimos no começo desta Unidade, as propriedades são utilizadas para definir características que serão aplicadas aos elementos HTML. A seguir, veremos algumas dessas propriedades e como elas alteram o _layout_ de uma página _web_ .

#### Background

As propriedades do _background_ são usadas para definir uma cor ou uma imagem de fundo e estão listadas a seguir:

- _Background-color;_

- _Background-image;_

- _Background-repeat;_

- _Background-attachment;_

- _Background-position._

A propriedade _background-color_ especifica a cor de fundo do elemento. Por exemplo:
```css
body {background-color: #b0c4de;}
```

Já a propriedade background-image define uma ou mais imagens a serem usadas como fundo para o elemento.

Por exemplo:

```css
body {background-image:url(“paper.gif”);}
```

##### Importante

Ao se utilizar a _background-image_ , recomenda-se utilizar uma propriedade auxiliar, como a _background-color_ , visto que pode ocorrer alguma falha no carregamento da imagem.

A propriedade _background-repeat_ pode ser utilizada conjuntamente para repetição da imagem de fundo:

- **_Repeat:_** a imagem é repetida na vertical e na horizontal, até o preenchimento da área do elemento;

- **_Repeat-_ x** **_:_** a imagem repetida somente na horizontal;

- **_Repeat-_ y** **_:_** a imagem repetida somente na vertical;

- **_No-repeat:_** a imagem é inserida apenas uma vez no plano de fundo. Pode ser utilizada de modo que a imagem não atrapalhe o texto, como o exemplo da Figura 2:

![[pw2-02-fig04.webp]]

**Figura 2 –** Exemplo de uma página utilizando _background-image_ **Fonte:** Reprodução

**#ParaTodosVerem:** imagem de exemplo da utilização do _background-image_ . Na parte superior, há um título escrito “Exemplo _background-image_ ”. Logo abaixo, dois parágrafos com textos que descrevem a estilização do conteúdo na página. À direita, há uma imagem de uma árvore nas cores rosa e marrom, sendo que em um dos galhos encontra-se uma coruja. Fim da descrição.

Nesse exemplo, a imagem de fundo é mostrada numa posição de modo que ela não perturbe o texto. O código CSS utilizado é mostrado a seguir:

```css
body { background-image: url(“img_tree.png”); background-repeat: no-repeat; background-position: right top; margin-right: 200px; }
```

Perceba que, para obtermos o efeito desejado, foi necessário utilizar uma nova propriedade, o _background-position_ que indica a posição na qual a imagem de fundo será inserida.

Alguns dos valores possíveis dessa propriedade são:

- **_Left top:_** à esquerda superior;

- **_Right center:_** à direita e ao centro;

- **_Center bottom:_** ao centro inferior.

#### Fontes e Texto

Quando o desejamos formatar a exibição de textos, as propriedades CSS geralmente se enquadram em duas categorias:

- **Estilos de fontes:** afetam a fonte do texto, como, por exemplo, tamanho, negrito e itálico, entre outros;

- **Estilos de** **_layout_ de texto:** afetam o espaçamento e outros recursos de layout do texto, como, por exemplo, o espaço entre linhas e o alinhamento do texto dentro de uma caixa de conteúdo.

##### Estilos de Fontes

A propriedade _font_ define família , tamanho e estilo do texto:

- _Font-family;_

- _Font-style;_

- _Font-size._

A família da fonte de um texto é definida com a propriedade _font-family_ , cujo valor (nome da fonte) é uma _string_ ou uma lista de _strings_ separadas por vírgula. Procure sempre terminar a lista com uma fonte genérica, que se destina a uma possível falha nas escolhas do programador.

Veja o exemplo a seguir:

```css
p{font-family: “Lucida Grande”, _Lucida, Verdana, Sans-serif_ ;}
```

A propriedade _font-style_ tem 3 valores:

- **Normal:** a própria fonte;

- **_Italic_ :** itálico;

- **Oblique:** muito similar ao itálico, porém, menos utilizado.

```css
p.normal {font-style:normal;} p.italic {font-style:italic;} p.oblique {font-style:oblique;}
```

Já o tamanho do texto é definido pela propriedade font-size, que pode ter um valor absoluto ou relativo:

###### Valor Absoluto

- Define o texto a um tamanho especificado;

- Não permite que o usuário altere o tamanho do texto em todos os navegadores (ruim por razões de acessibilidade);

- O tamanho absoluto é útil quando o tamanho físico da saída é conhecido.

###### Valor Relativo

- Define o tamanho relativo aos elementos;

- Permite que o usuário altere o tamanho do texto em navegadores.

- A seguir, temos um exemplo que se utiliza de valores relativos e absolutos:

```css
/*Tamanho absoluto*/
h1 {font-size:40px;}
h2 {font-size:30px;}
p {font-size:14px;}
/*Tamanho relativo*/
h1 {font-size:2.5em;} /* 40px/16=2.5em */
h2 {font-size:1.875em;} /* 30px/16=1.875em */
p {font-size:0.875em;} /* 14px/16=0.875em */
body {font-size:100%;}
h1 {font-size:2.5em;}
h2 {font-size:1.875em;}
p {font-size:0.875em;}
```

###### Estilos de Layout de Texto

Completando a formatação de _layout_ de texto, as propriedades que veremos são:

- **_Color_ :** é utilizada para configurar a cor do texto:

```css
body {color: _blue_ ;} h1 {color:#00ff00;} h2 {color:rgb(255,0,0);}
```

- **_Text-align_ :** é usada para especificar o alinhamento do texto à esquerda, direita, centralizado ou justificado:

```css
h1 {text-align: _center_ ;} p.date {text-align: _right_ ;} p.main {text-align: _justify_ ;}
```

- **Text-decoration:** é frequentemente utilizada nos links para configurar ou remover decorações do texto:

```css
a {text-decoration: _none_ ;} h1 {text-decoration: _overline_ ;} h2 {text-decoration: _line-through_ ;} h3 {text-decoration: _underline_ ;} h4 {text-decoration: _blink_ ;}
```

- **_Text-transform_ :** é usada para especificar o _uppercase_ e _lowercase_ nos textos:

```css
p.uppercase {text-transform: _uppercase_ ;} p.lowercase {text-transform: _lowercase_ ;} p.capitalize {text-transform: _capitalize_ ;}
```

- **_Text-indentation:_** é usada para definir um espaçamento horizontal antes do início da primeira linha do texto, em outras palavras, uma indentação da primeira linha ou parágrafo:

```css
p {text-indent:50px;}
```

##### Importante

Quando utilizamos a marcação ```p.main {text-align: _justify_ ;}``` estamos justificando o texto do parágrafo (```<p>```) cuja classe é main.

#### Estilos de Borda de um Elemento

A propriedade _border_ é responsável por adicionar contorno ao redor de seu conteúdo e pode ter diferentes estilos e tamanhos, podendo ser utilizada em diferentes elementos HTML, como, por exemplo, o ```<input>```. As especificações do CSS permitem definir espessura, cor e estilo para a borda, além de ser possível especificar cada uma das quatro bordas individualmente.

A sintaxe resumida dessa propriedade é apresentada na Figura 3, a seguir.

![[pw2-02-fig06.webp]]

**Figura 3 –** Sintaxe da propriedade _border_

**#ParaTodosVerem:** imagem que descreve a sintaxe da propriedade _border_ . Da esquerda para a direita é especificada a propriedade e suas definições: “border: border-width border-style border-color”. Na parte inferior da imagem, existem três quadros que descrevem cada um dos estilos aplicados à borda. Fim da descrição.

A declaração da borda pode ser feita resumidamente, como visto na Figura 5, porém, também é possível fazer a declaração individualmente de cada propriedade.

Os exemplos a seguir produzem o mesmo efeito:

```css
.main{border: 5px solid red;}
```

Ou

```css
.main{ border-width: 5px; border-style: solid; border-color: red; }
```

#### Margens e Espaçamentos

A propriedade _margin_ permite adicionar ao redor do elemento um distanciamento na parte externa. A margem não tem cor de fundo e é completamente transparente. As margens superior, inferior, direita e esquerda podem ser alteradas de forma independente, usando suas propriedades separadas:

- **_Margin-top_ :** determina o espaçamento superior;

- **_Margin-right_ :** determina o espaçamento no lado direito;

- **_Margin-bottom_ :** determina o espaçamento inferior;

- **_Margin-left_ :** determina o espaçamento no lado esquerdo.

Para centralizar um elemento na tela ou dentro de outro elemento, podemos utilizar o valor auto, como mostra o exemplo a seguir:

```html
<html>
<head>
       <title>CSS</title>
       <style>
              .box {
                   width: 400px;
                   border: 2px solid rgb(186, 184, 228);
              }
              .box p {
                     width: 250px;
                     margin: 0 auto;
              }
       </style>
</head>
<body>
       <div class="box">
              <p>Parágrafo centralizado dentro de um box de largura de 400px.
              </p>
       </div>
</body>
</html>
```

Observe, no exemplo, que, como queremos centralizar o parágrafo, a propriedade _margin_ : auto foi aplicada somente a esse elemento. Poderíamos aplicar a mesma formatação ao box para centralizá-lo, como foi feito anteriormente.

Veja a seguir como ficaria essa formatação:

```css
.box p { width: 400px; border: 2px solid rgb(186, 184, 228); margin: 0 auto; }
```

##### Importante

A propriedade _margin_ pode desestruturar o _layout_ da página HTML, pois altera o posicionamento dos elementos. Portanto, use-a com cuidado!

Outra propriedade utilizada para definir o espaçamento ao redor de um elemento é o _padding_ , que define o espaço interno entre um elemento e sua respectiva borda. Assim como na propriedade _margin_ , também é possível determinar os espaçamentos superior, inferior, direito e esquerdo de forma independente, usando suas propriedades separadas.

Vamos alterar o exemplo anterior, para aplicar um _padding_ de 20px ao parágrafo:

```css
.box { width: 250px; margin: 0 _auto_ ; padding: 20px; }
```

A Figura 4 mostra a comparação entre a formatação do parágrafo antes e depois da aplicação do _padding_ de 20px ao parágrafo.

![[pw2-02-fig08.webp]]

**Figura 4 –** Comparação entre os exemplos propostos

**Fonte:** Reprodução

**#ParaTodosVerem:** imagem que compara a utilização da formatação do parágrafo. À esquerda, há uma caixa contendo o texto “Parágrafo centralizado dentro de um box que tem largura de 400px.”. Logo abaixo, encontra-se a descrição “Parágrafo sem _padding_ 20px” e uma seta aponta para a caixa que contém o texto. À direita, há uma caixa contendo o texto “Parágrafo centralizado dentro de um box que tem largura de 400px. _Padding_ de 20px!”. Logo abaixo, encontra-se a descrição “Parágrafo com _padding_ 20px” e uma seta aponta para a caixa que contém o texto. Fim da descrição.

Na Figura 5, temos a renderização de um elemento HTML, que exibe um determinado conteúdo, de acordo com a formatação CSS. Perceba a diferença entre _margin_ e _padding_ , bem como a função do _width_ e do _height_ , que determinam a largura e a altura do elemento, respectivamente.

![[pw2-02-fig09.webp]]

**Figura 5 –** Apresentação visual de um elemento de acordo com a formatação CSS **Fonte:** Reprodução

**#ParaTodosVerem:** imagem ilustrativa de um elemento formatado com CSS. A Figura é composta por três retângulos de tamanhos diferentes, sendo o maior transparente, com borda tracejada, o seguinte na cor cinza com uma borda sólida na cor preta e, no centro, encontra-se o terceiro retângulo na cor azul com o texto “Conteúdos” e, abaixo, “elemento HTML”. No retângulo do centro, há duas setas: uma horizontal, indicando a largura do retângulo ( _width_ ), e outra vertical, indicando a altura ( _height_ ). No retângulo maior, com bordas tracejadas, há a indicação de cada um dos lados, contendo os textos, em sentido horário: “ _right_ ”, “ _bottom_ ”, “ _left_ ” e “ _top_ ”. Fim da descrição.

## Módulos CSS3

A versão mais recente das folhas de estilo é o CSS3 que, diferentemente de suas versões anteriores, foi desenvolvido em módulos que introduziram novos recursos que mudaram amplamente a forma como as páginas _web_ são vistas pelos usuários.

Vejamos, a seguir, alguns dos principais módulos e como utilizá-los.

#### Bordas e Sombras com CSS3

A partir do CSS3, podemos criar bordas arredondas, adicionar sombras nas caixas e usar imagens como borda, sem a necessidade de um programa de editoração.

O Quadro 2 apresenta as principais propriedades das bordas e suas compatibilidades com os navegadores:

**Quadro 2 –** Principais propriedades e compatibilidade com navegadores

|**Propriedade**|**Chrome**|**Explorer**|**Mozilla**|**Safari**|**Opera**|
|---|---|---|---|---|---|
|border-radius|5.0<br>4.0 -webkit-|9.0|4.0<br>3.0 -moz-|5.0<br>3.1 -webkit-|10.5|
|box-shadow|10.0<br>4.0 -webkit-|9.0|4.0<br>3.5 -moz-|5.1<br>3.1 -webkit-|10.5|

##### Importante

Na Tabela 1, os números seguidos por -webkit-, -moz- ou -oespecificam a primeira versão que funcionou com um prefixo.

A propriedade _border-radius_ define um raio de curvatura nos quatro cantos de um _box_ e permite adicionar o efeito de arredondamento ao elemento, independentemente do _box_ ter ou não uma borda declarada.

Veja a Figura 6, a seguir:

![[pw2-02-fig11.webp]]

###### Figura 6 – Comparação entre o arredondamento com e sem a borda declarada. Fonte: Reprodução

**#ParaTodosVerem:** imagem comparando o arredondamento com e sem bordas declaradas. A figura é composta por dois retângulos, sendo o superior com borda na cor vermelha e fundo cinza e o inferior sem bordas e com o fundo também cinza. Acima do primeiro retângulo, está o título “ _Box_ com borda de 2px” e acima do segundo retângulo está o título “ _Box_ sem borda”. Fim da descrição.

A seguir, temos o código utilizado para o box com borda declarada:

```css
.comBorda { border: 2px solid #991e1e; padding: 10px 40px; background: #ecebeb; width: 300px; border-radius: 25px; -moz-border-radius: 25px; }
```

A propriedade _box-shadow_ define uma ou mais sombras para um elemento:

```css
.sombra { border: 1px solid; padding: 10px; box-shadow: 5px 10px 8px #888888; }
```

#### Outras Formatações com CSS3

A partir do CSS3, a estilização de textos passou a contar com novas propriedades, entre as quais vamos destacar, nos exemplos a seguir, o _text-shadow_ e _word-wrap_ :

```css
_/*Efeito de sombra no texto*/_ h1{text-shadow: 5px 5px 5px #FF0000;}
_/*Efeito quebra de linha*/_ p {word-wrap: break-word;}
```

Como vimos anteriormente, a família da fonte de um texto é definida com a propriedade _font-family_ . Entretanto, você pode querer utilizar uma fonte que não está instalada no computador do usuário. Isso é possível por meio da regra _@font-face_ , que permite incluir uma fonte a partir da _Web_ .

Veja o exemplo a seguir, no qual importamos a fonte “ _Shantell Sans_ ”, a partir da biblioteca do _Google_ , e utilizamos na formatação do parágrafo:

```css
@import url(‘https://fonts.googleapis.com/css2?family=Shantell’); p{font-family: ‘Shantell Sans’, cursive;}
```

##### Site

O _Google_ tem uma Biblioteca para facilitar o uso de fontes remotas. Visite o _Google Fonts_ e explore os tutoriais e funcionalidades disponíveis na ferramenta.

Com a propriedade CSS _tranforms_ é possível esticar, girar, aumentar e torcer um elemento HTML.

Os principais métodos que veremos são:

- **_Rotate_ (x):** gira um elemento no sentido horário ou anti-horário, de acordo com um determinado ângulo (x);

- **_Translate_ (x,y):** permite mover um elemento de uma posição para a outra, dependendo do parâmetros de posição passados dos eixos x e y;

- **_Scale_ (x):** permite aumentar ou diminuir o tamanho de um elemento.

A seguir, temos um exemplo completo utilizando a propriedade _transform_ .

```html
<!DOCTYPE html>
<html lang="en">
<head>
        <title>Imagem transform</title>
        <style>
               .imagem {
                      transform: scale(0.2) rotate(360deg);
                      /*transition: all 2s*/;
               }
               .imagem:hover {
                      transform: scale(0.7);
               }
        </style>
</head>
<body>
        <img src="css.png" alt="" class="imagem">
</body>
</html>
```

Se você digitou o código acima, pôde perceber que seu navegador exibe uma imagem (logo do CSS) e, quando passamos o ponteiro do _mouse_ sobre ela, a imagem gira e aumenta de tamanho.

Você entendeu o que código faz?

Não!

Sem problema, pois, no Quadro 3, vamos analisar o que está acontecendo.

###### Quadro 3 – Exemplo comentado

|**Linha(s)**|**Descrição**|
|---|---|
|Linha 7|Definimos o tamanho da imagem para 20% (**scale(0.2)**) e<br>uma rotação de 360 graus (**rotate(360deg)**).|
|Linha 10|A pseudo-classe:**hover**corresponde ao usuário mover o<br>cursor do_mouse_sobre a imagem.|
|Linha 11|O tamanho da imagem muda para 70% (**scale(0.7)**).|
|Linha 8|Adiciona um efeito de transição de 2s a todos os elementos<br>**(transition: all 2s)**.|

Para finalizar esta Unidade, devemos detalhar a propriedade _transition_ , que permite definir a transição entre dois estados de um elemento HTML. Experimente excluir a linha 11 do código acima e perceberá que a imagem aumenta de tamanho quando movemos o cursor do _mouse_ sobre ela quase instantaneamente, sem o efeito de rotação!

Observe, nesse último exemplo, o efeito de transição aplicado para alterar o comprimento de uma ```<div>```:

```css
div { width: 100px; height: 100px; background: _red_ ; transition: width 2s; } div:hover { width: 300px; }
```

##### Site

O CSS3 _Generator_ é uma ferramenta que auxilia desenvolvedores iniciantes na geração de códigos CSS3. Dentre as opções disponíveis, é possível encontrar: _border-radius_ , _box-shadow_ e _text-shadow_ , entre outras.
