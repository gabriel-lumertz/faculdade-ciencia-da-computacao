---
materia: "Circuitos Lógicos"
modulo: "Unidade Lógica e Aritmética"
semestre: 2
unidade: 4
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 04.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 4"]
---

# Unidade Lógica e Aritmética

## Tópicos da Unidade

- **Unidade Lógica e Aritmética (ULA)**

- **O Ciclo de Instrução**

- **O Pipeline**

- **Circuitos Sequenciais**

## Objetivos de Aprendizado

O objetivo desta unidade é capacitar o aluno a usar corretamente os registradores do computador, consumindo menos memória, ao mesmo tempo em que acelera o ciclo de instruções.

## Contextualização

A Unidade Central de Processamento ou Central Processing Unit (CPU) é considerada por muitos o cérebro do computador; porém, podemos dizer que ele é o coração também, uma vez que gera informações que alimentam o sistema operacional e este, por usa vez, os programas.

Tecnicamente, sua função é executar programas armazenados na memória principal, buscando suas instruções, examinando essas instruções e identificando seus comandos, como visto na última unidade e, então, executá-las sequencialmente.

Nesta unidade da disciplina, aprenderemos como que a CPU realiza sua função e como as instruções se comportam quando migram entre as memórias.

Bom estudo!

## Unidade Lógica e Aritmética (ULA)

A unidade lógica e aritmética é o componente da CPU responsável pelas execuções das operações matemáticas dos dados, ou seja, é na ULA que as operações das instruções estudadas, realmente, são trabalhadas interpretadas e as respostas são geradas. As operações que a ULA compreende são:

- Soma;

- Multiplicação;

- Operação lógica AND;

- Operação lógica XOR;

- Deslocamento à direita;

- Incremento;

- Subtração;

- Divisão;

- Operação logica OR;

- Operação complemento;

- Deslocamento à esquerda;

- Decremento.

Normalmente, essas operações utilizam um ou dois valores e, por isso, a ULA possui duas entradas e ambas se concentram a uma saída, via barramento interno.

![[cl2-04-fig01.webp]]

*Figura 1: Estrutura da CPU com destaque para a ULA*

*Fonte: Monteiro, M., Introdução a Organização de Computadores.*

![[cl2-04-fig02.webp]]

*Figura 2: Interligação da ULA com a CPU.*

*Fonte: Monteiro, M., Introdução a Organização de Computadores.*

É possível definir que a ULA funciona como um conjunto de circuitos lógicos, utilizados conforme o tipo de operação a ser realizada, que recebem na entrada dois ou, às vezes um; valores, que seguem pela circuitaria, determinados pelas portas lógicas e, na saída, entregam um resultado.

Vamos exemplificar, aqui, a soma de dois valores binários, X=1 e Y=1, que irão produzir o valor Z=0 e um bit _carry_ (C=1) que tem a função de armazenamento em um registrador especial do processador para referências, quando necessário. Chamamos esse registrador de FLAG. O que muitos desconsideram é que as distâncias percorridas fisicamente têm grande influência no tempo de resposta, apenas para lembrar, a ULA ainda obedece à fórmula _e = vt_ , onde:

- e = é a distância entre a entrada e a saída do circuito.

- v = é a velocidade atingida pelos sinais elétricos que são representações dos bits através do circuito que é, nominalmente, a velocidade da luz; porém, jamais alcança os 300.000km/s, pois isso só ocorre no vácuo.

- t = é o tempo de execução da operação, ou seja, o tempo de percurso dos sinais desde a entrada até a saída.

![[cl2-04-fig03.webp]]

*Figura 3: Circuito lógico da ULA.*

*Fonte: Monteiro, M., Introdução a Organização de Computadores.*

O circuito somador é a base de funcionamento da ULA, classificado, essencialmente, pelo somador _half adder_ ou somador parcial e o somador _full adder_ , que é o somador completo.

No somador parcial, a soma é realizada apenas com os dois valores binários envolvidos recebidos na entrada (X e Y como visto na figura 3) e em sua saída, entrega um resultado Z e o carry (o carry, às vezes, pode não acontecer), ou seja, a figura 3 é uma representação lógica de um somador parcial. No somador completo, o carry é considerado na soma, que fica com três parcelas.

Dessa forma, as ULAs, em sua totalidade, são fabricadas como um circuito somador que pode somar dois valores numéricos, independentemente da quantidade de bits que eles possam possuir, dependendo diretamente da palavra do processador.

Mais para frente na disciplina, nós aprenderemos sobre os circuitos lógicos e, então, retomaremos os exemplos práticos dos somadores, utilizando a representação de circuitaria de suas portas lógicas.

### Processadores

Um processador tem a função de armazenar dados em uma memória e, então, usar esses dados para o correto processamento. Esse processamento envolve a busca de instruções do programa armazenado, exame e identificação dos opcodes e operandos dessa instrução e, por fim, a execução do mesmo para que o programa “rode” corretamente.

Como já mencionado, para executar o processamento das instruções, a CPU usa uma quantidade de memória para o armazenamento temporário de dados, ela mantém a posição de memória da última instrução e, com isso, recebe o valor de endereçamento, onde obtém a instrução seguinte para o processamento contínuo.

Para realizar todo o trabalho corretamente, a CPU segue alguns passos, descritos a seguir:

1. **Busca de instrução:** a CPU executa a leitura de uma instrução localizada na memória. 2. **Interpretação de instrução:** decodificação da instrução em busca da ação desejada.

3. **Busca de dados:** carregamento, se necessário, de um dados da memória ou dispositivo de E/S.

4. **Processamento de dados:** operações aritméticas ou lógicas sobre os dados carregados.

5. **Escrita de dados:** escrita dos dados processados.

*Fonte: https://goo.gl/4EpV8e*

Na figura 4, há um diagrama simplificado da CPU, já demonstrado na unidade anterior. Conforme a figura, podemos resumir a CPU como um dispositivo composto por uma ULA (Unidade Lógica e Aritmética) e uma UC (Unidade de Controle). Vimos, na última unidade, que a ULA tem a função de processar todas as instruções, conforme sua construção de opcodes e operandos, já a UC é responsável por controlar a transferência de dados e instruções entre a CPU e os demais componentes do computador, além de controlar o próprio funcionamento da ULA. Faz parte também da composição de uma CPU uma quantidade de memória especial chamada Registrador que tem a função de armazenar dados imediatos para o processamento.

![[cl2-04-fig04.webp]]

*Figura 4: Estrutura da CPU com destaque para a ULA*

*Fonte: Monteiro, M., Introdução a Organização de Computadores.*

Uma visão mais atenta da figura 4 nos mostra todos os caminhos percorridos por um sinal dentro da CPU, sendo eles os caminhos de transferência de dados e a sinalização de controle da UC que, por muitos, é chamado de barramento interno de CPU. Esse sinal de controle é utilizado apenas para transferência interna das partes da instrução durante seu trabalho, sem contato com o ambiente externo à CPU; a esta comunicação externa cabe o trabalho do barramento de transferência de dados.

### Registradores

Os registradores são unidades de memória de alto nível ou hierarquia que possuem duas funções definidas:

- Registradores visíveis para o usuário: possibilitam ao programador de linguagem de montagem ou de máquina minimizar referências à memória, pela otimização do uso de registradores.

- Registradores de controle e de estado: são usados pela unidade de controle para controlar a operação da CPU e por programas privilegiados do sistema operacional para controlar a execução de programas.

### Registradores Visíveis ao usuário

Esses registradores são aqueles que o programador pode referenciar por conta própria via linguagem de máquina executada pela CPU e pode ser dividido em:

- Registradores de propósito geral: podem conter operandos que executem qualquer tipo de operação, sendo de propósito geral; porém, como tudo na vida, há exceções, onde esses registradores armazenam valores não gerais, como operações com número de ponto flutuante ou pilhas.

- Registradores de dados: são usados apenas para conter dados e não podem ser empregados no cálculo de endereços de operandos.

- Registradores de endereços: podem funcionar como os de propósito geral

- ou para um endereçamento especial como:

- Registradores de segmento: utilizados para armazenar endereçamentos

- segmentados.

- Registradores de índices: utilizados para endereçamentos indexados.

- Apontador de topo de pilha: utilizado na pilha visível para o usuário; dessa forma, a pilha ficará alocada na memória, onde um registro especial endereçará o topo da pilha.

- Registradores de códigos de condição ou flags: são bits utilizados pela CPU como resultados de operações.

### Registradores de controle e de estado

Uma CPU utiliza vários tipos de registradores para controlar a operação e, por sua vez, a maioria dessas não são visíveis para o programador, em contraposto ao modelo anterior. Lembrando que diversas máquinas possuem registradores construídos de forma diferente. Então, foi preciso criar um padrão de registradores para funções específicas, como segue:

- Contador de programa (PC): contém o endereço da instrução a ser buscada.

- Registrador de instrução (IR): contém a última instrução buscada.

- Registrador de endereçamento à memória (MAR): contém o endereço de uma posição de memória.

- Registrador de armazenamento temporário de dados (MBR): contém uma palavra de dados a ser escrita na memória ou a palavra lida mais recentemente.

Esses registradores são responsáveis pelo transporte de dados entre CPU e memória externa, sem que o usuário tome conhecimento dessa ação, sendo que dentro da CPU esses dados são entregues somente para a ULA. Há ainda a possibilidade de um registrador intermediário que interage entre o MBR e a E/S da ULA.

Uma vez clara a necessidade de diversos tipos de registradores na CPU, criou-se um conjunto conhecido como Palavra de Estado de Programa (PSW) que irá conter os códigos de condição além de informações do estado da instrução, constituídos dos seguintes campos:

- Sinal: contém o bit de sinal do resultado da última operação aritmética.

- Zero: atualizado com valor 1 se o resultado da última operação for O.

- ‘Vai-um’: atualizado com valor 1 se uma operação resultar em um ‘vai-um’ para fora do bit de ordem superior (adição) ou em um ‘vem-um’ para o bit de ordem superior (subtração). É usado por operações aritméticas de múltiplas palavras.

- Igual: atualizado com valor 1 se uma comparação lógica resultar em igualdade.

- Overflow: usado para indicar overflow aritmético.

- Habilitar/desabilitar interrupção: usada para habilitar ou desabilitar interrupções.

- Supervisor: indica se a CPU está executando em modo supervisor ou em modo de usuário. Certas instruções privilegiadas apenas podem ser executadas no modo supervisor, assim como certas áreas de memória apenas podem ser acessadas no modo supervisor.

É necessário também que a CPU possua um registrador que sempre aponte para um ponto na memória, onde haja informações do estado original da instrução. Quando esse ponto na memória for especificamente uma memória virtual, esse registrador apontará para a tabela de páginas.

Uma forma de facilitar o desenvolvimento correto dos registradores ocorre quando o programador tem conhecimento total sobre sistemas operacionais, pois ele sabe como o sistema irá interagir com a CPU.

## O Ciclo de Instrução

O ciclo de instruções de um computador ocorre quando a CPU busca uma instrução em um campo de memória. Para tanto, é utilizado um registrador chamado contador de instruções que sempre irá guardar o endereçamento da instrução a ser executa, ou seja, após fazer uma busca, o contador de instruções já armazena o endereçamento da próxima instrução para manter o processamento sequencial.

Após a busca, a instrução deve ser entregue para o processador e isso ocorre através do carregamento dos dados no registrador de instruções do processador que criará bits que identificarão que ação o processador deve executar nos dados. Assim, ele pode interpretar a instrução e executar cada ação corretamente. Essas ações estão listadas a seguir:

- Processador-memória: transferência de dados do processador para a memória

- ou da memória para o processador.

- Processador E/S: transferência de dados entre o processador e um dispositivo

- periférico por meio de um módulo de E/S.

- Processamento de dados: execução de operações aritméticas ou lógicas

- sobre os dados.

- Controle: determinadas instruções podem especificar que a sequência de execução de instruções seja alterada.

Como já dito anteriormente, em unidades anteriores, o computador possui uma memória ou registro de armazenamento chamado AC (acumulador), considerando instruções e dados de 16 bits, organizamos a palavra do processador em

16 bits; assim, a instrução é construída contendo 4 bits para o código de operação, conforme estudado anteriormente.

Para exemplificar o funcionamento do ciclo de instrução, vamos analisar a execução parcial de uma aplicação mostrada na figura 5.

![[cl2-04-fig05.webp]]

*Figura 5: Diagramação do Ciclo de Instrução.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

No passo 1, temos que o PC (contador de instruções) está em 300, ou seja, o programa já rodou 299 instruções e está, agora, executando a instrução 300 que é carregada no IR (registrador de instruções).

No passo 2, os quatro primeiros bits do IR são interpretados, de forma que seu comando é o armazenamento do AC (acumulador) de um valor. O valor que deve ser armazenado no AC está descrito e endereçado (endereço 940) nos 12 bits restantes da instrução do IR.

No passo 3, o PC sobe para 301, ou seja, para o próximo ciclo de instrução que é, então, carregada para o IR.

No passo 4, a instrução é interpretada e, como no passo 2, é identificado que uma soma deve ser feita com o conteúdo endereçado como AC e o endereçado como 941; por fim, o resultado deve ser endereçado de volta para AC, apagando o valor que lá havia.

No passo 5, o PC muda, mais uma vez, para a próxima instrução que é buscada e carregada em IR.

No passo 6, novamente, da mesma forma que no passo 2, a instrução é interpretada como a ação de armazenamento do valor do AC para o endereço de memória 941, sobrescrevendo o valor existente nessa posição.

Na figura 5, foi descrito o funcionamento de uma execução de programa, utilizando três ciclos de instruções, todos com os momentos de busca e execução. Como sabemos, há processadores com arquiteturas complexas que podem ter vários comandos e endereçamentos de memória, o que reduziria o número de ciclos e, possivelmente, o tempo de processamento.

Os estados de um ciclo de instruções podem ser descritos por:

**Cálculo de endereço de instrução (CEI):** **_instruction address calculation:_** nesse estado temos a determinação do endereço da próxima instrução que será carregada. Esse estado geralmente envolve a soma de um valor constante ao endereço da instrução anterior.

**Busca de instrução (BI):** **_instruction fetch:_** nesse estado, a instrução calculada é carregada ou lida da memória para o processador.

**Decodificação de instrução (DI):** **_instruction operation decoding:_** nesse estado faz-se a análise do código da instrução carregada que será executada. Esse estado determina qual é a operação a ser realizada e quais operandos serão utilizados.

**Cálculo de endereço de operando (CEO):** **_operand address calculation:_** ocorre quando a operação atual envolver uma referência a operando na memória ou nos dispositivos de E/S, para então carrega-lo.

**Busca de operando (BO):** **_operand fetch:_** o operando é localizado na memória ou é lido no dispositivo de E/S.

**Execução da operação (EO):** **_data operation:_** nesse passo há a execução da operação indicada pela instrução.

**Armazenamento de resultado (AR):** **_operand store:_** escrita do resultado do processamento.

*Fonte: https://goo.gl/ilnwtd*

![[cl2-04-fig06.webp]]

*Figura 6: Diagrama de transição de estados de um ciclo de instrução.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

Os estados na parte superior da figura 6 envolvem transferências de valores entre o processador, de um lado, e a memória ou um dispositivo de E/S, de outro. Os estados na parte inferior do diagrama envolvem apenas operações realizadas internamente no processador. O estado (CEO) aparece duas vezes, pois uma instrução pode envolver uma operação de leitura.

### Fluxo de dados do clico de instruções

Não existe uma sequência correta única para o fluxo de dados, pois esse fluxo depende da forma como a CPU foi projetada; porém, é possível que se estime uma estrutura, ao menos, lógica, de como deve ser a sequência.

Basicamente, um ciclo de busca é constituído de um momento onde a instrução é lida da memória. Nessa sequência, o PC mantém o endereço da próxima instrução que deve ser carregada. Esse endereço é carregado para o MAR (via address bus), A UC comanda que seja feita a leitura da memória e o valor lido é copiado no MBR e, então, para o IR (via data bus), o contador sobe um valor que é a próxima instrução a ser executada.

A figura 7 mostra uma sequência de ciclo de instruções, demonstrando o fluxo das informações, semelhante ao apresentado na figura 5; porém, com a adição dos barramentos que realizam o transporte dos dados da instrução para seus respectivos controladores.

![[cl2-04-fig07.webp]]

*Figura 7: Fluxo de dados do clico de busca.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

## O Pipeline

Podemos dizer que um pipeline funciona de forma semelhante a uma linha de montagem uma vez que as instruções passam por uma sequência de estágios. Vamos tomar o seguinte exemplo:

Sabemos que um ciclo de instrução possui várias etapas. Então, vamos pegar as etapas de busca e execução das instruções, enquanto parte da instrução está sendo executada a memória não está trabalhando. Nesse instante, a memória poderia ser utilizada em paralelo com a execução; dessa forma, o pipeline executa duas funções paralelamente, enquanto uma parte da instrução é executada a próxima está sendo armazenada de forma temporária, quando a execução termina, a memória de trabalho recebe o valor carregado na memória temporária e começa uma nova execução. Enquanto isso, uma nova instrução é carregada temporariamente e assim por diante. Chamamos essa sequência de trocas de função de busca antecipada de instrução (instruction prefetch) ou superposição de busca (jetch overlap).

A figura 8 mostra duas formas de execução: na primeira (a), há uma execução sem pipeline e na segunda forma (b), há uma execução com pipeline, conforme a descrição de pipeline.

![[cl2-04-fig08.webp]]

*Figura 8: Demonstração lógica do trabalho do pipeline.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

Com essa explicação, fica óbvio que usando o pipeline o tempo de execução do ciclo diminui bastante; porém, isso só ocorre quando os tempos de busca e execução são o mesmo, o que dificilmente acontece, pois é comum que o tempo de execução seja maior que o de busca devido às maiores operações que devem ser feitas.

Quando há instruções de desvio, a próxima instrução que deve ser buscada não teve aquele carregamento prévio, pois seu endereçamento não é conhecido e a busca em paralelo com a execução não é possível, pois essa descoberta só ocorre durante a execução.

O desvio condicional é quando uma instrução sendo executada faz referência à outra instrução ou dado em um determinado endereçamento diferente daquele sequencial à execução do programa. Essa referência servirá como dado para se alcançar o resultado da instrução em execução no momento e despois é descartada; porém, esse desvio de percurso gera um atraso no ciclo e impede a correta execução do pipeline.

Para tentar solucionar o problema das instruções de desvio ou desvio condicional, é executada uma estratégia de adivinhação, tecnicamente chamada de preempção, ou seja, quando uma instrução de desvio condicional é passada do estágio de busca para o de execução, o estágio de busca obtém na memória a instrução, imediatamente, seguinte à instrução de desvio. Então, se não ocorrer o desvio, nenhum tempo será perdido. Se ocorrer o desvio, a instrução buscada deve ser descartada, sendo buscada uma nova instrução.

As instruções de desvio, realmente, interferem no tempo do ciclo de instruções e mesmo com a preempção de endereçamento não se obtém uma solução otimizada. Para tanto, é preciso que o pipeline tenha mais estágios de trabalho paralelo, da mesma forma que demonstrada, quando falamos sobre os estados do clico de instrução:

- Busca de instrução (BI);

- Decodificação da instrução (DI);

- Cálculo de operandos (CD);

- Busca de operandos (BD);

- Execução da instrução (EI);

- Escrita de operando (ED).

Na figura 9, temos a demonstração de um pipeline, onde nove instruções tiveram seu tempo de processamento conjunto reduzido de 54 unidades de tempo (9 instruções de 6 unidades de tempo) para 14 unidades de tempo, usando os estados de ciclo de instruções.

![[cl2-04-fig09.webp]]

*Figura 9: Diagrama de tempo para operação da pipeline de instruções.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

Em contraponto, no caso de uma interrupção (parada da execução devido à alta prioridade de outro processo ou programa) ou um desvio condicional, se imaginarmos as mesmas nove instruções de 6 unidades de tempo; porém, com um desvio condicional ocorrendo da instrução três para a instrução 15.

Nesse caso, a CPU não tem como saber de que modo fazer a preempção, ou seja, a instrução 4 é carregada e sua execução ocorre, normalmente, até que no momento de desvio da instrução 3, acontece paralelamente, chame ou referencie a instrução 15. Nesse momento, todas as instruções ocorrendo em paralelo são interrompidas e aguardam o fim da instrução 15 e suas subsequentes. Quando o resultado dessas execuções subsequentes terminarem e o valor resultado indicar o retorno para a instrução 3, todas as instruções interrompidas retomam seu trabalho, caso contrário, elas irão aguardar o fim das instruções, subsequente à instrução 15 e depois serão retomadas, como demonstrado na figura 10.

![[cl2-04-fig10.webp]]

*Figura 10: Desvio condicional na operação de uma pipeline de instruções.*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores.*

### Desempenho da pipeline

Além de lidar com os desvios condicionais da pipeline e as interrupções, é muito importante sabermos como se dará o desempenho da pipeline. Para tanto, veremos algumas equações para fazer essa medição de desempenho.

Podemos dizer que o tempo relativo  de uma pipeline de instrução é o tempo que um conjunto inteiro de instruções leva para avançar um estágio da pipeline. Esse tempo de ciclo pode ser determinado pela equação:

$$\tau = \max[\tau_i] + d \;\to\; \tau_m + d \qquad i,\ 1 \le i \le k$$

Onde:

- $\tau _{m}$ = atraso máximo de estágio (atraso por meio do estágio de maior atraso).

- K = número de estágios da pipeline de instrução. $\tau _{m}$

- D = tempo necessário para propagar sinais e dados de um estágio para o próximo.

Nessa equação, o (d) é a aproximação ao pulso de um relógio e ($\tau _{m}$) >> d. Se considerarmos que uma quantidade de instruções representada por (n) sem o desvio condicional, o tempo total $T_{k}$ para executar todas as (n) instruções é representado por:

$$T_k = [k + (n - 1)] \times \tau$$

Se lembrarmos do exemplo gráfico anterior (figuras 8 e 9), onde havia 9 instruções com 6 unidades de tempo cada e sem desvio condicional teríamos, então, 14 unidades de tempo para todo o clico do conjunto de instruções, provado pela equação:

$$14 = [6 + (9 - 1)]$$

É possível calcular o quão mais rápido uma execução com pipeline sobre uma execução sem pipeline, calculando o _speedup_ (comparação de velocidades) entre elas, da seguinte forma:

$$S_k = \frac{T_1}{T_k} = \frac{n \times k \times \tau}{[k + (n - 1)] \times \tau} = \frac{n \times k}{k + (n - 1)}$$

A figura 11 demonstra duas vertentes de avaliação de desempenho de ciclo de instruções. Na parte (a), é demonstrado um _speedup_ de execução de um conjunto de instruções em função de instruções executadas em cada conjunto sem a presença do desvio condicional. N parte (b), é demonstrado um gráfico de _speedup_ ; porém, dessa vez, em função da quantidade de estágios de pipeline que cada conjunto possui, onde se pode notar que quanto maior o número de estágios, maior o _speedup_ .

É possível notar que somente aumentar a quantidade de estágios acelera o processo, isso se torna claro na parte (b) da figura 11, onde o _speedup_ aumenta quando se aumentou demais o número de estágios; porém, o número de instruções diminuiu. Isso ocorre devido ao aumento de custo, por atrasos entre estágios e pelo fato de que instruções de desvio requerem que a pipeline seja esvaziada, ou seja, o uso de um número de estágios entre 6 e 9 parece ser mais adequado, sendo contraproducente o uso de um número de estágios maior.

![[cl2-04-fig11.webp]]

*Figura 11: _Speedup_ s obtidos com o uso de pipeline de instruções*

*Fonte: Stallings, W., Arquitetura e Organização de Computadores*

### Visão Elétrica de Postas que Compõem uma ULA Simples

Como já vimos, uma ULA tem a função de processar números usando o mesmo formato que o resto do circuito digital. Os sistemas numéricos de complemento para um e complemento para dois permitem que a subtração seja realizada pela adição do minuendo com o complemento do subtraendo, simplificando o circuito lógico. Uma vantagem do complemento para dois em relação aos outros sistemas é que a representação possui apenas um zero, não possuindo um “zero negativo”.

Podemos resumir o trabalho de uma ULA de formas:

##### Operações simples:

- Operações aritméticas com inteiros;

- Operações lógicas bit a bit AND, NOT, OR, XOR;

- Operações de deslocamento de bits (deslocamento, rotação por um número específico de bits para esquerda ou direita, com ou sem sinal); deslocamentos podem ser interpretados como multiplicações ou divisões por 2.

##### Operações complexas:

O engenheiro de hardware deve projetar uma ULA para calcular qualquer operação; no entanto, isso gera complexidade; o problema é que quanto mais complexa a operação, mais cara é a ULA, mais espaço utiliza do processador e mais dissipa energia. Dessa forma, é uma obrigatoriedade o estudo entre o poder de processamento e a sua complexidade, satisfazendo aos requisitos do processador ou de outro circuito. Imagine um cenário, onde é preciso calcular a raiz quadrada. O engenheiro teria as seguintes opções:

1. Projetar uma ULA extremamente complexa que calcula a raiz quadrada de qualquer número num único passo. Isso é chamado cálculo em passo-único de clock.

2. Projetar uma ULA bastante complexa que calcula a raiz quadrada de qualquer número em vários passos. Mas, existe um truque, os resultados intermediários vão através de uma série de circuitos arranjados em linha, como numa linha de produção, que faz com que a ULA seja capaz de aceitar novos números para cálculo antes mesmo de terminar o cálculo dos anteriores. Isso faz com que a ULA seja capaz de produzir números tão rápido como cálculos em passo-único de relógio, com um atraso inicial até os números começarem a sair. Isso é chamado cálculo em pipeline.

3. Projetar uma ULA complexa que calcula a raiz quadrada através de vários passos. Isso é chamado de cálculo iterativo e usualmente confia no controle de uma complexa unidade de controle com microcódigo.

4. Projetar uma ULA simples no processador e vender separadamente um processador especializado e caro que o consumidor possa instalá-lo ao lado desse, realizando uma das opções acima. Isso é chamado de coprocessador.

5. Dizer aos programadores que não há nenhum coprocessador e que não há nenhuma emulação, assim eles têm que escrever seus próprios algoritmos para calcular a raiz quadrada por software. Isso é chamado de bibliotecas de software.

6. Emular a existência de um coprocessador, ou seja, sempre que um programa tenta realizar o cálculo da raiz quadrada, faz o processador verificar se há coprocessador presente e o utiliza se está ali; se não há, interrompe o programa e invoca o sistema operacional para realiza o cálculo da raiz através de algum algoritmo de software. Isso é chamado de emulação de software.

É comum que processadores poderosos utilizem a opção #1 para as operações mais simples, #2 para as operações complexas mais comuns e #3 para as operações extremamente complexas. Isso é possível através da construção de ULAs complexas.

Na figura 12, você tem um exemplo da representação dos circuitos envolvidos na construção de uma ULA simples de 2-bit que faz AND, OR, XOR e adição.

![[cl2-04-fig12.webp]]

*Figura 12: Representação de uma ULA simples de 2-bit que faz AND, OR, XOR e adição Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

Como seriam as representações de suas portas lógicas na forma estruturadas de construção? Podemos ver a representação dos circuitos elétricos correspondente das portas lógicas que podem existir na ULA e a estrutura de construção em chip, nas figuras a seguir:

![[cl2-04-fig13.webp]]

*Figura 13: Layout da porta lógica NOT*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig14.webp]]

*Figura 14: Layout da porta lógica AND*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig15.webp]]

*Figura 15: Layout da porta lógica OR*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig16.webp]]

*Figura 16: Layout da porta lógica XOR*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig17.webp]]

*Figura 17: Layout do módulo de portas lógicas AND*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig18.webp]]

*Figura 18: Layout do módulo de portas lógicas OR Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig19.webp]]

*Figura 19: Layout do módulo de soma/subtração*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig20.webp]]

*Figura 20: Layout do seletor de funções da ULA Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig21.webp]]

*Figura 21: Layout do seletor de ULA ativa*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

![[cl2-04-fig22.webp]]

*Figura 22: Layout da ULA*

*Fonte: SILVA, Rodrigo; ADAMCZEVSKI, Tiago; ULA de 2 entradas de 4 bits e 4 Operações, Universidade Federal do Paraná, 2010*

## Circuitos Sequenciais

Agora que já estudamos vários tipos de circuitos e seus elementos de memória, o funcionamento da ULA e do processador, podemos usar essa base para avançar nos conceitos de dispositivos mais complexos, sendo aquele estudado agora, os circuitos sequenciais.

Classicamente podemos afirmar que um circuito sequencial é composto por um circuito combinacional e elementos de memória, onde suas entradas e as saídas estão conectadas ao circuito combinacional. O conceito clássico de elemento de memória é de um circuito capaz de armazenar informação codificada em binário. Nesses elementos, a saída do circuito combinacional tornam-se entradas para os elementos de memória, recebendo o nome de variáveis de próximo estado. As saídas desses elementos de memória tornam-se parte das entradas para o circuito combinacional e recebem o nome de variáveis do estado atual. Logo, podemos relacionar as conexões entre o circuito conbinacional e os elementos de memória configurando o que se costuma chamar laço de realimentação, pois a saída de um bloco é entrada para o outro e vice-versa.

O estado de um circuito sequencial é determinado pela informação armazenada nos elementos mencionados, assim o circuito sequencial recebe informação binária das entradas que, juntamente com a informação do estado atual, determinam os valores das saídas e os valores do próximo estado, como demonstrado na figura 23. Seguindo essa linha de raciocínio, fica mais fácil de compreender que as saídas do circuito sequencial dependem não apenas das entradas, mas também do estado atual, armazenado nos elementos de memória. O mesmo raciocínio pode ser usado nas variáveis de próximo estado, logo, em função deste comportamento sequencial é especificado pela sequencia tempostal de entradas, saídas e estados internos.

Conceitualmente, divide-se os circuitos sequenciais em dois tipos, conforme o comportamento temporal dos seus sinais: síncronos e assíncronos, mas esse conceito veremos, a fundo, em outra unidade.

Chamamos de flip-flops aqueles elementos de memória utilizados nos circuitos sequenciais síncronos. Um flip-flop nada mais é que um circuito digital que possui duas entradas e duas saídas, e é capaz de armazenar um bit de informação. Nos flip-flops temos duas entradas que não são intercambiáveis: uma é reservada ao sinal de controle (relógio) e a outra recebe o dado (bit) a ser armazenado. As saídas correspondem ao dado (bit) armazenado e ao seu complemento.

No exemplo do sinal de relógio, determinamos o instante em que o flip-flop mostra o valor do dado, o que corresponder a uma borda de subida ou a uma borda de descida, dependendo de como o flip-flop é constituído. O diagrama da figura 23 mostra que o valor de cada virável de estado é armazenado em um flip- flop específico. Os valores que representam o próximo estado só são mostrados na borda ativa do relógio. Logo, o estado atual fica armazenado no conjunto de flip-flop até que uma nova borda do relógio chegue, quando, então, o próximo estado passa a ser o estado atual e um novo próximo estado será gerado pelo circuito combinacional.

![[cl2-04-fig23.webp]]

*Figura 23: Layout da ULA*

*Fonte: GUNTZEL, José Luiz; NASCIMENTO, Francisco; Introdução aos Sistemas Digitais, 2001*

Desde que devidamente alimentado com energia, um flip-flop pode manter indefinidamente um estado, até que os sinais de entrada assumam uma configuração tal que o façam mudar de estado. Essa configuração depende de como o flip-flop é constituído. O estado em que um flip-flop se encontra usualmente é associado ao valor binário que ele está armazenando. Desta forma, num dado instante, um flipflop estará armazenando ou o valor lógico 1 (um) ou o valor lógico 0 (zero), pois esses são os dois valores possíveis para uma variável Booleana.

### Breve simulação

No material complementar, há um link para uma simulação de funcionamento da ULA. Então, acesse o link e, além de aproveitar maiores explicações sobre a CPU (algumas que ainda veremos na disciplina futuramente), atente-se, mais especialmente, ao simulador de parte operativa.

Nessa seção, você terá acesso a um simulador online na soma de dois valores pela ULA (somador parcial) e a entrega do resultado. Além disso, verá como ocorre o transporte dos dados entre registradores e ULA.

Essa simulação funciona como um resumo do estudado nessa unidade. Desse modo, experimente e faça várias simulações, conforme as instruções do site e discuta suas impressões e resultados com os amigos de sala no fórum virtual.
