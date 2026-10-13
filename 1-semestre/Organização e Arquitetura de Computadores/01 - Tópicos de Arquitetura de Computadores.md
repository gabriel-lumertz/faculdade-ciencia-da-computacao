---
materia: "Organização e Arquitetura de Computadores"
modulo: "Tópicos de Arquitetura de Computadores"
semestre: 1
unidade: 1
tipo: material-teorico
fonte: "raw/1-semestre/ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES/Organização e arquitetura de computadores 01.pdf"
tags: [faculdade, organizacao-e-arquitetura-de-computadores, semestre-1]
aliases: ["Organização e Arquitetura de Computadores - Unidade 1"]
---

# Tópicos de Arquitetura de Computadores

## Tópicos da Unidade

- Introdução – Histórico

- Conceitos básicos

- Arquitetura de Von Neumann

- Computadores de uso geral e computadores de uso específico

- Medidas de desempenho

- Representação da Informação

##### Nesta primeira aula, você irá conhecer um pouco sobre a evolução dos computadores, os conceitos que envolvem a arquitetura básica de um computador e outros conceitos, como medida de desempenho, computadores de uso geral e específico e representação da informação. Iniciaremos com um breve histórico e, depois, ao ler o texto, você poderá compreender a ideia de Von Neumann e a arquitetura básica de um computador.

Você poderá esclarecer os pontos sobre os quais ainda tenha dúvidas através do fórum de discussão. Sua participação é importante como contribuição para o desenvolvimento de todos.

## Atenção

Para um bom aproveitamento do curso, leia o material teórico atentamente antes de realizar as atividades.  É importante também respeitar os prazos estabelecidos no cronograma.

## Contextualização

Abaixo, encontram-se trechos do artigo “Um Processador Básico para o Ensino de Conceitos de Arquitetura e Organização de Computadores” de Morandi. D. et al. disponível em < http://revistaseletronicas.pucrs.br/ojs/index.php/hifen/article/view/3779/2891 >, acessado em 22.04.2012. Nesse artigo é apresentada a importância do conhecimento da Arquitetura para uma melhor compreensão da programação. Leia, abaixo, alguns pontos relevantes.

“O estudo do funcionamento de um computador e de seu processador é fundamental na formação de alunos de cursos de graduação em Computação. Isso porque determinados conceitos utilizados nas disciplinas da área de Algoritmos e Programação são melhor compreendidos pelos alunos quando eles entendem os seus significados ao estudar a arquitetura do computador.

Para as fases iniciais, a seleção de processadores para o ensino concorrente da lógica de programação e de conceitos de arquitetura de computadores deve facilitar o estabelecimento de relações entre as abstrações lógicas necessárias à programação e a implementação dessas abstrações em hardware.

Nesse contexto, ao buscar estabelecer uma relação entre as necessidades dos alunos que estão iniciando a programar e as representações em hardware correspondentes, devem-se identificar os principais pontos em comum que são tradicionais fontes de incompreensão para os estudantes e que podem ser elucidados de forma concreta. Como exemplo, podem ser mencionadas as relações entre: (i) declaração de variável e alocação de memória; (ii) constantes e operandos imediatos; (iii) atribuição de variáveis e sua correspondência com as operações de acesso à memória; e (iv) operações aritméticas e sua execução no hardware,; entre outras relações.”

Estudar a arquitetura de computadores realmente nos ajuda a entender determinados conceitos abstratos tratados isoladamente nas disciplinas de programação de computadores.

## Introdução – Histórico

O computador consiste em um conjunto de circuitos eletrônicos organizados para funcionar como um sistema integrado, realizando inúmeras tarefas de uso geral. Esta incrível máquina funciona devido a programas, como sistemas operacionais e aplicativos, que comandam os circuitos ao qual chamamos de hardware. Estudar arquitetura e organização dos computadores nos ajudará a entender determinados aspectos que podem influenciar o desenvolvimento de aplicativos. Para que possamos entender a arquitetura atual, é interessante conhecermos a evolução dos computadores, portanto prepare-se para voltar ao tempo em que os computadores não eram essenciais à vida dos seres humanos.

No dicionário, o verbete para a palavra computador apresenta, entre outras, a seguinte definição: “aquele que faz cômputos, cálculos". Quem já estudou a história dos computadores terá em mente que o primeiro **computador eletrônico desenvolvido foi o "ENIAC"** , mas, se considerarmos a definição do dicionário, então, chegaremos à conclusão de que o ENIAC não foi o primeiro aparelho desenvolvido para computar. Mais abaixo você irá notar que ele foi o primeiro computador digital projetado. Mas vamos por partes até chegar a ele.

As primeiras anotações, segundo Garbi, aconteceram com a invenção da escrita em meados do quarto milênio a.C. Com a evolução da escrita e com o conhecimento que o homem já tinha em relação a quantidades, foi possível desenvolver técnicas para fazer anotações em _tablets_ de barro cozido. Conforme o homem foi evoluindo, as necessidades de realizar cálculos mais rápidos também foram crescendo. Uma das primeiras ferramentas desenvolvidas para auxiliar o cálculo chama-se Ábaco. A data do desenvolvimento do ábaco é imprecisa; algumas fontes descrevem que os babilônios o usavam para realizar cálculos por volta de 2.400 a.C. Na Idade Média os romanos também o usavam, no entanto o aperfeiçoamento dessa ferramenta foi feita pelos japoneses e chineses.

![[oac1-01-fig02.webp]]

**Figura 1:** Ábaco, **Fonte:** http://www.educ.fc.ul.pt/docentes/opombo/seminario/abaco/index.htm

É lógico que outras ferramentas foram inventadas para auxiliar o homem a calcular com maior rapidez; não é nossa intenção descrever todas elas. Vamos nos concentrar somente naquelas que contribuíram, de alguma forma, para o desenvolvimento e evolução dos computadores digitais. O ábaco não supria todas as necessidades dos intelectuais do século XVII, portanto novas iniciativas para o desenvolvimento de novas ferramentas foram feitas. Foi nesse século que o inglês Willian Oughtred inventou a régua de cálculo, que consistia em uma régua que apresentava resultados pré-definidos de multiplicações.

![[oac1-01-fig03.webp]]

*Figura 2: Régua de Cálculo, fonte http://www.inf.ufrgs.br/~cabral/museu.html*

Nesse mesmo século, Blaise Pascal inventou uma máquina para cálculos. Essa máquina, chamada máquina de Pascal, resolvia alguns cálculos que a régua de cálculo não estipulava, pois apresentava alguns resultados pré-definidos.

#### A régua de Oughtred auxiliou o desenvolvimento de logaritmos.

Charles Babbage, conforme Garbi, foi outro notável precursor que gastou quase toda a vida e a fortuna no aperfeiçoamento de uma máquina de calcular concebida dentro de princípios válidos até hoje. Não chegou a ir muito longe, pois a tecnologia da época não permitia o desenvolvimento de peças no nível de que precisava.

Na primeira metade do século XX, Alan Turing, natural da Inglaterra, começou a questionar as máquinas de cálculos desenvolvidas até então. Uma de suas áreas de interesse era a lógico-matemática e, aproveitando-se das pesquisas e do seu envolvimento nessa área, ele forneceu uma descrição geral da teoria dos computadores. Conforme Garbi, seu artigo "On Computable Numbers", publicado em 1937, marcou o início de uma era. Seu doutorado foi feito nos Estados Unidos, na Universidade de Princeton. Foi nessa época que conheceu John Von Neumann.  Neumann reconheceu a importância das ideias de Turing relacionadas aos futuros computadores. Devido à Segunda Guerra Mundial, Turing foi lembrado pelos Ingleses como colaborador de grande importância para decifrar as mensagens usadas pelos Alemães. Essas mensagens eram enviadas após serem submetidas a um equipamento ao qual chamaram de Enigma. Turing e a equipe de pesquisadores que comandava desenvolveram uma máquina chamada Colossus com o objetivo de encontrar padrões nas mensagens enviadas. Com essa máquina conseguiu ajudar seu país, decifrando mensagens e, consequentemente, combatendo os submarinos alemães.

John Von Neumann, ainda na Segunda Guerra Mundial, dedicou-se ao desenvolvimento do computador, tomando como base a teoria de Turing. Ele conseguiu resolver um dos principais problemas técnicos da época, relacionado ao armazenamento de dados em memórias magnéticas. Esse importante passo possibilitou que os programas pudessem ser armazenados diretamente em componentes eletrônicos e não mais em fitas perfuradas. Esse e outros fatos ocorridos na história da evolução dos computadores permitiram que, hoje, possamos ter um computador para ser usado em casa, em empresas, nas universidades e em qualquer outro local onde se faça necessário.

A contribuição de Neumann para a computação foi fundamental; ele fez parte da equipe que desenvolveu o ENIAC, considerado o primeiro computador eletrônico. Até pelas condições tecnológicas da época, o ENIAC ocupou um grande espaço físico e científico: para se ter ideia do espaço físico, o conjunto todo ocupava três andares de um prédio.

![[oac1-01-fig04.webp]]

**Figura 3:** ENIAC, **Fonte:** http://www.museudocomputador.com.br/enciteclado.php

Felizmente a tecnologia evoluiu muito rapidamente; a válvula (1907), um dos principais componentes eletrônicos do ENIAC, começou a ser substituída pelos transistores (1947) e circuitos integrados (1958). Como consequência, os computadores tornaram-se bem menores, ocupando menos espaço e passando a ter custo mais acessível para as empresas. O processador (1971) alavancou a produção de computadores pessoais; com ele foi possível diminuir ainda mais essas máquinas e reduzir muito o custo de produção e, consequentemente, o preço. Atualmente, podemos notar que não há grandes invenções na linha desses semicondutores; o que se faz é inserir uma quantidade maior de componentes dentro de uma pastilha de silício, o que permite presenciarmos manchetes de notícias como “Processador com 32 núcleos, como isto é possível?”.

A evolução tecnológica não tem fim, sempre teremos novidades, no entanto a linha que se está seguindo é o da miniaturização dos componentes e também dos equipamentos. A tendência caminha para o processamento, ou seja, inclusão do microprocessador na maioria dos equipamentos eletrônicos, como micro-ondas, televisões, geladeiras, fogões e até automóveis e outros.

Atualmente o termo computação ubíqua ou computação invisível está se tornando mais comum. Os processadores e os softwares fazem parte de nossas vidas e, muitas vezes, não nos damos conta disso. Com certeza, ao seu redor deve haver muitos objetos com essa característica. Alguns exemplos? Celulares, tablets, notebooks, televisão, circuito fechado de TV, câmeras fotográficas, filmadoras, alarmes e outros que, futuramente, farão parte de nossas vidas como roupas, tênis, blusas, bolsas, etc.

## Conceitos básicos

O conceito de arquitetura e organização de computador refere-se à forma como se interligam e se comunicam os vários componentes eletrônicos e mecânicos do computador. Essa organização determina aspectos relacionados à qualidade, desempenho e aplicação para os quais o computador vai ser usado.

Chamo a sua atenção para o fato de que um computador digital é uma máquina que pode resolver problemas executando um conjunto limitado de instruções e essas instruções estão estritamente relacionadas ao microprocessador de um determinado fabricante, um programa escrito em linguagem de alto nível, como Java, C++, VB.NET, C# e outras, que, quando executadas, passam por algumas conversões até virarem instruções que o microprocessador possa entender.Os microprocessadores só entendem os bits “1” e “0”, portanto qualquer programa é convertido a uma dessas instruções, constituídas de “1” e “0”, limitadas do microprocessador. Esse procedimento é usado por ser mais confiável para codificar informações digitais e por propiciar maiores velocidades de processamento. As instruções primitivas de um processador formam uma linguagem por meio da qual as pessoas, desde que tenham conhecimento, podem se comunicar. Essa linguagem é denominada linguagem de máquina.

O diagrama básico de um computador é composto por três elementos: unidade central de processamento, dispositivos de entrada e saída e a memória.

![[oac1-01-fig05.webp]]

**Figura 4:** Diagrama básico de um computador. **Fonte:** Tanenbaum

A unidade central de processamento é considerada o cérebro do computador. Sua função é executar programas que foram armazenados na memória principal, à qual damos o nome de memória RAM. Nesse dispositivo ficam os programas e os aplicativos que estão sendo executados no momento, portanto o sistema operacional tem a função de controlar essa arquitetura, buscando as instruções, examinando-as e disponibilizando para execução uma após a outra.

Os componentes eletrônicos e mecânicos são conectados por um conjunto de fios paralelos ao qual damos o nome de barramento. Eles têm a função de servir de via para a transmissão de endereços, dados e sinais de controles. Os barramentos podem ser externos à CPU; neste caso ele serve para conectar a memória e os dispositivos de entrada e saída, mas também podem ser internos à CPU, ou seja, dentro do chip da CPU há barramentos que são usados para o tráfego de instruções ou dados capturados da memória.

Analisando a figura 4, podemos notar que a CPU é composta por algumas outras partes. Uma delas é a unidade de controle, que é responsável por endereçar, ou seja, apontar para uma posição da memória onde estará o dado ou instrução a ser carregada para o processador e controlar se esses dados serão lidos ou escritos na memória principal. Analogamente podemos considerar que a memória é parecida com um vetor; cada linha é composta por oito bits e tem um número ao qual damos o nome de endereço. A CPU tem que, de alguma maneira, capturar as informações contidas na memória para serem processados. Essas informações são capturadas pela indicação do endereço de onde eles estão armazenados.

A outra é a unidade lógica e aritmética, que efetua operações básicas como adição, subtração, multiplicação, divisão e comparação dos dados.

![[oac1-01-fig06.webp]]

**Figura 5:** Unidade Lógica e Aritmética. **Fonte:** Tanenbaum.

Conforme pode ser verificado na figura 5, a unidade lógica e aritmética recebe duas informações, uma de cada registrador. Esses dados serão processados pela unidade lógica e aritmética, que retornará um resultado e irá inseri-lo em um dos registradores. Portanto você pode perceber que os dados vêm dos registradores, passam pela unidade lógica e aritmética e um resultado é obtido e enviado para um dos registradores. Basicamente é assim que funciona a unidade lógica e aritmética: os dados são enviados da memória principal para os registradores e o resultado da operação pode ser inserido em um dos registradores ou, então, voltar direto para a memória principal.

Os microprocessadores atuais contêm uma pequena memória de alta velocidade usada para armazenar resultados temporários e controlar informações. Essa memória, chamada registrador, é composta de uma pequena quantidade de espaço. Normalmente, todos os registradores têm o mesmo tamanho. Cada registrador tem uma função específica e eles podem ser lidos e escritos em altas velocidades, pois são internos à CPU e usam o seu barramento interno.

Registradores são memórias, portanto sua função é armazenar dados temporariamente. Por estarem dentro do microprocessador e devido ao material utilizado na sua fabricação, os registradores são memórias de altíssimas velocidades, eles têm uma função importante, pois o microprocessador usa as informações contidas nos registradores para processamento.

## Arquitetura de Von Neumann

John Von Neumann, conforme já mencionado, era uma matemático com grande interesse na área da computação. Ele apresentou uma arquitetura de computador que é usada ainda hoje no projeto de computadores. Sua arquitetura reúne os seguintes componentes: uma memória, uma unidade aritmética e lógica, uma unidade central de processamento, composta por diversos registradores, e uma unidade de controle, que tem a função de auxiliar na busca de um programa na memória instrução por instrução.

![[oac1-01-fig08.webp]]

**Figura 6:** Arquitetura de Von Neumann. **Fonte:** Tanenbaum.

Todas as máquinas construídas até o início do projeto do ENIAC eram programadas e controladas através de meios externos, como cartões perfurados, fitas perfuradas, painéis de interruptores, cabos de conexões etc.; dispunham de pouquíssima memória para armazenar os dados e os resultados intermediários dos cálculos. A construção do ENIAC, cuja capacidade de armazenamento era de vinte números, consumiu mais de 17.000 válvulas eletrônicas. Um fator decisivo para viabilizar o projeto de uma nova máquina foi a ideia de utilizar técnicas para implementar memória de custo mais baixo para substituir as válvulas. Com essa ideia, tornou-se possível pensar numa máquina com dezenas ou centenas de milhares de bits. John Von Neumann foi um dos responsáveis pelo desenvolvimento das pesquisas em memórias, pois sua ideia era fazer com que os programas fossem armazenados diretamente nos computadores e que os meios descritos acima para armazená-los deixassem de ser utilizados. Com sua contribuição, os computadores e os programas tornaram-se mais rápidos, mais flexíveis e mais eficientes.

## Computadores de uso geral e computadores de uso específico

Algumas vezes você poderá se deparar com as terminologias “computador de uso geral” e “computador de uso específico”. Vamos conceituar cada uma delas e dar alguns exemplos para elucidar essas definições.

Um computador de uso geral é aquele desenvolvido para executar uma variedade de atividades; o projeto desses computadores é feito para que eles possam lidar com diversas situações e circunstâncias. Como exemplo, podemos citar todos os computadores que são anunciados para venda, geralmente, usando um sistema operacional Windows, Linux ou MAC. Esses computadores são adquiridos para serem usados em uma variedade grande de situações, como acesso à internet, leitura e-mails, telefonemas, desenvolvimento de textos, planilhas, banco de dados, desenhos, execução de jogos, filmes, programas e aplicativos em praticamente todos os ramos profissionais. Além disso, esses computadores permitem a personalização de interfaces e áreas de trabalho conforme a preferência de cada um. É importante que fique claro que esses computadores têm uma arquitetura que permite que isso seja possível desde que sejam instalados os softwares aplicativos para executar as atividades em questão.

Os computadores de uso específico já são projetados para executar uma quantidade limitada de tarefas. A arquitetura desses computadores é projetada para potencializar o desempenho em detrimento da variedade de atividades e quantidade de programas a serem executados. Geralmente estes computadores são apresentados com formas apropriadas à atividade para a qual ele foi desenvolvido. São exemplos de computadores de uso específico os medidores de tráfego em redes de computadores, roteadores também usados em redes de computadores, televisão, aparelho celular (smartphones), computadores usados em computação gráfica para desenvolvimento de filmes e desenhos. Esses computadores, conforme já foi descrito, usam componentes específicos para determinadas funções; os processadores, as interfaces gráficas e os sistemas operacionais são desenvolvidos para proporcionar o melhor desempenho do conjunto. Em linhas gerais, não há como executar outras atividades a não ser aquela para a qual ele foi projetado, portanto, esses computadores costumam ser mais caros.

## Medidas de desempenho

O tempo de execução é, geralmente, a unidade de medida usada para determinar o desempenho de um computador. Nesse sentido, devem ser consideradas algumas variáveis, como: a quantidade de processos que estão sendo executados, a quantidade de memória disponível, a velocidade do clock, a quantidade de instruções executadas por ciclo, dentre outras. Resumindo, a medida de desempenho de um computador depende da velocidade de cada um de seus diferentes principais componentes.

Muitas vezes a velocidade do clock e a quantidade de núcleos nos processadores são anunciadas como referência ao desempenho dos computadores, no entanto outros fatores devem ser analisados, embora muitos deles acabem sendo compatíveis entre si. Esses fatores incluem o acesso aos dispositivos de entrada e saída, o software básico e a hierarquia de memória.

Uma das partes mais prejudiciais ao desempenho refere-se aos dispositivos de E/S, principalmente aqueles que envolvem partes mecânicas para acesso à informação, como é o caso dos HDs e dispositivos de escrita e leitura ótica. O acesso a esses dispositivos ocorre com menos evolução em relação aos processadores, aspecto que influencia o desempenho do conjunto na execução de tarefas.

Vamos analisar o impacto do sistema de E/S no desempenho descrito por Guntzel:

_Suponha que temos um benchmark que executa em 100 segundos divididos em: 90s de processador + 10s de E/S. Se o tempo de processador melhorar em 50% ao ano para os próximos anos, mas o tempo de E/S se mantiver, quanto esse programa vai ficar mais rápido ao final de 5 anos?_ _Obs. Benchmark são programas específicos para medir o desempenho._ _Solução:_ _Tempo decorrido = tempo de processador + tempo de E/S 100 = 90 + Tempo de E/S_

|**_Após n anos_**|**_Tempo_**<br>**_de_**<br>**_Processador_**|**_Tempo_**<br>**_E/S_**|**_de_**|**_Tempo_**<br>**_decorrido_**|**_%_**<br>**_Tempo_**<br>**_decorrido_**<br>**_gasto em E/S_**|
|---|---|---|---|---|---|
|**_0_**|_90s_|_10s_||_100s_|_10%_|
|**_1_**|_90/1.5=60s_|_10s_||_70s_|_14%_|
|**_2_**|_60/1.5=40s_|_10s_||_50s_|_20%_|
|**_3_**|_40/1.5=27s_|_10s_||_37s_|_27%_|
|**_4_**|_27/1.5=18s_|_10s_||_28s_|_36%_|
|**_5_**|_18/1.5=12s_|_10s_||_22s_|_45%_|

Analisando a tabela acima, podemos notar que o tempo de execução do processador, considerando uma melhora de cinquenta por cento ao ano, executa a atividade em 90 segundos no primeiro ano e chega a executar a mesma atividade em 12 segundos após cinco anos. No entanto, se o tempo do dispositivo de E/S continuar o mesmo, ou seja, conforme o exemplo, dez segundos, podemos perceber que, após cinco anos, a porcentagem do E/S chega a quase cinquenta por cento na execução da atividade, ou seja, enquanto o processador executa a atividade em doze segundos, o dispositivo de E/S continua levando dez segundos para executá-la.

Algumas iniciativas estão sendo implementadas em notebooks e outros aparelhos, como a utilização de memória flash no lugar de HDs. Esta iniciativa permite que seja dispensada a parte mecânica na leitura desses dispositivos de armazenamento. Dessa forma há um ganho considerável na leitura e escrita de dados que precisam ser armazenados para uso futuro.

Em linhas gerais, se temos como objetivo avaliar o desempenho de um computador, então temos que considerar o conjunto: processador, dispositivos de entrada e saída e memória. Sendo assim, temos que avaliar o tempo de resposta, também chamado de tempo de execução, que corresponde ao tempo total necessário para que o conjunto possa completar uma tarefa e a vazão também conhecida como _throughput,_ que tem a função de indicar a quantidade de tarefas terminadas por unidade de tempo geralmente dada em segundos. Como referência, a seguinte formula é usada para determinar o desempenho de um computador:

#### Desempenho(x)=1/Tempo de execução(x)

Tomando como base dois computadores X e Y, se o desempenho de X é maior que o desempenho de Y, então podemos expressá-lo da seguinte maneira:

Desempenho(x) > Desempenho de (Y), pois 1/tempo de execução(x) > 1/tempo de execução(Y)

Em análise de um projeto de computador, normalmente, relaciona-se o desempenho de dois computadores diferentes de maneira quantitativa, usando a seguinte relação:

n=Desempenho(x)/Desempenho(y)

Exemplo: se um computador “A” executa um programa em 10 segundos e o computador “B” executa o mesmo programa em 15 segundos, quanto o A é melhor que B?

Usando a fórmula acima teremos n=15/10 = 1,5

Portanto, temos que A tem um desempenho 1,5 vezes maior que B.

## Representação da Informação

Como já citado, os computadores usam uma forma diferente para tratar as informações que devem ser processadas: enquanto nós, seres humanos, tratamos a informação através de um conjunto de caracteres alfanuméricos, os computadores consideram apenas bits “1” e “0”, ou seja, se há ou não um nível de voltagem, geralmente dada por +5v ou 0v, onde +5v indica o valor binário “1” e o 0v indica o valor “0” em binário. Esta técnica de trabalho garante às máquinas maior desempenho e facilidade na representação de cada informação.

Nós, seres humanos, trabalhamos com um sistema de numeração na base 10, ou seja, com os números de 0 a 9 conseguimos representar qualquer número e com o alfabeto conseguimos escrever sobre tudo. Os computadores trabalham com o sistema de numeração binária, pois só há dois símbolos, “0” e “1”. Com esse sistema de numeração, ele consegue representar qualquer número e também representar todas as letras do alfabeto.

Trabalhar com o sistema binário é quase impossível para nós seres humanos, no entanto deve haver uma forma de tradução do que entendemos para que uma máquina possa entender. Os primeiros computadores eram manipulados usando algum tipo de material que pudesse representar 1 e 0; o cartão perfurado e as chaves on/off tinham essa finalidade. Essa época foi marcada por baixa produtividade e complexidade no desenvolvimento de programas para executarem determinadas tarefas. Com o passar do tempo, foram surgindo alguns programas para controlar essas máquinas, aos quais foi dado o nome de sistemas operacionais. Com eles foi possível tirar a responsabilidade do especialista sobre o controle total da máquina. Sendo assim, o foco maior, por parte dos especialistas, voltou-se para o desenvolvimento de programas para realizar determinadas tarefas. Mesmo assim, lidar apenas com 1 e 0 para desenvolver um programa ainda tornava a atividade complexa e sacrificante, principalmente se algum erro fosse cometido durante o desenvolvimento. Muitas vezes, era melhor refazer o código em vez de procurar onde estava o erro.

Surgiram algumas linguagens de programação, às quais chamamos de linguagem de alto nível. Essas linguagens têm como finalidade tornar a programação mais atraente. Elas representam uma linguagem mais próxima daquela que um programador possa entender; são utilizadas palavras mais próximas de nossa linguagem. Dessa forma o programador foca mais na lógica da programação e não das particularidades da estrutura da linguagem de máquina.

De qualquer forma, após escrever um programa em linguagem de alto nível, ela deverá ser convertida para a linguagem de máquina, ou seja, em “0” e “1”. Essa interpretação ou compilação gera um custo relacionado ao desempenho na execução do programa, por esse motivo aquelas aplicações que necessitam de velocidade na execução - como jogos, sistemas operacionais, programas que têm a tarefa de renderização de imagens e outros - são desenvolvidas usando linguagens de mais baixo nível como Assembler, C, C++.
