---
materia: "Circuitos Lógicos"
modulo: "Operações de Circuitos Digitais"
semestre: 2
unidade: 5
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 05.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 5"]
---

# Operações de Circuitos Digitais

## Tópicos da Unidade

- **Circuitos sequenciais síncronos e assíncronos**

- **Os** **_Latches_**

- **Diagrama de Estados**

- **Análise de Circuitos Sequenciais**

- **Maquinas de Estados**

## Objetivos de Aprendizado

Nesta unidade, o aluno terá conhecimento sobre os tipos de sistemas e o trabalho com máquinas específicas. Dessa forma, estará apto a realizar trabalhos com operações avançadas de circuitos digitais.

## Contextualização

Para entendermos os circuitos sequenciais, precisamos estudar suas duas formas de apresentação: Os sistemas Síncronos e Assíncronos. Para tanto, vamos exemplificar e criar formas de se entender cada passo desses sistemas, analisando também as máquinas de estado.

Além disso, vale lembrar que estudaremos técnicas simples para projetar circuitos lógicos que satisfaçam um dado conjunto de requisitos.

Bom estudo!

## Circuitos sequenciais síncronos e assíncronos

Como já visto, superficialmente, em outro momento de nossa disciplina, os circuitos sequenciais podem ser divididos em dois tipos, conforme o comportamento temporal dos seus sinais: síncronos e assíncronos.

O comportamento de um circuito sequencial assíncrono depende da ordem na qual as entradas mudam e o estado do circuito pode se alterar a qualquer tempo, como consequência de uma mudança de suas entradas. Os elementos de memória utilizados nos circuitos sequenciais assíncronos apresentam uma capacidade de armazenamento que está associada diretamente ao atraso de propagação dos circuitos que os compõem.

Em outras palavras, o tempo que esses circuitos levam para propagar uma mudança de suas entradas até suas saídas pode ser encarado como o tempo durante o qual eles retêm os valores aplicados antes da mudança e, além disso, esse fenômeno coincide com o conceito de memória, para os circuitos digitais.

Nos circuitos sequenciais assíncronos, os elementos de memória são compostos por portas lógicas que provêm um atraso de propagação com valor adequado para o funcionamento do circuito. Então, um circuito sequencial assíncrono pode ser visto como um circuito combinacional com realimentação.

O projeto de circuitos com realimentação apresenta grandes dificuldades, uma vez que seu funcionamento correto é dependente das características temporais dos componentes (portas lógicas e fios). A principal dificuldade provém do fato de que os componentes apresentam atrasos que não são fixos, podendo ser diferentes mesmo para exemplares com mesma função e de um mesmo fabricante. Desta forma, os circuitos sequenciais assíncronos têm sido evitados, sempre que possível, em favor do uso de circuitos sequenciais síncronos.

Um circuito sequencial síncrono utiliza um sinal especial denominado de relógio (ou _clock_ , em inglês), o qual tem a função de cadenciar uma eventual troca de estado. A figura 1 mostra um exemplo de sinal de relógio. A forma de onda de um sinal de relógio é dita monótona, pois não se altera ao longo do tempo. Nela podem ser identificados: a borda de subida, a borda de descida, o nível lógico zero e o nível lógico um. O tempo que decorre para o sinal se repetir é denominado período e é representado por T. Por exemplo, o tempo entre duas bordas de subida sucessivas é igual a T. Da mesma forma, o tempo entre duas bordas de descida sucessivas é igual a T.

![[cl2-05-fig01.webp]]

*Figura 1: Exemplo de _Clock_*

A frequência de um sinal de relógio ou _clock_ é representada por f ou Hz e pode ser definida como sendo o inverso do período ou tempo, ficando:

$$f = \frac{1}{T} \text{ ou } Hz = \frac{1}{s}, \text{ onde } s = \text{segundos}$$

Dessa forma, podemos facilmente observar que o período é mensurado, usando-se múltiplos de segundo (ms = milissegundo = $10^{-3}$s; µs = microssegundo = $10^{-6}$s; ns = nanossegundo = $10^{-9}$s; ps = picossegundo = $10^{-12}$s) e para medir a frequência, usam-se os múltiplos da unidade Hertz (KHz = quilohertz = $10^{3}$HZ; MHz = megahertz = $10^{6}$Hz; GHz = gigahertz = $10^{9}$Hz).

Exemplo: Se um circuito trabalha a frequência de 200MHz, significa que os blocos combinacionais precisam ter um atraso menor que o período do relógio, identificado pela função:

$$T = \frac{1}{200 \times 10^{-6}\,\text{s}} = 0{,}005 \times 10^{-9}\,\text{s} = 5\,\text{ns}$$

Em um circuito sequencial síncrono, o sinal de relógio determina quando os elementos de memória irão mostrar os valores de suas entradas. Dependendo do tipo do circuito que será utilizado como um elemento de memória; esta amostragem das entradas será sincronizada pela borda ascendente ou descendente do relógio. Independentemente do tipo da sincronização, o tempo que passa entre duas amostragens sucessivas equivale a T, o período do relógio. Isso implica que mudanças no estado de um circuito sequencial síncrono irão ocorrer somente após a borda do sinal de relógio, na qual seus elementos de memória são disparados.

*Fonte: https://goo.gl/mz193N*

![[cl2-05-fig02.webp]]

*Figura 2: Diagrama de blocos de um circuito sequencial síncrono*

Os **_flip-flops_** são os elementos de memória que são utilizados nos circuitos sequenciais síncronos. Um **_flip-flop_** é um circuito digital com duas entradas e duas saídas que é capaz de armazenar informação em um bit. Suas entradas não são intercambiáveis, sendo uma reservada ao sinal de controle (que é o relógio) e a outra entrada recebe o dado (que é o bit) que será armazenado. Já as saídas correspondem ao dado (que é o bit) armazenado e o seu complemento direto.

O sinal do relógio descreve o preciso momento em que o **_flip-flop_** determina o valor do dado, que pode corresponder a uma borda de subida ou a uma borda de descida, de acordo como o **_flip-flop_** for constituído.

Na figura 2, é possível notar que o valor de cada uma das variáveis de estado é armazenado em um **_flip-flop_** específico. Os valores do próximo estado apenas são amostrados na borda ativa do relógio; dessa forma, o estado atual é armazenado no conjunto de **_flip-flops_** até que uma nova borda do relógio seja ativada. Assim, o próximo estado passa a ser o estado atual e um próximo estado novo é gerado pelo circuito combinacional.

*Fonte: https://goo.gl/mz193N*

Se alimentado corretamente com energia, o _flip-flop_ mantém indefinidamente um estado até que os sinais de entrada assumam uma configuração que os façam mudar de estado. Isso depende de como o flip-flop é constituído.

O estado atual de um _flip-flop_ é relativo ao valor binário que ele armazena, assim, em um instante, o _flip-flop_ está armazenando o valor lógico 1 ou valor lógico 0, sendo esses os dois valores possíveis para uma variável Booleana.

## Os Latches

Existem vários tipos de _flip-flops_ e esses se diferem pelo número de entradas que possuem e também pela maneira, pela qual tais entradas afetam o estado em que se encontra o _flip-flop_ .

Os tipos mais simples de _flip-flops_ são chamados de latches, os quais operam por níveis de sinais na entrada, também chamados de “sensíveis a nível” e eles são a base da construção de qualquer outro _flip-flop_ mais avançado.

Para entendermos como um latch funciona, vamos focar nosso estudo no _Latch_ RS. Importante salientar que há outros tipos a serem estudados e são de suma importância, como o latch RS controlado e o _latch_ D.

### O Latch RS

Esse é o _latch_ mais simples que existe, sendo construído com o uso de duas portas NOR com 2 entradas em cada e essas portas podem ser conectadas, conforme a figura 3. Você pode observar duas entradas, que são denominadas R e S e duas saídas, que são denominadas Q e Q . É observável também uma conexão entre a saída e a entrada NOR n2. Há a conexão entre a saída Q e a entrada NOR n1. Essas conexões são chamadas de realimentações e, no caso dos circuitos digitais, são responsáveis pela propriedade de armazenamento do circuito.

![[cl2-05-fig03.webp]]

*Figura 3: Latch RS com portas NOR*

Chamamos os circuitos que possuem realimentação de sequenciais, pois seu comportamento depende não somente dos valores das portas de entrada, mas somado a isso, o estado em que o circuito se encontra; dessa forma, a análise do funcionamento do _latch_ RS deve obedecer aos seguintes passos:

- 1º Identificação da combinação de entrada capaz de determinar o estado do latch de maneira independente do estado anterior.

- 2º O estado determinado no passo 1 é assumido como sendo o estado inicial, assim a aplicação de uma nova combinação de entradas para verificar como o circuito se comporta, ou seja, se muda de estado ou não.

- 3º Repetição dos passos 1 e 2 para cada combinação de entradas capaz de determinar o estado do circuito de maneira independente.

- 4º Feito os procedimentos iniciais, você encontra, agora, uma tabela de comportamento denominada “tabela de transição de estados” ou “tabela de transição” a qual é uma característica do _latch_ .

Imagine que, no exemplo da figura 3, sejam aplicados simultaneamente os valores 1 e 0 às entradas R e S no instante de tempo t0. É sabido que o valor 1 quando aplicado a qualquer entrada de uma porta NOR determina o valor da saída desta porta como sendo 0, independente dos valores das demais entradas.

Seguindo esse procedimento, se aplicarmos R=1 e S=0 no tempo t0, a saída Q será estabilizada com valor 0 em t0+td (n1), onde td (n1) é o atraso da porta por NOR n1, a partir do tempo t0+td (n1), ambas entradas desta porta estarão estabilizadas em 0. Assim, a partir do tempo t0+td (n1) + td (2), onde td (n1) é o atraso da porta por NOR n2, a saída Q estará estabilizada com o valor lógico 1.

Continuando a operação desse _latch_ , aplicam-se, agora, os valores R=0 e S=0 às entradas no instante de tempo t0, com t1 > t0 + td (n1) + td (n2) . Pensando em função dos atrasos das portas n1 e n2, as saídas   não se alterarão ineditamente.

Para efeitos de análise, consideramos que a entrada n1, que está conectada a Q, continua com o valor lógico 1 e que a entrada de n2 que está conectada a Q continua com o valor lógico 0. Desta forma, logo após o instante t1, n1 terá 0 e 1 em suas entradas, fazendo com que sua saída, que é a saída Q do circuito, permaneça no valor lógico 0. De maneira semelhante, logo após, t1, n2 terá suas entradas 0 e 0, fazendo com que sua saída, que é a saída Q do _latch_ , permaneça com o valor lógico 1. As formas de onda que ilustram o resultado da aplicação sucessiva destes dois vetores de entrada (R=1,S=0) e (R=0,S=0) no _latch_ RS são mostradas na figura 4.

![[cl2-05-fig04.webp]]

*Figura 4: Formas de onda para aplicação do vetor de entrada (R=1;S=0) seguido do vetor (R=0;S=0) no latch RS*

Continuando o processo, podemos trabalhar, agora, com a simulação (R=0 e S=1) no tempo t0 e (R=0 e S=0) no tempo t1. Nesse exemplo, em t0 + td (n2) a saída Q estará estabilizada com o valor lógico 0. Uma vez que existe a ligação física entre a saída   e uma das entradas da porta NOR n1, após o instante   a saída de estará estabilizada com o valor lógico 1.

Se supormos mais uma vez que _t_ 1> _t_ 0 + _td_ (n2) + (n1) _td_ , é possível admitirmos que, logo após o tempo t1, as saídas Q e Q continuaram com seus valores anteriores. A figura 5 mostra as formas de onda para essa suposição.

![[cl2-05-fig05.webp]]

*Figura 5: Formas de onda para aplicação do vetor de entrada (R=0;S=1) seguido do vetor (R=0;S=0) no _latch_ RS.*

É possível perceber que, em todas as situações vistas até aqui, os valores obtidos pelas saídas Q e Q são sempre complementares, sendo este o motivo pelo qual elas recebem tais denominações. Se aplicarmos o vetor de entrada (R=1 e S=1), as duas saídas irão se estabilizar em 1, o que entra em conflito com o visto até agora.

Se um _latch_ deve armazenar um dentre dois estados possíveis para uma variável Booleana e se o estado está associado ao valor de Q e Q, onde Q exibe o estado e Q o seu complemento; então, como seria o estado representado pela situação Q=1 e Q=1?

Por não haver uma resposta plausível a essa pergunta, acabou sendo decidido, por convenção, que esse seria um estado proibido ou indeterminado; assim, a situação (R=1 e S=1) deve sempre ser evitada, no caso do _latch_ RS.

Conforme já mencionado, um _latch_ , assim como um _flip-flop_ , pode assumir um dentre dois estados possíveis. Esses estados correspondem aos valores que uma variável Booleana pode assumir, ou seja, 0 e 1. O estado 0 é chamado estado reset e o estado 1 é também chamado _estado set_ .

Ao analisarmos as formas de onda da figura 4, podemos extrair que a aplicação do vetor (R=1 e S=0) faz com que o _latch_ migre para o _estado set_ (onde a saída é estabilizada com o valor lógico 1), independente do seu estado anterior. Caso, após isso, for aplicado o vetor (R=0 e S=0), o latch não muda seu estado.

Se continuarmos a análise com formas de onda da figura 5, podemos observar que a aplicação do vetor (R=0 e S=1) faz com que o _latch_ vá para o estado _reset_ (onde a saída Q estabiliza com o valor lógico 0), independente de seu estado anterior. Se, após isso, for aplicado o vetor (R=0 e S=0), não muda o estado em que o latch está, mas por outro lado, o vetor (R=1 e S=1) deve ser evitado, uma vez que é o estado proibido.

Resumidamente, temos:

*Tabela 1 - Resumo do Funcionamento Sequencial do latch RS*

|**R**|**S**|**Q**|**Q**|**Ação**|
|---|---|---|---|---|
|1|0|0|1|Vaipara estado reset|
|0|0|0|1|Mantém estado reset(= estado anterior)|
|0|1|1|0|Vaipara estado set|
|0|0|1|0|Mantém estado reset(= estado anterior)|
|1|1|0|0|Estadoproibido|

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

A tabela anterior pode ser escrita de maneira mais compacta, de modo a incorporar a informação da dependência temporal.

*Tabela 2 - Resumo de transição de estados para o latch RS*

|**R**|**S**|**Qt+1**|**Comentário**|
|---|---|---|---|
|0|0|Qt|Mantém estado anterior|
|0|1|1|estado set|
|1|0|0|estado reset|
|1|1|-|estadoproibido|

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Na tabela 2, há a listagem dos valores possíveis para as entradas na coluna à esquerda, admitindo-se que esses valores estão sendo aplicados no instante de tempo t. Para cada situação de entradas, o novo valor da saída para o instante imediatamente posterior t+1 encontra-se na coluna à direita. Como a saída Q sempre exibe o complemento da saída Q, apenas o valor de Q é listado, ficando Q subentendido.

## Diagrama de Estados

É possível expressar circuitos sequenciais por meio de um diagrama chamado Diagrama de Estados, sendo o _Latch_ RS um circuito sequencial, pode-se usar um diagrama de estados para representar seu funcionamento, como pode ser visto na figura 6.

![[cl2-05-fig06.webp]]

*Figura 6: Diagrama de estados para o latch RS*

No diagrama da figura 6, podem ser observados os estados reset e set representados por nodos (os círculos). A transição entre os estados é representada pelas setas. As condições das entradas, cuja determinada transição pode ocorrer, está definida junto à aresta respectiva.

Um exemplo disso é o _Latch_ RS no estado reset; para que ele vá para o estado set, será necessário que (R=0 e S=1), caso isso não ocorra, o latch ficara no estado em que se encontra.

Não é necessário desenhar o diagrama toda vez que houver uma ocorrência do latch RS. Para facilitar, usa-se a simbologia apresentada na figura 7.

![[cl2-05-fig07.webp]]

*Figura 7: Símbolo do _latch_ RS.*

## Análise de Circuitos Sequenciais

É comum dentre os mecanismos de empregados na descrição de comportamentos de circuitos sequenciais os Diagramas de Estados, as Tabelas de Transição de Estados, as Tabelas de Saídas e as Equações Booleanas.

Nós chamamos de análise o processo de avaliar e descrever o funcionamento de um circuito, a partir de usa estrutura, ou seja, partimos de um esquema de projeto de um circuito sequencial e determinamos o comportamento de seus recursos.

Como um exemplo de análise, vamos determinar uma tabela de transição de estados, a tabela de saída e o diagrama de estados baseados no esquema da figura 8.

![[cl2-05-fig08.webp]]

*Figura 8: Esquema de Circuito Sequencial*

Como pode ser visto, o circuito possui uma entrada camada (cnt) e uma saída chamada (Y) e dois _flip-flops_ .

Como primeiro passo na análise, temos de determinar as equações Booleanas para as entradas de cada _flip-flop_ , em função da entrada externa (cnt) e das saídas dos _flip-flops_ (Q0 e Q1), ficando:

- D0 = cnt⊕Q0 = cnt·Q0+cnt·Q0

$$D0 = \overline{cnt} \times Q1 + cnt \times \overline{Q1} \times Q0 + cnt \times Q1 \times \overline{Q0}$$

As equações de D0 e D1 são conhecidas como “equações de excitação”, pois elas descrevem o comportamento dos sinais que são aplicados às entradas dos _flip-flops_ , os quais irão determinar o estado do circuito sequencial para o próximo ciclo de relógio.

Para continuar a análise, é preciso aplicar as equações de excitação às equações dos _flip-flops,_ obtendo-se, assim, as “equações de estado”. Como no exemplo da figura 8, temos _flip-flops_ do tipo D, onde Qt+1 = Dt (a saída copia a entrada), ficando as equações da seguinte forma:

$$Q0_{t+1} = cnt \times Q0_t + cnt \times Q0_t$$

$$Q0_{t+1} = \overline{cnt} \times Q1_t + cnt \times \overline{Q1_t} \times Q0_t + cnt \times Q1_t \times \overline{Q0_t}$$

$Y = Q0 \times Q1$, para a saída

Utilizando as equações de estado, passa a ser possível montar a tabela de transição de estados do circuito, onde, nas colunas mais para a esquerda, ficam os valores referentes às variáveis de entrada e ao estado atual, enquanto que nas colunas mais para a direita estão os valores correspondentes ao próximo estado associado a cada combinação de entradas. Assim, os estados de um circuito sequencial são definidos pelos valores binários armazenados nos seus _flip-flops_ .

Dessa forma, temos quatro números de estados possíveis para o circuito estudado, uma vez que as variáveis (Q0 e Q1) podem valor de 00, 01, 10 e 11.

*Tabela 3: Tabela de transição de estados para o circuito da figura 8*

|**Entrada**|**Estado**|**atual**|**Próxim**|**o estado**|
|---|---|---|---|---|
|cnt|Q1~~t~~|Q0~~t~~|Q1~~t+1~~|Q0~~t+1~~|
|0|0|0|0|0|
|0|0|1|0|1|
|0|1|0|1|0|
|0|1|1|1|1|
|1|0|0|0|1|
|1|0|1|1|0|
|1|1|0|1|1|
|1|1|1|0|0|

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Na tabela, podemos observar oito combinações de entradas referentes aos 4 estados do circuito (estado atual), combinados com os 2 valores possíveis para a entrada cnt.

Associado a cada uma destas combinações, existe um estado que será armazenado pelo circuito após a próxima borda ascendente do sinal de relógio, que é o chamado próximo estado. O próximo estado é definido pelas equações de estado:

$$\begin{aligned} Q0_{t+t} &= \overline{cnt} \times Q0_t + cnt \times \overline{Q0_t} \\ Q0_{t+t} &= \overline{cnt} \times Q0_t + cnt \times \overline{Q0_t} \times Q0_t + cnt \times Q1_t \times \overline{Q0_t} \end{aligned}$$

Também pode ser observado na tabela que sempre que (cnt) valer 0, o próximo estado será igual ao estado atual, ou seja, não se muda de estado. Já quando (cnt) vale 1 o circuito muda de estado na chegada de uma borda ascendente do relógio (clock). Utilizando a equação de saída, temos, agora, a tabela de saída, conforme a tabela 4.

*Tabela 4: Tabela de saída para o circuito da figura 8*

|**Entrada**|**Estado**|**atual**|**Saída**|
|---|---|---|---|
|cnt|Q1t|Q0t|Y|
|0|0|0|0|
|0|0|1|0|
|0|1|0|0|
|0|1|1|1|
|1|0|0|0|
|1|0|1|0|
|1|1|0|0|
|1|1|1|1|

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Tendo as tabelas de transição de estado e de saída, pode ter também uma representação gráfica das informações das tabelas, a essa representação chamamos de “Diagrama de Estados”, onde cada estado que o circuito pode armazenar é representado por um nó em que são registrados os valores das variáveis de estado e os valores das variáveis de saídas do circuito.

Nesse diagrama, temos as transições entre estados indicados por arestas (os arcos com as setas) e junto a cada uma dessas arestas são anotadas as condições das variáveis de entrada necessárias para a transição ocorrer.

Na figura 9, você pode observar o diagrama gerado para o circuito da figura 8, onde fica fácil perceber que o sinal (cnt) é um sinal de habilitação, em que se (cnt)=0 a contagem é parada (os _flip-flops_ mantêm os estados) e se (cnt)=1, o circuito continua a contagem de onde parou. Com essa observação, pode-se dizer que é a representação de um contador síncrono de módulo-4 (que conta de 0 a 3). Além disso, o sinal de saída Y serve para indicar quando a contagem atingiu o valor 3 (Q1=1 e Q0=1). Logo, enquanto o circuito permanecer no estado 11, Y permanecerá com o valor 1.

![[cl2-05-fig09.webp]]

*Figura 9: Diagrama de estados para o circuito sequencial da figura 8*

Na figura 10, são mostradas formas de onda que ilustram uma possível contagem: o circuito foi suposto partir do estado 00 e o sinal (cnt) foi mantido com valor lógico 1 por 3 ciclos de relógio consecutivos. Após, (cnt) foi feito igual a zero, o que desabilitou a contagem. Com isso, o circuito contou de 0 a 3, parando em 3. Verifique o comportamento da saída Y durante esta operação.

![[cl2-05-fig10.webp]]

*Figura 10: Diagrama de tempos para uma possível operação do circuito sequencial da figura 8*

Vamos realizar mais exemplo que será bastante importante para o próximo conceito. Vamos determinar a tabela de transição de estados, a tabela de saída e o diagrama de estados para o circuito apresentado na figura 11.

![[cl2-05-fig11.webp]]

![[cl2-05-fig12.webp]]

*Figura 11: Esquema de Circuito Sequencial*

Este circuito estudado agora se diferencia do apresentado anteriormente no elemento de saída Y, que apesar de também depender da entrada (cnt), neste caso, Y=1 somente quando (Q1 e Q0 = 11) e (cnt)=1 (somente quando o circuito estiver contado).

###### Y = cnt x Q0 x Q1, para a saída

Como a diferença desse circuito está na saída, a tabela de transição de estados é a mesma do exemplo anterior, ficando diferente somente a tabela de saída conforme apresentado abaixo:

*Tabela 5: Tabela de saída para o circuito da figura 11*

|**Entrada**|**Estado**|**atual**|**Saída**|
|---|---|---|---|
|cnt|Q1t|Q0t|Y|
|0|0|0|0|
|0|0|1|0|
|0|1|0|0|
|0|1|1|0|
|1|0|0|0|
|1|0|1|0|
|1|1|0|0|
|1|1|1|1|

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

No diagrama de estados desse exemplo, além de se anotar as condições de entrada para a transição ocorrer em cada aresta, anotam-se também os valores das saídas, ficando como mostrado na figura 12.

![[cl2-05-fig13.webp]]

*Figura 12: Diagrama de estados para o circuito sequencial da figura 11*

Na figura 13, são mostradas formas de onda que ilustram uma possível operação do Circuito O circuito conta de 0 até 3. No meio do ciclo em que a contagem atinge o valor 3 (portanto, Y=1), o sinal (cnt) passa a valer 0, o que suspende a contagem e faz Y passar para 0.

![[cl2-05-fig14.webp]]

*Figura 13: Diagrama de tempos para uma possível operação do circuito sequencial da figura 11*

## Máquinas de Estados

Nos dois exemplos anteriores, cada um dos circuitos estudados por nós corresponde a um dos modelos possíveis de circuitos sequenciais, sendo eles:

![[cl2-05-fig15.webp]]

Exemplo1: Modelo dependente dos estados ou modelo de Moore.

Exemplo2: Modelo dependente das entradas ou modelo de Mealy.

*Figura 14: Modelos de Circuitos Sequenciais*

No caso do modelo de Moore, as saídas dependem única e exclusivamente do estado em que o circuito se encontra, de modo que uma mudança nos valores das entradas só toma efeito após a próxima borda do relógio. Já no caso do modelo de Mealy, as saídas dependem não somente do estado em que o circuito se encontra, mas também do valor atual das entradas externas, de modo que se estas se alteraram ainda antes da troca de estados, as saídas do circuito podem se alterar.

As figuras 15 e 16 mostram os diagramas de blocos para o modelo de Moore e de Mealy, respectivamente.

![[cl2-05-fig16.webp]]

*Figura 15: Diagrama de blocos para o modelo de Moore*

Nos diagramas de bloco, o bloco combinacional é subdividido em dois outros blocos; um deles fica responsável pela geração do próximo estado, chamado “bloco de próximo estado” (implementando equações de estado apenas) e outro bloco que gera os valores de saída chamado de “bloco de saída”. Além desses blocos de lógica combinacional, existe um conjunto de _flip-flops_ que armazenam os estados do circuito, sendo o número de estados possíveis 2n, sendo (n) o número de _flip-flops_ .

No caso dos Exemplos 1 e 2, o bloco de saída caba sendo constituído apenas pela porta E que gera o sinal de saída Y e o bloco de próximo estado contém as portas que estão à esquerda dos _flip-flops_ , sendo essas as que implementam as funções de estado.

![[cl2-05-fig17.webp]]

*Figura 16: Diagrama de blocos para o modelo de Mealy*

