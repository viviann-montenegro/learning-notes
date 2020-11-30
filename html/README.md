# :bookmark_tabs: HTML



O **HTML** é uma linguagem de marcação de texto (HyperText Markup Language), ou seja, uma linguagem para a **estruturação** de conteúdos na web. Utilizamos o HTML para adicionar e organizar todo o conteúdo de nossas páginas web, sejam eles, textos, imagens, links, vídeos, etc. Para isso, o HTML faz uso de uma estrutura em **tags**, utilizadas para delimitar e informar ao navegador o **tipo de conteúdo** que estamos adicionando, para que este saiba como **interpretar**. Além das tags, existem alguns **atributos** que podem ser adicionados a elas, para estruturar de forma ainda mais **específica** nosso conteúdo. A estrutura básica de um **elemento** no HTML é:

​						< “nome da tag” “atributos” (nem sempre obrigatório) > “conteúdo” </ “nome da tag”>

- _**\<a** href="url"**>** “texto” \</a>_ - tag de abertura.
- _\<a **href="url"**> “texto” \</a>_ - atributos.
- _\<a href="url"> **“texto”** \</a>_ - conteúdo.
- _\<a href="url"> “texto” **\</a>**_  - tag de fechamento.

Nem todas as tags possuem **tag de fechamento**, existem algumas como **\<meta>** são chamadas de **tags vazias** pois não possuem conteúdo entre tags.

A **estrutura** básica que precisamos para iniciar um **documento HTML** é:

```html
<!DOCTYPE html>
	<html>
        <head>
            <meta charset="UTF-8">
            <title>Titulo</title>
        </head>
        <body>
        </body>
	</html>
```

- _\<!DOCTYPE html>_ - esta tag **informa** ao navegador que se trata de um documento do **tipo** HTML5, para que este saiba como **interpreta-lo**.
- _\<html> … <\html>_ - esta tag **abre** o documento **HTML**, tudo que for escrito dentro dela faz parte dele.
- _\<head> … <\head>_ - esta tag diz respeito ao **cabeçalho** da página, nela são passadas informações para nosso documento que **não aparecerão** no navegador como os metadados e os links para arquivos de estilo e código.
- _\<meta charset=“UTF-8”>_ - a tag meta diz sobre os **metadados** da página, no caso do atributo **charset**, configuramos o **conjunto de caracteres** da página para o **padrão UTF-8**, assim não teremos problemas com caracteres especiais e acentuações.
- _\<title> … \</title>_ - a tag title define o **titulo da página** que aparecerá na **aba do navegador**.
- _\<body> … \</body>_ esta tag engloba **todo o conteúdo** da página que será mostrada no navegador, é o **corpo** do nosso documento.

Além destas tags que compõem a estrutura básica do nosso documento, temos outras como:

- _\<div> ... \</div>_ - representa um **bloco** de conteúdos **sem significado expressivo** para o navegador.
- _\<section> ... \</section>_ - esta é uma **seção genérica** de conteúdos.
- _\<header> ... \</header>_ - utilizado para **cabeçalho** da página ou de parte dela.
- _\<article> ... \</article>_ - representa um **conteúdo relevante** na página, como um artigo por exemplo.
- _\<aside> ... \</aside>_ - contém um conteúdo **relacionado ao conteúdo principal**, normalmente usado como barras laterais.
- _\<footer> ... \</footer>_ - utilizado para o **rodapé** da página ou de parte dela.
- _\<hn> ... \</hn> (n = 1 a 6)_ - elementos h1 a h6 são **títulos** representados por **ordem de importância**. Normalmente a página tem **apenas um h1** e utilizamos **até o h4** apenas.
- _\<p> ... \</p>_  - parágrafo para **textos maiores** e mais densos, no entanto suporta vídeos, imagens e etc.
- _\<a href=“url”> ... \</a>_ - é uma **ancora** para interligar conteúdos web, href recebe o **hiperlink** para onde a ancora aponta, pode ser link do próprio site, de uma página externa, de um telefone (prefixo tel) ou ainda de um e-mail (prefixo mailto).
- _\<img src=“url”> ... \</img>_ - elemento utilizado para **inserir imagens**, src é um atributo **obrigatório** que recebe o **caminho** da imagem (externa ou interna).
- _\<ul> ... \</ul>_ - representa uma lista onde a **ordem dos itens não é importante**.
- _\<ol> ... \</ol>_ representa uma **lista ordenada**, onde a ordem dos itens importa.
- _\<li> ... \</li>_ - utilizado para criar **itens** de lista.