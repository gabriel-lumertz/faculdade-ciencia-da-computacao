---
materia: "Lógica Computacional"
modulo: "Lógica de Predicados"
semestre: 1
unidade: 4
tipo: material-teorico
fonte: "raw/1-semestre/LÓGICA COMPUTACIONAL/Lógica Computacional 04.pdf"
tags: [faculdade, logica-computacional, semestre-1]
aliases: ["Lógica Computacional - Unidade 4"]
---

# Lógica de Predicados

#### Motivação: a Lógica Proposicional

A lógica proposicional, igualmente conhecida como lógica das proposições, ou ainda lógica simbólica, utiliza proposições – ou símbolos lógicos – e conectivos lógicos.

Vejamos algumas características da lógica proposicional.

Utiliza proposições interligadas por conectivos lógicos – operadores –, mostrados a seguir:

As proposições simples, ou símbolos proposicionais, comumente são letras minúsculas, tais como p, q, r, s, t, a, b, c, d;

Uma proposição lógica simples ou composta é uma afirmativa adequadamente formada, que terá um valor verdadeiro ou falso;

A lógica proposicional tem algumas limitações, que serão superadas na lógica de **predicados** , a saber: estabelecer características para determinados objetos e relacionamentos entre objetos.

### Glossário

**Predicados: permitem estabelecer relações entre objetos ou especificar características dos objetos.**

Assim, em lógica proposicional:

- **p:** Ana é uma mulher;

- **q:** Ana é alta;

- **r:** Ana tem 25 anos;

- **s:** Ana é irmã de Luiz;

Enquanto em lógica de predicados:

```
mulher(Ana, "alta", 25);
```

irmãos(Ana, Luiz).

As lógicas proposicional e de predicados não permitem ou consideram algum nível de certeza nas afirmações. Por exemplo, p: Ana é alta – em lógica proposicional – e alta(Ana) – em lógica de predicados – não fornecem o grau de certeza da afirmação. Logo, Ana poderia ter uma altura apenas um pouco acima da média das mulheres em determinado universo, ou Ana poderia ser consideravelmente alta – o que não fica claro nas proposições lógicas utilizadas como fatos.

###### Quadro 1 – Principais conectivos lógicos

![[lc1-04-fig01.webp]]

Vejamos descrições mais detalhadas dos principais conectivos empregados nas lógicas proposicional e de predicados:

- **Λ:** conjunção, operação E; por exemplo, p Λ q; por exemplo, ~q (não q);

- ∨ **:** disjunção, operação OU; por exemplo, p ∨ q;

- **~:** negação, operação NÃO, em alguns textos usa-se ¬;

- **→:** condicional; por exemplo, p → q, que significa **se p então q** ;

- **↔:** bicondicional; por exemplo, p ↔ q, que significa **p se e somente se q** ;

- **( ):** para agrupamento de termos (prioridade) e para especificar a lista de parâmetros de um predicado; **≤ < > ≥ = ≠:** operadores de relação (comparação);

Veja, a seguir, dois exemplos de proposições lógicas compostas em lógica proposicional:

a Λ (b ∨ c) → d;

(p ∨ ~q) ↔ a.

Perceba os símbolos proposicionais **a** , **b** , **c** , **d** , **p** , **q** e os conectivos ou operadores lógicos ~ Λ ∨ → ↔.

A Lógica de Primeira Ordem (LPO), ou lógica de predicados, igualmente conhecida como Cálculo de Predicados de Primeira Ordem (CPPO), ou simplesmente cálculo de predicados, é usualmente uma extensão da lógica proposicional.

As possibilidades da lógica de predicados são superiores às da lógica proposicional.

A lógica de predicados é também uma forma de armazenar conhecimento – dados e “regras” para raciocínio lógico ou inferência.

O elemento fundamental da lógica de predicados é o predicado. Podemos considerar o predicado como uma função, que poderá ter uma lista de parâmetros ou argumentos e que retornará um valor lógico – verdadeiro ou falso. Se comparado a funções/métodos de _Java_ , C++ e de outras linguagens de programação, ou com funções matemáticas, que podem retornar valores numéricos, textos etc., um predicado sempre retornará um valor lógico.

Em lógica de predicados podemos utilizar todos os conectivos lógicos – operadores – da lógica proposicional, mas também são permitidos os chamados quantificadores.

A quantificação é uma construção que especifica para quais indivíduos de um domínio de discurso se aplica uma proposição lógica. Os quantificadores ∀ e ∃ – universal e existencial – são utilizados para esse objetivo, onde:

- ∀ **x** significa **para todo o x** , **para qualquer x** , **qualquer que seja x** ; ou seja, exprime fatos sobre todos os objetos do universo;

- ∃ **x** significa **existe um x** , **existe algum x** , **existe pelo menos um x** ; ou seja, exprime fatos sobre objetos particulares.

∀ e ∃ são conhecidos como quantificadores universal e existencial, respectivamente.

A utilização de quantificadores permite melhor descrição da situação que necessitamos representar, isto é, são elementos que ajudam no sentido de melhor compreensão do problema.

#### Convenções Utilizadas para a Lógica de Predicados

Na bibliografia desta área podemos encontrar diferentes convenções para escrever proposições na lógica ou cálculo de predicados, isto é, para representar as constantes, variáveis e nomes de predicados – símbolos de predicados –, mudando um pouco de um autor para outro. Inclusive, deve-se observar as características específicas de linguagens de programação que utilizem como base teórica a lógica de predicados, por exemplo, as considerações obrigatórias em uma linguagem como _Prolog_ .

###### Quadro 2 – Convenções para o cálculo de predicados

###### Sintaxe do Cálculo de Predicados: Símbolos

**Os elementos básicos da sintaxe do cálculo de predicados são símbolos que se referem a objetos, relações e funções:**

- Símbolos para constantes, que se referem a objetos, como Aphrodite e Zeus;

- Símbolos para variáveis, que se referem a objetos ou conjunto de objetos, como x, y, z, ...;

- Símbolos para predicados, que se referem a relações entre objetos, como Irmão, Primo;

- Símbolos para funções, que se referem a funções de objetos, como Pai, Mãe.

*Fonte: Adaptado de SICHMAN; COSTA, s.d.*

Já em linguagem de programação como _Prolog_ , que utiliza como base a lógica ou o cálculo de predicados, a convenção é bem diferente (exemplo a seguir). Observe que as variáveis devem ser escritas com letra inicial maiúscula. As constantes simbólicas – pedro, ana, rosa, _java_ , _python_ , no exemplo – e os nomes de predicados – pessoa, caracteristica, conhece, candidatoVaga, _write_ , no seguinte exemplo – serão escritos com letra inicial minúscula.

Para utilizar uma ortografia correta, poderíamos considerar que a linguagem _Prolog_ permite, também, empregar constantes de tipo texto, _strings_ , escrevendo o texto entre aspas, vejamos:

```
característica("Ana", "responsável").
conhece("Pedro", "Java").
conhece("Pedro", "Python").
```

**Exemplo de programa na linguagem de programação** **_Prolog_ :**

```
pessoa(pedro).
pessoa(ana).
pessoa(rosa).
caracteristica(pedro, honesto).
caracteristica(pedro, responsavel).
caracteristica(ana, honesto).
caracteristica(rosa, responsavel).
conhece(pedro, java)
conhece(pedro, python)
conhece(ana, php)
conhece(rosa, vb6)
candidatoVaga(P) :- caracteristica(P,honesto),
caracteristica(P,responsavel), conhece(P,java),
conhece(P,vbnet).
?-write("Candidatos à vaga:"), candidatoVaga(pr), write(Pr).
```

###### Convenção Adotada nesta Unidade

Utilizaremos a convenção a seguir para escrever proposições na lógica de predicados:

**Nomes de predicados (símbolos):** utilizaremos letra inicial minúscula;

**Nomes de variáveis:** utilizaremos letra inicial minúscula;

**Constantes (como nomes de pessoas, cidades, países):** utilizaremos letra inicial maiúscula. Por exemplo:

```
capital(p,q)
capital(Espanha, Madri)
mulher(Ana)
```

Observe que os nomes próprios de pessoas, países e cidades – Espanha, Madri, Ana – foram escritos com letras iniciais maiúsculas, enquanto os nomes dos predicados **capital** e **mulher** foram escritos com letras iniciais minúsculas e as variáveis **p** , **q** foram escritas com letras minúsculas.

Veja também que o predicado **mulher** possui apenas um parâmetro, que é uma pessoa – Ana, no exemplo anterior. Neste caso, o predicado **mulher** estabelece uma característica ao argumento Ana – **Ana é uma mulher** .

Já o predicado **capital** possui dois parâmetros, ou argumentos, separados por uma vírgula. Esse predicado estabelece uma relação entre os seus dois argumentos. Por exemplo, **capital (Espanha, Madri)** estabelece que **Madri é a capital do país Espanha** .

Em princípio não existe limite para a quantidade de argumentos ou parâmetros de um predicado – outro exemplo, utilizaremos agora um predicado **capital** com três parâmetros:

```
capital(Brasil, Brasília, 2500000)
```

Que mostra que a capital do país Brasil é Brasília, que possui uma população de 2.500.000 habitantes.

Os exemplos anteriores permitem observar a superioridade da lógica/cálculo de predicados com relação à lógica proposicional, no sentido de nos permitir estabelecer propriedades para objetos individuais e relacionamentos entre esses objetos.

A lógica de predicados pode ser utilizada como base teórica ao projeto e à implementação de linguagens de programação dentro do **paradigma da programação lógica** .

A seguir veremos como seria uma possível representação do exemplo ( _Prolog_ ) utilizando a nossa convenção para a lógica de predicados:

```
pessoa(Pedro)
pessoa(Ana)
pessoa(Rosa)
caracteristica(Pedro, "honesto")
caracteristica(Pedro, "responsável")
caracteristica(Ana, "honesto")
caracteristica(Rosa, "responsável")
conhece(Pedro, Java)
conhece(Pedro, Python)
conhece(Ana, PHP)
∀p: caracteristica(p, "honesto") ^ caracteristica(p, "responsável") ^
conhece(p, Java) ^ conhece(p, Kotlin) → candidatoVaga(p)
```

Observe que nomes próprios como **Pedro** , **Ana** , **_Java_** e **_Python_** foram escritos com letra inicial maiúscula, enquanto constantes como **honesto** e **responsável** foram escritos como textos entre aspas e a variável **p** foi escrita com letra minúscula.

A proposição lógica da condicional → poderá ser lida como **qualquer que seja p, se p tiver como característica ser honesto, e p for responsável, e p conhece as linguagens de programação** **_Java_ e** **_Kotlin_ , então p será candidato à vaga** .

No próximo exemplo apresentamos mais um exemplo de lógica de predicados utilizando a convenção proposta nesta Unidade.

Fatos como nota(Ana, 5.5) utilizam dois argumentos ou parâmetros, sendo que o primeiro é o nome do aluno e o segundo é a sua nota. Este predicado – fato, neste caso – estabelece um relacionamento entre **Ana** e **5.5** , sinalizando que **Ana possui a pontuação 5.5 como nota** .

Por sua vez, **aprovado(x)** indica que a pessoa **x** está aprovada. Neste caso, o predicado **aprovado** atribui uma característica à pessoa **x** .

Ademais, utilizaremos três condicionais que nos permitem representar determinado raciocínio lógico, ou seja, partindo de condições chegaremos a uma determinada conclusão:

$$\forall \mathbf{x}\colon \forall \mathbf{n}\colon \text{nota}(x, n) \land n >= 7.0 \rightarrow \text{aprovado}(x);$$

∀ **x:** ∀ **n:** nota(x, n) ^ n < 7.0 → reprovado(x);

∃ **x:** aprovado(x).

A proposição lógica ∀ **x** : ∀ **n: nota(x, n) ^ n >= 7.0 → aprovado(x) pode ser lida como qualquer que seja x, qualquer que seja n, se o aluno x tem nota n, e essa nota n for maior ou igual que 7.0, então o aluno x está aprovado** .

Já a proposição lógica ∀ **x:** ∀ **n: nota(x, n) ^ n < 7.0 → reprovado(x) pode ser lida como qualquer que seja x, qualquer que seja n, se o aluno x tem nota n, e essa nota n for menor que 7.0, então o aluno x está reprovado** . Nas duas primeiras proposições lógicas utilizamos o quantificador universal ∀.

Por fim, a proposição lógica ∃ **x: aprovado(x)** poderia ser interpretada como **existe pelo menos um x, tal que esse aluno x está aprovado** . Aqui utilizamos o quantificador existencial ∃.

|**Exemplo de lógica de predicados utilizando a nossa convenção:**|
|---|
|Sejam:|
|nota(Júlio, 9.5)<br>nota(Ana, 5.5)<br>nota(Luiz, 7.0)<br>nota(Betty, 8.0)|
|∀**x:** ∀n: nota(x, n) ^ n >= 7.0 → aprovado(x);|
|∀**x:** ∀n: nota(x, n) ^ n < 7.0 → reprovado(x);|
|∃**x:**aprovado (x).|

Um livro onde encontraremos vários exemplos e exercícios sobre lógica de predicados é **Matemática discreta e suas aplicações** , de Kenneth Rosen (2010).Veja, o exemplo a seguir, um exercício proposto por este autor, que apresentamos com uma possível solução – observe que Rosen escreve os nomes dos predicados com letras iniciais maiúsculas (R e H, neste caso):

###### Exercício resolvido (Adaptado de ROSEN, 2010):

Transcreva estas proposições para o português, em que R(x) é “x é um coelho” e H(x) é “x salta” e o domínio são todos os animais.

∀x (R(x) → H(x))

Todo coelho salta. Qualquer que seja x, se x é um coelho, então ele salta;

∀x (R(x) ^ H(x))

Todos os animais são coelhos e saltam;

∃x (R(x) → H(x))

Existe um animal que se é o coelho então ele salta;

∃x (R(x) Λ H(x))

Existe pelo menos um coelho que salta.

Outros exemplos de lógica de predicados presentes no terceiro capítulo – **Lógica de Predicados de Primeira Ordem** – do livro intitulado **Lógica Aplicada à Computação** , de Newton José Vieira (s.d.), mostram a utilização de quantificadores, predicados e variáveis – observe que neste caso o autor utiliza nomes de predicados com letra inicial minúscula:

**Exemplo de lógica de predicados:**

```
∃x tia(x,Ana) (Ana tem uma tia);
```

∀x∃y gosta(x,y) (Todo mundo gosta de alguém);

- ∃x∀y gosta(x,y) (Alguém gosta de todo mundo);

- ∀x∀y (irmãos(x,y) → irmãos(y,x)) (Se Fulano e Beltrano são irmãos, então Beltrano e Fulano são irmãos);

- ∀x∀y (gosta(x, mãe(y)) → gosta(y,x)) (Todos gostam de quem gosta de sua mãe); ∀x(∃y ama(x,Y) → ∀zama(z,x)) (Todos amam quem ama alguém).

Para finalizar, veremos alguns exemplos completos, detalhadamente comentados, utilizando a lógica de predicados com a convenção desta Unidade.

###### Exemplo 1

Neste primeiro caso utilizaremos o predicado progenitor, que possui dois parâmetros: o primeiro é o nome do(a) progenitor(a) e o segundo argumento é o nome do(a) filho(a).

progenitor (Ana, Pedro) Ana é progenitora do Pedro progenitor (Pedro, Rosa) Pedro é progenitor da Rosa progenitor (Luiz, Leila) Luiz é progenitor da Leila progenitor (Carlos, Heitor)

|homem (Pedro)|Pedro é homem|
|---|---|
|homem(Luiz)|Luiz é homem|
|mulher(Ana)|Ana é mulher|
|mulher(Rosa)|Rosa é mulher|

###### ∀x: ∀y: progenitor(x,y) ^ mulher (x) → mãe(x,y).

A proposição lógica anterior tem este significado em português: **para todo x, para todo y, SE x for progenitor de y E x for mulher, ENTÃO x é mãe de y** .

###### ∀x: ∀y: progenitor(x,y) ^ homem (x) → pai(x,y).

A proposição lógica anterior teria este significado em português: **qualquer que seja x, qualquer que seja y, SE x for progenitor de y E x for homem, ENTÃO x é pai de y** .

###### Exemplo 2

Outras proposições lógicas mais complexas poderiam ser elaboradas como continuação do exemplo anterior. Veja a seguir proposições que definem avô, irmãos, primos e tio. Tente fazer uma figura para cada definição, o que lhe permitirá melhor analisar o relacionamento definido:

∀x: ∀y: ∀z: progenitor(x,y) ^ progenitor(y,z) ^ homem (x) → avô(x,z);

- ∀x: ∀y: ∀z: progenitor(x,y) ^ progenitor(x,z) → irmaos(y,z);

- ∀x: ∀y: ∀a: ∀b: progenitor(x,y) ^ progenitor(a,b) ^ irmaos(x,a) → primos(y,b);

- ∀x: ∀a: ∀b: progenitor(a,b) ^ irmaos(a,x) → tio(x,b).

Analisemos a penúltima proposição lógica, que utiliza os predicados **progenitor** , **irmaos** e **primos** . Estamos definindo aqui quando uma pessoa **y** e outra **b** são primos. A leitura dessa proposição lógica poderia ser: **para todo x, para todo y, para todo a, para todo b, SE x é progenitor de y E a é progenitor de b, ENTÃO y e b são primos** .

###### Exemplo 3

Com fatos – axiomas – com a seguinte estrutura:

```
populacao(nome da cidade, população da cidade)
capital (nome do país, nome da cidade)
```

Por exemplo:

```
    populacao(Campinas, 2000000)
    populacao("Campinas", 2000000)
    populacao(SaoPaulo, 15000000)
Ou um texto para a cidade:
    populacao("São Paulo", 15000000)
Exemplos de fatos:
    populacao(Lima,1500000)
    populacao(Brasília, 3000000)
    capital(Brasil,Brasilia)
    capital(Peru,Lima)
```

Definamos proposições para inferir: **Cidade grande – que tenha mais de 2.500.000 habitantes:** ∀c: ∀h: populacao(c, h) Λ (h > 2500000) → cidadeGrande(c);

∀c, ∀p: cidadeGrande(c) Λ capital(p, c) → capital_importante(c).

Ou desta forma:

- ∀c, ∀p, ∀h: capital(p, c) Λ populacao(c, h) Λ h > 2500000 →capital_importante(c)
