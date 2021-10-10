
<p align="center">
  <img width="300" src="docs/assets/img/logo.png">
</p>
<h1 align="center">AlligaBot</h1>

 ![GitHub issues](https://img.shields.io/github/issues/fga-eps-mds/2021-1-Bot?color=red)
 ![GitHub closed issues](https://img.shields.io/github/issues-closed/fga-eps-mds/2021-1-Bot?color=green)
 ![GitHub pull requests](https://img.shields.io/github/issues-pr/fga-eps-mds/2021-1-Bot?color=orange)
 ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/fga-eps-mds/2021-1-Bot?color=brightgreen)
 ![GitHub branches](https://badgen.net/github/branches/fga-eps-mds/2021-1-Bot/)
 ![GitHub repo size](https://img.shields.io/github/repo-size/fga-eps-mds/2021-1-Bot?color=purple)
 ![GitHub contributors](https://img.shields.io/github/contributors/fga-eps-mds/2021-1-Bot?color=ff69b4)
 ![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)
<!-- ![GitHub commits count](https://badgen.net/github/commits/fga-eps-mds/2021-1-Bot/)
<!-- [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/fga-eps-mds/2021-1-Bot/blob/main/LICENSE) -->

## 💻 Visão Geral
O AlligaBot propõe-se a ajudar a combater desinformação
no contexto da pandemia do COVID-19, facilitando a  divulgação 
de informações importantes através de um chat bot que responderá as dúvidas
mais frequentes.
	

## 💡 Ideia e Incentivo
Com o decorrer da pandemia percebemos a preocupante e crescente desinformação da
população, e quando tal fato está relacionado a uma pandemia global é 
extremamente perigoso. Por isso achamos necessária a divulgação de informações 
pertinentes sobre a COVID-19 para informar a população e, de alguma forma, 
ajudar no combate mundial ao vírus.

<!-- ## ⚙️ Funcionalidades
- [x] Checkbox:
  - [x] Sub-Checkbox
    - Tópico 1
    - Tópico 2 -->

 ## 📦 Releases
  Release 1 - 14 de setembro
  - [Apresentação Geral](https://youtu.be/S_MtOdIb13s)
  - [Apresentação Equipe Capivaras](https://www.youtube.com/watch?v=TWQMUeZd9EY)
  - [Apresentação Equipe Plus Ultra](https://www.youtube.com/watch?v=5FDRdg9cj_k)
  - [Apresentação Equipe Slowbros](https://www.youtube.com/watch?v=mxh4G5HwLlE)
  
<!--  Release 2 - 28 de outubto -->

## 🚀 Como executar o projeto
### 🛠 Tecnologias e Pré-Requisitos
Esse projeto usa algumas ferramentas para o seu desenvolvimento:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install-win10) para 
desenvolvimento em Windows 10
- [Make](https://www.gnu.org/software/make/)

Você pode assistir esse [vídeo](https://www.youtube.com/watch?v=oQ08ZaOAiGU)
para instalar as ferramentas do Docker e o WSL no Windows 10. Além disso, note
que Docker Compose é um programa diferente do Docker e deve ser instalado 
separadamente.

### ✔️ Instalando e executando
Baixe o repositório e entre nele

    git clone https://github.com/fga-eps-mds/2021-1-Bot.git
    cd 2021-1-Bot

Crie um arquivo para as variáveis ambiente e o preencha com as
informações que faltam.

    cp .example.env .env

Para preencher essas variáveis, dê uma olhada na seção da 
[FAQ "Onde conseguir os tokens e as variáveis de ambiente?"](docs/2021-09-16-faq.md).
Faça build das imagens rodando o seguinte comando:

    make build 

Se esta é a sua primeira vez executando esse comando, isso pode levar 
alguns minutos. Em seguida suba os contêineres com

    make run

Então, treine o bot executando:

    make train


Para conversar com o chatBot, execute o seguinte:

    make shell

Para sair do shell, digite `/stop` ou faça <kbd>Ctrl</kbd>+<kbd>C</kbd>.
Não se esqueça de desligar os containers quando terminar sua sessão de
desenvolvimento. Para desligar os contêineres basta executar:

    make stop

Se você quiser adicionar novos diálogos ao AlligaBot você deve fazer alterações 
no arquivos `bot/domain.yml` e `bot/data/*.yml`, e, em seguida, deve treiná-lo
novamente:

    make train


## 🤝 Como contribuir para o projeto

[Guia de Contribuição](docs/_posts/2021-08-16-como-contribuir.md)

[Código de Conduta](docs/_posts/2021-08-21-code_of_conduct.md)

[Política de Branches](docs/_posts/2021-08-19-branches.md)

[Políticas de Commits](docs/_posts/2021-08-18-commits.md)

[Template para criação de issues](.github/ISSUE_TEMPLATE/custom.md)

[Template para criação de pull requests](.github/pull_request_template.md)

## 👨‍💻 Desenvolvedores
<table class="tg">
<thead>
  <tr>
    <th class="tg-uzvj">Capivara :ox:</th>
    <th class="tg-uzvj">PlusUltra :fleur_de_lis:</th>
    <th class="tg-uzvj">Slowbrows :pig2:</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/49570180?v=4&s=45" alt="Ana Carolina" width="45" height="45">       <br><a href="https://github.com/AnaCarolinaRodriguesLeite" target="_blank" rel="noopener noreferrer"> Ana Carolina </a></td>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/44625056?v=4&s=45" alt="Amanda Nobre" width="45" height="45">        <br><a href="https://github.com/AmandaNbr" target="_blank" rel="noopener noreferrer">Amanda Nobre</a></td>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/78568172?v=4&s=45" alt="Henrique Hida" width="45" height="45">        <br><a href="https://github.com/HenriqueHida" target="_blank" rel="noopener noreferrer">Henrique Hida</a></td>
  </tr>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/36899389?v=4&s=45" alt="Image" width="45" height="45">        <br><a href="https://github.com/MegahNevel" target="_blank" rel="noopener noreferrer"> Eduardo Levenhagem</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/48847770?v=4&s=45" alt="Erick Levy>">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/Ericklevy">Erick Levy</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/39713656?v=4&s=45" alt="Kayro César>">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/kayrocesar">Kayro César</a></td>
  </tr>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/52364259?v=4&s=45" alt="Kathlyn Lara" width="45" height="45">        <br><a href="https://github.com/klmurussi" target="_blank" rel="noopener noreferrer"> Kathlyn Lara</a></td>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/54580766?v=4&s=45" alt="[Douglas Monteles]" width="45" height="45">        <br><a href="https://github.com/DouglasMonteles" target="_blank" rel="noopener noreferrer">Douglas Monteles</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/44177946?v=4&s=45" alt="Luiz Petengill">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/LuizPettengill">Luiz Petengill</a></td>
  </tr>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/79016306?v=4&s=45" alt="Lameque" width="45" height="45">        <br><a href="https://github.com/LamequeFernandes" target="_blank" rel="noopener noreferrer">Lameque Fernandes </a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/78758172?v=4&s=45" alt="Victor Eduardo">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/victorear05">Victor Eduardo</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/53947083?v=4&s=45" alt="Matheus Rapahel">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/matheusrazor">Matheus Rapahel</a></td>
  </tr>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/54778783?v=4&s=45" alt="Matheus Sousa" width="45" height="45">        <br><a href="https://github.com/gatotabaco" target="_blank" rel="noopener noreferrer">Matheus Sousa</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/85000470?v=4&s=45" alt="Pedro Lucas">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/PedroLSF">Pedro Lucas</a></td>
    <td class="tg" style="text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://avatars.githubusercontent.com/u/73257118?v=4&s=45" alt="Matheus Akio">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="https://github.com/matheusakio">Matheus Akio</a></td>
  </tr>
  <tr>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/35047444?v=4&s=45" alt="Thaos Rebouças" width="45" height="45">        <br><a href="https://github.com/Thais-ra" target="_blank" rel="noopener noreferrer">Thais Rebouças</a></td>
    <td class="tg" style="text-align:center;">        <img src="https://avatars.githubusercontent.com/u/37981839?s=45&v=4" alt="Yudi Yamane" width="45" height="45">        <br><a href="https://github.com/yudi-azvd" target="_blank" rel="noopener noreferrer">Yudi Yamane</a></td>
    <td class="tg" style="text-align:center;"></td>
  </tr>
</tbody>
</table>
<small>Feito com <a href="https://www.tablesgenerator.com/html_tables">
  Tables Generator</a>.
</small>

## 📝 Licença
Este projeto está licenciado sob os termos da licença 
[GNU GPL v3.0](./LICENSE).

