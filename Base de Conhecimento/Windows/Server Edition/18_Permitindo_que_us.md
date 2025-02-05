# Permitindo que usuários instalem impressoras locais sem conceder a permissão de Administrador Local

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** gpo impressora driver 

**Última modificação:** 2015-03-31 21:42

**Autor:** Claudio Junior

---

<h3 class="post-name">Permitindo que usuários instalem impressoras locais sem conceder a permissão de Administrador Local.</h3>
<div class="post-rating"> </div>
<div class="post-author"><img src="http://i1.social.microsoft.com/profile/u/avatar.jpg?displayname=latamblog&size=large" alt="LatamBlog" border="0" /><a href="http://social.technet.microsoft.com/profile/LatamBlog">LatamBlog</a> </div>
<div class="post-date">9 Jan 2012 8:26 AM </div>
<div class="post-attributes">
<ul class="attribute-list">
<li class="attribute-item post-reply-count"><a class="internal-link view-replies" href="http://blogs.technet.com/b/latam/archive/2012/01/09/permitindo-que-usu-225-rios-instalem-impressoras-locais-sem-conceder-a-permiss-227-o-de-administrador-local.aspx#comments">0</a></li>
</ul>
</div>
<div class="post-content user-defined-markup">
<p>By <a href="http://blogs.technet.com/b/latam/archive/2006/12/08/felicio-silva.aspx">Felicio da Silva</a></p>
<p><strong>Introdução</strong></p>
<p>Desde o Windows Vista, muitas opções foram aprimoradas com o intuito de aumentar a granularidade das permissões necessárias aos usuários para instalação de impressoras na rede e locais. Atualmente, existem opções de controlar os servidores de impressão que podem ser utilizados, e inclusive é possível controlar como será a experiência do usuário quando uma impressora na rede for instalada.</p>
<p>Essa nova maneira de controlar como os usuários interagem com a instalação de um dispositivo de impressão esta diretamente relacionada ao Point and Print. O Point and Print é uma funcionalidade presente no Windows Vista e 7 que realiza o download automático e instala o driver de impressora quando um usuário se conecta a uma impressora na rede. Para saber mais sobre o Point and Print e as opções detalhadas que estão disponíveis, consulte o seguinte documento:<a href="http://msdn.microsoft.com/en-us/windows/hardware/gg463359.aspx">http://msdn.microsoft.com/en-us/windows/hardware/gg463359.aspx</a></p>
<p><strong>Configurando o Point and Print via Group Policy</strong></p>
<p>Nesse blog, eu irei descrever o passo a passo para conceder a usuários que não pertencem ao grupo de Administradores Locais, a permissão para instalar qualquer impressora, seja ela na rede ou local. Iremos fazer isso através de uma GPO, e posso adiantar desde já que a liberação em questão não depende do Nível Funcional do Domínio ou da Floresta. Portanto mesmo que você tenha um domínio com nível funcional 2003, você poderá utilizar um desktop rodando Windows 7 com o RSAT instalado para criar e configurar a GPO que irá permitir a instalação de impressoras por usuários que não são administradores locais. Para maiores informações sobre como instalar o RSAT consulte<a href="http://www.microsoft.com/download/en/details.aspx?id=7887">http://www.microsoft.com/download/en/details.aspx?id=7887</a></p>
<p>Uma vez que você esteja com o RSAT instalado no Windows 7, ou que você esteja conectado a um Domain Controller rodando o Windows Server 2008 ou superior. Basta abrir o Group Policy Management, criar uma nova GPO e navegar pelo caminho abaixo:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/5008.image\_5F00\_230AE07D.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/8306.image\_5F00\_thumb\_5F00\_5BD5147D.png" alt="image" width="628" height="410" border="0" /></a></p>
<p>Clique duas vezes em Point and Print Restrictions:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/0602.image\_5F00\_7E49A338.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/5076.image\_5F00\_thumb\_5F00\_2366EDA5.png" alt="image" width="628" height="578" border="0" /></a></p>
<p>Na janela acima, poderemos configurar como será a experiência do usuário quando ele tentar adicionar uma impressora compartilhada em algum servidor de impressão. Meu objetivo nesse tutorial, é mostrar como configurar uma GPO que permita que os usuários possam instalar qualquer impressora na rede ou local, e que a instalação seja o menos complicada possível. Portanto, nas configurações acima, eu não vou especificar os servidores de impressão, permitindo assim que qualquer servidor seja utilizado. Eu também vou configurar a politica para que os usuários não recebam mensagens de confirmação para elevação de privilégio. . O Administrador também possui a opção de configurar o Point and Print através de políticas de User ou Computer, dando ainda mais flexibilidade na aplicação desta funcionalidade.</p>
<p><strong>Permitindo a instalação de drivers como usuário não Administrativo.</strong></p>
<p>Uma vez configuradas essa opções, resolvemos a questão da experiência do usuário no momento da instalação de uma impressora pela rede ou local, no entanto ainda precisamos liberar uma politica adicional para permitir a instalação do driver local. Para tal iremos navegar até a politica abaixo:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/4428.image\_5F00\_4FA37489.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/6558.image\_5F00\_thumb\_5F00\_473F9F32.png" alt="image" width="628" height="283" border="0" /></a></p>
<p>Dentro dessa politica podemos cadastrar os GUIDs de dispositivos que iremos permitir que usuários não administradores possam instalar. No caso das impressoras, iremos cadastrar dois GUIDs:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/1781.image\_5F00\_06311FCE.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/2352.image\_5F00\_thumb\_5F00\_72A3C02C.png" alt="image" width="628" height="577" border="0" /></a></p>
<p>Clique em SHOW, e cadastre os GUIDs:</p>
<p>{4658ee7e-f050-11d1-b6bd-00c04fa372a7}</p>
<p>{4d36e979-e325-11ce-bfc1-08002be10318}</p>
<p>Se você fez tudo certo, deverá visualizar algo semelhante a essa janela:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/5670.image\_5F00\_182D3D8E.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/6646.image\_5F00\_thumb\_5F00\_3B7A3233.png" alt="image" width="511" height="345" border="0" /></a></p>
<p>Para uma lista completa dos GUIDs que você pode utilizar para liberar sua instalação a usuários não administradores consulte: <a href="http://msdn.microsoft.com/en-us/library/ff553426(v=vs.85).aspx">http://msdn.microsoft.com/en-us/library/ff553426(v=vs.85).aspx</a></p>
<p>Uma vez configurada a GPO, basta criar um usuário de teste e coloca-lo em uma OU. Depois basta fazer o link da nova GPO que você criou a essa OU. Não esqueça também de mover a conta de computador ou conta de usuário, dependendo do tipo de política, para a mesma OU que possui o Link com a nova GPO.</p>
<p>Ao final, teste a instalação de uma impressora local ou de rede de modo a fazer a instalação com um usuário que não possui permissões administrativas no Computador, o resultado deve ser semelhante ao abaixo:</p>
<p><a href="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/1460.image\_5F00\_56B28B34.png"><img title="image" src="http://blogs.technet.com/cfs-file.ashx/\_\_key/communityserver-blogs-components-weblogfiles/00-00-00-48-45-metablogapi/1778.image\_5F00\_thumb\_5F00\_75F53207.png" alt="image" width="627" height="462" border="0" /></a></p>
<p><strong>Conclusão</strong></p>
<p><br />Neste artigo descrevemos como utilizar a funcionalidade do Point and Print para instalação automática de impressoras no computador do usuário sem que este possua privilégios administrativos. Vimos que é possível a automação da entrega destas configurações através de Group Policy de forma totalmente desassistida e transparente para o usuário.</p>
</div>