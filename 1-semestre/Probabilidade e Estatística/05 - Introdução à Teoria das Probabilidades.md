---
materia: "Probabilidade e Estatística"
modulo: "Introdução à Teoria das Probabilidades"
semestre: 1
unidade: 5
tipo: material-teorico
fonte: "raw/1-semestre/PROBABILIDADE E ESTATÍSTICA/Probabilidade e Estatística 05.pdf"
tags: [faculdade, probabilidade-e-estatistica, semestre-1]
aliases: ["Probabilidade e Estatística - Unidade 5"]
---

# Introdução à Teoria das Probabilidades

## Tópicos da Unidade

- **Introdução**

- **Conceitos Importantes de Probabilidade**

- **Probabilidade em um Espaço Amostral Finito**

- **Cálculo da Probabilidade de um Evento**

- Regra da Adição – Probabilidade da União de Dois Eventos - P(A ∪ B) – Conjunção Ou

- **Probabilidade do Evento Complementar**

- Regra da Multiplicação – Probabilidade da Intersecção de Dois Eventos-P (A ∩ B) – Conjunção E

- **Finalizando**

## Objetivos de Aprendizado

- Nesta Unidade, você irá aprender um pouco sobre a Introdução à Teoria das Probabilidades. Definiremos experimento aleatório, espaço amostral e evento.

- Aprenderemos a calcular a probabilidade de um evento, probabilidade de um evento complementar e a usar a regra da adição e da multiplicação de probabilidades.

## Contextualização

Convide a moçada para uma aposta em que todos os jogos de azar foram úteis na construção da Teoria das Probabilidades.

##### Cenário 1

França, século XVII. Um matemático e filósofo mostra-se preocupado com um jogo fictício entre duas pessoas igualmente imaginárias. A disputa havia chegado a um ponto em que um dos participantes aparentemente tinha mais chance de ganhar do que o adversário. O francês em questão se pergunta: como dividir com justiça as apostas?

Ele é Blaise Pascal, que começou a estruturar a Teoria das Probabilidades em correspondências trocadas com outro matemático e colega seu, Pierre de Fermat.

Portanto, logo na origem, probabilidade era sinônimo de jogo de azar

##### Cenário 2

Alemanha, século XX. Um físico alemão – Werner Karl Heisenberg – complica ainda mais a crença clássica do determinismo quando afirma que é impossível especificar e determinar simultaneamente a posição e a velocidade de uma partícula subatômica com precisão absoluta.

À medida que a determinação de uma dessas grandezas fica mais precisa, avalia Heisenberg, mais incerta se torna a outra. Esse é, basicamente, o enunciado do Princípio da Incerteza. E incerteza é quase o mesmo que probabilidade.

Se no início o cálculo de probabilidades era destinado a prever resultados de jogos de azar, hoje em dia é muito mais do que isso. Trata-se de uma ferramenta fundamental para os cálculos estatísticos, as estimativas, as previsões econômicas, meteorológicas, políticas e muito mais.

Lembre-se de que o jogo de pôquer já foi tema de diversos filmes; inspirou artistas e escritores. Um bom exemplo é o texto humorístico _Pôquer Interminável_ , de Luis Fernando Veríssimo, que faz parte do livro _O Analista de Bagé_ .

Para conferir conteúdo na íntegra, acesse: http://goo.gl/6jqXWt

## Introdução

A Teoria das Probabilidades é utilizada para determinar as chances de um experimento aleatório acontecer.

### Experimento Aleatório

O experimento aleatório é um de tipo prova em que seu resultado não pode ser determinado antes de se realizar o experimento. Por exemplo: jogar um dado e anotar o número da face que ficará voltada para cima.

Sabemos que há seis resultados possíveis, que são os números 1, 2, 3, 4, 5 e 6. Entretanto, é impossível prever qual será o resultado antes de realizar o experimento. Se desconhecermos os resultados, a teoria das probabilidades possibilita que descubramos as chances de ocorrência de cada um dos resultados possíveis para o dado.

Por exemplo

1. Qual a chance de ocorrência da face 1, 2 e 3 em um dado. Podemos dizer que a chance é:

Face 1 = 1/6 Face 2 = 1/6 Face 3 = 1/6

Lemos: 1 chance em 6 possibilidades

![[pe1-05-fig01.webp]]

*Fonte: iStock/Getty Images*

2. Num grupo de 15 lâmpadas, 3 são defeituosas. Considere o experimento: uma lâmpada é escolhida ao acaso e observamos se ela é ou não é defeituosa. Trata-se de um experimento aleatório com dois resultados possíveis:

   - a) A lâmpada é defeituosa (chance 3/15 ou 1/5) Lemos: 3 chances em 15 possibilidades.

   - b) A lâmpada é boa.(chance 12/15 ou 4/5)

Lemos: 12 chances em 15 possibilidades

Percebemos que a probabilidade de se escolher uma lâmpada boa é bem maior do que de se escolher uma lâmpada defeituosa.

## Conceitos Importantes de Probabilidade

Nesta parte de nosso estudo, iremos definir alguns conceitos importantes sobre Probabilidade.

### Espaço Amostral – Ω

Espaço Amostral é o conjunto formado por todos os resultados possíveis de um experimento aleatório. Usamos a letra grega ômega, cujo símbolo é Ω, para identificar um espaço amostral. A notação matemática que usamos é:

Ω { _ , _ , _ , ... }

Dentro das chaves, vamos descrever todos os resultados possíveis para o lançamento do dado.

### Evento

Definimos evento em probabilidade como sendo qualquer subconjunto do espaço amostral. Para designar um evento, usaremos sempre letras maiúsculas do alfabeto.

A notação matemática que usamos é:

```
A = { _ , _ , _ , ... }
```

Dentro das chaves, vamos descrever os resultados possíveis.

Vejamos alguns exemplos:

Seja o experimento aleatório: Lançar um dado e observar a face superior, temos que:

|  | Resultado |
|---|---|
| Espaço amostral | $\Omega = \{1, 2, 3, 4, 5, 6\}$ |
| **Evento A:** ocorrência de n° par | A = {2, 4, 6} |
| **Evento B:** ocorrência de n° ímpar e múltiplo de 3 | B = {3} <br> O evento que contém somente **UM** elemento é chamado de **evento elementar** |
| **Evento C:** ocorrência de um n° menor que 7 | C = {1, 2, 3, 4, 5, 6} <br> Este tipo de evento composto por **TODOS** os elementos do espaço amostral é chamado de **evento certo** |
| **Evento D:** ocorrência do n° 5 | D = {5} <br> O evento que contém somente UM elemento é chamado de **evento elementar** |
| **Evento E:** ocorrência de um n° maior que 6 | E { } <br> O evento, cujo resultado do conjunto é vazio, é chamado de **evento impossível** |

## Probabilidade em um Espaço Amostral Finito

Dado um experimento aleatório, vamos fazer afirmações a respeito das chances de cada um dos possíveis resultados.

Considere Ω = {$a_{1}$, $a_{2}$, $a_{3}$, ..., $a_{n}$}. Vamos atribuir a cada elemento um número real que exprima a chance de eles ocorrerem.

- O evento { a1} ocorre com chance P1.

- O evento { a2} ocorre com chance P2.

- O evento { an } ocorre com chance Pn.

O que queremos dizer é que podemos associar a cada elemento descrito em um evento uma probabilidade.

## Cálculo da Probabilidade de um Evento

Para calcular a probabilidade de um evento, devemos fazer:

$$P(A) = \frac{\text{número de maneiras como o evento pode ocorrer}}{\text{número de elementos do espaço amostral}}$$

Devemos exprimir a probabilidade de um evento por números fracionários ou decimais usando sempre três casas decimais significativas.

Por exemplo:

P = 0,0000128506 arredondar para 0,0000129 (três casas decimais significativas).

A probabilidade de um evento é sempre um número menor ou igual a 1. A soma de P1 + P2 + ... + Pn = 1.

Vamos trabalhar com alguns exemplos para ficar mais claro.

##### Exemplo 1

Em um teste realizado por uma Universidade, uma questão típica de múltipla escolha tem 5 respostas possíveis. Respondendo aleatoriamente, qual a probabilidade de essa questão estar errada?

###### Resolução

Para calcular a probabilidade do evento questão errada, temos 5 alternativas; dessas, 4 são erradas e 1 é certa. Portanto, para calcularmos essa probabilidade, devemos usar a fórmula:

$$P(A) = \frac{\text{número de maneiras como o evento pode ocorrer}}{\text{número de elementos do espaço amostral}}$$

$$P\ (\text{resposta errada}) = \frac{4}{5} \text{ ou } 0{,}8$$

*Resposta*

4 A probabilidade de esta questão estar errada é de 5<sup>(lê-se 4 erradas em 5</sup> possibilidades) ou, ainda, 0,8.

##### Exemplo 2

Uma seguradora fez um levantamento sobre mortes causadas por acidentes domésticos e chegou à seguinte constatação: 160 mortes foram causadas por quedas, 120 por envenenamento e 70 por fogo ou queimaduras. Selecionando aleatoriamente um desses casos, qual a probabilidade de que a morte tenha sido causada por envenenamento?

###### Resolução

Queremos calcular a probabilidade do evento de morte por envenenamento. Somando o total de mortes, elas perfazem um total de 350. E as mortes por envenenamento são 120.

Usando a fórmula $P(A) = \frac{\text{número de maneiras como o evento pode ocorrer}}{\text{número de elementos do espaço amostral}}$, temos

###### Mortes por envenenamento

$$P\ (\text{morte por envenenamento}) = \frac{120}{350} = 0{,}343$$

Total de mortes

###### Resposta

120 A probabilidade de morte por envenenamento é de . Lê-se 120 em 350 350 possibilidades ou, ainda, de 0,343.

##### Exemplo 3

No lançamento de uma moeda, qual a probabilidade da face que fica voltada para cima ser “cara”?

###### Resolução

Uma moeda tem um total de duas possibilidades ou a face que fica voltada para cima é par ou é coroa.

número de maneiras como o evento pode ocorrer Usando a fórmula P ( A) = , temos número de elementos do espaço amostral 1 P (face cara) = ou 0,5. 2

###### Resposta

A probabilidade de que a face da moeda que fica voltada para cima seja cara é 1 de 2<sup>(lê-se uma possibilidade de cara em duas) ou 0,5.</sup>

## Regra da Adição – Probabilidade da União de Dois Eventos - P( A ∪ B ) – Conjunção Ou

Quando queremos juntar dois conjuntos ou eventos, em probabilidade dizemos que queremos fazer a UNIÃO de dois eventos. Matematicamente temos: sejam os eventos A e B, a probabilidade de A∪ B (lê-se A união B) são todos os elementos de A ou de B.

A operação que devemos realizar é a descrita a seguir.

### Regra formal da adição

Temos duas situações para fazer a união de dois eventos: i) quando os eventos não têm elementos em comum e; ii) quando os eventos têm elementos em comum.

Vamos representar graficamente dois experimentos aleatórios e seus eventos A e B, um em que temos elementos em comum e um em que não temos eventos em comum.

![[pe1-05-fig03.webp]]

*Eventos Mutuamente Exclusivos. (Não tem elementos em comum)*

![[pe1-05-fig04.webp]]

*Eventos com Elementos Comuns – Não são Mutuamente Exclusivos*

(O mesmo elemento aparece nos dois eventos)

Então, para fazer a união de dois eventos, devemos considerar duas situações distintas:

- P( A∪ B) = P (A) + P(B), quando os eventos A e B são eventos mutuamente exclusivos (não têm elementos em comum).

- P( A∪ B) = P (A) + P(B) – P (A ∩ B), quando há elementos comuns aos eventos A e B.

Vamos a um exemplo de aplicação: o quadro a seguir representa um teste realizado com um medicamente chamado Seldane, que é utilizado para dor de cabeça.

Algumas pessoas tomaram o medicamento e outras tomaram placebo, que é um comprimento sem o poder ativo da droga.

| **Seldane**       | **Placebo** | **Grupo controle** | **Total** |      |
| ----------------- | ----------- | ------------------ | --------- | ---- |
| Dor de cabeça     | 49          | 49                 | 24        | 122  |
| Sem dor de cabeça | 732         | 616                | 602       | 1950 |
| Total             | 781         | 665                | 626       | 2072 |

Vamos calcular as probabilidades pedidas.

1. Determine a probabilidade de se obter uma pessoa que fez uso de placebo ou estava no grupo de controle.

Veja que temos de trabalhar com a união de eventos. Note a conjunção ou! **O 1º evento é: fez uso de placebo. O 2º evento é: estava no grupo de controle.**

###### Resolução

Os eventos são mutuamente exclusivos, pois não tem jeito de uma pessoa ter feito uso de placebo e estar no grupo de controle. Note no quadro que as colunas são independentes. Portanto, os eventos são independentes.

Temos, então, que: P( A∪ B) = P (A) + P(B).

Calculando cada uma das probabilidade pela fórmula:

Lembrem-se! Para calcular cada uma das probabilidades, temos de usar a fórmula:

número de maneiras como o evento pode ocorrer P ( A) = número de elementos do espaço amostral

$$P\ (\text{placebo ou grupo de controle}) = \frac{665}{2072} + \frac{626}{2072} = \frac{1291}{2072} = 0{,}623$$

$$P\ (\text{placebo}) = \frac{\text{total de placebo}}{\text{total de pessoas}} \qquad P\ (\text{grupo controle}) = \frac{\text{total do grupo controle}}{\text{total de pessoas}}$$

*Resposta*

A probabilidade de se obter uma pessoa que fez uso de placebo ou estava no grupo de controle é de 0,623. Passando para porcentagem, 62,3%.

2. Determine a probabilidade de se obter alguém que tenha usado Seldane ou

   - que não teve dor de cabeça.

Veja que temos que trabalhar com a união de eventos. Note a conjunção ou! **O 1º evento é: fez uso de Seldane. O 2º evento é: não teve dor de cabeça.**

###### Resolução

Os eventos NÃO SÃO mutuamente exclusivos; eles apresentam elementos em comum. Veja na Tabela que a coluna do Seldane cruza com a coluna sem dor de cabeça.

Isso significa que pessoas que estão no grupo que tomaram Seldane também estão no grupo das que não tiveram dor de cabeça.

Temos, então, que P( A∪ B) = P (A) + P(B) – P (A ∩ B).

total Seldane e sem dor de cabeça P Seldane total de pessoas

$$P\ (\text{Seldane ou sem dor de cabeça}) = \frac{781}{2072} + \frac{1950}{2072} - \frac{732}{2072} = \frac{1999}{2072} = 0{,}965\,.$$

total de Seldane total sem dor de cabeça P Seldane P Seldane total de pessoas total de pessoas

###### Resposta

A probabilidade de se obter alguém que tenha usado Seldane ou que não teve dor de cabeça é de 0,965 ou, ainda, 96,5%.

## Probabilidade do Evento Complementar

Sejam A e A (complementar de A em relação à Ω), esses eventos são mutuamente exclusivos, ou seja, não tem elementos em comum.

Logo, P( A∪ A) = P (A) + P(A).

Temos que P (A) + P(A) = 1.

Como A∪ A = Ω e P (Ω) = 1, daí vem:

$$P\ (\bar{A}) = 1 - P(A).$$

Traduzindo para Língua Portuguesa: Um evento complementar é aquele, como o nome já diz, que complementa o espaço amostral.

Veja o exemplo: Seja o experimento: lançamento de um dado.

O Espaço Amostral é: Ω ={ 1, 2, 3, 4, 5, 6 }.

Seja o Evento A: face par voltada para cima, portanto A = { 2, 4, 6 }.

Seja A, ou seja, o complementar de A. O complementar de A seriam os elementos que faltam para completar o espaço amostral, portanto:

A = { 1, 3 , 5 }.

Como A∪ A = Ω, isso significa que se juntarmos os elementos de A com os elementos de A, temos como resultado o espaço amostral Ω.

Veja que é verdade { 2, 4, 6 } U { 1, 3 , 5 } = { 1, 2, 3, 4, 5, 6 }.

Vamos calcular as probabilidades do evento A e do evento complementar de A (A).

3 Calculando a probabilidade de A temos: 6<sup>.</sup>

3 Calculando a probabilidade de A, temos também: 6<sup>.</sup>

A formula diz que se somarmos P (A) + P(A) = 1. Vamos ver se é verdade?

3 3 6 1. Veja: é verdade! 6 6 6

Concluímos com isso que a soma das probabilidades de um evento qualquer com o seu complementar é sempre igual a 1. Isso significa que todo espaço amostral tem probabilidade igual a 1, o que justifica dizermos:

P (Ω) = 1

Resolvendo essa equação: P (A) + P (A) = 1 → P(A) = 1 – P (A) que é a fórmula que devemos usar para calcular o valor da probabilidade de um evento complementar.

Vejamos alguns exemplos.

##### Exemplo 1

Seja P (A) = 2/5, determine P (A).

###### Resolução

Para calcular o complementar, devemos usar a fórmula:

$$P(\bar{A}) = 1 - P\ (A)$$

$$P(\bar{A}) = 1 - \frac{2}{5} = \frac{5}{5} - \frac{2}{5} = \frac{3}{5}$$

*Resposta*

3 A probabilidade do complementar de A é 5<sup>ou 0,6.</sup>

##### Exemplo 2

Determine P (A), dado P (A) = 0,228.

###### Resolução

Para calcular o complementar, devemos usar a fórmula:

$$P(A) = 1 - P\ (A)$$

$$P(\bar{A}) = 1 - 0{,}228 = 0{,}772$$

*Resposta*

A probabilidade do complementar de A é 0,772 ou 77,2%.

## Regra da Multiplicação – Probabilidade da Intersecção de Dois Eventos-P (A ∩ B) – Conjunção E

Para determinar a probabilidade de intersecção de dois eventos, devemos considerar se os eventos são independentes, ou seja, se a ocorrência de um deles não afeta a ocorrência do outro.

### Regra formal da multiplicação

Podemos usar a regra da multiplicação em duas situações: quando os eventos são independentes, ou seja, a ocorrência de um deles não afeta a ocorrência do outro e quando os eventos são dependentes um do outro, quando a ocorrência de um afeta a ocorrência do outro evento.

EVENTO INDEPENDENTE P (A ∩ B) = P (A) . P(B)

EVENTO DEPENDENTE P (A ∩ B) = P (A) . P(B\A)

Vejamos alguns exemplos de aplicação da regra da multiplicação.

##### Exemplo 1

Uma empresa produz um lote de 50 filtros dos quais 6 são defeituosos. Nestas condições, escolhidos aleatoriamente 2 filtros, determine a probabilidade de ambos serem bons.

###### a) Com reposição (eventos independentes)

###### Resolução

Colocamos os 50 filtros em uma caixa, damos assim a todos a mesma oportunidade de serem escolhidos.

Temos, então, nessa caixa, 44 filtros bons e 6 filtros ruins. Retiramos o primeiro deles. Dizemos, então, que a probabilidade de retirada de um filtro bom 44 é de . 50 44 bons

Total de filtros

Devolvemos esse filtro para a caixa e aí procedemos a uma nova retirada, com 44 a mesma probabilidade de 50<sup>. Ao devolver o filtro para a caixa, o número de</sup> elementos do espaço amostral se mantém o mesmo. Isso identifica um evento independente.

Retirar dois filtros bons significa que o 1º e o 2º filtros devem ser bons. Veja que a conjunção usada nesse caso foi e, o que denota que temos de usar a regra da multiplicação.

> Vamos usar a regra da multiplicação para eventos independentes
>
> **$P\ (A \cap B) = P\ (A)\ .\ P(B)$ (são independentes)**

$$P(\text{bom e bom}) = \frac{44}{50} . \frac{44}{50} = \frac{1936}{2500} = 0{,}774$$

*Resposta*

Escolhidos aleatoriamente 2 filtros, a probabilidade de que ambos sejam bons, com reposição, é de 0,774 ou 77,4%.

###### b) Sem reposição (eventos dependentes)

Colocamos os 50 filtros em uma caixa, damos, assim, a todos a mesma oportunidade de serem escolhidos. Temos, então, nessa caixa, 44 filtros bons e 6 filtros ruins. Retiramos o primeiro deles. Dizemos, então, que a probabilidade de 44 retirada de um filtro bom é de 50<sup>. Veja que, nesse caso, por ser SEM REPOSIÇÃO,</sup> não devolvemos o filtro para a caixa. Temos, então, agora na caixa, 49 filtros. Procedemos a uma nova retirada com probabilidade de:

43 → Havia 44 bons 1 já foi retirado. Restaram 43. 49 → Havia 50 filtros no total. 1 já foi retirado e não devolvido. Restaram 49.

Como não devolvemos o filtro para a caixa, o número de elementos do espaço amostral se alterou, o que caracteriza um evento dependente. A realização do 1º evento afetou a realização do 2º evento, pois o espaço amostral não se manteve.

Retirar dois filtros bons significa que o 1º e o 2º devem ser bons. Veja que a conjunção usada nesse caso foi e, o que denota que temos de usar a regra da multiplicação.

Vamos usar a regra da multiplicação para eventos dependentes:

Essa notação P (A ∩ B) = P (A) . P(B\A) denota que o 44 43 1892 evento A afetou P bom e bom . 0, 772 50 49 2450 o evento B.

###### Resposta

Escolhidos aleatoriamente 2 filtros, a probabilidade de que ambos sejam bons, SEM reposição, é de 0,772 ou 77,2%

## Finalizando

Bem, espero que você tenha gostado de estudar e trabalhar com probabilidades.

Parece ser difícil, mas com a prática dos exercícios vai ficar mais fácil. Portanto, não deixe de realizar a Atividade de Sistematização, para fixar os conceitos que aprendeu e tirar suas dúvidas.
