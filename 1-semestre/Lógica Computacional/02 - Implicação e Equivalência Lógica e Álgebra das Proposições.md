---
materia: "Lógica Computacional"
modulo: "Implicação e Equivalência Lógica e Álgebra das Proposições"
semestre: 1
unidade: 2
tipo: material-teorico
fonte: "raw/1-semestre/LÓGICA COMPUTACIONAL/Lógica Computacional 02.pdf"
tags: [faculdade, logica-computacional, semestre-1]
aliases: ["Lógica Computacional - Unidade 2"]
---

# Implicação e Equivalência Lógica e Álgebra das Proposições

Como já é de amplo conhecimento, a lógica computacional é a base da computação,de modo que utilizamos os seus conceitos em atividades do dia a dia e para resolver problemas. Já a álgebra das proposições é um dos tópicos da lógica mais relevantes para a computação, pois é a base para o projeto de circuitos digitais, ou seja, de portas lógicas e álgebra de Boole.

Assim, para o entendimento do conteúdo, o estudo das relações de implicação e de equivalência, de grande importância na lógica, será realizado de maneira sucinta, como convém ao nosso estudo. Antes, porém, definiremos alguns conceitos introdutórios.

Portanto, nesta Unidade veremos a implicação e equivalência lógica e os conectivos utilizados, os quais serão importantes para aplicarmos a álgebra das proposições utilizando as principais hipóteses lógicas equivalentes, adotadas principalmente para a simplificação e manipulação de expressões lógicas com vistas à prova da validade de argumentos.

Por diversos algoritmos de manipulação de proposições da lógica proposicional assumirem que tais proposições são apresentadas em um formato predefinido, chamado de forma normal, veremos as formas normais conjuntiva e disjuntiva.

Bom estudo!

#### Implicação Lógica e Equivalência Lógica

Entre os tópicos abordados nesta Unidade, iniciaremos com o estudo da relação entre as proposições compostas, com dois relacionamentos: implicação lógica e equivalência lógica.

###### Implicação Lógica

De acordo com a definição, dadas as proposições compostas **P** e **Q** , diz-se que ocorre implicação lógica – ou relação de implicação – entre **P** e **_Q_** quando a proposição condicional **P** → **Q** é uma tautologia.

**Notação:** P ⇒ Q.

### Importante!

**Os símbolos** ⇒ **e → têm significados diferentes:** ⇒ **entre duas proposições dadas indica uma relação, isto é, que a proposição condicional associada é uma tautologia; enquanto→ realiza uma operação entre proposições, dando origem a uma nova proposição p → q (que pode conter valores lógicos V ou F).**

Para que você melhor entenda, veja o exemplo a seguir, cujo objetivo é mostrar a seguinte relação: (p ∧ q) ⇒ (p ↔ q) – observe que temos duas proposições compostas:

P(p, q) = p ∧ q Q(p, q) = p ↔ q

Para isso, devemos construir a tabela-verdade das proposições **P** e **Q** – para facilitar, faremos tudo na mesma tabela – e aplicar o operador → entre as quais (P ⇒ Q), caso a tabela gerada seja uma tautologia, determinando que existe implicação lógica entre as proposições.

**Tabela 1**

![[lc1-02-fig01.webp]]

Como P → Q é uma tautologia, então, (p ∧ q) ⇒ (p ↔ q), isto é, ocorre a implicação lógica entre **P** e **Q** .

Algumas implicações lógicas também são conhecidas com regras de inferência ou de derivação; pois da verdade da proposição antecedente podemos concluir a verdade da proposição consequente.

Sempre que o antecedente é verdadeiro, obtemos o consequente verdadeiro, isto é, nunca ocorre a implicação falsa, pois teria de acontecer, na tabela-verdade, pelo menos uma linha em que o antecedente fosse verdadeiro e o consequente, falso. Na seguinte Tabela apresentamos algumas implicações lógicas notáveis:

**Tabela 2**

|**Denominação**|**Implicações lógicas**|
|---|---|
|_Modus ponens_, ou método de<br>afirmação|P∧(P → Q)⇒Q|
|_Modus tollen_, método da<br>negação, ou Lei do absurdo|~Q∧(P → Q)⇒~P|
|Silogismo hipotético|(P → Q)∧(Q → R)⇒(P → R)|
|Silogismo disjuntivo|(P∨Q)∧~P⇒Q|
|Dilema construtivo|(P → Q)∧(R → S)∧(P∨R)⇒(Q∨S)|
|Dilema destrutivo|(P → Q)∧(R⇒S)∧(~Q∨~S) → (~P∨<br>~R)|
|Simplificação conjuntiva|(P∧Q)⇒P|
|Simplificação disjuntiva, ou<br>adição|P⇒(P∨Q)|

Elabore a tabela-verdade de cada uma das implicações lógicas apresentadas na Tabela 2 e verifique que todas são tautológicas.

###### Equivalência Lógica

Conforme a definição, dadas as proposições compostas **P** e **Q** , diz-se que ocorre uma equivalência lógica entre **P** e **Q** quando as tabelas-verdade geradas pelas proposições compostas **P** e **Q** forem idênticas, ou seja, quando a bicondicional **P ↔ Q** for uma tautologia.

**Notação:** P ⇔ Q – lê-se: **P é equivalente a Q** .

No exemplo a seguir o objetivo é verificar se as proposições **P** e **Q** são equivalentes; para tanto, considere:

P(p, q) = (p → q) ∧ (q → p) Q(p, q) = p ↔ q

Para isso, devemos construir a tabela-verdade das proposições **P** e **Q** – para facilitar, faremos tudo na mesma tabela – e aplicar o operador ↔ entre as quais (P ⇔ Q), caso a tabela gerada seja uma tautologia, o que determinará equivalência lógica entre as proposições.

![[lc1-02-fig02.webp]]

Assim, (p → q) ∧ (q → p) ↔ (p ↔ q) é uma tautologia, ou seja, as proposições **P** e **Q** são equivalentes, e conforme pode ser observado na tabela-verdade, as colunas **P** e **Q** são iguais.

O estudo desses dois tipos especiais de tautologia – implicação e equivalência lógica – é utilizado na prova por dedução natural.

#### Equivalências Notáveis e Álgebra das Proposições

De acordo com o conteúdo apresentado, duas proposições lógicas são equivalentes quando exprimem os mesmos resultados, ou seja, o papel que desempenham é o mesmo. A seguir veremos as equivalências lógicas notáveis, estas que são utilizadas na álgebra das proposições; ou seja, assim como na Matemática Básica, onde estudamos operações algébricas com números reais e complexos, na álgebra das proposições estudamos operações envolvendo proposições.

**Negação da Negação – Dupla Negação: ~(~p)** ⇔ **p**

**Tabela 4**

|**p**|**~p**|**~(~p)**|
|---|---|---|
|F|V|F|

|**p**|**~p**|**~(~p)**|
|---|---|---|
|V|F|V|

De acordo com essa tabela-verdade: ~(~p) ⇔ p.

Logo, a negação da negação – dupla negação – de uma proposição é logicamente equivalente à proposição.

### Importante!

**A lógica do cotidiano é diferente da lógica computacional, pois é comum em português ao afirmar sentenças como esta: Não, não vou ao cinema.**

**Onde se deseja representar um reforço de que não irá ao cinema – ou seja, reforço da negação. Contudo, na lógica computacional usar duas vezes a negação significa afirmar a sentença. Veja este exemplo:**

**p: Não tem ninguém aqui.**

**~p: Tem ninguém aqui. ~(~p): Tem alguém aqui.**

**Não tem ninguém aqui é logicamente equivalente a Tem alguém aqui.**

###### Leis de Morgan

A seguir veremos as duas equivalências notáveis que compõem as conhecidas **leis de Morgan** .

#### Negação da Conjunção

Analisaremos um exemplo para melhor entendimento da equivalência; para isso, considere as seguintes proposições:

**P(p, q) = ~(p** ∧ **q)** : Não é verdade que a comida é farta e saborosa é logicamente equivalente a:

- **Q(p, q) = ~p** ∨ **~q** : A comida não é farta ou não é saborosa.

- **Ou seja** : P ⇔ Q = ~(p ∧ q) ⇔ ~p v ~q

Para confirmar a equivalência, considere a seguinte tabela-verdade das proposições compostas **P** e **Q** :

**Tabela 5**

![[lc1-02-fig03.webp]]

*Observe, na tabela-verdade, que: ~(p ∧ q) ⇔ ~p ∨ ~q*

Logo, a negação de uma conjunção (∧) é logicamente equivalente a disjunção das negações.

#### Negação da Disjunção

Considere o exemplo a seguir, com as proposições compostas **P** e **Q** :

**P(p,q) = ~(p** ∨ **q):** Não é verdade que 2 é número par ou 3 é número ímpar é logicamente equivalente a:

**Q(p,q) = ~p** ∧ **~q** : 2 não é número par e 3 não é número ímpar.

**Ou seja** : P ⇔ Q = ~(p ∨ q) ⇔ ~p ∧ ~q

Para verificar a equivalência negação da disjunção, observe esta tabela-verdade:

**Tabela 6**

![[lc1-02-fig04.webp]]

**Assim** : ~(p ∨ q) ⇔ ~p ∧ ~q

Logo, a negação de uma disjunção (∨) é logicamente equivalente a conjunção das negações.

A partir de então apresentaremos o nome e a equivalência lógica correspondente, ressaltando que as apresentadas anteriormente e as seguintes são aplicadas da maneira mais simples ao seu pleno entendimento; porém, a equivalência pode ser aplicada em proposições mais complexas, bastando ser mantida a lógica da equivalência.

### Leis Idempotentes

- 1) p ∨ p ⇔ p

- 2) p ∧ p ⇔ p

### Leis Comutativas

- 1) p ∧ q ⇔ q ∧ p

- 2) p ∨ q ⇔ q ∨ p

**Importante! Não existe a comutativa para o operador condicional (→).**

**Leis Associativas**

1) p ∨ (q ∨ r) ⇔ (p ∨ q) ∨ r

2) p ∧ (q ∧ r) ⇔ (p ∧ q) ∧ r

### Leis Distributivas

- 1) p ∧ (q ∨ r) ⇔ (p ∧ q) ∨ (p ∧ r)

2) p ∨ (q ∧ r) ⇔ (p ∨ q) ∧ (p ∨ r)

### Condicional

- 1) ~(p → q) ⇔ ~(~p ∨ q) ⇔ p ∧ ~q

2) p → q ⇔ ~q → ~p

- 3) p → q ⇔ ~(p ∧ ~q) ⇔ ~p ∨ q

### Bicondicional

1) p ↔ q ⇔ (p → q) ∧ (q → p)

2) p ↔ q ⇔ q ↔ p (comutativa)

3) ~(p ↔ q) ⇔ ~p ↔ q ⇔ p ↔ ~q Ou:

~(p ↔ q) ⇔ (p ∧ ~q) ∨ (~p ∧ q)

### Absorção

- 1) p ∧ (p ∨ q) ⇔ p

- 2) p ∨ (p ∧ q) ⇔ p

### Complementares ou Identidade

Considere **t** = tautologia e **c** = contradição:

- 1) p ∨ ~p ⇔ t

- 2) p ∧ ~p ⇔ c

- 3) ~t ⇔ c

- 4) ~c ⇔ t

- 5) p ∨ t ⇔ t

- 6) p ∧ c ⇔ c

- 7) p ∧ t ⇔ p

- 8) p ∨ c ⇔ p

### Vídeos

**Equivalências Lógicas – Raciocínio Lógico**

Para melhor entendimento da aplicabilidade das equivalências lógicas notáveis apresentadas, demonstraremos a relação entre as proposições compostas **P** e **Q** utilizando álgebra das proposições; para isso utilizaremos o método dedutivo, considerando as seguintes proposições:

P(p, q, r) = (p → q) ∨ (p → r)

Q(p, q, r) = p → q ∨ r

Objetivo: demonstrar que **P** ⇔ **Q** . Para tanto, aplicaremos as equivalências lógicas notáveis em **P** , as quais indicadas em cada linha, até mostrar a equivalência à **Q** :

|(p → q)∨(p → r)|Condicional|
|---|---|
|~p∨q∨~p∨r|Comutativa|

|~p∨~p∨q∨r|Idempotente|
|---|---|
|~p∨q∨r|Associativa|
|~p∨(q∨r)|Condicional|
|p → q∨r||

Podemos observar que a proposição resultante é **Q** e é mais simples, pois a quantidade de conectivos lógicos é menor, sendo equivalente à proposição **P** , ou seja, **P** ⇔ **Q** .

Veremos outro exemplo para reforçar o conteúdo, cujo objetivo é demonstrar a relação **R** ⇔ **S** entre as proposições compostas **R** e **S** ; assim:

R(p, q) = ~(p ∨ q) ∨ (~p ∧ q) S(p) = ~p

Para isso, aplicaremos as equivalências lógicas notáveis em **R** , indicadas em cada linha, até mostrar a equivalência à **S** :

|~(p∨q)∨(~p∧q)|Leis de Morgan|
|---|---|
|(~p∧~q)∨(~p∧q)|Distributiva|
|~p∧(~q v q)|Complementares|
|~p∧t|Complementares|

Podemos observar que a proposição resultante é **S** , portanto: **R** ⇔ **S** .

#### Forma Normal

Para facilitar os mecanismos de dedução, torna-se necessário, em alguns casos, transformar determinada proposição de uma forma para outra, especialmente à normal. Isto se deve ao fato de alguns sistemas automáticos de dedução utilizar em apenas essas formas para trabalharem.

Diz-se que uma proposição está na Forma Normal (FN) somente se contém apenas os conectivos ~, ∧ e ∨.

As proposições a seguir estão na FN:

$$\sim p \land \sim q$$

$$\sim(\sim p \lor \sim q)$$

$$(p \land q) \lor (\sim q \lor r)$$

Já as proposições lógicas compostas mostradas a seguir não estão na forma normal:

$$\sim p \rightarrow q$$

$$a \lor b \rightarrow q$$

$$a \leftrightarrow b$$

Toda proposição pode ser levada para uma FN equivalente, eliminando os conectivos → e ↔, se existirem. Para isto, basta utilizar as equivalências a seguir:

p → q ⇔ ~p ∨ q

E:

p ↔ q ⇔ (~p ∨ q) ∧ (p ∨ ~q)

Nesta Unidade estudaremos duas FN:

![[lc1-02-fig07.webp]]

**Figura 1 – Formas normais**

Tais como os nomes sugerem, FNC e FND priorizam o alcance dos conectores de conjunção (∧ na FNC), ou disjunção (∨ na FND).

###### Forma Normal Conjuntiva (FNC)

Uma proposição está na FNC se todas as seguintes afirmações forem verdadeiras:

Contém, quando muito, os conectivos ~, ∧ e ∨;

O conectivo ~ não aparece repetido (como ~~), nem tem alcance sobre operações ∨ ou ∧; por exemplo, um termo como ~(p ∧ q) não seria permitido. Ou seja, a negação (~) só é permitida sobre uma proposição simples;

Uma conjunção ∧ pode ter alcance sobre uma disjunção ∨, mas o contrário não seria permitido; por exemplo, p ∧ (q ∨ r) seria permitido, mas uma proposição como p ∨ (q ∧ r) não seria aceita na FNC.

Vejamos as seguintes proposições na FNC:

- ~ p ∧ ~ q

- ~p ∧ q ∧ r

- (~p ∨ q) ∧ (~q ∨ ~r)

Para qualquer proposição pode-se determinar a FNC realizando as seguintes transformações:

T1) Eliminam-se os conectivos → e ↔ utilizando estas equivalências:

p → q ⇔ ~p v q

E:

p ↔ q ⇔ (~p ∨ q) ∧ (p ∨ ~q)

T2) Eliminam-se as negações repetidas e parênteses precedidos de ~ pelas equivalências da dupla negação e leis de Morgan.

T3) O alcance do operador de disjunção (∨) sobre o resultado da conjunção(∧) é eliminado pela equivalência das leis distributivas:

p ∨ (q ∧ r) ⇔ (p ∨ q) ∧ (p ∨ r) E:

(p ∧ q) ∨ r ⇔ (p ∨ r) ∧ (q ∨ r)

Para melhor entendimento, veja o seguinte exemplo, no qual cada equivalência aplicada é indicada em uma linha:

**Determinar a FNC da proposição** : ~(((p ∨ q) ∧ ~q) ∨ (q ∧ r))

|~(((p∨q)∧~q)∨(q∧r))|Leis de Morgan|
|---|---|
|~((p∨q)∧~q)∧~(q∧r)|Leis de Morgan|
|(~(p∨q)∨~(~q))∧(~q∨~r)|Dupla negação e Leis de Morgan|
|((~p∧~q)∨q)∧(~q∨~r)|Lei distributiva|
|((~p∨q)∧(~q∨q))∧(~q∨~r)|Complementares|
|(~p∨q)∧(~q∨~r)|Está na FNC|

###### Forma Normal Disjuntiva (FND)

Consideraremos que uma proposição lógica está na FND se e somente se as condições forem verdadeiras, vejamos:

Contém, quando muito, os conectivos ∨, ∧ e ~;

O conectivo ~ não aparece repetido (como ~~), nem tem alcance sobre operações ∨ ou ∧; por exemplo, um termo como ~(p ∧ q) não seria permitido. Ou seja, uma ~ opera apenas sobre uma proposição simples;

Uma disjunção ∨ pode ter alcance sobre uma conjunção ∧, mas o contrário não seria permitido; por exemplo, p ∨ (q ∧ r) seria permitido, mas uma proposição como p ∧ (q ∨ r) não seria aceita na FND.

Assim como na FNC, qualquer proposição que não esteja na FND pode permanecer, cabendo aplicar as transformações indicadas a seguir:

T1) Eliminam-se os conectivos → e ↔ utilizando as seguintes equivalências:

p → q ⇔ ~p v q E:

p ↔ q ⇔ (~p ∨ q) ∧ (p ∨ ~q)

T2) Eliminam-se as negações repetidas e parênteses precedidos de ~ pelas equivalências da dupla negação e leis de Morgan.

T3) O alcance do operador de conjunção (∧) sobre o resultado da disjunção(∨) é eliminado pela equivalência das leis distributivas:

p ∧ (q ∨ r) ⇔ (p ∧ q) ∨ (p ∧ r)

E:

(p ∨ q) ∧ r ⇔ (p ∧ r) ∨ (q ∧ r)

Para melhor entendimento, veja o seguinte exemplo, no qual cada equivalência aplicada é indicada em uma linha:

**Determinar a FND da proposição** : (p → q) ∧ (q → p)

|(p → q)∧(q → p)|Condicional|
|---|---|
|(~p∨q)∧(~q∨p)|Leis distributivas|
|(~p∧(~q∨p))∨(q∧(~q∨p))|Leis distributivas|
|(~p∧~q)∨(~p∧p)∨(q∧~q)∨(q<br>∧p)|Complementares|
|(~p∧~q)∨c∨c∨(q∧p)|Complementares|
|(~p∧~q)∨(q∧p)|Está na FND|

Já no caso a seguir temos a classificação em FN, FNC, FND ou nenhuma das formas:

|a∧(b∨c)|FN e FNC|
|---|---|
|a∧(b∨~~c)|FN|
|(p → q)∧(q → p)|Nenhuma das formas|
|~(p∧~q)|FN|
|~p∨~~q|FN|
|a∧(b∨c∨d)|FN e FNC|

|a ↔ b|Nenhuma das formas|
|---|---|
|a∨(b∧c)|FN e FND|
|a∧b|FN, FNC e FND|

Observe que nas formas normais não estamos interessados em simplificar as proposições compostas, mas sim determinar a sua forma normal conjuntiva ou disjuntiva.
