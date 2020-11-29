# :game_die: Estrutura de Dados



Na programação **estrutura de dados** são estruturas **organizadas** para o armazenamento de dados na **memória**. Tais estruturas apresentam formatos para que realizem algumas ações básicas como: **adicionar** dados à estrutura, **localizar** um determinado dado, **listar** os dados adicionados, **remover** os dados adicionados, **esvaziar** a estrutura completamente e **classificar** os dados.

Dentre as estruturas podemos listar algumas como principais:

- _Vetores_: um **vetor** é uma estrutura unidimensional indexada, também conhecido como **array**. Em sua declaração fica determinado seu **tamanho** e cada uma de suas posições terá um **índice** de 0 até (tamanho - 1). Cada **posição** armazena um **valor** que fica relacionado ao seu índice. Cada vetor armazena dados de apenas um **tipo de dados**.

- _Matrizes_: uma **matriz** é uma estrutura multidimensional indexada, também pode ser chamada de **array** como os vetores. uma matriz é uma espécie de **vetor de vetores**.

- _Registro_: um **registro** é uma estrutura que fornece um formato especializado para armazenar **informações**. Diferente dos arrays, o registro permite o armazenamento de **mais de um tipo de dados**, sendo cada informação armazenada em um **campo** específico. Para **acessar** um campo de um registro utiliza-se a forma ‘registro.campo’.

- _Listas_: as **listas** são estruturas compostas por **nós** (campo composto pelo valor armazenado e por um ou dois ponteiros apontados para outro nó) que armazenam dados de um determinado tipo em uma **ordem especifica** e podem ser **ajustadas** quanto ao tamanho. Existem dois tipos quando falamos de listas, as listas **ligadas** (onde cada nó aponta para o próximo nó e a navegação é unidirecional) e as listas **duplamente ligadas** (onde cada nó aponta para o nó anterior e para o próximo nó, e a navegação é então bidirecional).

- _Pilha_: as **pilhas** são coleções de elementos que apenas **permitem acesso a um item** de dados armazenados **por vez**. As pilhas podem ser classificadas em dois tipos, **LIFO** - Last in, first out (onde o último elemento é colocado no topo da pilha e, portanto, deve ser o primeiro a ser removido) e **FIFO** - First in, first out (onde o primeiro elemento é inserido no inferior da pilha e será o primeiro a ser retirado pelo topo). 

- _Filas_: as **filas** podem ser imaginadas como pilhas na **horizontal** seguindo o mesmo padrão da pilha **FIFO**, assim como em filas na vida real, o **primeiro** a entrar é também o **primeiro** a sair.

- _Árvore_: as **árvores** são estruturas onde os elementos são organizados de forma **hierárquica**, onde o elemento do topo é a **raiz** e suas **subárvores** são os **nós** ou **folhas** (caso seja o elemento final e não tenha subárvores). Em árvores **binárias** as subárvores à **esquerda** do nó tem valores **menores** e as subárvores à **direita** tem valores **maiores**.

- _Tabela Hash_: a **tabela hash**, também conhecida como tabela de **dispersão** ou **espalhamento**, é uma estrutura que associa **chaves de pesquisa** aos **valores**. Esta estrutura faz uso da função **Hashing** para espalhar os elementos de forma **não ordenada** e dentro do array, associa-los a chaves.

- _Grafos_: as estruturas do tipo **grafos** permitem **programar relação** (arestas) entre os **objetos** (nós ou vértices). Sua estrutura é similar à de uma **Rede Social**.

