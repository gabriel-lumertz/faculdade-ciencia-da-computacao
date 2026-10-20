---
materia: "Circuitos Lógicos"
modulo: "Circuitos Lógicos"
semestre: 2
unidade: 1
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 01.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 1"]
---

# Circuitos Lógicos

## Tópicos da Unidade

- **Introdução**

- **Sistemas**

- **Circuitos Digitais/Circuitos Lógicos**

- **Sistema de Numeração**

- **Medi** **ç ão de Desem** **p enho de Com** **p utadores**

## Objetivos de Aprendizado

- O objetivo dessa unidade é de levar ao aluno o conhecimento da evolução tecnológica e, então este passará a estudar os conceitos de sistemas de numeração o que o tornará apto a realizar distinções tecnológicas e também a fazer conversões matemáticas entre sistemas numéricos.

## Contextualização

Atualmente, o termo digital é tão comum em nosso palavreado que nem pensamos o que essa palavra realmente significa, mas o mais importante é que esse termo torna possível o funcionamento de elementos como computadores, robôs, médicos eletrônicos, transportes, entretenimento, dentre muitos outros. Nesta unidade, você verá vários elementos desse mundo digital, além de novos conhecimentos que ampliarão seu conhecimento da área.

Quando trabalhamos com números, mais especificamente, quando trabalhamos com as representações digitais dos números, estamos quantificando por comparação ou proporcionalidade, elementos de cálculo por símbolos chamados dígitos. Podemos usar como exemplo um relógio digital, onde as horas do dia são representadas por dígitos decimais e esses valores são comuns em qualquer lugar do mundo; dessa forma, tornando o método de medição único.

A representação pode ser digital ou analógica, sendo na analógica feita de forma contínua e na digital, feita passo a passo ou mais tecnicamente de forma discreta.

## Sistemas

Utilizamos o termo sistema digital quando há uma combinação de dispositivos projetados para lidar com informações lógicas ou com quantidades físicas representadas de forma digital, ou seja, as quantidades trabalhadas só podem assumir valores discretos. Os dispositivos que trabalham dessa forma são em sua grande maioria dispositivos eletrônicos. Pode-se exemplificar um sistema digital por um equipamento audiovisual ou telefônico.

Quando trabalhamos com o termo sistema analógico, estamos falando de dispositivos que podem manipular quantidades físicas que são representadas de forma analógica, onde as quantidades físicas acabam variando sobre um intervalo contínuo de valores, como, por exemplo, a amplitude do sinal de saída de um receptor de rádio que pode ter uma gama de valores de zero até milhares.

Claro que se existem duas frentes de trabalho, uma tem mais vantagem que a outra, como mostrado a seguir:

- Sistemas digitais são mais fáceis de projetar: Isto se deve ao fato de que os circuitos utilizados são circuitos de chaveamento, em que os valores exatos de tensão ou corrente não são importantes, mas apenas o intervalo (ALTO ou BAIXO), no qual eles se localizam.

- Fácil armazenamento de informação: Isto é alcançado por circuitos de chaveamento especiais, capazes de capturar a informação e guardá-la pelo tempo que for necessário.

- Maior exatidão e precisão: Sistemas digitais podem manipular quantos dígitos de precisão forem necessários, para o que, basta adicionar um número maior de circuitos de chaveamento. Em sistemas analógicos, a precisão está, geralmente, limitada a três ou quatro dígitos, porque os valores de corrente e tensão são diretamente dependentes dos valores dos componentes dos circuitos e também são afetados por flutuações randômicas (ruído).

- A operação do sistema pode ser programada: É bastante simples projetar sistemas digitais, cuja operação pode ser controlada por um conjunto de instruções, constituindo um programa. À medida que a tecnologia avança, a programação de sistemas vem se tornando cada vez mais simples. Sistemas analógicos também podem ser programados; entretanto, a variedade e a complexidade das operações disponíveis são bastante limitadas.

- Circuitos digitais são menos afetados pelo ruído: Flutuações na tensão (ruído) não são tão críticas em sistemas digitais porque o valor exato da tensão não é tão importante, desde que a amplitude do ruído também não seja tão grande que nos impeça de distinguir corretamente os níveis lógicos.

- Um maior número de circuitos digitais pode ser colocado em um circuito integrado: É verdade que circuitos analógicos também foram beneficiados com o grande desenvolvimento da tecnologia de fabricação de circuitos integrados, mas sua complexidade e a utilização de componentes economicamente inviáveis de serem integrados (capacitores de alto valor, resistores de precisão, indutores, transformadores) têm impedido que sistemas analógicos alcancem o mesmo nível de integração.

Se há vantagens, podemos esperar também algumas desvantagens. No mundo real, quase tudo é medido de forma analógica, sendo as medições operadas e controladas por um tipo de sistema. São elas: a temperatura, a pressão, posicionamento, velocidade, entre muitos outros. Você pode até achar que não, mas quando você determina uma hora ou uma temperatura, você está, na verdade, fazendo uma aproximação digital de uma grandeza inerentemente analógica.

Para tirarmos alguma vantagem digital de medições analógicas, temos que seguir alguns passos, como converter as entradas analógicas para digital, processar a informação digital e converter as saídas digitais de volta à forma analógica.

A Figura1 mostra um diagrama de blocos de um típico sistema de controle de temperatura. Como se pode ver no diagrama, a temperatura é medida por um dispositivo analógico e o valor medido é, então, convertido para uma representação na forma digital por um conversor analógico-digital (conversor A/D).

![[cl2-01-fig01.webp]]

*Figura1: Diagrama de blocos de um sistema de controle de temperatura que utiliza técnicas de processamento digital, possíveis graças às conversões analógico-digitais.*

*Fonte: Ronald J. Tocci; Sistemas Digitais – Princípios e Aplicações.*

Em seguida, este valor é processado por um circuito digital que pode incluir ou não um computador digital. A saída digital é, então, convertida de volta à forma analógica por um conversor digital-analógico (conversor D/ A). Esta saída analógica é fornecida como entrada a um controlador que realiza algum tipo de ação para ajustar a temperatura.

A necessidade de conversão entre formas analógicas e digitais pode ser considerada uma desvantagem por causa do seu custo e complexidade adicionais. Um outro fator que, geralmente, é importante é o tempo extra necessário para realizar estas conversões. Em muitas aplicações, esses fatores são compensados pelas numerosas vantagens de usarmos técnicas digitais, em razão das quais a conversão entre quantidades digitais e analógicas tomou-se algo bastante comum na tecnologia atual.

Existem situações, entretanto, em que a utilização de técnicas analógicas é mais simples e econômica. Por exemplo: a amplificação de sinais é mais facilmente realizada com o auxílio de circuitos analógicos. É comum observar as técnicas analógicas e digitais serem utilizadas em um mesmo sistema de modo a se tirar proveito das vantagens de cada uma das técnicas. Nesses sistemas híbridos, uma das mais importantes etapas do projeto é determinar em que partes devem ser empregadas as técnicas analógicas e aquelas em que devem ser utilizadas técnicas digitais.

## Circuitos Digitais/Circuitos Lógicos

Os circuitos digitais são sempre projetados para produzir tensões de saída que estejam dentro dos intervalos predeterminados para os binários 0 e 1, além de também serem utilizados na resposta a essas tensões, ou seja, um circuito digital responderá do mesmo modo a todas as tensões de entrada que estiverem dentro do intervalo permitido para o 0; de maneira semelhante, ele não distinguirá entre tensões de entrada que estejam dentro do intervalo permitido para 1.

Na Figura 2, você encontra uma representação de um circuito digital com entrada _V_ i e saída _V_ 0. É possível identificar na figura que o _V_ 0 é idêntico em ambos os casos, uma vez que as duas fontes de entrada de sinal possuem diferentes valores de tensão; logo, elas possuem o mesmo valor binário.

![[cl2-01-fig02.webp]]

*Figura 2: Um circuito digital responde a um nível binário (O ou 1) e não ao valor exato da tensão de entrada. Fonte: Ronald J. Tocci; Sistemas Digitais – Princípios e Aplicações.*

Chamamos de lógica do circuito a forma como um circuito digital responde a uma entrada. Cada tipo de circuito digital obedece a um determinado conjunto de regras lógicas e por essa razão também chamamos os circuitos digitais de circuitos lógicos.

Quase todos os circuitos digitais existentes nos sistemas digitais modernos são circuitos integrados (CIs). A grande variedade de CIs lógicos disponível tornou possível a construção de sistemas digitais complexos menores e mais confiáveis do que aqueles construídos com circuitos lógicos discretos.

## Sistema de Numeração

Os processadores têm por função básica executar operações matemáticas como a soma, subtração, divisão, dentre outras mais complexas. Para tanto, foram criadas diversas formas para se tentar reproduzir tais funções no computador, sendo a mais comum a notação posicional.

Conceitualmente falando, na notação posicional, os algarismos assumem valores diferentes de acordo com a posição relativa dele, sendo o valor total do número a soma dos valores relativos de cada algarismo. Assim sendo, dependendo do sistema de numeração adotado, a quantidade de algarismos que o compõe é chamada de base e, assim, chegamos à famosa conversão de bases.

Pode parecer estranho esse conceito, pois a cultura ocidental não utiliza a notação posicional, pois esta é característica dos numerais hindu-arábicos. No sistema ocidental, basta relacionarmos um valor a outro e pronto. Para tanto, convencionou-se dez algarismos (0,1,2,3,4,5,6,7,8,9) que chamamos de sistema decimal. Em outras palavras, a base de um sistema é a quantidade de algarismos que esse sistema possui; logo, no ocidente, utilizamos um sistema de base 10, bem como há o sistema binário que possui base 2 (0 e 1) utilizado como base da linguagem computacional.

Para descobrirmos um número de uma base (x), simplesmente, utilizamos o Teorema Fundamental da Numeração, representado por:

$$N_{10} = \sum_{i=-m}^{n-1} d \times b^{i}$$

Onde: N = número equivalente na base 10; d = dígito; b = base (em outro sistema de numeração); i = índice do dígito ou expoente da base “b”; m = quantidade de dígitos à direita da vírgula; n = quantidade de dígitos à esquerda da vírgula.

*Fonte: https://goo.gl/DbIjPQ*

Vamos usar, como exemplo, uma conversão do sistema binário para decimal:

- 101,012 (onde b=2, m=2, n=3) temos:

   - N10 = 1 x 2<sup>2</sup> + 0 x 2<sup>1</sup> + 1 x 2<sup>0</sup> + 0 x 2<sup>–1</sup> + 1 x 2<sup>–2</sup>

   - N10 = 4 + 0 + 1 + 0 + 0.25

   - N10 = 5.25

Veremos, agora, uma conversão do sistema octal para decimal:

- 10118 (onde b=8, n=4) temos:

   - N10 = 1 x 8<sup>3</sup> + 0 x 8<sup>2</sup> + 1x 8<sup>1</sup> + 1 x 8<sup>0</sup>

   - N10 = 512 + 0 + 8 + 1

   - N10 = 521

Veremos, agora, uma conversão do sistema Hexadecimal para decimal:

- 101116 (onde b=16, n=4) temos:

   - N10 = 1 x 16<sup>3</sup> + 0 x 16<sup>2</sup> + 1 x 16<sup>1</sup> + 1 x 16<sup>0</sup>

   - N10 = 4096 + 0 + 16 + 1

   - N10 = 4113

Em nosso material complementar, temos o link para um jogo da Cisco de conversões entre binário e decimal, jogue e veja até onde chega, será uma forma bastante competitiva de aprender. Será que você consegue raciocinar como uma máquina?

De forma muito mais fácil que a conversão para o sistema decimal, a conversão do sistema decimal para outro é realizada dividindo o valor inteiro ou multiplicando o valor fracionário até que se chegue ao inteiro, que se quer converter sucessivamente pelo valor da base para a qual se quer converter. Vamos verificar os exemplos:

Pegando o valor 37,125, dividimos primeiro o inteiro:

$37_{10} \to ?_{2}$

- 37 ÷ 2 = 18, _resta_ 1

- 18 ÷ 2 = 9, _resta_ 0

- 9 ÷ 2 = 4 _resta_ 1

- 4 ÷ 2 = 2, _resta_ 0

- 2 ÷ 2 = 1, _resta_ 0

Se pegarmos o resultado da última divisão e de ordem retroativa o resto de cada outra divisão, teremos o valor no sistema binário; $37_{10}$ → $100101_{2}$.

Agora, pegamos a parte fracionária para dividir:

$37{,}(125)_{10} \to ?_{2}$

- 0,125 × 2 = 0,25, _fração de_ 0

- 0,25 × 2 = 0,50, _fração de_ 0

- 0,50 × 2 = 1,00, _inteiro_ 1

Se pegarmos a representação do digito anterior à vírgula, de forma consecutiva, teremos como resultado 37,($125)_{10}$ → 37,($001)_{2}$; adicionando o valor descoberto do valor inteiro, temos, então, 37,$125_{10}$ → 100101,$001_{2}$.

Agora, falta vermos as conversões do sistema Binário para o Octal e Hexadecimal. A conversão de base 2 para base 8 se dá da seguinte forma:

- na parte inteira, deve-se formar grupos de três dígitos à esquerda, complementando-se com zeros;

- na parte fracionária, deve-se formar grupos de três dígitos à direita, complementando-se com zeros. Essa conversão deve utilizar a tabela de conversão para identificar o valor que cada grupo representa.

*Tabela 1: Tabela de conversão de sistemas*

|**Decimal**|**Binário**|**Octal**|**Hexadecimal**|
|---|---|---|---|
|0|0|0|0|
|1|1|1|1|
|2|10|2|2|
|3|11|3|3|
|4|100|4|4|
|5|101|5|5|
|6|110|6|6|
|7|111|7|7|
|8|1000|10|8|
|9|1001|11|9|
|10|1010|12|A|
|11|1011|13|B|
|12|1100|14|C|
|13|1101|15|D|
|14|1110|16|E|
|15|1111|17|F|

*Fonte: Elaborado pelo autor.*

Vamos usar, como exemplo de conversão, o seguinte valor binário:

- $010101{,}010100_{2} \to ?_{8}$

- 010 = 2  101 = 5  010 = 2  100 = 4

Assim, temos:

- 010101,$010100_{2}$ → 25,$24_{8}$

A conversão do sistema Binário para Hexadecimal se dá igualmente à conversão para Octal, apenas usando grupos de quatro dígitos à esquerda e à direita, ao invés de três, utilizando a mesma tabela, veja o exemplo:

- $11001011101{,}1111011_{2} \to ?_{16}$

- 0110=6  0101=5  1101=D  1111=F  0110=6

Assim, temos:

- 11001011101,$1111011_{2}$ → $65DF6_{16}$

Essas são as conversões mais utilizadas dentre a área de programação para entender melhor as linguagens de baixo nível. A seguir, na unidade, veremos outras formas de leitura e medição, mas, dessa vez, de desempenho de processamento.

## Medição de Desempenho de Computadores

O desempenho de qualquer hardware computacional tem duas perspectivas de extrema importância para seus fabricantes: a perspectiva do fabricante do hardware que pretende evolucionar o mercado com melhorias de desempenho dos seus componentes e a perspectiva do usuário que pretende realizar comparações entre sistemas distintos, ou seja, quem tiver a melhor tecnologia para o objetivo específico do usuário e, por fim, ganhar a confiança deste, será a empresa com maior lucro que, no fim das contas, é o objetivo de qualquer empresa.

A medição do desempenho dos computadores é, geralmente, feita por comparação entre sistemas de hardware diferentes, no qual aquele com menor tempo de execução é considerado o mais potente e mais desejado.

Para essa execução, alguns elementos são levados em consideração como a “latência” ou “Tempo de Execução”, que é o intervalo de tempo entre o início e o fim de uma tarefa. Há também o “throughput” que é o trabalho feito durante um dado tempo, ou seja, quantas tarefas, determinado processador consegue executar em um tempo específico. O sistema de hardware ideal é aquele com alto throughput e baixa latência, ou seja, maior quantidade de tarefas realizadas por tempo específico e menor tempo de execução.

Antes de iniciarmos os trabalhos com instruções na próxima unidade, devemos compreender alguns conceitos sobre desempenho de computadores. O Desempenho do Sistema refere-se ao tempo de execução de um programa com o sistema sem nenhuma carga de processamento. Há também o Desempenho de Processamento que se refere ao tempo do processamento para as tarefas.

É função do projetista de hardware otimizar o desempenho do computador, reduzindo o tempo de processamento, bem como é função do programador reduzir o número de ciclos que um programa consome para executar determinada tarefa.

Essa eterna batalha do engenheiro de hardware e do programador pelo melhor desempenho é dada pela equação ciclo/instrução chamado CPI (Cycles Per Instruction) que nada mais é que o valor médio da quantidade de tempo necessário para processamento pelo número de instruções que serão processadas. Dizemos que é uma média, pois instruções diferentes podem demorar tempos diferentes.

De uma forma bem simplificada (por enquanto), pode-se definir o tempo de execução de um programa pela equação:

$$\text{tempo} = \frac{\text{instruções}}{\text{programa}} \times \frac{\text{ciclos}}{\text{instrução}} \times \frac{\text{segundos}}{\text{ciclo}} = \frac{\text{segundos}}{\text{programa}}$$

#### Clube do Hardware – Programas para teste de Desempenho

Visitando o endereço abaixo, você encontrará dezenas de aplicações para medição de desempenho do sintético e aplicação. Acesse, explore, conheça e experimente para se familiarizar com as ferramentas mais adequadas a cada situação:

https://goo.gl/97WRmi

Nas próximas unidades, vamos explorar mais profundamente os conceitos de instrução e CPU, os quais vão necessitar dos conhecimentos aqui estudados; então, não deixe de exercitar e participar dos fóruns para sanar todas suas dúvidas. Nos vemos lá, abraços!
