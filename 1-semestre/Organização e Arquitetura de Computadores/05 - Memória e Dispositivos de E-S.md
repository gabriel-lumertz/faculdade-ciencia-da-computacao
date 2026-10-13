---
materia: "Organização e Arquitetura de Computadores"
modulo: "Memória e Dispositivos de E-S"
semestre: 1
unidade: 5
tipo: material-teorico
fonte: "raw/1-semestre/ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES/Organização e arquitetura de computadores 05.pdf"
tags: [faculdade, organizacao-e-arquitetura-de-computadores, semestre-1]
aliases: ["Organização e Arquitetura de Computadores - Unidade 5"]
---

# Memória e Dispositivos de E-S

#### Memória e Dispositivos de E/S

- Memórias

- Dispositivos de Entrada e Saída

###### Nesta unidade, você irá estudar sobre os meios de armazenamento primário e secundário, além de conhecer características básicas de alguns dispositivos de entrada e saída. Os trabalhos que desenvolvemos devem ficar armazenados em algum dispositivo para que possamos utilizá-los. Você irá aprender que estes dispositivos são chamados de memória primária (ou memória RAM) e memória secundária. Todas as informações que estão na memória RAM são apagadas assim que o computador é desligado, por este motivo foram desenvolvidos os dispositivos secundários.

Nesta quinta aula, você irá estudar sobre os vários dispositivos para armazenamento primário e secundário disponíveis, irá entender como são construídos e como a evolução da tecnologia nos permite gravar mais informações sem aumentar o tamanho destes dispositivos. Você encontrará também informações sobre alguns dispositivos de entrada e saída.

Nesta quinta e última aula você irá estudar sobre os dispositivos de armazenamento, principalmente os vários tipos de memória RAM e memórias secundárias, além de uma introdução básica aos dispositivos de entrada e saída.

O primeiramente deve-se ler a contextualização, e nela você irá conhecer algumas técnicas para melhorar o desempenho do seu computador sem ter que investir em hardware.

Logo em seguida, você deverá ler o _conteúdo_ da aula, você encontrará, como primeiro assunto, detalhes da memória RAM. Hoje há vários tipos de memórias e você irá conhecer quais as diferenças entre elas. Além disto, poderá verificar alguns procedimentos executados pelo computador em relação à memória que prejudicam seu desempenho. Seguindo o texto, você estudará também características das memórias secundárias. Há vários modelos de memória secundária e nela armazenamos nossos trabalhos para poder usá-los futuramente. Houve uma evolução significativa nas memórias secundárias e você poderá conhecer algumas delas. Além destes assuntos, você irá estudar sobre dispositivos de entrada e saída.

Todo o conteúdo deve ser lido com bastante atenção e deve ser compreendido. Desta forma, você estará apto a prosseguir com as atividades que serão propostas.

Após estudar o texto, você deverá analisar a _apresentação narrada_ . Nele você poderá estudar os pontos relevantes do assunto desta quinta aula.

Com estes conceitos já desenvolvidos, você estará pronto para participar do fórum e das atividades.

Participe do fórum de discussão, poste suas dúvidas para que possamos esclarecê-las.

Vamos iniciar?

### Contextualização

A velocidade de processamento dos trabalhos submetidos ao processador depende também de como a memória está sendo usada. Se a memória RAM estiver com quase toda a capacidade sendo usada, então você terá problemas. E se a memória secundária também estiver com sua capacidade quase que tomada, então também você terá problemas de desempenho. Veja no link abaixo como fazer para deixar o seu computador com um desempenho aceitável sem ter que investir em hardware.

http://windows.microsoft.com/pt-BR/windows7/Optimize-Windows-7-for-better-performance

### 1. Memórias

Numa breve definição, memória é um dispositivo capaz de armazenar informações e, quando solicitado, fornecê-las. A memória eletrônica começou a ser viabilizada a partir da ideia de programa armazenado, elaborada por Von Neumann. Até então, havia a possibilidade de armazenamento das informações em dispositivos que não eram eletrônicos, como fita de papel.

Na década de 40, algumas iniciativas em busca de formas de armazenamento digital foram feitas, porém algumas delas foram desenvolvidas para uso específico, como o computador eletrônico digital projetado pelo professor John Vincent Atanasoff da Universidade de Iowa nos EUA. Este computador utilizava memória de varredura mecânica, usando capacitores com cilindros rotativos que continham contatos elétricos interligados por capacitores de papel.

![[oac1-05-fig02.webp]]

**Figura 1:** Computador ABC. **Fonte** : en.wikimedia.org.

O ENIAC, um dos primeiros computadores digitais, já usava o conceito de memória. No entanto, sua programação ainda tinha algumas restrições, pois era feita através de uma central de comutação, muito parecida com uma mesa telefônica. Isto tornava a programação muito lenta. Era necessário que a programação pudesse ser feita de forma eletrônica também.

Para armazenamento das informações, o ENIAC usava válvulas,  componente que tem um tamanho considerável em relação aos componentes utilizados atualmente, por este motivo que o ENIAC ocupava grande espaço para comportar sua estrutura.

![[oac1-05-fig03.webp]]

**Figura 2:** Parte da estrutura do ENIAC. **Fonte** : en.wikimedia.org.

O UNIVAC começou a inovar a forma de armazenar as informações. Utilizava uma memória de ferrite, que ainda era uma forma rudimentar de armazenar informações. Esta memória tinha 1024 bits e conseguia armazenar 128 Bytes de informação, muito pouco para os dias atuais.

Na década de 70, a Intel lançou o primeiro chip DRAM (Dynamic Random Access Memory ) que veio substituir a memória de ferrite. Este chip foi usado no computador HP 9800. Atualmente, o acesso à memória de forma aleatória, conhecida como memória RAM, ainda é largamente usada no armazenamento de informações que estão sendo executadas. As memórias evoluíram e tornaram-se cada vez menores. Alguns problemas ainda são encontrados, como velocidade de acesso e resposta, no entanto as pesquisas continuam no sentido de melhorar estas características.

Vamos estudar vários dispositivos de armazenamento, ver como eles funcionam e conhecer suas características.

##### Memória RAM

A memória RAM é basicamente formada por conjuntos de transistores combinados que acabam formando uma estrutura chamada _flip flops_ . Este tipo de memória tem como característica a vantagem de ser lida e escrita pela CPU continuamente, no entanto, quando a máquina é desligada, perde suas informações.

A memória DRAM (Memória de Acesso Aleatório Dinâmico) é composta por um transistor e um capacitor conectados formando uma célula de memória capaz de armazenar um bit de dado. O capacitor é um componente que tem como característica manter, mesmo que seja por milésimos de segundos, a informação desejada. Se não houver uma atualização (à qual chamamos de _refresh_ ), o dado é perdido. Para evitar que as informações sejam perdidas, o controlador de memória ou a própria CPU devem carregar todos os capacitores mantendo a informação armazenada. Esta técnica acontece várias vezes por segundo, neste tipo de memória, e tem como agravante o processo para manter estas informações armazenadas, o que acaba tornando a memória lenta.

![[oac1-05-fig04.webp]]

**Figura 3:** Representação de células em uma memória DRAM.

**Fonte:** http://blogdjau.blogspot.com.br/2011_02_01_archive.html

Na figura acima, podemos observar que cada intersecção entre linhas e colunas tem uma célula de memória composta um por um transistor e um capacitor. A intersecção entre linha e coluna é ativada para representar o bit 1 ou desativada para representar o bit 0. Cada célula é definida por um endereço que se dá por esta intersecção.

A memória RAM estática usa uma técnica totalmente diferente da memória dinâmica. Ela é construída de maneira que um conjunto de quatro ou seis transistores, montados de forma combinacional (FLIP FLOPS), represente uma célula para armazenar uma informação. 10

Neste tipo de técnica, não há necessidade de refrescamento da memória, pois o conjunto de transistores mantem a informação sempre ativa, além de ser significativamente mais rápida que a RAM dinâmica. Uma desvantagem deste tipo de técnica fica por conta do tamanho do componente (chip) para armazenar as informações. Isto se deve à quantidade de transistores usados para compor uma célula. Como visto acima, temos que ter de quatro a seis transistores para formar uma célula com capacidade de armazenar apenas um bit.

Por ser mais rápida, a memória RAM estática é usada como memória cache, geralmente implementada dentro dos processadores, e a memória RAM dinâmica é usada como memória RAM, mais conhecida como memória DRAM.

Além da SRAM (memória estática) e da DRAM (memória dinâmica), há outros modelos de memória RAM, cada um com uma característica diferente, conforme pode ser observado abaixo.

- **FPM DRAM** ( _Fast Page Mode_ ou memória RAM de modo de paginação rápida): usa a mesma técnica de armazenamento da memória dinâmica, no entanto evolui na forma de leitura e escrita na memória. Ela parte do princípio de que a maioria das informações é gravada de forma sequencial na memória, com isto é possível trabalhar na forma de enviar o endereçamento para a leitura das informações.

- **EDO DRAM** ( _Extended Data-Out_ ou memória RAM de saída estendida): segue a técnica usada na FPM RAM, porém não aguarda toda a leitura de um bit para começar a ler o próximo. Com esta técnica é possível aumentar o desempenho em até 5% em relação à memória FPM DRAM.

- **SDRAM** ( _Synchronous DRAM_ ou memória DRAM síncrona): também tem como princípio que os dados são colocados sequencialmente na memória, sendo assim é posicionado na linha e movido rapidamente pela coluna para obter as informações. O sincronismo refere-se ao uso do mesmo ciclo de clock da placa mãe para leitura e escrita.

- **DDR SDRAM** ( _Double Data Rate SDRAM_ ou Memória SDRAM com taxa de transferência dupla): tomou como base a técnica usada na SDRAM, no entanto transfere dois dados por pulso de clock. Teoricamente obtém-se o dobro do desempenho se tomarmos como base a transferência de um dado a cada pulso de clock.

- **RDRAM** ( _Rambus DRAM_ ou memória RAM dinâmica de Rambus): é uma memória dinâmica, porém alterou sua arquitetura em relação à DRAM. Ela usa um barramento interno de alta velocidade batizado como Rambus, opera com taxa de dados de 800 Mhz ou 1.600 MB/s.

- **VRAM** ( _Vídeo RAM_ ): é uma memória usada em adaptadores de vídeo ou aceleradores 3D. Este tipo de memória tem duas portas (multiporta) e isto acelera a gravação e leitura, pois simultaneamente pode ser acessada pela CPU e pelo processador gráfico.

A memória RAM é muito importante no conjunto da arquitetura de computadores. Ela armazena todos os programas e dados que serão executados pelo processador, no entanto é uma memória volátil, ou seja, desligando o computador as informações serão perdidas. Esta característica exige que a maioria das informações processadas seja gravada em um tipo de memória não volátil para uso futuro (veremos alguns exemplos mais abaixo), no entanto sempre que executamos um programa que não esteja na memória RAM ele deverá ser buscado na memória não volátil e inserido na memória RAM para que seja executado pelo processador.

Analisando desta forma, é fácil verificarmos que quanto mais aplicativos abrirmos simultaneamente, mais memória acaba sendo consumida e se o computador for composto de pouca memória RAM, então a concorrência pelo seu uso será inevitável. O aplicativo que queremos executar será carregado para a memória RAM, no entanto algum outro aplicativo deverá deixar a memória para que este ocupe um espaço. Este controle é feito pelo sistema operacional, que decide, por algumas técnicas implementadas, qual aplicativo deixará a memória volátil para que o outro aplicativo ocupe este espaço. Este processo de liberar espaço na memória RAM para carregar outro aplicativo de uma memória não volátil é chamado de “swap” e quanto mais _swaps_ ocorrerem, mais lenta ficará a execução dos programas. A lentidão ocorre porque os itens abaixo devem ser checados:

- Verificar se há espaço na memória RAM;

- Não havendo espaço, analisar qual aplicativo pode deixar a memória RAM para execução do outro;

- Salvar status das informações e dos aplicativos que irão ser descarregados da memória RAM em uma memória não volátil;

- Liberar espaço na memória RAM conforme verificação feita;

- Carregar o aplicativo e as informações para a memória RAM.

Os itens descritos acima são controlados pelo sistema operacional e levam um tempo para serem executados. Dois itens - “salvar status das informações...” e “Carregar o aplicativo e as informações...” - descritos acima, contribuem ainda mais para a lentidão, pois envolvem leitura e escrita através do acionamento de partes eletromecânicas. Geralmente os aplicativos que queremos executar estão gravados em uma memória não volátil, por exemplo, o HD (Hard Disk) e como veremos mais abaixo, a leitura e escrita nestes dispositivos de entrada e saída exigem o acionamento de partes mecânicas que contribuem para a lentidão do conjunto.

Na figura abaixo, pode-se verificar a troca de processos entre memória RAM e o HD: a memória RAM já está cheia e deve ser liberado espaço para que o programa a ser executado ocupe um espaço. Vale ressaltar que algumas informações sobre o aplicativo que está saindo da memória RAM, e também as informações, devem ter seu status armazenado em algum lugar, pois se o usuário voltar ao aplicativo que está ainda em aberto para ele, este procedimento de swap deve novamente ser feito para trazer, no ponto em que estavam, o aplicativo e as informações.

![[oac1-05-fig05.webp]]

**Figura 4:** Swapping. **Fonte:** http://ces33.wikidot.com/gerenciamento-de-memoria

##### 1.1 Memória Secundária

Conforme estudado até agora nesta unidade, você pôde perceber que se desligarmos o computador, as informações que estão armazenadas na memória RAM são perdidas, portanto temos que gravar os trabalhos que estamos desenvolvendo em algum local onde poderemos resgatá-los quando for preciso. Para estes casos, as informações são armazenadas em algum dispositivo de memória secundária.

Existem vários tipos de armazenamento secundário que são divididos em três grupos: armazenamento magnético, armazenamento óptico e armazenamento usando memória Flash.

Os principais tipos de armazenamento magnético são:

- Disquetes (pouquíssimo utilizados atualmente);

- Discos Rígidos;

- Fitas magnéticas;

Os principais tipos de armazenamento óptico são:

- CD-ROM

- DVD

O armazenamento em memória Flash usa um chip de memória para gravação.

- 1.1.1. Armazenamento Magnético

As informações relevantes para nós, seres humanos, devem ser gravadas em dispositivos para que possamos recuperá-las futuramente. Como já vimos, chamamos estes dispositivos de memória secundária. Estes dispositivos se diferenciam na forma como os bits são gravados para posterior resgate. No armazenamento magnético, os dados são gravados de forma semelhante, mesmo que os dispositivos tenham formatos diferentes. Os meios magnéticos de armazenamento são cobertos de partículas minúsculas de ferro que, quando estimuladas por uma corrente elétrica, formam um campo magnético semelhante a um imã.

Conforme apresentado na figura abaixo o cabeçote de leitura e gravação percorre a superfície com partículas de ferro carregando-as magneticamente quando passa por elas, portanto no momento de gravação das informações há uma corrente elétrica no cabeçote de leitura e gravação. Os bits “1” e “0” são representados alterando a direção da corrente elétrica.

![[oac1-05-fig06.webp]]

**Figura 5:** Leitura e Gravação no meio magnético

**Fonte:** http://palazzo.pro.br/Joomla/pt-BR/homepage/tecnologia/152-disco-magnetico.html

Para ler os dados que estão gravados, o cabeçote de leitura e gravação passa pela superfície sem corrente elétrica, porém como a superfície magnética do meio de armazenamento tem carga magnética, então ela emite uma pequena corrente que é capturada pela cabeça de leitura e gravação. Dependendo do sentido da carga magnética, obtêm-se os bits 1 e 0.

Os disquetes e as fitas magnéticas têm esta característica e foram usados por um período grande para armazenar informações.

![[oac1-05-fig07.webp]]

**Figura 6:** Disquete 3<sup>1/2</sup> **. Fonte:** toca do tazbugado

O problema com este tipo de armazenamento está no transporte e no local onde serão guardados, pois não podem ficar expostos próximos a imãs e qualquer situação onde possa ser criado um campo magnético, como é o caso de transporte em metrô e fios de alta tensão.

Os discos rígidos têm o mesmo princípio de gravação e leitura de um disquete, mas são diferentes quanto ao material usado: enquanto um disquete usa uma superfície flexível, o disco rígido, como o próprio nome já define, é construído com uma superfície rígida e com vários discos (que chamamos também de pratos de metal), que gira sobre um eixo. Os pratos são revestidos de óxido de ferro e são envoltos por uma caixa selada conforme pode ser visto na figura 7. Todas estas características ajudam na precisão da leitura e gravação das informações,

![[oac1-05-fig08.webp]]

**Figura 7:** Discos rígidos. **Fonte:** Projeto idec

Tanto os disquetes quanto os discos rígidos são organizados na forma de setores e trilhas, organização que ocorre quando os formatamos. Conforme pode ser observado na figura 5, cada trilha é composta por vários setores; quando se formata um disco, um conjunto de trilhas é criado. Cada trilha de um disco é dividida em partes menores, a que chamamos de setores e cada setor recebe um número de identificação. Desta forma, fica mais fácil a cabeça leitora se deslocar de uma forma aleatória e não sequencial, como acontece com as fitas magnéticas.  Para aumentar a capacidade de armazenamento, é possível armazenar informações dos dois lados do disco.

##### 1.1.2 Armazenamento Óptico

Com o passar do tempo, conforme a quantidade de dados foi crescendo, houve a necessidade de desenvolver meios de armazenamento cada vez mais compactos e com maior poder de armazenamento. Uma das soluções foi gravar as informações em CD/DVD.

Para gravar dados em CD/DVD usa-se a técnica de armazenamento óptico, que oferece precisão altíssima através do feixe de luz. Desta forma consegue-se representar um bit no menor espaço possível, ou seja, em uma área com proporções pequenas podemos gravar muito mais informações. O laser produz um feixe de luz concentrado, ou seja, toda a energia da luz é alinhada na mesma direção, permitindo que seja focalizada com uma precisão máxima uma área muito pequena.

Para entender como os dados são gravados em um CD/DVD precisamos primeiro entender como eles são desenvolvidos.

Conforme podemos ver na figura 8, os CDs têm quatro camadas. A maior parte do material corresponde ao policarbonato (99%), o restante (1%) divide-se em uma camada refletiva, uma de proteção e por último, a camada que decora o disco, que se define como etiqueta. A camada refletora, geralmente composta de prata, armazena as informações no CD em forma de plataforma ou depressão. O ponto que reflete a luz do sensor de laser é a plataforma e o ponto que dispersa a luz é chamado de depressão. Com esta técnica, os valores binários são armazenados no CD.

![[oac1-05-fig09.webp]]

**Figura 8:** Composição de um CD. **Fonte** :http://www.tecmundo.com.br/dvd/8778-como-sao- feitos-os-discos-de-cds-dvds-e-blu-rays-.htm

A diferença entre um CD-R e um CD-RW, está em um material a mais, adicionado entre a camada de policarbonato e a camada protetora, que consiste em uma tinta que permite que o laser modifique os dados gravados.

A capacidade de armazenamento de uma empresa e até mesmo de um usuário residencial tem que ser bastante grande, pois a cada dia necessitamos de mais espaço para armazenar filmes, músicas, dados, imagens e fotos. O mercado nos oferece algumas alternativas, como o DVD e o Blu-ray. O processo de gravação e leitura são os mesmos usados pelos CDs, no entanto, como pode ser observado na figura 9, o laser usado tem o feixe de luz mais fino, possibilitando ler e escrever mais informações em uma área semelhante à dos CDs.

O problema do armazenamento nestes dispositivos está no tempo de acesso às informações. Este tempo está relacionado a dois fatores: a velocidade com que o disco gira e o tempo para levar a cabeça de leitura até a trilha onde se encontram as informações solicitadas. Por ter partes mecânicas envolvidas em todo o processo, desde a requisição da informação até a disponibilização dela para o usuário, torna-se lento em relação às informações que já se encontram na memória RAM.

A evolução não para e novos dispositivos estão sendo projetados para substituir, gradativamente, os dispositivos que usam partes mecânicas para armazenamento. Atualmente, principalmente em substituição de HDs, os componentes SSDs (Unidade de Estado Sólido) estão sendo usados.

![[oac1-05-fig10.webp]]

**Figura 9:** Característica CD, DVD e Blu-Ray. **Fonte:** http://www.tecmundo.com.br/dvd/8778-como-sao-feitos-os-discos-de-cds-dvds-e-blu-rays-.htm

Estes componentes são conhecidos por memória Flash e já são vendidos no formato de pen drive. O futuro destes componentes é promissor. Há uma vertente que acredita que em um futuro próximo, assim que o preço começar a baixar devido à produção em massa, estes componentes se tornarão comuns em computadores pessoais e servidores de grande porte.

### 2. Dispositivos de Entrada e Saída

Introduzir dados do meio externo para processamento em uma máquina ou então ter acesso a informações processadas por ela é uma das características mais importantes na interação homem máquina. Os aplicativos e/ou programas têm esta função de interação, no entanto para que isto seja viabilizado há vários dispositivos que permitem a introdução, ao quais chamamos de “dispositivos de entrada” e a apresentação destas informações, ao quais chamamos de “dispositivos de saída”. Como dispositivos de entrada, podemos citar o teclado, caneta ótica e o mouse, dentre outros. Como dispositivos de saída, temos a impressora, o monitor, plotter e outros que você irá estudar nesta unidade.

Na arquitetura de um computador há componentes que se encarregam de intermediar a comunicação do meio externo com o interno e também do meio interno para o meio externo. Estes componentes têm a função de portas de I/O ( _Input / Output_ , ou Entrada e Saída). Portanto, as portas de I/O são os dispositivos encarregados de estabelecer comunicação entre o meio interno do qual fazem parte e um dispositivo externo qualquer. Considerando desta forma, existem I/Os desde os mais elementares, até os que algumas vezes chegam a ser mais sofisticados do que a própria CPU ao qual estão ligados, que em alguns casos podem até ter dentro de si outro microprocessador para coordenar o trabalho.

##### 2.1. Tipos de I/O

Podemos, em princípio, usar qualquer método em hardware para retirar ou colocar informações para processamento. Os métodos mais comuns usados são:

- Comunicação entre equipamentos (Série ou Paralela);

- Comunicação com o usuário (Controle de teclado, displays, vídeo);

- Controle de equipamentos (sensores, motores, conversores);

- Funções especiais (Timers, priorizadores, etc.);

A comunicação serial foi uma das primeiras a serem disponibilizadas nas máquinas para viabilizar a comunicação com o meio externo. Este tipo de comunicação caracteriza-se pelo envio dos dados usando um único canal de comunicação. Ou seja, para transmitir uma palavra de 8 bits, eles devem passar por um componente que irá serializá-los, dispondo cada bit no tempo para depois efetuar a transmissão. A figura abaixo demonstra a transmissão serial.

![[oac1-05-fig12.webp]]

**Figura 10:** Transmissão serial. **Fonte:** http://pt.kioskea.net/contents/pc/serie.php3

Este tipo de transmissão tem um desempenho menor que a transmissão paralela, pois os dados devem ser enfileirados para depois serem transmitidos.

A transmissão paralela consiste em enviar todos os 8 bits de forma paralela de uma única vez. Desta forma, conforme pode ser observado na figura abaixo, não há necessidade de enfileirar cada bit da palavra para transmiti-los.

![[oac1-05-fig13.webp]]

**Figura 11:** Transmissão Paralela. **Fonte:** http://pt.kioskea.net/contents/pc/serie.php3

Transmitindo desta forma o desempenho é bem melhor, embora o custo deste tipo de transmissor seja mais elevado que o serial, pois, para uma transmissão serial há apenas um circuito para transmissão e na transmissão paralela, vários circuitos deverão ser montados, aumentando assim o custo.

A comunicação com usuários é feita através de dispositivos de saída que convertem os sinais elétricos em um formato que possamos entender e os dispositivos de entrada convertem os sinais que entendemos para sinais elétricos. Vamos conhecer o funcionamento de alguns dispositivos de entrada e depois veremos alguns dispositivos de saída.

##### 2.2. Teclado

## Para Pensar

Como bem sabemos, o teclado é um dispositivo de entrada. Sua principal função é converter em sinais elétricos o que está sendo digitado. Até este ponto nada de novidade. Mas, como funcionam os teclados?

O teclado é composto por um controlador ou processador e uma grade de circuitos (matriz), combinados de forma a representar qualquer tecla que compõe o teclado. Em linhas gerais, quando uma tecla é pressionada, o controlador recebe um sinal que identifica a tecla pressionada; de posse desta informação, ele envia uma solicitação de interrupção para o processador (CPU). O programa ou aplicativo que está sendo utilizado avalia a solicitação que está armazenada em um buffer para dar a resposta adequada.

![[oac1-05-fig15.webp]]

**Figura 12:** Detalhes do esquema técnico de um teclado tipo spectrum. **Fonte:** http://www.garrettimus.org/CantinhoSpeccy/print/tecladopc_00.html.

Existem vários tipos de materiais usados para identificar a tecla pressionada, dentre eles podemos citar:

- Domo de borracha

- Membrana

- Contato metálico

- Elemento de espuma.

##### 2.3. Mouse

A partir do momento que a interface gráfica foi desenvolvida, o mouse passou a ter sua importância no mundo dos computadores. Os primeiros mouses foram desenvolvidos utilizando-se de uma técnica a partir de um plano de coordenadas cartesianas (pontos x e y). Para isto utiliza-se uma bola e duas rodinhas, uma representando o eixo x e outra representando o eixo y. Quando o mouse é movimentado sobre uma superfície plana, a bola movimenta as rodinhas e esses movimentos são detectados por sensores que enviam as informações para o computador na forma de alterações na posição atual do ponteiro ou cursor.

O mouse ótico não tem partes mecânicas e sim um fotodetector que percebe o movimento efetuado sobre uma plataforma plana e envia as coordenadas para o computador.

##### 2.4. Tela sensível ao toque

Algumas telas atualmente são desenvolvidas para reconhecimento de toque. A ideia é basicamente a mesma para todas, ou seja, o objetivo é detectar alterações a partir do momento que há uma intervenção (toque) na superfície. Há vários tipos de circuitos desenvolvidos para detectar esta alteração a partir do toque, as mais usadas são as que usam circuito para monitorar as mudanças de estados. Os _tablets_ permitem que seja usado um sistema de reconhecimento de multitoques. Ou seja, pode-se tocar em dois pontos da tela para, por exemplo, realizar um zoom ou então reduzir uma imagem ou texto.

##### 2.5. Monitor de vídeo

Há vários dispositivos de saída, sendo os mais importantes o monitor de vídeo, a impressora e o sistema de som.

O monitor de vídeo, segundo Norton (1996), cria imagens com um tipo especial de cristal líquido que normalmente é transparente, mas fica opaco quando carregado com eletricidade.

##### 2.6. Impressoras

A impressora ainda tem função importante no conjunto computacional, pois não foi totalmente substituída apenas por documentos digitais. Há vários tipos de impressoras, desde as matriciais, jato de tinta, laser, toner e até impressoras em 3D.

Há vários outros dispositivos de entrada e saída disponíveis para computadores; o que diferencia um do outro são as interfaces para serem conectadas aos _slots_ e os _drivers_ desenvolvidos pelos fabricantes para comunicação com o sistema operacional.
