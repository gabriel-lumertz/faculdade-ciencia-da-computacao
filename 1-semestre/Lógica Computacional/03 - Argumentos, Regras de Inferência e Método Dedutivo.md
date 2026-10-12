---
materia: "Lógica Computacional"
modulo: "Argumentos, Regras de Inferência e Método Dedutivo"
semestre: 1
unidade: 3
tipo: material-teorico
fonte: "raw/1-semestre/LÓGICA COMPUTACIONAL/Lógica Computacional 03.pdf"
tags: [faculdade, logica-computacional, semestre-1]
aliases: ["Lógica Computacional - Unidade 3"]
---

# Argumentos, Regras de Inferência e Método Dedutivo

#### Argumentos (Símbolo |--- Ⱶ )

Segundo Alencar Filho (2006), “[...] chama-se argumento toda a afirmação de que uma dada sequência finita P1, P2..., Pn de proposições lógicas tem como consequência ou acarreta uma proposição final Q”.

Que poderá ser lido ou interpretado de algumas maneiras, tais como:

P1, P2, P3..., Pn **acarretam** Q;

Q **se deduz de** P1, P2, P3..., Pn;

Q **se infere de** P1, P2, P3..., Pn.

### Saiba Mais

**Um argumento está composto por uma sequência finita de proposições lógicas (premissas) e uma proposição final (conclusão).**

Encontraremos o conceito de argumento em diferentes fontes: livros, _sites_ , dicionários, em alguns casos com definições mais simples ou diretas. O exemplo clássico, encontrado frequentemente, mostra uma argumentação para chegar à conclusão da mortalidade de um homem específico – Sócrates. Em **Lógica – argumento – um conjunto de enunciados articulados entre si** .

### Leitura

**Lógica - Argumento - Um Conjunto de Enunciados Articulados Entre Si O autor Heidi Strecker apresenta uma definição informal de argumento.**

**ACESSE**

A noção de argumento é fundamental para a lógica. Argumento é um conjunto de enunciados que estão relacionados uns com os outros. Argumento é um raciocínio lógico. Observe o seguinte argumento:

Todos os homens são mortais;

Sócrates é homem;

Logo, Sócrates é mortal.

Este é um argumento formado por duas premissas e uma conclusão. Os dois primeiros enunciados são as premissas e o último enunciado é a conclusão. Os fatos apresentados nas premissas servem de evidência para a conclusão, isto é, são eles que sustentam a conclusão.

### Validade de um Argumento – Definição

Um argumento P1, P2, P3..., Pn Ⱶ Q será considerado válido se e somente se a conclusão Q for verdadeira todas as vezes que as premissas P1, P2, P3..., Pn forem verdadeiras (ALENCAR FILHO, 2006).

### Glossário

**Sofisma: Na língua portuguesa informal, a palavra sofisma poderia ser utilizada como sinônimo de mentira, enganação, enquanto sofistas**

### Critério de Validade de um Argumento – Teorema

Existe uma forma simples para determinar se um argumento é válido ou não, que consiste em verificar se a condicional correspondente para o argumento é uma tautologia ou não – se for uma tautologia, tal argumento será válido.

Por exemplo, um argumento P1, P2, P3..., Pn Ⱶ Q é válido se e somente se a condicional associada a este argumento:

$$(P1 \land P2 \land P3 \land \ldots \land Pn) \rightarrow Q$$

For tautológica, ou seja, se esta condicional for uma tautologia.

**Glossário Argumentação: uma afirmação (argumento) composta por proposições lógicas separadas em premissas e conclusão, sendo que a conclusão será verdadeira todas as vezes que as premissas são verdadeiras.**

### Comparando Implicação Lógica e Argumento Válido

São conceitos com certa semelhança e poderiam ser confundidos, de modo que os analisaremos detalhadamente.

**Implicação lógica:**

$$P(p,q,r) \Rightarrow Q(p,q,r)$$

Ou P (p,q,r) implica a proposição Q (p,q,r) se a condicional P (p,q,r) → Q (p,q,r) for uma tautologia.

Observe que _P_ e _Q_ são proposições lógicas simples ou compostas quaisquer.

###### Argumentação:

Um argumento P1, P2, P3..., Pn Ⱶ Q é válido se a condicional associada a esse argumento – conjunções das premissas e condicional com a conclusão _Q_ :

(P1 ∧ P2 ∧ P3 ∧ ... ∧ Pn) → Q for tautológica.

Observe a conjunção de P1, P2, P3... (proposições lógicas compostas quaisquer).

###### Argumentos Válidos Fundamentais

São argumentos que nem precisariam de demonstração, dado que são verdadeiros, de modo que podemos confiar em sua validade. São, basicamente, dez argumentos – mostrados a seguir:

###### Tabela 1 – Argumentos válidos fundamentais

|**I. Adição (AD):**<br>(I)   pͰp∨q<br>(II) pͰq∨p|**VI.****_Modus Tollens_ (MT):**<br>p → q , ~qͰ~p|
|---|---|
|**II. Simplificação:**|**VII. Silogismo Disjunto (SD):**|
|(I) p∧qͰp|(I)  p∨q , ~pͰq|
|(II) p∧qͰq|(II) p∨q , ~qͰp|
|**III. Conjunção (CONJ):**<br>(I) p , qͰp∧q<br>(II) p , qͰq∧p|**VIII. Silogismo hipotético (SH):**<br>p → q , q → rͰp → r|
|**IV. Absorção (ABS):**<br>p → qͰp → (p∧q)|**IX. Dilema Destrutivo (DD):**<br>p → q , r → s , ~q∨~sͰ~p∨<br>~r|
|**V.****_Modus Ponens_(MP):**|**X. Dilema Construtivo (DC):**|
|p → q , pͰq|p → q , r → s , p∨rͰq∨s|

Em todos os argumentos válidos fundamentais aqui apresentados podemos demonstrar que as condicionais das conjunções das premissas Pi e a conclusão _Q_ são tautologias.

$$(P1 \land P2 \land P3 \land \ldots \land Pn) \rightarrow Q$$

A afirmação anterior será demonstrada neste **exemplo** :

Vejamos, construindo uma tabela-verdade, que a **regra do silogismo disjuntivo** – ou **disjunto** – é um argumento válido.

Sabemos que p ∨ q, ~p Ⱶ q será um argumento válido se a condicional associada (p ∨ q) ∧ ~p → q for uma tautologia. Observe, no Quadro 2, que todos os valores na última coluna são verdadeiros (V), ou seja, demonstramos que essa proposição lógica é uma tautologia.

###### Tabela 2 – Tabela-verdade da regra do silogismo disjuntivo

![[lc1-03-fig01.webp]]

*Argumentos em Forma de Regras de Inferência*

Os argumentos válidos fundamentais já mostrados são utilizados para fazer inferências – executar passos que permitam efetuar uma demonstração, deduzir.

Por esse motivo, os argumentos são chamados, também, de **regras de inferência** .

Existe uma forma padronizada de escrever os argumentos, separando com uma linha horizontal as premissas – sobre o traço horizontal – e a conclusão – sob tal traço. De forma geral, uma regra de inferência seria assim representada:

![[lc1-03-fig02.webp]]

Assim, veremos a seguir as regras de inferência que se correspondem aos argumentos válidos fundamentais já mostrados.

#### Regras de Inferência

Derivam-se e são equivalentes aos **argumentos válidos fundamentais** . São, basicamente, dez regras de inferência, mostradas no Quadro 3.

Em todas as regras de inferência aqui apresentadas podemos demonstrar que a condicional das conjunções das premissas P1, P2..., Pn e a conclusão _Q_ são tautologias:

$$(P1 \land P2 \land P3 \land \ldots \land Pn) \rightarrow Q$$

*Tabela 3 – Regras de inferência*

![[lc1-03-fig03.webp]]

Como exercício posterior, tente construir a tabela-verdade para algumas das regras de inferência, de modo a demonstrar que a condicional, na última coluna do Quadro, é uma tautologia.

###### Exemplos de Utilização das Regras de Inferência

As regras de inferência podem ser empregadas na dedução de conclusões a partir de premissas dadas.

Utilizando a **regra da simplificação para deduzir** outras proposições lógicas; vejamos três situações:

![[lc1-03-fig04.webp]]

No exemplo do centro podemos afirmar que a conclusão:

~q se deduz de p ∧ ~q (premissa); ou

~q se infere de p ∧ ~q; ou

$p \land \sim q$ acarreta $\sim q$.

**Exemplo 2:**

Utilizando a **regra da adição** podemos deduzir outras proposições lógicas mais complexas, ou com símbolos proposicionais diferentes dos utilizados na regra (ALENCAR FILHO, 2002); vejamos:

![[lc1-03-fig05.webp]]

###### Exemplo 3:

Utilizando as **regras** **_modus ponens_** e **_modus tollens_** para deduzir outras proposições lógicas, temos:

![[lc1-03-fig06.webp]]

Considerando s ∧ ~q (a conclusão do primeiro exemplo) infere-se das duas premissas anteriores (ou podemos dizer que as duas premissas anteriores acarretam s ∧ ~q).

###### Exemplo 4:

Utilizando a **regra do silogismo hipotético** para deduzir outras proposições lógicas, temos:

![[lc1-03-fig07.webp]]

No primeiro exemplo, temos que a conclusão ~p → ~s se infere ou deduz das premissas:

**~p → q** ∨ **r** e **q** ∨ **r → ~s**

### Saiba Mais

**Os quatro primeiros exemplos utilizados são do livro intitulado Iniciação à lógica matemática, de Alencar Filho (2002).**

**Exemplo 5:**

Neste caso utilizaremos diferentes regras de inferência para demonstrar determinado argumento. Dito de outra forma, devemos demonstrar a validade do seguinte argumento – observe as três premissas e a conclusão r deste argumento:

$$p \rightarrow (q \rightarrow r), p \rightarrow q, p \vdash r$$

Primeiro, numeramos as premissas para facilitar a demonstração:

**Premissa (C1):** p → (q → r);

**Premissa (C2):** p → q;

**Premissa (C3):** p.

Agora, utilizamos algumas regras de inferência, de:

(C1) e (C3) utilizando MP – _Modus Ponens_ –, conclui-se (C4) q → r;

(C4) e (C5) utilizando MP, conclui-se, finalmente, (C6) r.

Chegamos à conclusão de que o argumento é válido, pois no item (C6) foi estabelecido r. Observe que r é a conclusão do argumento p → (q → r), p → q, p  Ⱶ  r

###### Exercício Proposto:

Demonstrar a validade dos seguintes argumentos utilizando as regras de inferência e outras equivalências conhecidas:

1 2

~ p → q, q → r, ~r ∨ s, ~s Ⱶ p p → q, r → s, q ∨ s → t, ~t Ⱶ ~p ∧ ~r

#### Método Dedutivo

Antes do estudo do método dedutivo revisaremos os significados do substantivo **dedução** e do verbo **deduzir** :

### Glossário

**Dedução:** ato ou efeito de deduzir.

Inferência lógica de raciocínio; conclusão, ilação;

**Rubrica: filosofia, lógica** ;

Processo de raciocínio através do qual é possível, partindo de uma ou mais premissas aceitas como verdadeiras (p. ex., A é igual a B e B é igual a C), a obtenção de uma conclusão necessária e evidente (no ex. anterior, A é igual a C).

**Deduzir:** concluir (algo) pelo raciocínio; inferir.

O método dedutivo é utilizado para demonstrar implicações (⇒) e equivalências lógicas (⇔);

No método dedutivo, a utilização das equivalências lógicas – estudadas no tema Álgebra das proposições – possui papel fundamental – assim como os **argumentos válidos fundamentais** estudados;

O método dedutivo é uma forma de demonstração mais eficiente se comparado à construção de tabelas-verdade – esta que, como sabemos, é um processo demorado e com possibilidade de erro;

Nas seguintes demonstrações utilizaremos, também, aqueles dois teoremas que estabelecem uma equivalência, ou uma implicação lógica se a bicondicional – no caso da equivalência – e a condicional – no caso da implicação – correspondentes forem tautológicas.

Para relembrar, veja a seguir:

P(p,q,r) ⇒ Q(p,q,r).

P(p,q,r) implica a proposição Q(p,q,r) se e somente se a condicional P(p,q,r) → Q(p,q,r) for uma tautologia.

P(p,q,r) ⇔ Q(p,q,r).

P(p,q,r) é equivalente à proposição Q(p,q,r) se e somente se a bicondicional P(p,q,r) ↔ Q(p,q,r) for uma tautologia.

Vejamos o método dedutivo em casos práticos.

**Exemplo 1:**

Demonstrar a implicação lógica p ∧ q ⇒ p pelo método dedutivo.

Segundo o teorema anterior, tal implicação lógica será verdadeira se e somente se a condicional p ∧ q → p for uma tautologia – se pudermos demonstrar que o seu resultado é sempre verdadeiro (V); isto utilizando a:

Transformação da condicional:

$$p \land q \rightarrow p$$

$$\Leftrightarrow \sim(p \land q) \lor p$$

Regra de Morgan:

⇔ (~p ∨ ~q) ∨ p

$$\Leftrightarrow \sim p \lor \sim q \lor p \ (\textbf{associatividade})$$

⇔ ~p ∨ p ∨ ~q ( **comutatividade** )

⇔ V

Como chegamos na constante V, conseguimos demonstrar que a implicação lógica p ∧ q ⇒ p é verdadeira.

###### Exemplo 2:

Demonstrar a implicação lógica p ∧ q ⇒ p ∨ q pelo método dedutivo.

A implicação lógica anterior será verdadeira se e somente se a condicional p ∧ q → p ∨ q for uma tautologia – se pudermos demonstrar que o seu resultado será sempre V.

p ∧ q → p ∨ q → utilizando a transformação da condicional:

$$\Leftrightarrow \sim(p \land q) \lor (p \lor q)$$

Utilizando a Regra de Morgan:

⇔ (~p ∨ ~q) ∨ (p ∨ q)

⇔ (~p ∨ p) ∨ (~q ∨ q)

⇔ V ∨ V

⇔ V

Demonstramos que a implicação lógica inicial p ∧ q ⇒ p ∨ q é verdadeira.

**Exemplo 3:**

Demonstrar, pelo método dedutivo, esta equivalência lógica:

(p → r) ∧ (q → r) ⇔ p ∨ q → r

Peguemos somente a parte esquerda da equivalência:

(p → r) ∧ (q → r) ⇔ (~p ∨ r) ∧ (~q ∨ r) transformação da condicional ⇔ (~p ∧ ~q) ∨ r distributividade (inversa).

- ⇔ ~(p ∨ q) ∨ r Regra de Morgan (inversa).

- ⇔ p ∨ q → r transformação da condicional (inversa).

Substituindo na equivalência inicial: p ∨ q → r ⇔ p ∨ q → r

A bicondicional correspondente é: p ∨ q → r ↔ p ∨ q → r

Mas veja que a bicondicional anterior é uma tautologia.

Demonstramos que (p → r) ∧ (q → r) é equivalente a p ∨ q → r, ou seja, a equivalência cuja análise foi solicitada (p → r) ∧ (q → r) ⇔ p ∨ q → r foi demonstrada.

###### Exemplo 4:

Já vimos a implicação lógica p ∧ q ⇒ p ∨ q, no **Exemplo 2** , pelo método dedutivo.

Assim, demonstraremos esta mesma implicação lógica p ∧ q ⇒ p ∨ q construindo uma tabelaverdade. Observe que, se a condicional (→) equivalente desta implicação lógica for uma tautologia, teremos demonstrado a implicação lógica.

Consideremos este exemplo para sugerir que, possivelmente, a demonstração utilizando tabelas-verdade é um procedimento mais trabalhoso e com maior possibilidade de erro, se comparada ao método dedutivo, não é mesmo?

![[lc1-03-fig08.webp]]

Para construir a tabela-verdade anterior, lembre-se das tabelas-verdade da conjunção, da disjunção e condicional – conteúdos estes apresentados na primeira Unidade desta Disciplina.

Observe que a última coluna dessa tabela-verdade contém apenas valores verdadeiros (V), ou seja, p ∧ q → p ∨ q é uma tautologia, dado que demonstramos a implicação lógica p ∧ q ⇒ p ∨ q.
