# :vs: Git e GitHub



O **git** é um software de **versionamento** de código. Já o **github** é uma plataforma para hospedagem de **repositórios** de código versionado com git, bem como uma **rede social** de desenvolvedores.

O git é atualmente um dos softwares mais usados para tal função, e isso se dá por sua estrutura. No git, arquivos são armazenados em **blobs** (_bolhas_), objetos que armazenam os **metadados** de determinado arquivo. Dentre estes metadados temos o tamanho do arquivo, seu conteúdo e seu **SHA1** (Secure Hash Algorithm), um conjunto de funções hash criptográficas que geram um **conjunto de caracteres identificador único de 40 dígitos**. Os blobs por sua vez são armazenados dentro de **trees**, que também tem seu próprio SHA1. E por fim temos os **commits**, objeto que une tudo e **dá sentido** à alteração que está sendo feita. Os commits, assim como as trees e os blobs, também possuem SHA1, sendo esse o **hash de todo o conteúdo** que o commit armazena (o tamanho, a tree, o **parent** - o commit ao qual ele esta ligado, o autor, a mensagem e o **timestamp** - a assinatura de data e hora de sua realização). Sendo assim, cada alteração em um arquivo altera seu SHA1, bem como o do blob onde o mesmo está armazenado, sua tree e gera a necessidade de um novo commit para significar toda esta alteração. Tudo isso serve para que haja **segurança** quanto aos arquivos enviados para o git ao se versionar um código.

Quando arquivos não estão dentro de um **repositório** git eles não são rastreados, por isso os chamamos de **untracked**. A partir do momento em que arquivos untracked são adicionados no repositório, passam a ser chamados de arquivos **tracked**, isto é, rastreados pelo git. Dentro dos arquivos rastreados temos arquivos **unmodified**, ou seja, arquivos que estão no repositório, sobre os quais já foi feito um commit e não houveram alterações (eles estão na versão mais recente), os arquivos **modified**, isto é, arquivos que foram modificados e precisam ser adicionados e realizar um commit para que se registre esta alteração (e eles passem a ser staged e unmodified novamente), e arquivos **staged**, que são arquivos que foram modificados e foram adicionados à ‘área’ de commit, arquivos ‘pré-commit’, aguardando o commit para voltarem a ser unmodified.

Além disso o git se comunica diretamente com o **github**, permitindo a distribuição do repositório local de forma **remota**. Mas é importante ressaltar que: antes de **enviar os arquivos** para o servidor todos devem estar **unmodified**, isto é, toda mudança precisa ser adicionada para se tornar staged e então receber um commit para estar pronta para o repositório remoto. No caso de arquivos no repositório remoto alterados no mesmo local por dispositivos diferentes, gerando **commits conflitantes**, o git recomendará que os arquivos sejam puxados para o repositório local e o **merge**, isto é, a junção dos commits conflitantes, seja feito **manualmente**.

Com estas definições compreendidas, podemos começar a trabalhar com o git e o github efetivamente. Sendo o git um **software de linhas de comando**, sua interação acontece no **terminal** (bash) e para isso precisamos de **comandos**. Vale lembrar que existem aplicativos com **interface gráfica** aplicada ao git para **facilitar**, porém ele foi idealizado para que fosse operado por linha de comando.

Os comandos para se utilizar o **git bash** são semelhantes aos comandos no **cmd do Windows**, porém com algumas diferenças. Além dos comandos em si é possível utilizar **flags** como atributos para alguns comandos. Os **principais comandos** que utilizaremos são:

## Comandos de manipulação e navegação

- _ls_ (_dir_ no Windows) - lista os itens do diretório atual.
- _cd ‘nome-da-pasta’_ - move a navegação para a pasta ‘nome-da-pasta’.
- _cd .._ - volta a navegação em um diretório.
- _cd/_ - volta a navegação para a pasta ‘raiz’.
- _clear_ (_cls_ no Windows) - limpa o console.
- _mkdir ‘nome-da-pasta’_ - cria a pasta ‘nome-da-pasta’. 
- _rmdir ‘nome’_ - deleta a pasta ou arquivo ‘nome’ (se for um arquivo use a extensão).
- _mv ‘nome’ ‘novo-nome_ - renomeia a pasta ou arquivo (se for um arquivo use a extensão).
- _mv ‘nome’ ‘local’_ - move a pasta ou arquivo.

## Comandos para repositórios git

- _git init_ - inicia o repositório git no diretório atual (cria o arquivo oculto .git).
- _git add_ - move arquivos modified para a staging área, passam a ser staged aguardando o commit.
- _git commit -m “msg”_ - cria um commit com a mensagem passada (-m serve para passar uma mensagem).
- _git status_ - mostra o status dos arquivos (unmodified, modified ou staged) e se precisa de um commit.
- _git remote add origin https://github.com/use/nome-do-repositorio.git_ - adiciona o caminho à ‘origin’.
- _git remote -v_ - lista os repositórios remotos cadastrados e seus identificadores.
- _git push origin master_ - envia o repositório local para o remoto.
- _git pull origin master_ - puxa o repositório remoto para o local.
- _git clone https://github.com/user/nome-do-repositorio.git_ - baixa um repositório remoto e cria uma cópia na maquina local.

## Comandos para configurações do git

- _git config list_ - mostra as configurações.
- _git config –global –unset “object.config”_ - remove uma configuração.
- _git config –global “object.config” ‘valor_ - adiciona uma configuração.
