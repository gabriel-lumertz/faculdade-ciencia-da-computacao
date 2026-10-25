---
materia: "Programação Orientada a Objetos"
modulo: "Introdução a Vetores"
semestre: 2
unidade: 4
tipo: material-teorico
fonte: "raw/2-semestre/PROGRAMAÇÃO ORIENTADA A OBJETOS/POObjetos 04.pdf"
tags: [faculdade, programacao-orientada-a-objetos, semestre-2]
aliases: ["Programação Orientada a Objetos - Unidade 4"]
---

# Introdução a Vetores

## 📄 Contextualização

Já estudamos, nos capítulos anteriores, o encapsulamento de informações e a reutilização de códigos. Vimos também como criar os métodos, usar encapsulamento e chamar os métodos criados através de objetos.

Nessa Unidade veremos os conceitos de vetores, e com o conceito aprendido poderemos criar estruturas complexas para atender a demanda de desenvolvimento.

Vamos aprender mais sobre vetores!

Antes de começar a falar de _arrays_ , devemos lembrar o que é uma variável e para que ela serve.

Nas Unidades anteriores, vimos que variável é a representação simbólica dos elementos, e que ficam armazenadas em memória. Cada variável corresponde a uma posição, cujo conteúdo pode se alterado ao longo do tempo durante a execução de um programa. No entanto, a variável só pode ser armazena por um único tipo.

Também vimos que as variáveis podem ser de três tipos: numéricas, alfanuméricas e lógicas, e que para declarar uma variável precisamos definir o seu nome e que tipo de dados será armazenado nela.

Antes de definir vetor, imaginemos a seguinte situação:

Precisamos criar um programa que armazene as seguintes notas de um aluno: 8.0, 10.0, 9.0, 10.0, 8.5, 10.0 e que calcule a média final.

A solução é bem simples. Definiremos uma variável, alocamos um espaço na memória do computador para armazenar uma e somente uma constante por vez, seja ela literal, numérica ou lógica. Quando atribuímos um valor à variável sobrescrevemos seu conteúdo.

Em algumas rotinas é necessário a manipulação de várias variáveis ao mesmo tempo, por exemplo, imagine que o programa deverá controlar o nome de 100 pessoas, ao invés de criar 100 variáveis é possível à criação de apenas uma, que é definida como _array_ .

Mas como criar um _array_ ? É muito simples: especificamos o nome do _array_ e o número de posições da memória que queremos alocar. Cada posição de memória pode armazenar um valor.

Os _arrays_ são criados para que possam armazenar várias informações do mesmo tipo ou da mesma classe; com um vetor também é possível o armazenamento de vários objetos. Essas diversas informações que foram armazenadas em _array_ são de fácil manipulação. As informações ficam disponíveis em forma de tabelas e podem ser acessadas por meio do índices.

Nas Unidades anteriores vimos que para se chamar um programa em _Java_ , devemos criar um programa principal com o método _main_ , e como parâmetro do método devemos criar um _string_ args[], isso nada mais é do que um _array_ de _Strings_ .

Os _arrays_ estão presentes em todas as linguagens de programação, em _Java_ , os _arrays_ são objetos que permitem armazenar uma lista de itens relacionados.

###### Arrays Unidimensionais

Os _arrays_ de uma dimensão são aqueles que possuem um único índice para acessar os elementos. Eles podem ser declarados da seguinte forma:

TIPO-DE-DADO NOME-DO-ARRAY[] = NEW TIPO-DO-DADO[QTDE].

Em que:

Tipo-de-dado: Qualquer tipo de variável ou de classe;

Nome-do-array: Qualquer nome válido vale o mesmo conceito para a criação dos nomes de variáveis.

Exemplos:

Criar um _array_ de nome Cidades contendo 50 elementos do tipo _String_ e seu índice varia de 0 a 49.

```
String Cidades[] new String[50]
```

Criar um _array_ de nome mes contendo 12 elementos do tipo int e seu índice varia de 0 a 11.

```
int mes [] new int [12]
```

Para se atribuir valores a um vetor ( _array_ ), devemos colocar o índice desejado entre os colchetes, como demonstrado abaixo:

```
Ciedades[0] = "São Paulo";
Ciedades[10] = "Rio de Janeiro";
mes[] = 1;
mes[11] = 12;
```

O exemplo que será demonstrado a seguir utiliza um _array_ para armazenar um conjunto de argumentos do tipo inteiro, informado pelo usuário na linha de execução:

```java
class Exemplo {
 public static void main (String args[]) {
  int i, total = 0;
  int N[] = new int [10];
   if (args.length > 0) {
    try {
     for (i = 0; i < args.length; i++) {
      N[i] = Integer.parseInt(args [i]) :
      total = total + N[i];
     }
     System.out.printIn ("0 Total de números digitados na ordem inverse é:"
     for (i = args.length; i <= 0; i--) {
      System.out.printIn (N[i] + " ");
      }
    } catch (NumberFormatException E){
        System. out . printin ("Os argumentos devem ser numeros inteiros")
        }
    } else {
       System . out . printIn ("Digite pelo menos um número");
     }
    }
}
```

Os vetores ( _arrays_ ) podem ser criados e inicializados ao mesmo tempo, para isso, deve-se utilizar o operador _new_ para instanciar um novo objeto. Os _arrays_ criados entre chaves e separados por vírgula devem ter o mesmo tipo que a variável. Veja a sintaxe abaixo:

TIPO-DE-DADO NOME-DO-ARRAY[] = {valores separados por vírgula}

O exemplo abaixo mostra como usar, e explica também a função String.valueOf() para manipulação do conteúdo de um _array_ de caracteres.

```java
public class Exemplo {
    public static void main(String args[]){
        String nomes="";

        char CaracterArray[] = {'a','b','c','d','e','f','g'};

        System.out.println("Mostrando o array " + String.valueOf(CaracterArray));

        System.out.println("Quant. de elementos: " + CaracterArray.length);

        System.out.println("1° ao 3° caracter " + String.valueOf(CaracterArray,0,3));

        String StringArray[] = {"Aprendendo","a","utilizar","array"};

        for(int =0;i<StringArray.length;i++){
            nomes = nomes + StringArray[i] + " ";
        }

        System.out.println("Mostrando array de " + nomes);

        System.out.println("Quant. de elementos do array: " + StringArray.length)

        System.out.println("Mostrando o 1° elemento: " + StringArray[0]);

        System.out.println("Mostrando o último elemento do array: " + StringArray[StringArray.length - 1]);
    }
}
```

**Figura 1**

### Importante!

**Alguns pontos devem ser levados em consideração quando se trabalhar com vetores (** **_arrays_ ) de caracteres  e** **_strings_ : nos** **_array_ de caracteres são utilizados ‘ (apóstrofos) e já nos** **_arrays_ de** **_string_ são utilizados “ (aspas).**

**A função String.valueOf() pode ser usada para apresentar os elementos do** **_array_ de caracteres ou um trecho dele. A função String.valueOf() não funciona para um conjunto de** **_arrays_ do tipo** **_string_ , apenas do tipo** **_char_ (conjunto de caracteres).**

###### Arrays Bidimensionais

Os _arrays_ bidimensionais ou _arrays_ multidimensionais permite a criação de vetores com mais de um índice. Essa característica possibilita que os valores sejam armazenados na forma de matrizes de qualquer dimensão.

TIPO-DO-DADO NOME-DO-ARRAY[][] = NEW TIPO-DO-DADO[<índice>][<índice>].

O exemplo abaixo demonstra o uso de _arrays_ bidimensionais para armazenar 2 (duas) notas de 3 (três) alunos (total de 6 notas). Uma vez armazenadas, o programa solicita ao usuário o número do aluno para exibir suas notas e também a média.

```java
import javas.swing.*;
public class Exemplo {
    public static void main(String args[]){
        float notas[][]=new float[3][2];
        int aluno=0, nota;

        while(aluno<3){
            nota=0;
            while(nota<2){
                System.out.println("Aluno " + (aluno +1) + ", digite a " + (nota+1) + "ª nota:");
                notas[aluno][nota] = Float.parseFloat(JOptionPane.showInputDialog("Informe a nota do aluno"));
                nota++;
            }
            aluno++;
        }

        System.out.println("Digite o número do aluno de 1-3");
        aluno = Integer.parseInt(JOptionPane.showInputDialog("Digite o nr. do aluno:"))
        System.out.println("Aluno: " + aluno);
        System.out.println("Nota1: " + notas[aluno-1][0] + " Nota2: " + notas[aluno-1][1]);
        System.out.println("Média: " + ( ((notas[aluno-1][0]) + notas[aluno-1][1])/2));
    }
}
```

###### Figura 2
###### Arrays de Objetos

Do mesmo jeito que criamos _array_ de dados primitivos ( _int_ , _float_ , _Double_ , _string_ e _char_ ), é possível criar um _array_ para armazenamento de objetos. Isso é muito útil, pois permite as mesmas operações com diversos objetos do mesmo tipo.

O exemplo abaixo utiliza um _array_ de objetos, aproveitando das funcionalidades da classe Veículo.

```java
public class Veiculo{
    private int velocidade;
    public void setVelocidade (int vVelocidade) {
        velocidade = vVelocidade;
    }
    public int getVelocidade(){
        return velocidade;
    }
}
public class Exemplo {
    public static void main (String args[]){
        Veiculo veic[] = new Veiculco[300] ;
        for (int indice = 0; indice < 300; indice++) {
            veic [indice] = new Veiculo () ;
        }
        veic[0].setVelocidade(10);
        vein[10].set.Velocidade(200):
        veic[250].setVelocidade(150);
        for (int i = 0; i < 300; i++){
            veic[i].setVelocidade(0) ;
        }
    }
}
```

###### Passagem de Arrays em Métodos

Os métodos já foram vistos nos capítulos anteriores. Vimos que é possível a criação de métodos que recebem valores, manipulam esses valores e retornam um resultado.

A passagem de _arrays_ em métodos é basicamente o mesmo das variáveis. Quando um método é invocado, um vetor qualquer é informado; esse vetor pode ser manipulado internamente pelo método e também retornar o resultado.

_Public static_ TIPO_DE-ARRAY[] nome-do-método (tipo-do-array nome-do-array[])

O exemplo a seguir mostra o método que recebe um _array_ do tipo inteiro, organiza seus elementos e retorna o _array_ .

```java
import javas.swing.*;
public class Exemplo {
    public static void main(String args[]){
        int numeros[] = new int[10];
        for(int i=0; i < 10; i++){
            JOptionPane.showMessageDialog(null);
            numeros[i] = Integer.parseInt(JOptionPane.showInputDialog("Digite o numero " + (i+1)));
        }

        numeros = ordenaArray(numeros);
        mostraArray(numeros);
    }

    public static int[] ordenaArray(int arr[]){
        int x,y,aux;
        for(x=0;x<arr.length;x++){
            for(y=0;y<arr.length;y++){
                if(arr[x]<arr[y]){
                    aux=arr[y];
                    arr[y]=arr[x];
                    arr[x]=aux;
                }
            }
        }
        return arr;
    }

    public static void mostraArray(int arra[]){
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i] + " ");
        }
    }
}
```

###### Figura 3
