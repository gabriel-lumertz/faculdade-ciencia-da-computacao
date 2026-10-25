---
materia: "Programação Orientada a Objetos"
modulo: "Classes x Objetos"
semestre: 2
unidade: 2
tipo: material-teorico
fonte: "raw/2-semestre/PROGRAMAÇÃO ORIENTADA A OBJETOS/POObjetos 02.pdf"
tags: [faculdade, programacao-orientada-a-objetos, semestre-2]
aliases: ["Programação Orientada a Objetos - Unidade 2"]
---

# Classes x Objetos

Vimos na unidade anterior como é a estrutura de um programa orientado a objetos e de um programa estruturado. Agora vamos apresentar como criar os métodos, usar encapsulamento e chamar os métodos criados através de objetos.

###### Mecanismo de Trabalho

A JVM interpreta os _bytecodes_ gerados pelo compilador.

![[poo2-02-fig01.webp]]

**Figura 1**

O objetivo da JVM é permitir que qualquer sistema operacional possa executar uma aplicação _Java_

#### Classe Java

```java
public class BemVindo {
public static void main(String args[]) {
System.out.println("Bem vindo a Java.");
}
}
```

**Importante!**

**Lembre-se o Java é** **_case sensitive_ (há diferença entre maiúsculas e minúsculas).**

#### Programa = Classe

```java
public class BemVindo {
public static void main(String args[]){
  System.out.println("Bem vindo"); /* esta linha impirme uma mensagem na tela*/
}
}
```

**Importante! Os arquivos Java têm que ter o nome da classe principal.**

No exemplo acima, o nome do arquivo seria Bemvindo.java e depois de compilado ficaria Benvindo.class

#### Nome da classe = Nome dos Arquivos

```java
public class BemVindo {
public static void main(String[ ] args){
	System.out.println("Benvindo");
	}
}
```

#### Método main

```java
public class BemVindo {
	public static void main(String[ ] args){
	  System.out.println("Bemvindo");
	}
}
```

```java
/** Aplicação Hello World */
public class MinhaClasse {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```

![[poo2-02-fig02.webp]]

**Figura 2**

#### Principais Conceitos

###### O que são Objetos?

São quaisquer coisas na natureza que possuam propriedades (características) e comportamentos (operações).

Exemplos de Objetos: um bolo, um cachorro, um livro, etc.

#### Orientação a Objetos

O termo orientação a objetos significa organizar o mundo real como uma coleção de objetos que incorporam estrutura de dados e um conjunto de operações que manipulam estes dados, como

**Tabela 1 – Classe: Pessoa**

|**Propriedades**|**Comportamento**|
|---|---|
|Nome|Andar|
|Profissão|Correr|
|Data de Nascimento|Trabalhar|
|Altura|Chorar|
|Peso|Dançar|
|Espécie|Andar|
|Cor das penas|Correr|
|Tamanho|Voar|
|Peso|Pousar|

#### Estrutura de um Objeto

Um objeto tem identificação, dados e comportamento, atributos e métodos.

Podemos dizer que objeto é espécie da classe, ou seja, uma instância da classe.

![[poo2-02-fig03.webp]]

*Figura 3*

*Fonte: Adaptada de Freepik*

Para finalizarmos as comparações entre Classe e Objetos temos os seguintes exemplos:

###### Tabela 2

|**Classes**|**Objetos**|
|---|---|
|Funcionário|Os funcionarios Pitoco Aguiar e<br>José da Silva|
|Carro de passeio|O astra, vinho, placa CIL 8445|

|**Classes**|**Objetos**|
|---|---|
|Nota Fiscal|A nota fiscal #29470 referente a<br>um computador_notebook_|

Em resumo, o objeto é definido pelo conjunto de valores dos seus atributos em determinado instante. O comportamento é definido pelo conjunto de métodos. Ao criar uma classe, ela passa a ser um tipo abstrato de dados que pode instanciar objetos. Para instanciar objetos usamos o operador _new_ .

![[poo2-02-fig04.webp]]

*Figura 4*

*Fonte: Adaptado de Freepik*

Uma coleção de carros  pode ser representada por uma classe chamada Carro. Cada carro desta coleção é a “instância” (objeto) da classe Carro.

#### Atributos

Os atributos são as características dos objetos, o estado do objeto equivale aos valores de todos os atributos. No caso do exemplo acima os atributos são representado pelo motor, cor e marca.

**Construindo a Classe em** **_Java_**

Um arquivo em _Java_ precisa de uma classe pública com o mesmo nome do arquivo, abaixo um exemplo de como criar o arquivo.

```java
public class <nome_da_classe> {
    <lista de atributos>
	<lista de métodos>
}
```

### Importante!

**Por padrão as classes e atributo em java devem seguir algumas regras:**

Somente letras, números e _underline_ ;

Não pode começar por números;

Não pode ter espaços em branco;

Não pode ser palavra reservada;

**Classes:** Possuem as iniciais maiúsculas e sem espaços ou caracteres especiais;

#### Tipos de Dados em Java

Java possui 8 tipos primitivos que podem ser usados como tipos de atributos e que são eles:

**_Byte_ :** 8 _bits_ ; **_Short_ :** 16 _bits_ ; **_Int_ :** 32 _bits_ ; **_Long_ :** 64 _bits_ ;

**_Float_ :** ponto flutuante de 32 _bits_ ;

**_Double_ :** ponto flutuante de 64 _bits_ ; **_Char_ :** _Unicode_ de 16 _bits_ ; **_Boolean_ :** _true_ / _false_ ; **_String_ :** classe.

Vejamos um exemplo de criação da classe carro e a instância da classe.

```java
public class Carro {
    String motor;
    String cor;
    String marca;
}

public class TestarCarro{
    public static void main(String args[]){
        Carro c1 = new Carro();
        Carro c2 = new Carro();

        c1.motor = '2.0';
        c1.cor = 'Prata'
        c1.marca = 'Citroen';

        c1.motor = '1.6';
        c1.cor = 'Vermelho'
        c1.marca = 'Ford';
    }
}
```

![[poo2-02-fig05.webp]]

**Figura 5** Fonte: Reprodução

**Classes: Atributos (Propriedades) + Métodos (Comportamento)** Método é a implementação de uma operação. Os métodos expressam os comportamentos que todos os objetos dessa classe possuem.

tipo nome (parâmetros) { instruções;

```html
<return resposta>;
```

#### Set e Get

Servem como métodos de leitura/escrita aos atributos de classes.

Um método de leitura para um atributo deve ser chamado de _get_ Xxx (onde Xxx é o nome do atributo). Este método não recebe nada como parâmetro, e retorna o mesmo tipo do atributo.

Já um método de gravação deve ser chamado _set_ Xxx, não retorna nada (geralmente), e recebe como parâmetro o valor que deve ser armazenado no atributo.

Na programação orientada a objetos, os atributos da classe quase nunca estão visíveis para os usuários, é necessário criar um método público para que a aplicação possa acessá-lo. Temos basicamente 3 modificadores de acesso:

**_Private_ ( - ):** é o mais restritivo de todos, atributos e métodos com esse modificador são visíveis somente dentro da definição da própria classe, acessando-o diretamente ou através de uma instância da mesma classe;

**_Protected_ ( # ):** define que atributos e métodos somente podem ser acessados por subclasses da classe onde está sendo definido;

**_Public_ ( + ):** é o mais abrangente de todos os tipos de acesso, declara que  elementos que o utilizam são acessíveis de qualquer classe _Java_ .

Vejamos a implementação do código:

```java
public class Carro {
    private String motor;
    private String cor;
    private String marca;

    public String getMotor(){
        return motor;
    }

    public void setMotor(String m){
        motor = m;
    }

    public String getCor(){
        return cor;
    }

    public void setCor(String c){
        cor = c;
    }

    public String getMarca(){
        return marca;
    }

    public void setMarca(String mc){
        marca = mc;
    }
}
```

**Figura 6** Fonte: Reprodução

Agora os atributos da classe Carro são privados, não é mais possível atribuir informações diretamente:

```java
// Versão riscada na figura (acesso direto aos atributos privados):
public class TestarCarro{
    public static void main(String args[]){
        Carro c1 = new Carro();
        Carro c2 = new Carro();

        c1.motor = '2.0';
        c1.cor = 'Prata'
        c1.marca = 'Citroen';

        c1.motor = '1.6';
        c1.cor = 'Vermelho'
        c1.marca = 'Ford';
    }
}

// Versão correta:
public class TestarCarro{
    public static void main(String args[]){
        Carro c1 = new Carro();
        Carro c2 = new Carro();

        c1.setMotor('2.0')
        c1.setCor('Prata')
        c1.setMarca('Citroen');

        c1.setMotor('1.6')
        c1.setCor('Vermelho')
        c1.setMarca('Ford');
    }
}
```

![[poo2-02-fig07.webp]]

**Figura 7** Fonte: Reprodução

Os métodos também possuem padrão de nomenclatura. Os métodos possuem sempre a primeira inicial minúscula e as outras iniciais maiúsculas.

Os métodos geralmente são ações que podem ser efetuadas entre os atributos do objeto.

Métodos que não retornam valores, apenas executam ações, são do tipo _void_ .

Por exemplo, na classe Carro, podemos criar um método que imprima seus atributos na tela, ou como vimos anteriormente, mostre o estado do objeto.

```java
public class Carro {
    private String motor;
    private String cor;
    private String marca;

    public String getMotor(){...}

    public void setMotor(String m){...}

    public String getCor(){...}

    public void setCor(String c){...}

    public String getMarca(){...}

    public void setMarca(String mc){...}

    public void imprimeDados(){
        System.out.println("Motor: " + motor);
        System.out.println("Cor: " + cor);
        System.out.println("Marca: " + marca);
    }
}
```

**Figura 8** Fonte: Reprodução

###### Métodos – Procedimentos

Os métodos podem ou não assumir tipos de dados, caso não assumam, são chamados de procedimentos, pois executam um conjunto de instruções sem devolverem valor algum a quem os chamou. Um método sem tipo recebe em sua definição a palavra-chave void no lugar do tipo.

```java
//Procedimento sem parâmetro
void frase() {
    System.out.println("Procedimento sem parâmetros");
}
```

###### Figura 9

*Fonte: Reprodução*

###### Métodos – Funções

Quando os métodos assumem algum tipo, eles são chamados de funções e precisam do comando return para devolver o valor resultante da execução de suas instruções internas.

```java
//Função sem parâmetro
String frase() {
    String mensagem = "Função sem parâmetro";
    return mensagem;
}
```

###### Figura 10

*Fonte: Reprodução*

Os métodos podem receber dados para serem utilizados internamente, os quais são chamados de parâmetros ou de argumentos.

Quando os parâmetros são passados para os métodos, é criada uma cópia dos valores.

Podemos passar vários parâmetros para os métodos, inclusive de tipos diferentes.

```java
//Procedimento com parâmetro
void numero (int n) {
    int resposta;
    resposta = n * 5;
    System.out.println(resposta);
}

//Função com parâmetro
int soma(int num1, int num2) {
    int resul;
    resul = n + m;
    return resul ;
}
```

**Figura 11**

*Fonte: Reprodução*

