---
materia: "Organização e Arquitetura de Computadores"
modulo: "Função Processamento"
semestre: 1
unidade: 3
tipo: material-teorico
fonte: "raw/1-semestre/ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES/Organização e arquitetura de computadores 03.pdf"
tags: [faculdade, organizacao-e-arquitetura-de-computadores, semestre-1]
aliases: ["Organização e Arquitetura de Computadores - Unidade 3"]
---

# Função Processamento

## UNIDADE

- Processadores RISC e CISC

- Nesta terceira aula, você irá estudar as características da função processamento. Saber como funciona o processamento das informações, ainda que de forma mais básica, facilitará o desenvolvimento de seu trabalho em qualquer ramo da computação em que possa atuar.

Nesta terceira aula referente à disciplina que estamos estudando, você irá se aprofundar um pouco mais nos conceitos relacionados ao processador. Você começará a estudar detalhes do processamento e também conhecerá a evolução dos processadores. Sabemos que os processadores evoluem constantemente no sentido de melhorar o desempenho da máquina. Por último você aprenderá a distinguir um processador com tecnologia CISC de outro com tecnologia RISC.

Você poderá esclarecer os pontos sobre os quais ainda tenha dúvidas através do fórum de discussão; é importante que participe inserindo suas dúvidas ou até mesmo respondendo aos colegas.

### Contextualização

Os processadores estão se tornando comuns na maioria dos aparelhos eletrônicos. Veja, neste vídeo, o processador fabricado pela Intel para facilitar a integração entre esses aparelhos e sua importância nos dias atuais. Vale ressaltar que surgem novas possibilidades para desenvolvimento de aplicações e de infraestrutura em redes de computadores.

http://olhardigital.uol.com.br/produtos/central_de_videos/dispositivos-inteligentes-a-caminho-da-sua-casa

### 1 - Função processamento

A Unidade Central de processamento (CPU) é responsável por grande parte das operações de um computador; ela é composta por milhares de componentes encapsulados em uma pastilha de silício. Os primeiros processadores tinham certa limitação em relação ao processamento dos dados, mas, conforme a tecnologia foi evoluindo, os processadores também evoluíram e, atualmente, temos processadores com alta capacidade de processamento. O primeiro processador foi projetado pela Intel. Conforme pode ser visto na figura abaixo, ele tem aparência de um chip comum.

![[oac1-03-fig02.webp]]

*Figura 1. Processador 4004 http://historiacomputadoresl.webnode. pt/servi%C3%A7os/componentes-ess*

Depois, foram projetados outros processadores contendo mais componentes internos sem aumentar o tamanho físico desses componentes. A figura 2 apresenta a evolução dos processadores Intel e AMD,

O microprocessador 4004 da Intel era composto por 2000 transistores. Como já foi descrito, ele era limitado em relação a operações e instruções a serem executadas. No início da década de 80, mais precisamente em 1981, a Intel lançou o processador 8088, o primeiro a ter 16 bits. Essa característica aumentou a velocidade de processamento, pois esses processadores podiam receber 16 bits de informações.  Fazendo uma análise um pouco mais profunda, trabalhar com 16 bits significa receber duas palavras de 8 bits. Até então os processadores podiam receber apenas uma palavra de cada vez; com 16 bits passaram a receber duas palavras de uma vez, ou seja, maior poder de processamento. O 8088 dispunha de 29.000 transistores e trabalhava com clock de 10 MHz. Um ano depois, em 1982, a Intel lançou o 286 com 139.000 transistores. Começava, então, a era x86, pois, até o momento, o 8086 era o único da série a ter sido lançado.

Em 1985, a Intel desenvolveu o 386 com 287.000 transistores e 32 bits. Foi o primeiro microprocessador a executar tarefas múltiplas; operava com clock de 33 MHz. No fim da década de 80, o 486 foi desenvolvido e oferecido ao mercado com um clock de 100 MHz. No final da década de 90, a quantidade de transistores passou a ser três vezes maior com o lançamento do Pentium III.

##### Unidade: Arquitetura e Organização de Computadores

O Pentium, que quebrou a série x86, foi apresentado em 1991 e continha 3 milhões de transistores. Em 2005, começou a era do multicore com o Intel Pentium D. Começava, a partir daí, a tecnologia Dual-Core em microprocessadores. Os avanços na tecnologia multicore continuaram surgindo: os processadores de quatro núcleos Intel Core 2Quad e outros processadores com mais núcleos em um único componente. Pelo que parece, essa evolução está longe de acabar.

![[oac1-03-fig03.webp]]

*Figura 2: http://www.hardware.com.br/dicas/processadores-iniciantes.html*

A evolução dos microprocessadores não está em apenas integrar milhões de componentes em um chip e aumentar a capacidade de clock. São desenvolvidos alguns meios para que a velocidade de processamento aumente; um deles foi o desenvolvimento do coprocessador aritmético. O coprocessador aritmético é um chip, ou parte de um chip, especialmente desenvolvido para realizar operações aritméticas complicadas. Os microprocessadores 80486 e Pentium têm um coprocessador interno. Esses coprocessadores aritméticos são especialistas em resolver cálculos com números decimais; eles conseguem resolver problemas mais rápido que a unidade Lógica e Aritmética.

A CPU, também conhecida como microprocessador, é encarregada de realizar as atividades relacionadas com a efetiva execução de uma operação, ou seja, tem a função de processar.

Processar o dado é executar com ele uma ação que produza algum tipo de resultado. Esta é a atividade fim do sistema de computação; ele existe para processar dados.

Entre as tarefas comuns a esta função - processamento - podem ser citadas as que realizam operações aritméticas, lógicas, movimentação de dados, desvios e operações de entrada e saída. O diagrama básico de um computador pode ser visto na figura abaixo. Note que há uma grande ênfase no processador, pois ele, em conjunto com o sistema operacional, é responsável pelo bom funcionamento do computador.

![[oac1-03-fig04.webp]]

*Figura 3: Diagrama básico do processador*

Perceba que a unidade aritmética e a unidade de controle são implementadas dentro da Unidade Central de Processamento (CPU). Ou seja, dentro do chip há circuitos combinacionais que desenvolvem as funções relacionadas às operações aritméticas e lógicas e que executam as instruções pela unidade de controle. Pela figura acima pode-se notar que as setas da unidade aritmética têm acesso direto à memória principal tanto para escrita quanto para leitura dos dados.

A unidade de controle tem a função de receber instruções, mais precisamente instruções/ dados, da unidade aritmética para decodificá-la e executá-la. Essas instruções/dados são enviadas pelo registrador de dados. Geralmente essas instruções/dados são endereçamentos e são usados para posicionar as instruções em algum ponto da memória principal para que possam ser lidas ou escritas.

A memória principal tem uma função bastante importante nos computadores digitais, pois é nela que fica armazenado todo e qualquer programa que está sendo executado. Portanto, tudo que nós vemos na tela, tudo que selecionamos com mouse está contido na memória principal para ser processado pela CPU. Dessa forma podemos concluir que a CPU faz a comunicação com a memória principal para capturar os dados ou instruções que nela estão armazenados. Esse é o conceito de programa armazenado que Von Neumann havia descrito em um de seus artigos e que é usado como base de todos os computadores digitais desenvolvidos atualmente.

Unidade: Arquitetura e Organização de Computadores

Pelo que foi descrito até agora, você já deve ter notado que a CPU faz o controle dos dados que devem ser lidos ou escritos na memória. Na memória principal, a qual chamamos de memória RAM, são armazenados dados e instruções: os dados, quando entram na CPU, são direcionados para a unidade lógica e aritmética; as instruções, quando entram na CPU, são direcionadas para a unidade de controle. É bom lembrar que os processadores contêm instruções próprias e limitadas projetadas pelos fabricantes e são elas que são executadas pela unidade de controle. Esse conceito, sobre dados e instruções, deve estar bem claro, pois iremos usá-lo futuramente.

O diagrama abaixo apresenta alguns componentes da unidade central de processamento (CPU), mais precisamente chamado de processadores. Vamos, primeiramente, conceituar cada um dos componentes internos do processador para depois entender a função de cada um deles de forma integrada.

![[oac1-03-fig05.webp]]

*Figura 4: Diagrama detalhado do processador*

UAL: a Unidade lógica e Aritmética tem como função receber dados para uma operação ou então comparação entre eles. Observe, na figura acima, que em um dos lados há duas entradas de dados para a UAL e do outro lado, uma saída. Isso significa que serão recebidos dois dados para uma operação aritmética ou comparação entre eles e o resultado sairá pelo outro lado da unidade lógica e aritmética.

Registradores (ACC): os dados vindos da memória principal ou os resultados obtidos pelo processamento na unidade lógica e aritmética podem ser inseridos, temporariamente, nos registradores. O acumulador (ACC) é um dos principais registradores dentro do processador, pois toda e qualquer operação é feita em relação a ele. Convém conceituar que esses registradores nada mais são que memórias de acesso rápido e estão inseridos dentro da unidade central de processamento para que a velocidade de comunicação entre ele e a unidade lógica e aritmética tenha melhor desempenho.

PC: significa contador de programas. Sua função é gerar endereços de memória para acessar os dados ou as instruções. Quando ligamos o computador, o contador de programa inicia-se com o endereço zero para que posicione no primeiro endereço de memória. Nesse endereço, os computadores são projetados para encontrar a memória FLASH, conhecida como BIOS, na qual se encontram as primeiras instruções para verificação do hardware e para carregar o sistema operacional do disco rígido para a memória principal.

MBR: este Registrador de Barramento de Memória tem a função de receber dados ou instruções que estão armazenados na memória ou de enviar dados ou instruções para a memória. Todos os dados ou instruções passam por este registrador no momento de leitura ou escrita; ele é a porta de saída ou de entrada do processador. Portanto, pelo conceito estabelecido, podemos concluir que, pelo MBR, trafegam dados ou instruções que vêm ou que vão para a memória principal.

MAR: o Registrador de Endereço de Memória recebe endereçamento tanto do contador de programa (PC) como também dos registradores de instruções. Sua função é apontar para o endereço de memória, indicando onde os dados ou instruções serão lidos ou escritos. Uma instrução pode indicar uma posição de memória. Quando isso ocorre, o decodificador de instruções envia para o registrador MAR esse endereço; por sua vez, o registrador MAR espelha esse endereço para o contador de programa e posiciona a memória para que os dados possam ser lidos ou escritos.

Relógio: o Relógio, como vimos anteriormente, tem a função de manter a sincronia de todos os componentes que estão dentro da unidade central de processamento. Ele gera sinais digitais síncronos para que os componentes mantenham, de forma síncrona, a comunicação dos dados.

UC: a Unidade de Controle tem como função receber uma instrução e decodificá-la. O barramento de controle é ligado aos componentes externos que recebem informações sobre leitura ou escrita e sobre o dispositivo em que essas ações devem ocorrer. Os dispositivos são identificados também por um endereço. Ele recebe essas instruções do registrador de instruções.

RI: o Registrador de Instrução recebe as instruções que estão armazenadas na memória. Sempre que uma instrução é carregada para a unidade central de processamento, ela é direcionada para este registrador. Sua função é decodificar essas instruções e passar parte dela para a unidade de controle e a outra parte para o registrador de endereçamento de memória.

Como se pode notar, muitos dos componentes são registradores que têm como função armazenar, temporariamente, um determinado dado. Esses registradores podem afetar a velocidade e, consequentemente, o desempenho do processador. Os computadores vendidos atualmente operam com 32 ou 64 bits. Isso determina o tamanho da palavra com que eles trabalham; quanto maior a palavra mais dados serão transportados em um ciclo. Portanto, se todos os outros recursos forem os mesmos em relação ao desempenho, um processador que usa um registrador que comporte palavras de 16 bits terá um desempenho duas vezes menor em relação a um processador que usa um registrador que comporte uma palavra de 32 bits. A tabela abaixo apresenta as características dos processadores durante toda a sua evolução, e, nela, você poderá verificar dados, como a data de desenvolvimento, quantidade de transistores, tamanho, velocidade de clock, o tamanho da palavra e quantos milhões de instruções por segundo caracterizavam os processadores em cada momento.

|Nome|Data|Transistores|Microns|Veloc de Clock|Largura de dados|MIPS|
|---|---|---|---|---|---|---|
|8080|1974|6.000|6|2 MHz|8 bits|0,64|
|8088|1979|29.000|3|5 MHz|16 bits<br>8 bits|0,33|
|80286|1982|134.000|1,5|6 MHz|16 bits|1|
|80386|1985|275.000|1,5|16 MHz|32 bits|5|
|80486|1989|1.200,000|1|25 MHz|32 bits|20|
|Pentium|1993|3.100,00|0,8|60 MHz|32 bits<br>64 bits|100|
|Pentium II|1997|7.500,00|0,35|233 MHz|32 bits<br>64 bits|300|
|Pentium III|1999|9.500,000|0,25|450 MHz|32 bits<br>64 bits|510|
|Pentium 4|2000|42.000,000|0,18|1,5 GHz|32 bits<br>64 bits|1.700|
|Pentium 4<br>“Prescott”|2004|125.000,000|0,09|3,6 GHz|32 bits<br>64 bits|7.000|
|Pentium D|2005|230.000,000|90 nm|2,8 GHz<br>3,2 GHz|32 bits||
|Core2|2006|152.000,000|65 nm|1,33<br>2,33 GHz|32 bits|26.000|
|Core 2 Duo|2007|820.000,000|45 nm|3 GHz|64 bits|53.000|
|Core i7|2008|731.000,000|45 nm|2,66 GHz<br>3,2 GHz|64 bits|76.000|

*Tabela 1: Microprocessadores Intel – fonte http://www.intel.com/pressroom/kits/quickreffam.htm*

#### 2.1 – Como funciona o processamento das informações

Acima, você conheceu a função de cada um dos componentes da unidade central de processamento. Esses componentes devem trabalhar de forma integrada, cada um executando as tarefas pelas quais são responsáveis. Mas o que acontece com os dados ou instruções que circulam pela unidade central de processamento?

Logo que o computador é ligado, o contador de programas (PC) é zerado, ou seja, o endereço do contador de programa é colocado em zero. Essa informação servirá como primeiro endereço para acessar uma instrução na memória, conforme descrito acima. Geralmente é no endereço zero que está a memória ROM com as primeiras instruções que, neste caso, se referem a um endereço. Sendo assim, o contador de programas envia essa informação (endereço) para o registrador de endereço (MAR), o qual posiciona-a no endereço zero da memória; neste caso, para os computadores atuais, esse endereço aponta para a BIOS.

Essa memória contém as primeiras instruções de verificação de periféricos e instruções para carregar o sistema operacional para memória principal. O registrador de endereço não lê as informações que estão na memória; ele apenas aponta para um determinado endereço, neste caso, informado pelo contador de programas (PC). Uma vez informado o endereço, o registrador de dados lerá a informação da primeira posição da memória; essa instrução será carregada e enviada, através do barramento interno, para o registrador de instrução (RI), pois, na primeira posição de memória, é conveniente que tenha uma instrução para iniciar todo o processo de boot. Deve ficar bem claro, até este momento, que todas as instruções seguirão esse fluxo, ou seja, passarão do registrador de dados para o registrador de instrução, o que ocorrerá caso a informação lida seja uma instrução. O registrador de instrução analisará essa instrução enviada a ele. Se essa instrução informar que um determinado dado deve ser lido em outra posição de memória, parte dessas informações, que neste caso é o endereço, vai para o registrador de endereço (MAR) e a outra parte da instrução, que será a instrução de leitura, irá para a unidade de controle. O registrador de endereço irá se posicionar nesse novo endereço informado pela instrução, e a unidade de controle acionará o circuito de leitura da memória, pois é exatamente isso que a instrução solicitou. Se já se tem o endereço e a unidade de controle solicitou a leitura dos dados, novamente o registrador de endereço pegará esse dado, posicionando-o em uma das entradas da unidade lógica e aritmética. Esse procedimento ocorre milhões de vezes por segundo na unidade central de processamento: ora é lida uma instrução, ora é lido um dado; a instrução é enviada para o registrador de instruções (RI) para ser decodificada, os dados são enviados para unidade lógica e aritmética para serem processados, executando uma operação aritmética ou comparação. Uma vez processados os dados da unidade lógica e aritmética, será retornado um resultado, o qual poderá ficar no acumulador ou em um dos registradores. Isso dependerá da instrução que está sendo executada.

De qualquer forma, o resultado será armazenado na memória principal. Dois fatos podem ocorrer aí: o resultado sairá da unidade lógica e aritmética e será gravado diretamente na memória principal através do registrador de dados ou o resultado da unidade lógica e aritmética será enviado para um registrador para, posteriormente, ser enviado para a memória principal. Todo esse conjunto tem que trabalhar de forma sincronizada. Os microprocessadores, conforme já descrito em aulas anteriores, têm um conjunto de instruções reduzidas e são essas instruções que vão determinar as operações que devem ocorrer dentro da unidade central de processamento. Qualquer linguagem de programação de alto nível, que tenha vários comandos para serem aplicados em um determinado programa, quando se apresentar em baixo nível, será convertida a uma dessas instruções de que o microprocessador dispõe.

![[oac1-03-fig06.webp]]

Há outro exemplo simples e mais genérico na análise do processamento dos dados. Conforme Norton (1996), pode-se utilizar a ideia de um cálculo matemático, neste caso, a multiplicação, para analisar o fluxo que os dados seguem para se obter o resultado. A ideia baseia-se no uso de uma calculadora sendo executada na tela do computador, idêntica à que está sendo apresentada na figura 5.

*Figura 5: Calculadora*

Suponha que a finalidade seja a multiplicação dos números 4 x 46 = e que a unidade de controle já enviou para a memória o primeiro número, o operador de multiplicação e também o segundo número. Dessa forma todos os dados para a operação já foram armazenados e, ao digitar o sinal de igual, o programa enviará uma instrução para a CPU efetuar a multiplicação.

Para cada instrução do programa, a CPU passa por um ciclo, do qual constam as seguintes etapas:

- a. um registrador recebe uma instrução da memória;

- b. procura-se o microcódigo correspondente àquela instrução;

- c. por último, executa-se o microcódigo.

Considerando o problema da multiplicação, a execução do microcódigo funcionará da seguinte forma:

- a. Carregue o primeiro número (4) para um registrador, neste caso, o registrador ax;

- b. carregue o segundo número (46) para o outro registrador, neste caso, o registrador bx;

- c. multiplique o valor contido no registrador ax pelo valor contido no registrador bx; o resultado insira no registrador cx;

- d. armazene o valor de cx na memória.

As duas primeiras instruções são muito parecidas. O que diferencia uma da outra é o registrador no qual serão armazenados os valores: o valor 4 será armazenado no registrador AX e o registrador BX receberá o valor 46. Ao ler a terceira instrução, a unidade de controle passa para a Unidade de Lógica e Aritmética a responsabilidade de efetuar a operação de multiplicação.

Conforme já foi citado, os processadores contêm um conjunto limitado de instruções e, dentre estas, há muitas que podem ser usadas para realizar a operação de multiplicação. Uma das técnicas que podem ser usadas na multiplicação entre dois números chama-se deslocamento de bits, ou seja, basta deslocar os bits para a esquerda na quantidade que se deseja multiplicar. Vamos analisar como funciona essa técnica com os valores que estamos trabalhando ( 4 x 46 ). O número 46, representado em binário, equivale a 00101110. Ao se deslocarem uma vez os bits para a esquerda, temos como resultado o valor 01011100, que, convertido para decimal, tem como resultado o número 92. Como os bits do número 46 foram deslocados apenas uma vez, a multiplicação efetuada foi 46 x 2, tendo como resultado o valor 92. Isso significa que, para obter o resultado da operação 46 x 4, temos que deslocar os bits do número 46 mais uma vez, portanto ele ficará da seguinte forma  10111000. Convertendo esse valor para o decimal, temos o número 184, que corresponde ao valor esperado da multiplicação.

O resultado será enviado pela unidade central de processamento para a memória e, finalmente, ele será enviado para o monitor de vídeo.

### 2 - Processadores RISC e CISC

Os processadores mais comuns encontrados em pequenos computadores são processadores para computação com um conjunto complexo de instrução – CISC. Eles têm como característica um conjunto de instruções grandes com centenas de instruções.

Outro tipo de processador foi projetado sob a seguinte teoria: se for um  conjunto de instruções pequenas, então muitas instruções serão repetidas e, consequentemente, serão executadas de forma mais rápida, permitindo ao processador concluir mais instruções durante um período de tempo com um custo menor de fabricação, pois serão necessários menos componentes internos para interpretar as instruções. A este tipo de CPU foi dado o nome de processadores RISC (ReducedInstruction Set Computing) ou processadores para computação com conjunto reduzido de instruções.

São exemplos de processadores CISC o 386 e 486, portanto, conforme conceito estabelecido, esses processadores são capazes de executar várias centenas de instruções complexas diferentes.

Atualmente os processadores são projetados com uma arquitetura híbrida, ou seja, usam o que tem de melhor a arquitetura RISC e o que tem de melhor a arquitetura CISC. São exemplos de processadores que utilizam arquitetura híbrida os processadores Pentium II, III e AMD e também o G4, utilizado nos Macintoshs.
