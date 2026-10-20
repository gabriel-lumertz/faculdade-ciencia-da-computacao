---
materia: "Circuitos Lógicos"
modulo: "Linguagem de Descrição de Hardware"
semestre: 2
unidade: 6
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 06.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 6"]
---

# Linguagem de Descrição de Hardware

## Tópicos da Unidade

- **Projeto de Circuitos Sequenciais**

- **Dispositivos Lógicos Programáveis**

## Objetivos de Aprendizado

O objetivo desta unidade é demonstrar, ao aluno, formas diferentes de projetos de circuitos.

## Contextualização

O projeto de um circuito sequencial, normalmente, inicia pela definição de seu comportamento de maneira textual e com a transcrição desse comportamento para um diagrama de estados, de modo a detalhar os estados existentes, as condições para trocas de estados e os valores das saídas. Pela análise do diagrama de estados, é possível identificar o modelo de máquina de estados a ser seguido (Moore ou Mealy).

Nesta unidade da disciplina, aprenderemos como que a CPU realiza sua função e como as instruções se comportam quando migram entre as memórias.

Bom estudo!

## Projeto de Circuitos Sequenciais

Quando estamos trabalhando com projetos de circuitos sequenciais, aprendemos como descrever o comportamento do circuito desejado por meio de um formalismo matemático, conhecido como equações booleanas e essas, por sua vez, são convertidas no próprio circuito lógico.

Mas somente a equação booleana não é suficiente para descrever como é o comportamento de um circuito sequencial. Para tanto, é preciso de um formalismo que incorpore a variável TEMPO.

A Máquina de Estados Finitos (FSM _– Finite State Machine_ ) é exatamente o formalismo necessário que consiste, basicamente, em um conjunto de estados que representam todos os estados ou modos possíveis de um sistema. Podemos dizer, de forma sistemática, que o FSM é o projeto de redes sequenciais.

O conceito de redes sequenciais as dividem em duas partes: uma delas são os flip-flops, que já estudamos, os quais são responsáveis pelo armazenamento de dados em unidades de memória, e a outra são as redes combinacionais que implementam as funções de entrada dos flip-flops e também da rede. Dois dos mais importantes elementos que temos que ter sempre em mente sao as maquinas de estado sólido do tipo: Máquina de Estados de Moore e Máquina de Estados de Mealy. Se lembramos o que já aprendemos em nossa disciplina, a FSM de Moore possui uma metodologia de projeto de rede sequencial que é função somente dos estados atuais da rede. O modelo geral dessa FSM pode ser visto na figura 1:

**clk**

![[cl2-06-fig01.webp]]

*Figura 1: Modelo geral de uma máquina de estados tipo Moore*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Na FSM de Moore, o sinal de saída somente é válido após o sinal do relógio

(clock) ser aplicado à rede.

Já em uma FSM de Mealy, a metodologia de projeto é baseada em uma saída que é função dos estados atuais da rede e das entradas do sistema ao mesmo tempo. O FSM de Mealy pode ser visto na figura 2:

![[cl2-06-fig02.webp]]

*Figura 2: Modelo geral de uma máquina de estados tipo Mealy*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Vamos reavivar alguns elementos de máxima importância para trabalharmos com redes sequenciais.

Para executarmos projetos de redes sequenciais, necessitamos seguir algumas etapas básicas:

1. Determinação do diagrama de estados;

2. Determinação da tabela de estados;

3. Codificação dos estados;

4. Montagem do mapa de transição;

5. Montagem e simplificação do mapa de entrada dos elementos de memória ( _flip-flops_ );

6. Montagem e simplificação do mapa de saída; e

7. Circuito esquemático.

### Determinação do Diagrama de Estados

Os diagramas de estados dos nossos projetos não são mais que os diagramas de transição com uma diferença, a cada estado recebe um nome e um valor correspondente às saídas.

Como exemplo, vamos projetar um detector de paridade ímpar de um sinal serial utilizando a metodologia FSM de Moore e os _flip-flops_ JK. Para determinarmos o diagrama de estados, vamos precisar estabelecer qual o requisito do projeto.

Um circuito detector de paridade ímpar de um sinal serial deve possuir apenas uma entrada de sinal e uma saída, a qual deve indicar se o número de valores “1” presentes no sinal de entrada é ímpar.

Esse diagrama deve conter a quantidade de estados necessários para a operação e seu comportamento de acordo com cada valor possível de entrada. Na figura 3, você pode observar a tabela de estados do detector serial de paridade ímpar.

![[cl2-06-fig03.webp]]

*Figura 3: Diagrama de estados do detector serial de paridade ímpar Fonte: TOCCI, Ronald J.; Sistemas Digitais*

### Determinação das Tabelas de Estados

A tabela de estados é uma representação tabulada do comportamento do obtido do diagrama de estados, com a inserção do valor da saída do sistema.

|Estado Atual|**Estad**<br>X = 0|**o Futuro**<br>X = 1|Saída (Z)|
|---|---|---|---|
|S0|S0|S1|0|
|S1|S1|S0|1|

*Figura 4: Tabela de estados*

##### Codificação dos Estados

Na implementação do mapa de designação dos estados, as seguintes orientações de projeto devem ser seguidas:

- a) Estados, cujos estados futuros são iguais, devem ficar próximos;

- b) Estados, seguintes a um mesmo estado, devem ficar próximos;

- c) Estados, que possuem a mesma saída, devem ficar próximos.

Para o exemplo, tem-se que:

![[cl2-06-001.webp]]

*Montagem do Mapa de Transição*

O mapa de transição nada mais é que uma representação em formato de mapa do diagrama de estados e da tabela de estados, com a codificação proposta na codificação de estados. Para o exemplo proposto, temos:

![[cl2-06-002.webp]]

*Montagem dos Mapas de Entrada dos Flip-flops*

Para realizar esta tarefa, devem-se utilizar as tabelas de transição dos _flip-flops_ , apresentadas no capítulo anterior, visualizando os estados atuais de Q e seus estados futuros, posicionando no mapa as entradas necessárias para causar tal transição. Para esse caso, temos:

![[cl2-06-003.webp]]

*Montagem do Mapa de Saída*

Obtido a partir da codificação dos estados:

![[cl2-06-004.webp]]

*Apresentação do Esquemático do Circuito Desenvolvido*

Basta implementar as equações lógicas obtidas com os elementos de memória utilizados. Para o exemplo, temos:

![[cl2-06-fig04.webp]]

*Dispositivos Lógicos Programáveis*

Como já estudo no curso, a evolução dos circuitos digitais deu-se dos transistores na sua forma unitária para a versão coletiva conhecida como circuitos integrados ou VLSI ( _Very Large Scale Integration_ ). Assim, a criação do microprocessador possibilitou um novo passo na evolução da microeletrônica com o desenvolvimento de chips de memória de ala densidade e o avanço na tecnologia de produtos lógicos como os Dispositivos Lógicos Programáveis (PLD).

Antigas gerações, de tecnologia de hardware, para projetos digitais apresentavam um grande número de chips contendo portas básicas (AND e OR). Com o avanço tecnológico, os projetos mais complexos passaram a usar circuitos de alta densidade que, em geral, incluem dispositivos como controladores, contadores, registradores e decodificadores, proporcionando o desenvolvimento de alternativas para obter flexibilidade em uma implementação.

Com o uso de módulos programáveis (portas básicas que permitem a implementação de sistemas digitais), estes módulos têm uma estrutura padrão e são personalizados para uma função particular.

Exemplos de tipos e classes de dispositivos programáveis (configuráveis) com capacidade de implementar funções lógicas são:

- PLA ( _Programmable Logic Array_ );

- PAL ( _Programmable Array Logic_ );

- CPLD’s ( _Complex Programmable Logic Devices_ );

- MPGA ( _Mask Programmable Gate Array_ );

- FPGA ( _Field Programmable Gate Array_ ).

A grande capacidade e a versatilidade dos novos dispositivos programáveis fizeram desses elementos uma alternativa mais que considerável no projeto de sistemas digitais. A utilização de algumas ferramentas de desenvolvimento como o EDA ( _Eletronic Design Automation_ ) ou, então, o ECAD ( _Eletronic Computer Aided Design_ ) possuem ciclos rápidos de projeto.

Hoje em dia, já não é mais necessário o desenho de portas lógicas individuais e planejar todas as interconexões, as linguagens de descrição de hardware (HDL) estão tão consolidadas no meio acadêmico quanto no meio industrial como a forma padrão na elaboração de projetos. Há também ferramentas de síntese lógica automática disponíveis que possibilitam mapear os circuitos em diversas tecnologias.

Com essa grande variedade, torna-se necessário uma prototipação mais rápida, pois o ciclo de vida dos produtos é cada vez mais curto em relação ao tempo necessário para o projeto e desenvolvimento em diversas categorias:

- CCl’s customizados ou ASICs ( _application specífic integrated circuits_ ): Esses dispositivos precisam de um método de fabricação especial devido a necessidade de se utilizar diversas máscaras específicas para cada etapa de projeto.

O longo tempo de desenvolvimento desses dispositivos aliados aos altos custos são alguns exemplos de problemas desses elementos, logo em aplicações de grande volume de produção esse custo é amortizado.

• MPGAs ( _mask-progratnmable gate arrays_ ): Esse dispositivo já possui uma fabricação mais rápida pois usa máscaras genéricas com módulos préprojetados, mas quando se trabalha com interconexoes de móduos ele volta a necessitar máscaras especialiadas. Como usa biblioteca de células seu tempo de projeto é mais rápido, bem como os custos menores.

• _Standard CelIs_ : Sua construção se dá de forma semelhante ao MPGA. Os módulos ou standard cells são salvos em módulos de banco de dados e os projetistas selecionam as células desejadas nesses bancos. Comparado aos anteriores, são menos eficientes em tamanho e desempenho mas de baixíssimo custo.

- PLDs ( _programmable logic devices_ ): O diferencial aqui é a capacidade de programação por parte do usuário, dessa forma elimina-se o processo de fabricação e aceleramos as mudanças quando necessário. Comparado com os demais, os PLDs tem um ciclo de projeto bem menor e seus custos são mais baixos também.

Com a grande quantidade de dispositivos CIs existentes hoje no mercado, os desenvolvedores e projetistas de sistemas lógicos passaram a implementar diversas novas funções em projetos de computadores e eletrônicos. Porém, houve um problema a se resolver, com o uso de uma quantidade grande de CIs, o espaço exigido também acabou por aumentar a placa do circuito impresso.

A redução no número de CI’s em um projeto acarreta em inúmeras vantagens além de menor espaço ocupado na placa de circuito impresso, também um menor consumo de energia, levando a utilização de fontes menores e mais baratas e maior confiabilidade no projeto, uma vez que possui um número menor de interligações, e velocidades mais altas.

O desenvolvimento de Dispositivos Lógicos Programáveis (PLD - _Programmable Logic Devices_ ) tem proporcionado a substituição de diversos chips por um único CI, além de poder ser programado pelo usuário, eliminando o processo de fabricação e facilitando eventuais mudanças no projeto, diminuindo o tempo e custo do projeto.

A estrutura interna de um PLD é baseada em um _array_ que conecta os barramentos aos blocos lógicos, aos pinos de entrada e saída, e aos blocos de memória. Os PLD’s, a princípio, possuíam apenas um único bloco lógico (que realizava globalmente as operações), conectado aos pinos de entrada e saída do dispositivo.

Com o aperfeiçoamento da tecnologia de fabricação, esses dispositivos receberam uma estrutura de interconexões programáveis, que viriam flexibilizar mais ainda a programação.

Na verdade, o grande desafio de Eletrônica Digital é o desenvolvimento do componente “universal” que alie versatilidade com elevada capacidade, alta velocidade, baixo custo e fácil manuseio. A evolução trouxe uma otimização do aproveitamento de espaço, aumentando ainda mais as interconexões do _array_ de blocos lógicos. A Figura 5 mostra a evolução dos PLD’s.

![[cl2-06-fig05.webp]]

*Figura 5: Evolução da arquitetura dos PLD’s da ALTERA Fonte: TOCCI, Ronald J.; Sistemas Digitais*

### Tipos de PLDs

Existem duas classificações de PLDs:

- Dispositivo de Lógica Programável Simples (“SPLD - _Simple Programmable Logic Device_ ”);

- Dispositivo de Lógica Programável de Alta Capacidade (“HCPLD - _High Capacity Programmable Logic Device_ ”).

![[cl2-06-fig06.webp]]

*Figura 6: Tipos de Dispositivo de Lógica programável Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Os PLD’s simples usam tecnologia CMOS, oferecem elementos de memória do tipo EPROM, EEPROM e memória FLASH, bem como possuem uma quantidade de portas abaixo de 600 e englobam os dispositivos PALs, GALs e outros componentes. Os HCPLDs (dispositivos lógicos programáveis de alta capacidade) oferecem mais de 600 portas disponíveis. Também utilizam tecnologia CMOS com memória EPROM, EEPROM, FLASH, SRAM e opções anti-fusível. Por HCPLD’s, entendem-se os dispositivos FPGA e CPLD.

### Os SPLDs ( Simple Programmable Logic Devices )

Os SPLDs possuem estrutura interna baseada em conjuntos de portas AND e OR que são chamados de arranjos lógicos e podem possuir _flip-flops_ ou não em sua saída. Esses PLDs são utilizados quando há necessidade de baixo custo e alto desempenho.

### Tipos de SPLDs

Matriz Programáveis Logicamente (PLA) ou Matriz programável logicamente em campo (FPLA)

Quando avaliamos uma PROM, percebemos a existências de duas matrizes de interconexões AND e OR, sendo a matriz AND fixa e a matriz OR é programável. Essa arquitetura é adequada àquelas onde cada combinação possível de entrada se faz necessária para a geração de uma função de saída, como, por exemplo, os conversores de código e tabelas de dados.

Na figura 7, você tem uma estrutura de PLA que é semelhante a da PROM, diferenciando-se apenas por:

- Dispor de menor quantidade de portas AND (não é decodificador completo);

- Ter duas matrizes de conexão das portas (AND e OR) programáveis (para compensar o número menor de portas AND).

Um PLA, embora seja o mais versátil de todos os Dispositivos Lógicos Programáveis por possuir dois conjuntos de fusíveis, é mais difícil de fabricar, projetar que a PROM; consequentemente, tem um custo mais alto.

![[cl2-06-fig07.webp]]

*Figura 7: PLA ainda não programada, com todos os fusíveis intactos*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

###### • Matriz Lógica Programável (PAL)

O diferencial do PAL é que ele não necessita que todas as combinações de entrada sejam programáveis. Logo, pode-se dizer que os PAL são uma simplificação dos PLA, sendo apenas a matriz de conexão das portas AND programável, a matriz OR é fixa, vide figura 8.

Cada porta AND pode ser programada para gerar qualquer dos produtos AND das duas variáveis de entrada e de seus complementos. Cada porta OR está ligada somente a duas das saídas ANDs. Isso limita a função a ser implementada a ter, no máximo, dois produtos AND. Se a função precisar de mais de dois produtos, não pode ser implementada nesta PAL, devendo ser escolhido outro modelo que tenha mais entradas para as portas OR. Caso seja necessário menos de dois termos para a implementação da função, as saídas não utilizadas devem ser colocadas no nível lógico “0”.

![[cl2-06-fig08.webp]]

*Figura 8: PAL ainda não programada, com todos os fusíveis intactos*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

###### • Arranjo Lógico Genérico (GAL)

As GAL’s (“ _Generic Array Logic_ ”) são estruturas como a PAL, mas possuem macrocélulas de saídas, as quais podem ser configuradas como lógica combinacional ou sequencial (registradores), como mostrada na Figura 9.

![[cl2-06-fig09.webp]]

*Figura 9: Circuito típico de uma GAL*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Uma única GAL pode substituir 24 tipos diferentes de PAL. A GAL é construída com a tecnologia CMOS; isso reduz o consumo de potência comparado a dispositivos bipolares, mas possui alta taxa de ruído. A Gal possui a mesma quantidade de pinos do que uma PAL, em torno de 20 e 24 pinos.

###### • Dispositivos Lógicos Programáveis Apagáveis (EPLD)

Os EPLD’s (“ _Ereaseable Programmable Logic Device_ ”) são dispositivos que têm quantidades de pinos entre 20 a 66, bem como um consumo mais baixo de potência do que as GALs, em torno de metade da potência, mas não são rápidos, embora possuem um custo baixo e são fáceis de usar em desenvolvimento de sistemas.

Além disso, são detentores dos registradores programáveis como tipo D, T, JK ou _Flip-flop_ RS com quatro entradas para clocks independentes.

No entanto, o problema dos EPLDs é que têm posse do arranjo de portas OR fixas e AND programáveis, as quais apresentam baixa utilização de portas.

São utilizados em telecomunicações e aplicação industrial. A figura 10 mostra uma macrocélula como decodificador de endereços, a qual tem oito termos de produtos, mas apenas um deles é usado. Entretanto, quando uma aplicação necessita de mais de oito termos de produtos deve ser feito um “loop” de realimentação o qual torna o projeto muito mais lento.

![[cl2-06-fig10.webp]]

*Figura 10: Macrocélula como decodificador de endereços*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

### Os Dispositivos de lógica Programável de Alta Capacidade (HCPLD)

Tendo em vista a necessidade cada vez maior de implementar circuitos muito complexos, conexões entre vários SPLDs foram criadas. Além disso, para contornar o problema de interconexão entre os vários chips, foi desenvolvido um chip único de grande complexidade.

Os HCPLD nada mais é que um dispositivo lógico programável que possui centenas de portas, quanto maior o número de portas do PLD, maior será sua complexidade e em se tratando de estrutura de conexão, os HCPLD são divididos em:

- CPLD ( _Complex Programable Logic Devices_ )

- FPGA ( _Field Programable Gate Array_ )

Normalmente, um HCPLD é constituído por várias estruturas que e repetem, conhecidas como células e cada célula é constituída de elementos que implementam a lógica combinacional, acompanhados dos já estudados _Latches_ (através de memórias e _flip-flops_ ) que são destinados à lógica sequencial.

Interligando estas duas estruturas,  existem multiplexadores programáveis que realizam a interligação destes blocos entre si e destes com o exterior da célula (para outra célula ou para barramentos).

Um barramento é uma estrutura que se destina a promover a interligação entre as células. É uma conexão física (trilha metalizada) disponíveis no interior do chip. Dependendo do tipo de PLD envolvido (FPGA ou CPLD), de sua complexidade e de seu fabricante, há diferentes recursos e modos de conexão. Basicamente, esses blocos de conexão são estruturas de conexão segmentadas (FPGA) e estruturas contínuas (CPLD).

A interface com o mundo exterior é feita através de unidades conhecidas como blocos de entrada e saída. Sua função é conectar as células aos pinos do integrado que, normalmente, pode ser realizada diretamente (Célula → Bloco I/O) ou indiretamente (Célula → Barramento → Bloco I/O). A seguir, serão descritas mais detalhadamente cada uma dessas estruturas.

### Tipos de HCPLD

- Dispositivos Lógicos Programáveis Complexos (CPLDs - _Complex Programmable Logic Devices_ )

Esse dispositivo é um conjunto de múltiplos PLDs em um único chip, onde os blocos lógicos se comunicam um com o outro através de interconexões programáveis. Essa arquitetura de dispositivo permite tornar muito mais aproveitável a integração do silício do dispositivo, permitindo a redução no custo. Um único CPLD pode substituir centenas de componentes.

![[cl2-06-fig11.webp]]

*Figura 11: Estrutura interna de um CPLD.*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

As interconexões programáveis formam um barramento que interliga os sinais das entradas ou saídas para as entradas de um bloco lógico, ou das saídas de um bloco lógico para as entradas do mesmo ou outro bloco. Além disso, cada bloco lógico é equivalente a um SPLD, contendo suas macrocélulas com suas interconexões. Diferente das interconexões configuráveis da SPLD, as interconexões entre os blocos lógicos da CPLD podem não ser totalmente conectáveis, ou seja, algumas conexões entre um bloco e outro, teoricamente, pode ser possível, mas, na prática, não podem ser executadas. Com isso, torna-se difícil utilizar 100% das macrocéculas.

- Arranjos Lógicos Programáveis em Campo (FPGA - _Field-Programmable Gate Array_ )

Esses arranjos são circuitos programáveis que não possuem planos AND e OR, mas sim milhares de unidades de blocos lógicos iguais e configuráveis. Essas unidades lógicas são tratadas como componentes padrões que podem ser configurados independentemente e interconectados a partir de uma matriz de trilhas condutoras e chaves programáveis.

![[cl2-06-fig12.webp]]

*Figura 12: Estrutura de um FPGA*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

Os dispositivos FPGA são divididos em duas unidades lógicas configuráveis, sendo uma delas (a menor) uma matriz AND/OR que é configurável. A outra unidade (maior) é um arranjo bidimensional que possui recursos mais complexos como multiplexadores, blocos de memória e contadores. Essa unidade, como visto na próxima figura, é um arranjo de elementos de circuitos não conectados que chamamos de blocos lógicos e recursos de interconexão, cuja configuração é obtida através de programação pelo usuário.

Os blocos lógicos, mostrados nas figuras 12 e 13, são interconectados através de segmentos de trilha e comutadores programáveis. Chama-se de roteamento a maneira pela qual esses comutadores programáveis e segmentos de trilha são posicionados para permitir a interconexão das células lógicas.

![[cl2-06-fig13.webp]]

*Figura 13: Arquitetura de uma FPGA.*

*Fonte: TOCCI, Ronald J.; Sistemas Digitais*

###### • Diferenças básicas entre CPLD e FPGA

Ambos são dispositivos lógicos programáveis e ambos, muitas vezes, são produzidos pelas mesmas companhias. Existem, porém, muitas diferenças entre as tecnologias associadas:

- FPGAs contém muitos pequenos blocos lógicos com _flip-flops_ (até da ordem de 1000000). CPLDs são compostos por um pequeno número (algumas centenas) de grandes blocos lógicos.

- FPGAs, tipicamente, são baseados em RAM, isto significa que perdem sua programação após desligar a alimentação. Portanto, precisam ser reconfigurados (reprogramados) após cada corte de energia. CPLDs são baseados em EEPROM mantendo sua programação após desligar a alimentação.

- CPLDs têm um tempo de resposta melhor, por ser composto de alguns poucos grande blocos lógicos. Em contrapartida, essa característica lhe dá menos flexibilidade.

- FPGAs têm recursos de roteamento especiais para implementar de maneira eficiente funções aritméticas e RAM. CPLDs não têm.

- FPGAs podem ser usados em projetos grandes e complexos, enquanto CPLDs estão restritos a projetos bem menores.
