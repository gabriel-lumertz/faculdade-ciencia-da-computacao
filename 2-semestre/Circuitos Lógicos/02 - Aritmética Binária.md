---
materia: "Circuitos Lógicos"
modulo: "Aritmética Binária"
semestre: 2
unidade: 2
tipo: material-teorico
fonte: "raw/2-semestre/CIRCUITOS LÓGICOS/Circuitos Lógicos 02.pdf"
tags: [faculdade, circuitos-logicos, semestre-2]
aliases: ["Circuitos Lógicos - Unidade 2"]
---

# Aritmética Binária

## Tópicos da Unidade

- **Representação De Variáveis Binárias**

- **O Transistor, Estrutura Básica**

- **Estrutura e Operação de Portas CMOS**

- **Portas Lógicas**

- **O Retardo de Propagação**

## Objetivos de Aprendizado

Esta unidade objetiva capacitar o aluno na identificação de representações de variáveis binárias, estrutura básica de um transistor, estrutura e operação de portas CMOS, portas NOT, NAND, NOR, portas complexas, retardo de propagação.

## Contextualização

Atualmente, o termo digital é tão comum em nosso palavreado que nem pensamos o que essa palavra realmente significa, mas o mais importante é que esse termo torna possível o funcionamento de praticamente todos eletrônicos que conhecemos. Nesta unidade, vamos identificar como os circuitos digitais interpretam sinais de entrada e os transformam em outros tipos de sinais, criando uma maior conversação entre dispositivos.

## Representação De Variáveis Binárias

Antes de falarmos sobre contas, aritmética, álgebra e muito outros assuntos, precisamos lembrar algumas questões básicas para entender as variáveis binárias. O termo variável diz respeito a qualquer elemento de uma população que se pode dar um valor numérico ou categoria e, então, este pode assumir valores diferentes de unidades observáveis.

Desse modo, podemos identificar o termo população como uma variável que gostaríamos de estudar. Então, dizemos que a população é constituída por todos os valores que a variável estudada pode assumir. Ao processo de observar uma variável damos o nome de experiência aleatória. Dizemos que a variável é quantitativa quando esta se refere a características que se possa contar ou medir, as quais, por sua vez, podem ser classificadas como variáveis quantitativas discretas, ou seja, variáveis relacionadas a elementos que só podemos contar e não medir; e as variáveis quantitativas contínuas, ou seja, aquelas que só podemos medir e não contar.

As variáveis também podem ser classificadas como qualitativas se não forem suscetíveis de medição ou contagem, mas unicamente de uma classificação, podendo assumir várias modalidades ou categorias. Quando essas variáveis possuem somente duas categorias, podemos dizer que elas são do tipo binária, como, por exemplo, o sexo de um grupo de pessoas.

Um exemplo mais próximo de nossa disciplina pode ser dado se pensarmos em um interruptor, quando está aberto, ou seja, quando não há corrente circulando pelo circuito, podemos dizer que o estado do interruptor é zero (0), mas se estiver fechado, ou seja, quando há corrente passando pelo circuito, podemos dizer que o estado do interruptor é um (1). Vale lembrar que um estado nunca pode ocorrer ao mesmo tempo que o outro em um mesmo circuito.

A Fig.1 mostra dois circuitos semelhantes que representam um interruptor de uma lâmpada, um circuito bastante simples, onde na parte A o circuito se encontra aberto e a lâmpada apagada e na parte B o circuito se encontra fechado e a lâmpada acesa. Esses circuitos também podem ser classificados como: circuitos digitais ou lógicos.

![[cl2-02-fig01.webp]]

*Figura 1 – Representação de um interruptor de lâmpada comum aberto (esquerda) e fechado (direita)*

## O Transistor, Estrutura Básica

O transistor existe hoje em qualquer equipamento eletrônico e foi desenvolvido em 1947 nos laboratórios da empresa de telefonia Beel, que teve sua ideia originária em buscar um dispositivo de funcionamento semelhante aos das válvulas.

Seu funcionamento baseia-se na capacidade de os transistores utilizarem uma baixa corrente elétrica que alimenta o nível de carga entre dois terminais. Existem dois tipos de transistores: o transistor de junção bipolar (TJB) e o transistor de efeito de campo (FET), que, como o próprio nome diz, funciona através do efeito de um campo elétrico na junção. Esse tipo de transistor tem muitas aplicações na área de amplificadores (operando na área linear), em chaves (operando fora da área linear) ou em controle de corrente sobre uma carga.

Os FETs têm como principal característica uma elevada impedância de entrada, o que permite seu uso como adaptador de impedâncias, podendo substituir transformadores em determinadas situações. Além disso, são usados para amplificar frequências altas com ganho superior ao dos transistores bipolares.

O transistor de junção bipolar é estruturado como dois diodos de junção PN representados pelas fronteiras entre os terminais que o constituem. Levando em consideração que um diodo opera em três regiões distintas, região de condução com polarização direta, região de corte com polarização reversa e região de ruptura com polarização reversa, as partes do transistor TJB são: emissões, base e coletor e as junções PN que nele existem são as fronteiras entre os terminais que identificam esse semicondutor, onde E representa o emissor, B a base e C o coletor, conforme demonstrado na figura a seguir:

![[cl2-02-fig02.webp]]

*Figura 2 – Representação de Transistores PNP e NPN mostrando suas regiões integrantes, incluindo as junções*

No funcionamento do transistor TJB, os extremos diferem-se entre si pela quantidade de cargas negativas ou elétrons; no meio, existe uma região de equilíbrio de cargas opostas que formam a região de depleção após emissor e coletor serem dopados, onde o emissor terá elétrons em grande quantidade que serão recebidos pelo coletor. Entre o emissor e o coletar, na base, localizam-se os portadores de carga que irão transferir os elétrons entre uma região e outra.

O processo de funcionamento se dá da seguinte forma:

A junção JEB (junção base-emissor) encontra-se polarizada diretamente e isso reduz a região de depleção que passa a ser condutora. Então, cargas vindas do emissor ocuparão pequenos espaços na base em virtude de elementos como a dopagem e construção, o que pode proporcionar uma menor excitação das partículas nesse meio.

Os elétrons combinados às lacunas constituem a corrente que irá fluir pela base que tecnicamente recebe o nome de IB. A grande maioria dos elétrons presentes na base são levados para o coletor devido à energia acumulada nessa região, resultante da polarização da junção base-emissor, além da distribuição dessas cargas que favorece o deslocamento.

Na junção base-coletor, ocorre a polarização reversa, criando um campo elétrico que atrai as cargas dentro do coletor e essas cargas constituem a corrente que percorre o coletor, sendo essa corrente maior que a da base; logo, podemos assumir que IC >> IB. Dessa forma, fica identificado como trabalho da base o controle do fluxo de cargas entre emissor e coletor.

Levando em consideração as regiões: Emissor, Base e Coletor, podemos ainda fazer distinções quanto às formas de montagem de um transistor que pode ser BC, EC e CC, lembrando que o termo comum é referência à ligação entre a zona que identifica o componente e o terra.

Base Comum (BC):

- Montagem: Entrada do sinal entre o emissor e a base. Saída do sinal entre coletor e base.

- Características: Possui um ganho de corrente (GI) menor que 1, ganho de tensão (GV) elevado, resistência de entrada (RIN) baixa e resistência de saída (ROUT) alta.

![[cl2-02-fig03.webp]]

##### Emissor Comum (EC):

- Montagem: Entrada do sinal entre a base e emissor. Saída do sinal entre coletor e emissor.

- Características: Possui um ganho de corrente (GI) elevado, ganho de tensão (GV) elevado, resistência de entrada (RIN) média e resistência de saída (ROUT) alta.

![[cl2-02-fig04.webp]]

**Emissor Comum**

##### Coletor Comum (CC):

- Montagem: Entrada do sinal entre a base e coletor. Saída do sinal do circuito do emissor.

- Características: Possui um ganho de corrente (GI) elevado, ganho de tensão (GV) menor que ou igual a 1, resistência de entrada (RIN) muito alta e resistência de saída (ROUT) muito baixa.

![[cl2-02-fig05.webp]]

**Coletor Comum**

As zonas de operação de um transistor são quatro: região de corte, zona ativa, região de saturação e região de ruptura. A zona ativa possui algumas condições de funcionamento como:

- Junção base-emissor diretamente polarizada → $V_{BE}$ > tensão limiar;

- Junção base-coletor inversamente polarizada → < VBC < VCC;

- 0 < VCE < VCC;

- Corrente de coletor determinada pela expressão $I_C = \beta_{CC} \times I_B$, onde $\beta_{CC}$ é o ganho estático de corrente do transistor (relação entre as correntes que saem pelo coletor e que entra no emissor);

- Amplificação de sinal da tensão variável com ganho da ordem de centenas.

Quando um transistor está trabalhando nas regiões de saturação e corte, assume o comportamento de uma chave, ou seja, interruptor aberto ou fechado (como já estudado). Na zona de corte, o transistor equivale a um interruptor aberto com corrente nula no coletor. Dessa forma, a tensão entre o coletor e o emissor, equivale a tensão contínua aplicada sobre ele ($V_{CE}$ = $V_{CC}$), assim $I_{B}$ ≅ 0 . Já na zona de saturação, o transistor corresponde a um interruptor fechado; logo, a tensão entre o coletor e o emissor será praticamente nula e a corrente no coletor irá atingir seu valor máximo (limitado pela resistência associada a ele) $I_{C}$ $V_{CC}$ $R_{C}$.

Na região de ruptura, há um valor que limita a tensão, conforme especificação do transistor, valor esse que, se ultrapassado, gerará dano ao componente, Na figura a seguir, você pode notar alguns exemplos de tensão de ruptura:

![[cl2-02-fig06.webp]]

*Figura 3 – Regiões de funcionamento de um transistor*

As principais aplicações de transistores seriam como amplificadores de corrente ou tensão e como controle ON-OFF (chaves do tipo liga-desliga), por exemplo, chavear um motor de alta potência com um sinal de um microcontrolador, amplificar um sinal e circuitos osciladores como luzes e contadores de tempo.

## Estrutura e Operação de Portas CMOS

Antes de tudo, devemos entender o que são os dispositivos CMOS. O termo CMOS ou _Complementary Metal-Oxide Semiconductor_ diz respeito a uma tecnologia utilizada em transistores de efeito de campo (FET) no lugar dos já estudados transistores bipolares na elaboração de circuitos integrados.

O uso dos dispositivos FET, como tudo, traz vantagens e desvantagens, mas com o avanço tecnológico, vem eliminando cada vez mais as desvantagens, aumentando a velocidade de trabalho e reduzindo seu consumo de energia.

Temos a seguir uma demonstração de como são construídos os CMOS ou MOSFETs nas aplicações de circuito integrados:

![[cl2-02-fig07.webp]]

*Figura 4 – Estrutura básica do dispositivo CMOS*

Podemos ver, na figura 4, o _gate_ ou controle do eletrodo no lugar da base e a polarização ocorre da fonte para o dreno, fazendo uma analogia ao transistor bipolar. Além disso, é possível também observar que entre o eletrodo do gate, que é constituído de uma placa de alumínio e o substrato ou canal, que é por onde passa a corrente, não existe contato elétrico ou junção; em seu lugar, existe uma fina camada de óxido de alumínio ou óxido-metálico que, por fim, dá o nome ao dispositivo (metal-oxide).

A corrente que circula entre a fonte e o dreno do dispositivo CMOS pode ser controlada pela tensão aplicada ao seu _gate_ . Assim, no tipo P uma tensão positiva de comporta aumenta sua condução, ou seja, faz com que ele sature e no tipo N, uma tensão negativa de comporta é que o leva à saturação.

Mais uma vez fazendo uma comparação com os tipos bipolares, podemos dizer, então, que enquanto os transistores bipolares são típicos amplificadores de corrente, os FETs ou transistores de efeito de campo MOS são típicos amplificadores de tensão.

Essa diferença leva o transistor de efeito de campo MOS a apresentar características muito interessantes para aplicações em Eletrônica Digital ou Analógica.

Uma delas está no fato de que a impedância de entrada do circuito é extremamente elevada, o que significa que precisamos praticamente só de tensão para controlar os dispositivos CMOS. Assim, é preciso uma potência extremamente baixa para o sinal que vai excitar a entrada de um circuito integrado CMOS, já que praticamente nenhuma corrente circula por esse elemento.

A outra está no fato de que, diferentemente dos transistores bipolares que só começam a conduzir quando uma tensão da ordem de 0,6 V vence a barreira de potencial de sua junção base-emissor, os FETs não têm esta descontinuidade de características, o que os tornam muito mais lineares em qualquer aplicação que envolva amplificação de sinais.

A tecnologia CMOS permite que os dispositivos tenham características excelentes para aplicações digitais. Quando utilizamos uma configuração com transistores do tipo N e O ao mesmo tempo, podemos usar, então, um circuito inversor, conforme a figura 5.

![[cl2-02-fig08.webp]]

*Figura 5 – Circuito Inversor*

Nesse circuito da figura 5, é possível ver que, dependendo da intensidade do sinal aplicado no _gate_ dos transistores ao mesmo tempo, um deles estará polarizado para condução máxima, ou seja, saturado, e o outro estará obrigatoriamente polarizado no sentido de corte de corrente.

## Portas Lógicas

Seja qual for o sistema digital que está trabalhando, sempre o representamos utilizando portas lógicas. Veremos a seguir as principais portas lógicas e seus métodos de funcionamento.

A primeira porta lógica estudada é a Porta AND (E) que representa a função E, seu funcionamento diz que a saída será 1 somente se ambas as entradas forem iguais a 1; nos demais casos, a saída será 0. A figura 6 mostra a representação da porta AND e uma implementação em um transistor TTL de 4 portas AND com alimentação VCC=5V.

![[cl2-02-fig09.webp]]

*Figura 6 – Porta Lógica AND (A), Transistor de 4 portas AND (B)*

Podemos representar também os resultados de uma saída da porta lógica através da representação da tabela verdade que nos demonstra a saída da porta de acordo com os sinais de entrada. Em lógica, dizemos que o valor 0 significa FALSO (F) e normalmente é representado por um nível de tensão 0V, isto é, um nível baixo de tensão ou BAIXO ou ainda LOW. Já o valor 1 significa VERDADEIRO (V) e é representado por um nível de tensão +VCC, ou seja, um nível alto de tensão ou ALTO ou ainda HIGH.

|**A**|**B**|**Y**|**A**|**B**|**Y**|
|---|---|---|---|---|---|
|0|0|0|F|F|F|
|0|1|0|F|V|F|
|1|0|0|V|F|F|
|1|1|1|V|V|V|
|**A**|**B**|**Y**|**A**|**B**|**Y**|
|_OV_|_OV_|_OV_|L|L|L|
|_OV_|+_Vcc_|_OV_|L|H|L|
|+_Vcc_|_OV_|_OV_|H|L|L|
|+_Vcc_|+_Vcc_|+_Vcc_|H|H|H|

*Figura 7 – Representações da Tabela Verdade para a porta lógica AND*

A próxima porta que veremos é a porta OR ou porta OU. Essa porta executa a função de soma dos sinais de entrada de forma booleana da seguinte maneira:

- Se a chave A está aberta (A=0) e a chave B aberta (B=0), não haverá circulação de energia no circuito; logo, a lâmpada fica apagada (S=0).

- Se a chave A está fechada (A=1) e a chave B aberta (B=0), haverá circulação de energia no circuito e a lâmpada fica acesa (S=1).

- Se a chave A está aberta (A=0) e a chave B fechada (B=1), haverá circulação de energia no circuito e a lâmpada fica acesa (S=1).

- Se a chave A está fechada (A=1) e a chave B fechada (B=1), haverá circulação de energia no circuito e a lâmpada fica acesa (S=1).

- Observando todas as quatro situações possíveis, pode-se concluir que a lâmpada fica acesa somente quando a chave A ou a chave B ou ambas estiverem fechadas.

### C

![[cl2-02-fig10.webp]]

*Figura 8 – Representações da porta lógica OR (A), Transistor de 4 portas do tipo OR (B) e Tabela Verdade da porta lógica OR (C)*

Veremos, agora, uma versão especial da porta OR, chamada XOR (OU ESPECIAL) que trabalha da seguinte forma: a saída será 1 quando os sinais de entrada forem diferentes entre si e 0 caso contrário.

![[cl2-02-fig11.webp]]

*Figura 9 – Representações da porta lógica XOR (A) e Tabela Verdade (B)*

A próxima porta lógica estudada representa a negação de um sinal, ou seja, se a variável estiver em 0, o resultado da função é 1 e se a variável estiver em 1, o resultado da função é 0. Essa porta também é conhecida como sistema inversor.

![[cl2-02-fig12.webp]]

*Figura 10 – Representações da porta lógica NOT (A), Transistor de 6 portas do tipo NOT (B) e Tabela Verdade da porta lógica NOT (C)*

Seguindo, temos a porta lógica NAND (NÃO E) que faz uma composição da porta NOT e da porta AND da seguinte forma: a saída será 0 se e somente se as N entradas forem iguais a 1; nos demais casos, a saída será 1.

![[cl2-02-fig13.webp]]

*Figura 11 – Representações da porta lógica NAND (A) e Tabela Verdade (B)*

A porta que veremos, agora, também é uma composição de duas outras, é a porta NOR (NÃO OU) que mescla as portas NOT e OR da seguinte forma: a saída será 1 se e somente se as entradas forem iguais a 0; nos demais casos, a saída será 0.

![[cl2-02-fig14.webp]]

*Figura 12 – Representações da porta lógica NOR (A) e Tabela Verdade (B)*

Há também a versão especial da porta NOR, chamada XNOR que trabalha da seguinte forma: a saída será 1 quando os sinais de entrada forem idênticos e 0 caso contrário.

![[cl2-02-fig15.webp]]

*Figura 13 – Representações da porta lógica XNOR (A) e Tabela Verdade (B)*

É possível fazer combinações ou interligações de portas lógicas, como no exemplo a seguir:

![[cl2-02-fig16.webp]]

|**A**|**B**|**C**|**Y**|
|---|---|---|---|
|0|0|0|1|
|0|0|1|0|
|0|1|0|1|
|0|1|1|1|
|1|0|0|1|
|1|0|1|1|
|1|1|0|1|
|1|1|1|1|

*Figura13 – Exemplo de portas lógicas combinadas (A) e Tabela Verdade (B)*

Para facilitar o tratamento analítico das diversas funções lógicas possíveis de serem implementadas através de portas lógicas, utiliza-se a representação da função lógica através de equações booleanas, conforme demonstrado na tabela 1:

*Tabela 1 – Representação das portas lógicas por equações Booleanas*

![[cl2-02-fig17.webp]]

Todo circuito lógico executa uma expressão booleana e, por mais complexo que seja o circuito, ele é composto pela interligação dos blocos lógicos básicos, para gerar as expressões lógicas, você deve averiguar qual circuito lógico está trabalhando e, então, adicionar as expressões vistas na tabela 1, parte por parte, até completar o circuito. Veja um exemplo na figura 14:

![[cl2-02-fig18.webp]]

*Figura 14 – Identificando as expressões conforme os circuitos lógicos*

Identificando a expressão do circuito lógico, também se torna possível identificar a tabela verdade desse circuito, da seguinte forma:

Considerando uma expressão S = A · B · C + A · D + A · B · D, você identificará 4 variáveis (A, B, C e D), usando a expressão $2^{4}$, você chega a 16 interpretações de sinal, como visto na figura 15. Agora, você pode criar colunas para cada subfórmula e após, mais uma coluna para o resultado do sinal de saída. Para cada subfórmula e o sinal de saída, você deve simplesmente aplicar a expressão sobre as variáveis.

|**A**|**B**|**C**|**D**|**A.B.C**|**A.D**|**A.B.D**|**S**|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|
|0|0|0|1|0|0|0|0|
|0|0|1|0|0|0|0|0|
|0|0|1|1|0|0|0|0|
|0|1|0|0|0|0|0|0|
|0|1|0|1|0|0|0|0|
|0|1|1|0|0|0|0|0|
|0|1|1|1|0|0|0|0|
|1|0|0|0|0|0|0|0|
|1|0|0|1|0|1|0|1|
|1|0|1|0|0|0|0|0|
|1|0|1|1|0|1|0|1|
|1|1|0|0|0|0|0|0|
|1|1|0|1|0|1|1|1|
|1|1|1|0|1|0|0|1|
|1|1|1|1|1|1|1|1|

*Figura 15 – Construção da tabela verdade de uma expressão lógica*

## O Retardo de Propagação

Um sinal lógico sempre sofre retardo em sua passagem através de um circuito. Os dois tempos correspondentes aos retardos de propagação são definidos como:

- _t_ PLH: tempo de retardo correspondente à passagem do nível lógico 0 para o nível lógico 1 (BAIXO para ALTO).

- _t_ PHL: tempo de retardo correspondente à passagem do nível lógico 1 para o nível lógico 0 (ALTO para BAIXO).

![[cl2-02-fig19.webp]]

*Figura 16 – Exemplo de Retardo de Propagação*

Em geral, _t_ PLH e _t_ PHL possuem valores diferentes, variando também em função das condições de carregamento, as quais o circuito está submetido. Tais valores são usados para compararem as velocidades de operação dos circuitos lógicos. Vamos tomar um exemplo com um circuito com retardo de propagação em torno de 10ns que é mais rápido do que um circuito com retardo da ordem de 20 ns.
