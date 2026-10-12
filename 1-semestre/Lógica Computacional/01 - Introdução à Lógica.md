---
materia: "Lógica Computacional"
modulo: "Introdução à Lógica"
semestre: 1
unidade: 1
tipo: material-teorico
fonte: "raw/1-semestre/LÓGICA COMPUTACIONAL/Lógica Computacional 01.pdf"
tags: [faculdade, logica-computacional, semestre-1]
aliases: ["Lógica Computacional - Unidade 1"]
---

# Introdução à Lógica

## Contextualização

Um bom motivo para estudar lógica computacional é que sua teoria é a base da computação e utilizamos os seus conceitos em atividades do dia a dia e até mesmo para resolver problemas. Para que possamos nos expressar, fazemos o uso de diferentes tipos de sentenças, por exemplo, quando afirmamos “Hoje está frio”, estamos diante de uma sentença afirmativa. Já quando fazemos uma pergunta, fazemos uso de uma sentença interrogativa e quando algo nos surpreende usamos sentenças exclamativas.

Em lógica, no entanto, só utilizamos sentenças que podem ser classificadas como verdadeiras ou falsas, ou seja, um único valor lógico, e dentre as sentenças que utilizamos no nosso dia a dia, apenas as afirmativas podem, assim, ser classificadas e na lógica computacional elas são conhecidas como proposições lógicas.

Já na área da computação, a lógica tem ligação estreita com a área, pois está relacionada diretamente com o desenvolvimento de linguagens para modelar situações e problemas, com o objetivo de solucioná-los.

Nesta Unidade iremos conhecer o que é lógica, a sua história e os tipos. Dentre os formalismos lógicos existentes, iremos apresentar os conceitos da lógica proposicional, considerada a formalização mais simples para representação do raciocínio, que utiliza em sua representação proposições simples e compostas. Na sequência conheceremos os conectivos lógicos, as tabelas-verdade e a classificação obtida a partir do resultado lógico gerado.

#### Introdução: o que é Lógica?

Para qualquer resposta que se dê a essa pergunta corre-se o risco de deixar de fora algum aspecto importante da lógica, pois normalmente associa-se a lógica apenas à matemática, esquecendo-se de que ela se aplica a todos os ramos do conhecimento humano. Porém, uma resposta ampla e precisa para essa difícil pergunta, é que a lógica é uma ciência que estuda os princípios e os métodos que permitem estabelecer as condições de validade e invalidade de **argumentos** .

### Glossário

**Argumento: é uma parte do discurso, que pode ser falado ou escrito, composto por uma ou mais sentenças, também conhecidas como premissas, e uma sentença denominada conclusão.**

Considere o exemplo de argumento apresentado na Figura 1:

![[lc1-01-fig01.webp]]

**Figura 1 – Exemplo de argumento, premissas e conclusão**

Na ciência da computação a lógica tem como papel principal o desenvolvimento de linguagens de modelagem e especificação, com o objetivo de permitir o raciocínio sobre situações e sistemas e no desenvolvimento de argumentos sobre situações específicas, que possam ser validados ou não.

Assim, na lógica estudamos a validade dos argumentos, cujo foco não está no conteúdo desses e sim no seu valor lógico e na sua estrutura. A lógica é também chamada de formal, simbólica ou matemática e tem como base três definições, cada uma associada a um período de sua evolução:

Lógica como um sistema de regras, concebida no período grego (século IV a.C. até o início do século XIX); Lógica como um conjunto de leis, período booleano (século XIX e primeira década do século XX);

Lógica como estrutura linguística, período contemporâneo.

A seguir apresentamos mais detalhes sobre cada período da história da lógica.

#### História da Lógica

A busca por regras que confirmem a validade de um argumento dominou o primeiro período, o qual é responsável pela primeira sistematização conhecida da lógica, uma coleção de tratados denominada _Organon_ . Esses tratados lógicos são de autoria de Aristóteles (384-322 a.C.), autor mais importante da mais influente escola de lógica desse período, e foram reunidos após sua morte.

No segundo período, a lógica passou a evoluir em um sentido mais matemático ou, mais precisamente, mais algébrico. A evolução nesse sentido representa uma mudança na definição de lógica, pois passou a buscar as suas leis como resultado de fórmulas algébricas. Essa aproximação da lógica com a álgebra deu-se devido à influência principalmente de George Boole (1815-1864). Ainda nesse período, G. Frege (1848-1925) desenvolveu um sistema de lógica por um método linguístico (cálculo proposicional) que se afastou do modo algébrico e teve muita influência na lógica contemporânea, descrita a seguir.

O período contemporâneo tem o seu início marcado a partir da publicação em três volumes do _Principia Mathematica_ em 1910, 1912 e 1913, respectivamente. É nesse período que o enfoque linguístico-formal se impõe, ou seja, a lógica passa a ser vista como estrutura linguística. Com isso, a lógica como uma linguagem, ou como um sistema de signos pressupõe uma sintaxe (regras ou leis de combinação dos signos) e uma semântica (interpretação e significado dos signos). É importante notar que a definição da lógica neste terceiro período integra as outras duas. A partir de 1930 até os dias atuais, a evolução da lógica caminha em uma direção de maior integração à matemática, atingindo uma complexidade técnica elevada e ampliando consideravelmente o seu domínio com aplicações nas mais diversas áreas, como Informática, Administração de Empresas, Física, Economia, Engenharia, dentre outras.

#### Classificação da Lógica

A Lógica é classificada em:

**Lógica indutiva:** útil no estudo da teoria da probabilidade;

- **Lógica dedutiva:** que pode ser dividida em:

   - **Lógica clássica:** considerada como o núcleo da lógica dedutiva, conhecida como cálculo de predicados de 1ª ordem. Três princípios regem à lógica clássica: da identidade, da contradição e do terceiro excluído, que serão apresentados a seguir;

   - **Lógicas complementares da clássica:** complementam de algum modo a lógica clássica estendendo o seu domínio. Exemplos: lógicas modal, deôntica, epistêmica, etc.;

   - **Lógicas não clássicas:** assim caracterizadas por derrogarem algum ou alguns dos princípios da lógica clássica. Exemplos: paracompletas e intuicionistas, paraconsistentes, não-aléticas, não-reflexivas, probabilísticas, polivalentes, lógica _fuzzy_ , dentre outras.

#### Lógica Proposicional e Tabela Verdade

Conforme já descrito, a lógica clássica possui três princípios: o da identidade, no qual todo objeto é idêntico a si mesmo; da contradição, em que de duas proposições contraditórias (uma é negação da outra), uma delas é falsa; e do terceiro excluído, dadas duas proposições contraditórias, uma delas é verdadeira. Com base nestes princípios, a proposição pode ter o valor lógico verdadeiro ou falso.

A lógica proposicional é o estudo do relacionamento lógico entre objetos conhecidos como proposições. Para melhor entendimento do conteúdo da unidade, é muito importante entender o que é proposição.

Veja algumas definições:

- “Chama-se Proposição todo conjunto de palavras ou símbolos que exprimem um pensamento de sentido completo.”

- **ALENCAR FILHO, 2006**

- “Uma proposição, na definição clássica, é o encadeamento de termos ou palavras, através de uma cópula verbal ou não, que expressam o conteúdo de um juízo, como verdadeiro ou falso.”

- **KELLER; BASTOS, 2008**

A linguagem natural (português, inglês, espanhol, etc.) é formada por um conjunto de caracteres que, devidamente combinados, formam palavras. Estas, por sua vez, quando combinadas, formam enunciados, que podem ser frases ou orações ou conjuntos de frases e orações.

A frase é o elemento de comunicação que relaciona palavras entre si de modo a estabelecer uma mensagem com sentido completo. As frases podem ser de vários tipos:

**Declarativa:** “O Sol é uma estrela.”;

**Imperativa:** “Não faça isto!”;

**Interrogativa:** “Onde você mora?”;

**Exclamativa:** “Parabéns!”.

Observe que nem todos os tipos de frases são claros e objetivos e um dos objetivos da lógica é estabelecer uma linguagem formal, através da qual se pode expressar com clareza, precisão e emitir juízo de verdadeiro (V) ou falso (F) para determinadas frases.

Portanto, proposição é uma frase declarativa (com sujeito e predicado), à qual pode ser atribuído, sem ambiguidade, um dos valores lógicos: verdadeiro (V) ou falso (F).

Para que você entenda o conceito de proposição, apresentamos a seguir exemplos de proposições:

Uberaba fica em Minas Gerais;

Marina é médica; 3 + 4 = 7;

Já não são proposições:

4 + 9 (Não tem predicado);

Qual a marca do carro da Maria? (Sentença interrogativa);

Que festa boa! (Sentença exclamativa).

As proposições podem ser simples ou compostas. As proposições simples ou atômicas são aquelas que não possuem nenhuma outra proposição como parte integrante de si mesma. São geralmente indicadas pelas letras minúsculas **p** , **q** , **r** , **s** , ... A seguir exemplos de proposições simples:

**p:** Carlos é careca;

**q:** Pedro é estudante;

**r:** O número 25 é quadrado perfeito.

Já as proposições compostas são aquelas formadas pela combinação de duas ou mais proposições e são simbolizadas pelas letras latinas maiúsculas **P** , **Q** , **R** , **S** , ... Por exemplo:

**P:** Carlos é careca **e** Pedro é estudante;

**Q:** Carlos é careca **ou** Pedro é estudante;

**R:** Se Carlos é careca, **então** é infeliz.

Observe que as proposições compostas utilizam conectivos para combinar duas ou mais proposições, para que você entenda a lógica de cada conectivo; primeiro é necessário a explicação e entendimento sobre tabela-verdade.

Tabela verdade é uma maneira prática de dispor organizadamente os valores envolvidos em uma proposição composta. Para a proposição simples **p** , temos os valores lógicos possíveis, conforme a figura abaixo:

![[lc1-01-fig03.webp]]

**Figura 2 – Diagrama de árvore e tabela verdade de uma proposição simples**

Considerando uma proposição composta com duas proposições simples, temos a Figura 3 representando o diagrama de árvore e a tabela verdade correspondente:

![[lc1-01-fig04.webp]]

**Figura 3 – Diagrama de árvore e tabela verdade de uma proposição composta**

Observe que o número de linhas de uma tabela verdade depende da quantidade de proposições simples distintas que compõe a proposição. Assim, o número de linhas de uma tabela verdade é dado por 2<sup>n</sup> , em que n é a quantidade de proposições simples distintas e 2 representa o número de valores lógicos possíveis (V ou F).

Assim, para **4** proposições simples teremos

#### Conectivos Lógicos

Os conectivos lógicos, também conhecidos como operadores lógicos, são palavras ou expressões que se usa para formar novas proposições a partir de outras proposições. Os conectivos lógicos e os respectivos símbolos adotados nesta unidade são apresentados no Quadro a seguir:

**Quadro 1 – Conectivos e os respectivos símbolos**

|**Conectivo**|**Símbolo**|
|---|---|
|Negação (não)|~|
|Conjunção (e)|^|
|Disjunção (ou)|v|
|Condicional (se... então)|→|
|Bicondicional (... se e somente se...)|↔|

### Saiba Mais

**Não há um padrão de simbologia utilizado pelos autores para representar os conectivos. Os apresentados no Quadro 1 são os adotados com frequência nos livros de lógica computacional.**

Para que vocês entendam a lógica dos conectivos lógicos, iremos apresentar para cada um a proposição composta na forma de texto e a sua representação simbólica correspondente e a tabela verdade para melhor detalhamento sobre cada operador.

##### Operações Lógicas sobre Proposições

#### Negação (não, ~)

Se p é uma proposição, a negação da proposição p é denotada por ~p (lê-se não p). Nos exemplos a seguir, V(p) indica o valor lógico da proposição p e V(q) indica o valor lógico da proposição q.

Se V(p) = V, então  V(~ p) = F;

Logo, a negação de uma proposição apresenta valor lógico oposto ao da proposição dada, conforme podemos observar na tabela verdade a seguir:

###### Tabela 1

|**p**|**~p**|
|---|---|
|V|F|
|F|V|

Exemplos:

**q:** Rio de Janeiro é um país.

A sua negação é:

**~q:** Rio de Janeiro **não** é um país.

Na forma simbólica temos:

```
V(q) = F;
```

V(~q) = V.

#### Conjunção (e, ^)

A conjunção de duas proposições (p ^ q)  é verdadeira se, e somente se, cada proposição for verdadeira e falsa nos demais casos. Conforme apresentado na tabela verdade abaixo:

**Tabela 2**

|**p**|**q**|**p ^ q**|
|---|---|---|
|V|V|V|
|V|F|F|
|F|V|F|

**p q p ^ q** F F F

Considere as seguintes proposições simples:

![[lc1-01-fig05.webp]]

*Disjunção (ou, v)*

O valor lógico é a falso quando **p** e **q** são ambas falsas e verdadeiras nos demais casos. A tabela verdade da disjunção é:

**Tabela 3**

|**p**|**q**|**p v q**|
|---|---|---|
|V|V|V|
|V|F|V|
|F|V|V|
|F|F|F|

Considere as seguintes proposições simples:

**p:** 3 < 3.1415; **q:** 2 não é número primo. A disjunção é: **p v q:** 3 < 3.1415 ou 2 não é número primo; V(p v  q) = V(p) v  V(q) = V v F = V.

### Importante!

**Na linguagem natural, o conectivo pode traduzir tanto a ideia de hipóteses mutuamente exclusivas (ocorre isto ou ocorre aquilo) quanto a de que pelo menos uma das hipóteses ocorre.**

#### Condicional (se... então..., →)

Chama-se proposição condicional uma proposição representada por " **se p então q** ", cujo valor lógico é falso no caso em que p é verdadeira e q é falsa e verdade nos demais casos.

Outras maneiras de se ler o condicional p → q:

q, se p;

p é condição suficiente para q;

q é condição necessária para p.

Vamos considerar a proposição condicional “Se chove, então a rua fica molhada”, também pode ser lida das seguintes formas:

Chover é uma condição suficiente para a rua ficar molhada;

A rua ficar molhada é uma condição necessária quando chove.

No condicional p → q, a proposição p é chamada antecedente e a proposição q é consequente. Veja a lógica do conectivo na tabela verdade abaixo:

**Tabela 4**

|**p**|**q**|**p → q**|
|---|---|---|
|V|V|V|
|V|F|F|
|F|V|F|
|F|F|V|

Dadas as proposições simples:

**p:** Chove;

**q:** Faz frio.

A condicional é:

**p → q: Se** chove, **então** faz frio.

##### Bicondicional (... se e somente se ..., ↔)

Chama-se proposição bicondicional uma proposição representada por " **p se e somente se q** ", cujo valor lógico é a verdade quando p e q são ambas verdadeiras ou ambas falsas, e falso nos demais casos. Outras maneiras de se ler o bicondicional p **↔** q:

- **p** é condição necessária e suficiente para **q** ;

**q** é condição necessária e suficiente para **p** .

**Tabela 5**

|**p**|**q**|**p ↔ q**|
|---|---|---|
|V|V|V|
|V|F|F|
|F|V|F|
|F|F|V|

Para que você entenda, considere o seguinte exemplo:

**p:** 2 é um número irracional;

**q:** A terra é plana.

A bicondicional é:

**p ↔ q :** 2 é um número irracional se e somente se a terra é plana;

V(p **↔** q)= V(p) **↔** V(q) = F **↔** F = V.

##### Precedência dos Conectivos Lógicos

Quando há uma proposição composta por vários conectivos sem parênteses, a ordem das operações segue a Tabela abaixo:

**Tabela 6**

|**Ordem**|**Conectivo**|
|---|---|
|1|~|
|2|^, v|
|3|→|
|4|**↔**|

A ordem de precedência entre os conectivos permite identificar a forma da proposição composta. Por exemplo:

p → q **↔** r é do tipo bicondicional, pois o último conectivo resolvido é **↔** ;

- p v ~q → q ^ r é do tipo condicional. Observe que o último conectivo a ser resolvido é →;

p v (~q → q ^ r) é do tipo disjunção inclusiva. O último conectivo a ser resolvido é v.

#### Classificações da Proposições

As proposições também podem ser classificadas de acordo com o valor lógico gerado como resultado. Para o entendimento, apresentamos a seguir as classificações.

##### Tautologia

Uma proposição composta é uma tautologia quando o seu valor é sempre a verdade ( **V** ), para quaisquer valores lógicos das proposições simples componentes. Considere o exemplo:

**P:** É noite ou não é noite.

Representada em forma de símbolos, temos:

**P:** p v ~p.

A tabela verdade correspondente:

**Tabela 7**

|**p**|**~p**|**p v ~p**|
|---|---|---|
|V|F|V|
|F|V|V|

Logo **p v ~p** é uma **tautologia** .

##### Contradição

Uma proposição composta é uma contradição quando o seu valor é sempre a falso ( **F** ), para quaisquer valores lógicos das proposições simples componentes.

**P:** É noite e não é noite.

Representada em forma de símbolos, temos:

**P:** p ^ ~p.

A tabela verdade correspondente:

**Tabela 7**

|**p**|**~p**|**p ^ ~p**|
|---|---|---|
|V|F|F|
|F|V|F|

Logo **p ^ ~p** é uma **contradição** .

##### Indeterminação ou Contingência

Uma proposição composta é indeterminada (ou contingente) quando **não** é uma tautologia e **não** é uma contradição.

As contingências são também denominadas proposições contingentes ou proposições indeterminadas. Vejam o exemplo a seguir:

**P:** Se é sábado então não é sábado.

Representada em forma de símbolos, temos:

**P:** p → ~p.

A tabela verdade correspondente:

||**Tabela 7**||
|---|---|---|
|**p**|**~p**|**p → ~p**|
|V|F|F|
|F|V|V|

Logo **P:** p → ~p é uma **indeterminação** .

Agora que já entendemos os conceitos básicos de lógica, vamos avançar com conteúdo. Nosso próximo passo será conhecer sobre implicações, equivalências lógicas e álgebra das proposições.
