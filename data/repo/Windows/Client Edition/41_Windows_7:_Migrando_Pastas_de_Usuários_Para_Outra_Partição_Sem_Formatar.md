# Windows 7: Migrando Pastas de Usuários Para Outra Partição Sem Formatar

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** windows, home, transferencia

**Última modificação:** 2018-10-02 19:12

**Autor:** Claudio Junior

---

<div class="wrapfullpost">
<div class="post hentry">
<h3 class="post-title entry-title"><a href="http://nataldelima.blogspot.com/2013/05/mudando-perfil-usuario-windows-de.html">Windows 7: Migrando Pastas de Usuários Para Outra Partição Sem Formatar</a></h3>
<div class="post-header-line-1"> </div>
<div class="postmeta-primary"><span class="meta\_author">Por Natal Lima às 15:42</span> <span class="meta\_categories">Marcadores:</span></div>
<div class="post-body entry-content">
<p> </p>
<div>Você acompanhou no <a href="http://nataldelima.blogspot.com.br/2013/04/carregar-perfil-windows-7-outra-particao.html">último artigo</a> que é possível carregar o perfil de usuário em uma partição diferente do sistema. Isso se torna vantajoso em caso de uma manutenção, ou mesmo formatação do sistema operacional, pois nesse caso o prejuízo seria apenas os programas que deverão ser reinstalados, ao passo que a partição com os dados nesse caso não seria afetada.</div>
<div>Mas e se você está usando seu Windows 7 há um bom tempo e está operando normalmente, há como forçá-lo a carregar sem a necessidade de formatar? A resposta é sim, e basicamente seguindo os passos do <a href="http://nataldelima.blogspot.com.br/2013/04/carregar-perfil-windows-7-outra-particao.html">último artigo</a>. Mas existe uma preparação prévia:</div>
<div class="separator"> </div>
<div>Antes de tudo, é preciso realizar um backup de seus dados. O Windows 7 tem um aplicativo de migração que facilita e muito o trabalho: é o Transferência fácil de arquivos. Para acessá-lo, clique no botão iniciar e digite na caixa de texto transfer. Com isso você visualiza o aplicativo.</div>
<div> </div>
<table class="tr-caption-container">
<tbody>
<tr>
<td><a href="http://3.bp.blogspot.com/-21DkDmIJOFs/UZUvkFIy1aI/AAAAAAAAAE8/lf740SbAExg/s1600/tela-01.jpg"><img title="Transferência fácil do Windows - como fazer backup" src="http://3.bp.blogspot.com/-21DkDmIJOFs/UZUvkFIy1aI/AAAAAAAAAE8/lf740SbAExg/s400/tela-01.jpg" alt="Transferência fácil do Windows - como fazer backup" width="400" height="313" /></a></td>
</tr>
<tr>
<td class="tr-caption">Na primeira tela de transferência fácil do Windows, escolha a terceira opção para realizar  o backup de seus arquivos</td>
</tr>
</tbody>
</table>
<div> </div>
<div>É importante que tenha uma case que comporte seu backup. Recomendo um HD externo ou um pen drive de alta capacidade. Com o HD externo conectado, escolha a terceira opção: um disco rígido externo ou unidade flash USB.</div>
<div> </div>
<table class="tr-caption-container">
<tbody>
<tr>
<td><a href="http://3.bp.blogspot.com/-it3N6riSmyo/UZUwV55WPQI/AAAAAAAAAFE/uOFTIwzQla8/s1600/tela-02.jpg"><img title="Selecione a opção este é o meu computador antigo" src="http://3.bp.blogspot.com/-it3N6riSmyo/UZUwV55WPQI/AAAAAAAAAFE/uOFTIwzQla8/s400/tela-02.jpg" alt="Selecione a opção este é o meu computador antigo" width="400" height="313" /></a></td>
</tr>
<tr>
<td class="tr-caption">Nessa tela, selecione a opção "Este é o meu computador antigo"</td>
</tr>
</tbody>
</table>
<div> </div>
<table class="tr-caption-container">
<tbody>
<tr>
<td><a href="http://3.bp.blogspot.com/-bIUh2QOCQ2Q/UZUwxIegNII/AAAAAAAAAFM/T6qOdGC44QY/s1600/tela-03.jpg"><img title="Perfis de usuários" src="http://3.bp.blogspot.com/-bIUh2QOCQ2Q/UZUwxIegNII/AAAAAAAAAFM/T6qOdGC44QY/s400/tela-03.jpg" alt="Perfis de usuários" width="400" height="313" /></a></td>
</tr>
<tr>
<td class="tr-caption">Aqui você visualiza os perfis de usuário, ou seja, todos os os usuários da pasta c:\users.</td>
</tr>
</tbody>
</table>
<div>É justamente aqui que estão os documentos, imagens, emails caso utilize Outlook, Thunderbird ou Windows Live Mail.</div>
<table class="tr-caption-container">
<tbody>
<tr>
<td><a href="http://3.bp.blogspot.com/-eM4WOo-r4cY/UZUxlmARDkI/AAAAAAAAAFU/7Ing2B89SUA/s1600/tela-04.jpg"><img title="Salvando o backup" src="http://3.bp.blogspot.com/-eM4WOo-r4cY/UZUxlmARDkI/AAAAAAAAAFU/7Ing2B89SUA/s400/tela-04.jpg" alt="Salvando o backup" width="400" height="313" /></a></td>
</tr>
<tr>
<td class="tr-caption">Apenas clique em salvar. Não é necessário senha.</td>
</tr>
</tbody>
</table>
<div> </div>
<div class="separator"> </div>
<div>Agora que seu backup está pronto e seus dados salvos, você precisa dividir o HD em duas partições, de modo que a partição C fique para sistema e a outra armazenará os dados. Não precisa formatar o HD para isso.  Veja nesse vídeo abaixo como fazer:</div>
<div> </div>
<div class="separator"><iframe src="https://www.youtube.com/embed/fxrsYSvSTqY?feature=player\_embedded" width="320" height="266" data-mce-fragment="1"></iframe></div>
<div> </div>
<div> </div>
<div>
<div>Consideramos no último post que uma instalação ideal de sistema operacional seria separar sistema de dados em partições diferentes, pois isso facilita em muito a manutenção. Mas por padrão o <em>Windows </em>cria a pasta users (usuários) na mesma partição de sistema. Seria mais interessante se pudéssemos padronizar a criação de novos perfis diretamente na partição de dados, por exemplo d:. </div>
<div> </div>
<div>Para fazer isso, não é uma simples questão de <em>CTRL+C</em> e <em>CTRL+V</em> na pasta <em>c:\users</em> para <em>d:\users</em>, pois visto que o sistema está em execução e usando arquivos carregados em seu perfil, você simplesmente não conseguirá fazer essa operação por esse método. Um método que ensinarei nesse artigo envolve editar o registro do windows. Apenas lembrando que os passos abaixo servem para o <em>Windows 7</em>. Não testei, mas acredito que sirva também para <em>Windows Vista</em> e <em>Windows 8</em>. Então siga os passos:</div>
<div>
<ul>
<li>Crie uma pasta chamada <em>Users</em> na partição <em>d:</em>, na raiz mesmo, de modo a ficar: <em>d:\Users</em>;</li>
<li>Segure a tecla <em>windows</em> e pressione E, de modo a abrir o <em>Windows Explorer</em>;</li>
<li>Aperte a tecla <em>TAB</em> e no menu que abrir selecione <em>"Ferramentas"</em>, e em seguida <em>"opções de pasta e pesquisa"</em>;</li>
<li>Selecione a guia <em>"modo de exibição"</em> e dentro da lista, marque a opção <em>"Mostrar arquivos, pastas ou unidades ocultas"</em>;</li>
<li>No <em>Windows Explorer</em>, clique na unidade <em>c:\</em> e em seguida na pasta <em>Users</em>;</li>
<li>Segure a tecla <em>shift</em> e dê um clique apenas para selecionar as pastas <em>Public</em> e <em>Default</em>;</li>
<li>Segure a tecla <em>CTRL</em> e aperte o C;</li>
<li>Agora vá à unidade <em>D:\</em> e abra a pasta <em>Users</em> que criamos no primeiro passo;</li>
<li>Dê um <em>CTRL + V</em> e serão coladas as pastas <em>Public</em> e <em>Default</em>;</li>
<li>Aperte o botão iniciar e no campo de busca digite <em>regedit</em>;</li>
<li>Assim que ficar visível no menu, clique com o botão direito e abra-o como administrador;</li>
<li>Na árvore do <em>Regedit</em>, clique nas chaves: <em><strong>HKEY\_LOCAL\_MACHINE -> Software -> Microsoft -> WindowsNT -> CurrentVersion -> ProfileList;</strong></em></li>
<li>À direita, clique na chave <em>Default</em> e substitua na caixa que abrir a variável <em>%SystemDrive%\</em> por <em>D:</em>, de modo a ficar: <em>d:\Users\Default</em>;</li>
<li>Agora clique na chave <em>Public</em> e e substitua na caixa que abrir a variável <em>%SystemDrive%\</em> por <em>D</em>:, de modo a ficar: <em>d:\Users\Public</em>;</li>
<li>Feche o <em>regedit</em>;</li>
<li>Vá no <em>painel de controle</em>, opção <em>usuários</em> e crie uma conta administrativa qualquer, por exemplo teste;</li>
<li>Dê um <em>logoff</em> (botão iniciar, seta ao lado do desligar e clique em trocar usuário) e entre com a conta que acabou de criar;</li>
<li>Abra o <em>Windows Explorer</em> e entre nas pasta <em>d:\users</em> e verifique se foi criada a pasta com o novo usuário;</li>
</ul>
<div>Pronto, agora está funcionando! Mas se você já está usando há algum tempo seu computador certamente seus arquivos e perfis estão carregando na unidade C, mas gostaria de carregar na D. Essas alterações que fizemos aplica-se aos perfis novos que serão criados a partir dessas alterações. Mas há a possibilidade de mudar isso? Sim, e de várias maneiras. Num próximo post vou ensinar uma maneira fácil utilizando uma ferramenta nativa do <em>Windows 7</em>.</div>
</div>
</div>
<div> </div>
<div> </div>
<div>Feito todos esses passos, é hora de voltar o backup. Conecte seu HD externo no PC e abra o arquivo com extensão .mig, que é o backup.</div>
<div> </div>
<table class="tr-caption-container">
<tbody>
<tr>
<td><a href="http://1.bp.blogspot.com/-\_XqftnrfPAo/UZUx1T31WaI/AAAAAAAAAFc/VUX2gqdlezg/s1600/tela-05.jpg"><img src="http://1.bp.blogspot.com/-\_XqftnrfPAo/UZUx1T31WaI/AAAAAAAAAFc/VUX2gqdlezg/s400/tela-05.jpg" width="400" height="313" /></a></td>
</tr>
<tr>
<td class="tr-caption">Siga os passos para restauração de seu backup.</td>
</tr>
</tbody>
</table>
<div class="separator"> </div>
<div class="separator">Lembre-se, antes de você mexer na estrutura do sistema, como modificar chaves de registro ou criação de partições, sempre é necessário realizar um backup, para evitar perdas desnecessárias.</div>
</div>
</div>
</div>