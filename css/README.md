# :art: CSS



O **CSS** é uma folha de estilos em cascata (Cascade StyleSheet), ou seja, é a linguagem que utilizamos para criar **regras de estilo** para **elementos ou grupos de elementos**. No CSS, bem como no HTML, existe uma estrutura básica para as declarações. Aqui ao invés de tags utilizaremos **seletores** e **blocos de declaração** com pelo menos uma declaração, isto é, regra de estilo.

```css
a, p, h1, h3 {
    color: blue;
    font-size: 14px;
}
```

- _‘a’, ‘p’, ‘h1’, ‘h3’_ - são os **seletores** CSS, elementos do HTML que referenciamos para aplicar o estilo.
- _‘color: blue;’ e ‘font-size: 14px;’_ - são as **declarações**, ou seja, regras de estilo que aplicaremos aos seletores.

Quando temos em um documento HTML **muitos elementos** de um **mesmo tipo** e não queremos aplicar o estilo a todos eles podemos fazer referencia a **classes ou ids**. Ambos no HTML aparecem como um **atributo** (como _\<header class=“header”> … \</header>_ ou _\<header id=“header”> … \</header>_ ) class ou id e, vale lembrar que, um atributo **class pode se repetir** quantas vezes quisermos no documento mas um atributo **id deve ser único**(não podemos ter dois elementos HTML com o mesmo id mas podemos com a mesma classe). Já no CSS vamos referenciar a classes por **."nome-da-classe”** e a ids por **#“nome-do-id”**.

Outro fator importante do CSS é a **composição** dos elementos, o **box model**. O box model, ou modelo de caixa, é a forma como os elementos são construídos dentro do CSS. Cada elemento terá:

- _margin_ - a **margem** que faz o **espaçamento entre os elementos** (pode ser espaçada e alinhada de forma automática com a declaração _margin: auto;_).
- _border_ - a **borda** dos elementos, esta **circunda** o conteúdo e seu preenchimento.
- _padding_ - o **preenchimento** dos elementos que faz o **espaçamento entre o conteúdo e a borda**.
- _content_ - o **conteúdo** desde elemento (texto, imagem, etc.)

Quando vamos fazer uma declaração no CSS para **atribuir** determinados valores aos **elementos de espaçamento do box model** podemos fazer atribuindo valores para o **eixo y** (superior e inferior) e para o **eixo x** (direita e esquerda) separadamente ( _padding: 10px 5px;_), atribuindo valores para **cada posição** (na ordem superior, direita, inferior, esquerda) separadamente (_padding: 10px 5px 15px 0_; No caso de um valor ser **0 não precisamos da unidade px** - pixels), ou ainda atribuindo valores para cada posição em **declarações individuais** (_padding-top: 10px; padding-right: 5px; padding-bottom: 15px; padding-left: 0;_). Podemos utilizar a unidade **px para pixels** ou a **porcentagem** de alteração com o símbolo ‘%’. Além disso, podemos definir também **larguras e alturas máximas** para as propriedades com as declarações _max-width_ e _max-height_, que determinam o **tamanho máximo** que os elementos podem ter.

Dentro do CSS podemos trabalhar com **atributos** como: dimensões, cores, tipos de fonte (no caso de textos), formatos, estilos e etc. Para isso temos algumas **propriedades** como as que vimos que compõem o box model e atributos diversos para cada uma destas propriedades, alguns destes são:

- _background_ - propriedade do plano de fundo da página.
  - _background-color: “cor”_ - altera a **cor** do background (as cores podem ser passadas com o nome da cor em inglês ou seu código HEX);
  - _background-image: “url”_ - adiciona uma **imagem** no background;
  - _background-position: “posição”_ - altera a **posição** do background;
- _border_ - propriedade da borda dos elementos (box model).
  - _border: “largura” “estilo” “cor”_ - altera a **largura ou espessura** da borda (tamanho px/%), seu **estilo** (solid, dashed - linha pontilhada ou dotted - bolinhas) e sua **cor** (como vimos com o espaçamento ela pode ser estilizada de forma separada para cada lado);
  - _border-radius: “tamanho”px_/% - altera a curvatura dos cantos da borda (para tornar a borda em circulo usamos o valor 50%);
- _font_ - propriedade das fontes presentes no documento.
  - _font-family: “nome-da-fonte”_ - altera a **fonte do texto**, podem ser fontes da web (sua url precisa ser referenciada no documento) ou instaladas na máquina; As fontes ‘safe’ estão na maioria dos dispositivos; Passar uma segunda fonte a deixa como fonte de **backup** caso a primeira não funcione;
  - _font-size: “tamanho”px_ - altera o **tamanho** da fonte;
  - _font-style: “estilo”_ - altera o **estilo** da fonte (como negrito ou italico);
  - _font-weight: “estilo”_ - altera o **peso** da fonte (como bold, diferente do negrito isso tem significado de importancia para o navegador);
- _text_ - propriedades dos textos no documento.
  - _text-transform: “estilo”_ - muda a **forma** do texto (como _uppercase_ - todos os caracteres em caixa alta, _lowercase_ - todos os caracteres em caixa baixa e _capitalize_ - as primeiras letras de cada palavra em caixa alta);
  - _text-decoration: “estilo”_ - muda os **destaques** do texto (como _underline_ - sublinhado, _overline_ - com linha acima, _line-throught_ - cortado ou _none_ - sem decoração);
  - _text-align: “estilo”_ - altera o **alinhamento** do texto.
- _list_ - propriedade das listas (ordenadas ou não).
  - _list-style-type: “estilo”_ - altera o tipo de **marcador** da lista (pode ser uma imagem com a declaração _list-style-image_);

