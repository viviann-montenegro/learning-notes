# :clapper: JavaScript



O **JavaScript** é uma linguagem de script **multiplataforma**, ou seja, executada em **tempo real** e utilizada em diversas plataformas (como navegadores e dispositivos móveis). Além disso é **client side**, executada na **máquina local**. O JavaScript é também uma linguagem **interpretada**, isto é, executada de cima para baixo e sem precisar sem transformada em outro tipo de arquivo para executar, diferente das linguagens **compiladas**. Através do **DOM** (Documento Object Model) o JavaScript consegue alterar todos os **elementos HTML** e todos os atributos e **estilos CSS**. 

Conta também com uma **tipagem fraca e dinâmica**, ou seja, não há **verificação das operações** (por exemplo, somar um inteiro e uma string gera uma conversão automática e não resulta em erros) e não há necessidade de **explicitar o tipo** da variável em sua criação (neste caso a variável tem seu tipo definido durante a atribuição de seu valor, o que chamamos de **inferência de tipo**). Para evitar problemas com esta tipagem existem ferramentas como o **TypeScript** (um  _superset_ de JS, que adiciona tipos em tempo de desenvolvimento e funcionalidades que o JS não tem por padrão como _interface_, _enums_ e _tipos genéricos_) e o **Flow** (que é similar ao TS em relação à checagem de tipos).

Dentre os **conceitos** do JavaScript temos as **funções de 1ª classe e de ordem maior** (que asseguram a atribuição de funções à variáveis e estruturas de dados, bem como sua passagem por argumentos), o **closure** (ou fechamento, diz respeito à capacidade das funções acessarem variáveis fora de seu escopo em seu ambiente de referência, quanto a escopos temos _global_, _de função_ de _de bloco_), o **currying** (que é a técnica de transformar uma função que recebe vários parâmetros em uma função que receba apenas um parâmetro e retorne, para cada parâmetro, uma nova função, ou seja, em uma _função pura_), o **hoisting**, que pode ser dividido em **hoisting de variável** (consiste em, caso uma variável seja referida antes de ser declarada, sua declaração _“sobe”_ para antes de sua referência evitando erros de variável não declarada, entretanto sua atribuição permanece no lugar em que foi feita e qualquer referencia anterior resultará em _“undefined”_) e **hoisting de função** (similar ao hoisting de variável porém, neste caso, a função _“sobe”_ completa, sua declaração e seu bloco de definição) e a **imutabilidade** (que evita _side effects_ ou alterações indesejadas nos atributos dos objetos, pois nos obriga a fazer uma cópia do objeto para realizar qualquer alteração, nunca em sua referencia).

Com relação às **variáveis**, temos três formas de declara-las:

- _var_ - utilizado para declarar uma **variável** em versões mais antigas, respeita os escopos _global_ e _de função_ porém não reconhece o escopo _de bloco_, o que o torna **menos indicado.** 
- _let_ - utilizado para declarar uma **variável** a partir de versões mais recentes, respeita todos os escopos e assim torna-se **mais indicado**.
- _const_ - utilizado para declarar **constantes**, ou seja, no caso de **tipos primitivos** não permite alteração de valor, no caso de **objetos** não permite alteração no _“ponteiro”_ mas possibilita mudança nas propriedades e no caso de **array** permite adição de itens, remoção de itens e mudar valores por referencia direta, mas não permite que o array seja transformado em outro. Também respeita todos os escopos.



