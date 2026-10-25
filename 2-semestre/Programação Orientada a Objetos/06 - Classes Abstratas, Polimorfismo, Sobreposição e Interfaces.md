---
materia: "Programação Orientada a Objetos"
modulo: "Classes Abstratas, Polimorfismo, Sobreposição e Interfaces"
semestre: 2
unidade: 6
tipo: material-teorico
fonte: "raw/2-semestre/PROGRAMAÇÃO ORIENTADA A OBJETOS/POObjetos 06.pdf"
tags: [faculdade, programacao-orientada-a-objetos, semestre-2]
aliases: ["Programação Orientada a Objetos - Unidade 6"]
---

# Classes Abstratas, Polimorfismo, Sobreposição e Interfaces

Na Unidade anterior estudamos os conceitos de Herança em POO, e o conceito de herança múltipla. Porém, alguns mecanismos adicionais devem ser implementados para garantir a estruturação das classes mantendo um certo padrão de nomenclatura.

Classes abstratas servem como molde para subclasses concretas que devem implementar seus métodos abstratos e herdar os métodos concretos. Além disso, temos interfaces que obrigam as classes que implementam a ter os métodos da interface. Isso faz com que tenhamos certeza que todas as subclasses dessa estrutura irão possuir os mesmos métodos (a mesma assinatura) através de sobreposição de métodos, criando um padrão.

Cada subclasse que implementa os métodos pode ter uma implementação de método diferente, apesar de ter a mesma assinatura. Isso caracteriza o polimorfismo, pois o nome será o mesmo, mas a forma diferente.

Projetos de sistemas OO possuem dezenas ou centenas de classes. A inserção de uma nova classe na hierarquia pode fazer com que o sistema perca o padrão, porém se ele herdar de classes abstratas e implementar interfaces, isso fará com que ele se “encaixe” no padrão.

Uma subclasse pode herdar apenas de uma superclasse, mas pode implementar várias interfaces.

### Classes Abstratas

À medida que você sobe na hierarquia de herança, as classes tornam-se mais gerais. Em algum momento, a classe torna-se tão geral que ela seria apenas uma base para as outras classes e não mais uma classe com instâncias específicas que você queira utilizar.

Uma classe abstrata é desenvolvida para representar entidades e conceitos abstratos. Usamos uma classe abstrata para criar um padrão de subclasses com comportamentos iguais.

Vamos analisar a Figura 1 a seguir:

![[poo2-06-fig01.webp]]

No Diagrama de classes representado na Figura 1 podemos criar classes comuns (classes concretas) para todas as classes representadas. Isso fará com que possamos instanciar objetos de qualquer uma das sete classes. Porém, a classe Veículo só serviu de molde para atributos e métodos comuns às subclasses Carro e Caminhão. Podemos, por exemplo, ter como atributos na classe Veículo “velocidade” e “passageiros”, e alguns métodos como “acelera”, “freia” e seus métodos de acesso “ _set_ ” e “ _get_ ”.

Desse modo, não há motivos para instanciar objetos da classe Veículo, pois ela serviu apenas como abstração das subclasses da mesma. Nesse caso, dizemos que Veículo pode ser uma classe abstrata.

Para a criação de uma classe abstrata usamos a palavra chave “ _abstract_ ”. Veja na Figura 2 a implementação da classe Veículo.

```java
public abstract class Veiculo {

    //Atributos
    private float velocidade;
    private int passageiros;

    //Construtores
    public Veiculo(float v, int p) {
        velocidade = v;
        passageiros = p;
    }
    public Veiculo() {
        this(0f, 0);
    }

    //Métodos de Acesso
    public void setVelocidade(float v) {
        velocidade = v;
    }

    public float getVelocidade() {
        return velocidade;
    }

    public void setPassageiros(int p) {
        passageiros = p;
    }

    public int getPassageiros() {
        return passageiros;
    }

    //Métodos abstratos
    public abstract void acelera();
    public abstract void freia();
}
```

**Figura 2 – Implementação de classe abstrata Veiculo** Fonte: Reprodução

Uma classe abstrata, além de seus métodos concretos, pode conter também métodos abstratos. Note na Figura 2 que temos dois métodos abstratos, “acelera” e “freia”. Métodos abstratos não possuem corpo, apenas a sua assinatura e eles devem ser implementados obrigatoriamente em suas subclasses, a não ser que suas subclasses também sejam abstratas e nesse caso, devem ser implementados na primeira classe concreta do diagrama.

Portanto, uma subclasse de uma classe abstrata herda os métodos concretos e se obriga a implementar os métodos abstratos.

```java
public class Carro extends Veiculo{

    //Atributos
    private float combustivel;

    //Construtores
    public Carro(float vel, int pas, float comb) {
        super(vel, pas);
        combustivel = comb;
    }
    public Carro() {
        this(0f, 0, 0f);
    }

    //Métodos de acesso
    public void setCombustivel(float comb) {
        combustivel = comb;
    }
    public float getCombustivel() {
        return combustivel;
    }

    //Métodos obrigatórios
    public void acelera() {
        setVelocidade(getVelocidade() + 1);
    }
    public void freia() {
        setVelocidade(getVelocidade() - 1);
    }
}
```

**Figura 3 – Implementação da subclasse concreta Carro** Fonte: Reprodução

Na Figura 3 temos a implementação da classe Carro, que é subclasse de Veiculo. Note que, por ser uma classe concreta, temos obrigatoriamente que implementar os métodos “acelera” e “freia”.

Nesse caso, não podemos instanciar objetos da classe abstrata Veiculo, ou seja, um comando do tipo “Veiculo v1 = new Veiculo();” estaria incorreto.

### Polimorfismo e Sobreposição

O termo polimorfismo é originário do grego e significa “muitas formas” ( _poli_ = muitas, _morphos_ = formas). A propriedade segundo o qual uma operação pode comportar-se diferentemente em classes diferentes.

O polimorfismo é o responsável pela extensibilidade em programação orientada a objetos, promovendo o reuso. Em termos de programação, é o princípio pelo qual duas ou mais subclasses de uma mesma superclasse podem invocar métodos quem tem a mesma identificação (assinatura), mas com comportamentos distintos, especializados para cada classe derivada.

Para exemplificar, pense no termo “abrir”. Você pode abrir uma porta, uma caixa, uma janela ou conta no banco. A palavra abrir pode ser aplicada a muitos objetos diferentes no mundo real e cada objeto interpreta a ação de “abrir” à sua maneira, entretanto podemos simplesmente dizer “abrir” para expressar a ação.

Uma linguagem polimórfica é a que suporta polimorfismo ( _Actionscript_ , _Java_ ), já a linguagem monomórfica não suporta polimorfismo (Pascal, ASP).

Uma maneira de utilizar o polimorfismo, utilização o mecanismo de **Sobreposição de Métodos** (do inglês _override_ ), que consiste em reescrever o método herdado da superclasse. Não confundir Sobrecarga de Métodos ( _overload_ ), que consiste em escrever métodos com o mesmo nome, porém com parâmetros diferentes, o que faz com que eles tenham assinaturas diferentes. Na Sobreposição de Métodos, a assinatura é idêntica ao método herdado, porém o corpo do método é alterado para o propósito específico da subclasse.

Na Figura 2, a classe abstrata Veiculo possui métodos abstratos “acelera” e “freia”. Isso fez com que fôssemos obrigados a implementar esses métodos na classe Carro conforme Figura 3. Se analisarmos novamente a Figura 1, notamos que as classes Uno e Ferrari herdam todos os atributos e métodos de Carro, incluindo os métodos acelera e freia.

Porém, sabemos que os objetos da classe Uno aceleram e freiam mais lentamente que objetos da classe Ferrari, portanto, devemos sobrepor esses métodos para que ajam de acordo com a realidade de cada objeto.

```java
public class Uno extends Carro{

    //Sem atributos

    //Construtores
    public Uno(float vel, int pas, float comb) {
        super(vel, pas, comb);
    }
    public Uno() {
        this(0f, 0, 0f);
    }

    //Sobreposição
    public void acelera() {
        setVelocidade(getVelocidade() + 0.5f);
    }
    public void freia() {
        setVelocidade(getVelocidade() - 0.5f);
    }

}

public class Ferrari extends Carro{

    //Sem atributos

    //Construtores
    public Ferrari(float vel, int pas, float comb) {
        super(vel, pas, comb);
    }
    public Ferrari() {
        this(0f, 0, 0f);
    }

    //Sobreposição
    public void acelera() {
        setVelocidade(getVelocidade() + 3.5f);
    }
    public void freia() {
        setVelocidade(getVelocidade() - 3.5f);
    }
}
```

**Figura 4 – Implementação das classes Uno e Ferrari** Fonte: Reprodução

Note na Figura 4 que nós reescrevemos os métodos acelera e freia das subclasses Uno e Ferrari, adaptando para as próprias necessidades. Podemos notar que a assinatura do método é idêntica à superclasse carro usando então o mecanismo de Sobreposição.

![[poo2-06-fig05.webp]]

**Figura 5 – Exemplo de Polimorfismo e Sobreposição** Fonte: Adaptada de Freepik

Veja mais um exemplo na Figura 5. Temos uma classe abstrata “Telefone” que possui um método **calcularConta** . Por herança, as classes “Movel” e “Fixo” recebem o método **calcularConta** , porém a maneira de calcular a conta de um Telefone Móvel e de um Telefone Fixo é diferente.

Nesse caso, através da Sobreposição de Métodos, reescrevemos os métodos **calcularConta** em cada subclasse para que se adapte à sua necessidade, criando então o conceito de Polimorfismo.

```java
public class Animal {
    public void andar(){
        System.out.println("pessoa andando");
    }
}
public class Cavalo extends Animal{
    public void andar(){
        System.out.println("Cavalo andando");
    }
}
```

**Figura 6 – Exemplo de Polimorfismo e Sobreposição** Fonte: Reprodução

Veja o exemplo da Figura 6, onde temos uma classe “Animal” que possui um único método “andar”. Criamos uma subclasse de Animal chamada Cavalo, que por herança recebe o método andar. Nesse exemplo, estamos sobrescrevendo o método andar para que faça outra coisa.

Tanto a classe Animal como a classe Cavalo são concretas e aceitam instanciar objetos, podemos ter o seguinte código _Java_ :

```
Animal a = new Animal();
Cavalo b = new Cavalo();
a.andar();
b.andar();
```

Para o objeto “a”, aparecerá a mensagem de “pessoa andando” e para o objeto “b” a mensagem será “Cavalo Andando”. Porém, podemos ter também o seguinte código:

```
Animal a = new Animal();
Animal b = new Cavalo();
b.andar();
```

No exemplo anterior, o resultado será o mesmo, para o objeto “a” aparecerá “pessoa andando” e para o “b” será “Cavalo andando”. Porém temos agora “b” como uma **variável polimórfica** . Um objeto do tipo Animal pode referir-se a um objeto do tipo Animal ou a um objeto de qualquer subclasse da classe Animal.

### Interfaces

Muitas linguagens de programação orientada a objetos não possuem o conceito de Herança Múltipla. Isso ocorre porque alguns mecanismos da POO são incompatíveis com processos de herança múltipla. Linguagens como C++ e EiƦel possuem mecanismos de herança múltipla, porém são pouco utilizados por serem complexos e por vezes ineﬁcientes. Vamos analisar a Figura 7 a seguir:

![[poo2-06-fig07.webp]]

**Figura 7 – Cenário de Herança Múltipla**

Analisando a Figura 7 podemos notar que a classe **ComboDrive** herda características das superclasses **GravadorDVD** e **GravadorCD** , caracterizando uma herança múltipla. Porém, sabemos que por herança as subclasses herdam todos os atributos e métodos da classe pai.

No nosso exemplo, o método “ _burn_ ” foi sobrescrito nas duas classes **GravadorCD** e **GravadorDVD** . Qual método ~~s~~ erá chamado quando invocarmos o método “ _burn_ ” da classe **ComboDrive** ?

Esse cenário não é possível em _Java_ e em muitas outras linguagens OO. Nesse caso, usamos outro mecanismo chamado Interfaces.

Uma interface especifica um conjunto de operações públicas de uma classe e/ou um componente. Uma interface não é uma classe, mas um conjunto de requisitos para classes que precisam se adequar a ela, ou seja, você nunca poderá utilizar o operador _new_ para instanciar uma interface.

![[poo2-06-fig08.webp]]

**Figura 8 – Interface**

Note na Figura 8 que Cliente não é uma classe e sim uma Interface. Ela define quais os métodos que deverão ser criados nas classes que a implementam. Uma interface não é herdada e sim implementada. Quando dizemos que uma classe implementa uma interface, estamos firmando um contrato de compromisso que essa classe, obrigatoriamente, implementará os métodos da interface.

Os métodos na interface são métodos “ocos”, ou seja, só possuem as assinaturas, mas não possuem corpo. Além dos métodos, as interfaces podem conter constantes, cujas classes que implementam a interface recebem as constantes como um mecanismo de herança.

Uma classe pode herdar apenas de uma superclasse, porém podem implementar diversas interfaces, podendo assim simular o mecanismo de herança múltipla.

![[poo2-06-fig09.webp]]

**Figura 9 – Interface Imprimível e classe Produto**

Na Figura 9 temos uma Interface Imprimivel e uma classe Produto. A implementação da Interface pode ser algo como:

```java
public interface Imprimivel {
 final char nlin = '\n';
 public String toString();
 public void toSystemOut();
}
```

Podemos notar que, ao invés de usar “ _public class_ ”, usamos “ _public interface_ ” para criação de interfaces e não classes. Nessa interface temos uma constante de nome “ _nlin_ ”, definida com o modificador “final” e a assinatura de dois métodos “ _toString_ ” e “ _toSystemOut_ ”. Notem que esses métodos são ocos e não possuem implementação, semelhante aos métodos abstratos vistos anteriormente, mas sem o “ _abstract_ ”. Todos os métodos de interface serão obrigatoriamente públicos.

Todas as classes que implementam a interface “Imprimivel” terão a obrigação de implementar os métodos “ _toString_ ” e “ _toSystemOut_ ”. Isso faz com que tenhamos um padrão de programação, assim não importa quais os métodos que as subclasses terão, saberemos que pelo menos esses 2 métodos existirão em todas as classes que implementam a interface.

Todos os métodos em uma interface são implicitamente abstratos, porém o modificador “ _abstract_ ” não é utilizado com métodos de interface, apesar de poder ser, ele é desnecessário.

Veja a seguir como uma classe implementa uma interface, utilizando o operador “ _implements_ ”.

```java
public class Produto implements Imprimivel {
 private String descricao;
 private int quantidade;
 public Produto(String d,int q) {
  descricao = d;
  quantidade = q;
}
 public String toString() {
  String resp = "Descrição:" + descricao;
  resp += nlin + "Qtde:" + quantidade;
  return resp;
 }
 public void toSystemOut() {
  String resp = "Descrição:" + descricao;
  resp += nlin + "Qtde:" + quantidade;
  System.out.print(resp);
 }
}
```

Veja no código da classe Produto que usamos a palavra chave “ _implements_ ” para dizer que a classe implementa a interface. Veja que tivemos que criar os métodos “ _toString_ ” e “ _toSystemOut_ ” dentro da classe.

```java
public class TesteProduto {
 public static void main(String args[]) {
  Produto prod = new Produto("Macarrão",10);
  prod.toSystemOut();
  System.out.println("\n" + prod.toString());
 }
}
```

Apesar de não podermos instanciar interfaces, podemos criar variáveis de interface e instanciar objetos de classes que a implementam. O código abaixo teria o mesmo efeito que o anterior:

```java
public class TesteProduto {
 public static void main(String args[]) {
  Imprimivel prod = new Produto("Macarrão",10);
  prod.toSystemOut();
  System.out.println("\n" + prod.toString());
 }
}
```

Podemos então perceber que o conceito de classes abstratas é semelhante ao de interfaces. Quando devemos usar uma ou outra?

Use classes abstratas quando você quer definir um “ _template_ ” para subclasses e você possui alguma implementação (métodos concretos) que todas as subclasses podem utilizar. Use interfaces quando você quer definir uma regra que todas as classes que implementem a interface devem seguir, independentemente se pertencem a alguma hierarquia de classes ou não. Claro que podemos também usar ambas no caso de uma simulação de herança múltipla.
