# Habilitando Auditoria de Pastas no Windows Server

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** auditoria, excluir, pastas, pasta, server

**Última modificação:** 2018-05-29 15:10

**Autor:** Claudio Junior

---

<h1 class="post-title entry-title">Habilitando Auditoria de Pastas no Windows Server 2008</h1>
<div class="post-header">
<div class="post-header-line-1"><span class="post-author vcard"><span class="fn">Por: Danilo M Monteiro</span></span><span class="post-labels"><a href="http://www.blogdodanilo.com.br/search/label/active%20directory" rel="tag">active directory</a>, <a href="http://www.blogdodanilo.com.br/search/label/GPO" rel="tag">GPO</a>, <a href="http://www.blogdodanilo.com.br/search/label/Microsoft" rel="tag">Microsoft</a>, <a href="http://www.blogdodanilo.com.br/search/label/Tutorial" rel="tag">Tutorial</a>, <a href="http://www.blogdodanilo.com.br/search/label/Windows%202008%20R2" rel="tag">Windows 2008 R2</a></span><span class="post-comment-link"><a href="http://www.blogdodanilo.com.br/2013/07/habilitando-auditoria-active-directory-windows.html#comment-form">6 comments</a></span></div>
</div>
<div id="post-body-5137378635595971320" class="post-body entry-content">
<div class="separator">Habilite a auditoria de arquivos no Windows para monitorar os eventos relacionados aos usuários, como: acessar, modificar e apagar arquivos e pastas monitorados em sua rede.</div>
<div class="separator">A configuração da Auditoria é feita em duas partes:</div>
<div class="separator"><strong>1) Habilitar a auditoria na pasta que deseja auditar</strong></div>
<div class="separator"><strong>2) Habilitar a auditoria por Diretiva de Grupo</strong></div>
<div class="separator"><strong> </strong></div>
<div class="separator"><strong>Configurando a Pasta que será auditada:</strong></div>
<div class="separator"><span class="notranslate">1.</span> <span class="notranslate">Abra o Windows Explorer e navegue até o arquivo (pasta) em questão.</span> <br /><span class="notranslate">2.</span> Clique com o botão direito do mouse na pasta e clique em <strong>Propriedades</strong>, clique na guia<span class="notranslate"> <strong>Segurança</strong><em>e após</em><strong> Avançado</strong><em>.</em></span> <br /><span class="notranslate">3.</span> <span class="notranslate">Alterne para a guia <em>de </em><strong>Auditoria </strong>e clique no botão <strong>Editar</strong><em>.</em></span> <br /><span class="notranslate">4.</span> <span class="notranslate">Clique em <strong>Adicionar </strong>para escolher os usuários e os grupos de monitoramento.</span> <span class="notranslate">A prática comum é adicionar o grupo de <strong>usuários autenticados.</strong></span> </div>
<div class="separator"><a href="http://2.bp.blogspot.com/-1KEq124f6tg/UeqbM1x2pOI/AAAAAAAAAiQ/Wd2iLMOVP5o/s1600/Aud+01.PNG"><img src="http://2.bp.blogspot.com/-1KEq124f6tg/UeqbM1x2pOI/AAAAAAAAAiQ/Wd2iLMOVP5o/s400/Aud+01.PNG" width="400" height="275" /></a></div>
<div class="separator"> </div>
<span class="notranslate">5.</span> <span class="notranslate">Selecione caixas em eventos necessários para tanto <em>Exito</em> e <em>Falha</em> em <em>Entrada de auditoria.</em></span> <span class="notranslate">Para uma auditoria explícita, selecione todas as caixas.</span><br />
<div class="separator"><a href="http://4.bp.blogspot.com/-ll\_wGVbYI60/UeqbMnG2-QI/AAAAAAAAAiE/z90oSXhPpC8/s1600/Aud+02.PNG"><img src="http://4.bp.blogspot.com/-ll\_wGVbYI60/UeqbMnG2-QI/AAAAAAAAAiE/z90oSXhPpC8/s400/Aud+02.PNG" width="307" height="400" /></a></div>
<br />Aplicando Auditoria via GPO<br /><span class="notranslate"><br /></span><span class="notranslate">1. Abra Iniciar -> Executar, d</span><span class="notranslate">igite <strong>secpol.msc</strong> e tecle Enter.</span> <br /><span class="notranslate">2.</span> Edite ou crie a GPO onde deseja aplicar a Auditoria.<br /><span class="notranslate">3.</span> <span class="notranslate">Navegue até <strong><em>Configuração de Segurança</em> -> <em>Diretivas locais</em> -> <em>Diretiva de auditoria.</em></strong></span> <br /><span class="notranslate">4.</span> <span class="notranslate">Edite a <strong>Auditoria de acesso a objetos.</strong></span><br />
<div class="separator"><a href="http://3.bp.blogspot.com/-CvVlou-W2xU/UeqbNHUXegI/AAAAAAAAAic/I3v1uWVTwv4/s1600/Aud+04.PNG"><img src="http://3.bp.blogspot.com/-CvVlou-W2xU/UeqbNHUXegI/AAAAAAAAAic/I3v1uWVTwv4/s400/Aud+04.PNG" width="400" height="217" /></a></div>
<div class="separator"> </div>
5. Nas Propriedades da Auditoria, marque as opções desejadas, conforme abaixo:<br />
<div class="separator"><a href="http://1.bp.blogspot.com/-CEXnRkwcKHY/UeqbNBK-y2I/AAAAAAAAAiY/UrV23\_vXunw/s1600/Aud+05.PNG"><img src="http://1.bp.blogspot.com/-CEXnRkwcKHY/UeqbNBK-y2I/AAAAAAAAAiY/UrV23\_vXunw/s400/Aud+05.PNG" width="333" height="400" /></a></div>
6. Clique em OK, e feche o Editor de GPO<br /><br />Para aplicar as configurações imediatamente no computador, abra o Prompt de Comando e digite o comando"<strong>gpupdate /force</strong>"<br />
<div class="separator"> </div>
<br /><span class="notranslate">Agora, todas as tentativas de acesso serão rastreadas no log de segurança do Visualizador de Eventos.</span> Se você quiser verificar quem excluiu determinado diretório, abra o <strong>Visualizador de Eventos</strong>em <strong>Logs do Windows</strong> na parte de <strong>Segurança</strong>. Procure o evento com número de <strong>identificação 4663</strong>, conforme mostrado abaixo.<br />
<div class="separator"><a href="http://1.bp.blogspot.com/-JY\_xXB2fmSE/UeqbNrJA2mI/AAAAAAAAAis/6mOWNWt8f64/s1600/Aud+07.PNG"><img src="http://1.bp.blogspot.com/-JY\_xXB2fmSE/UeqbNrJA2mI/AAAAAAAAAis/6mOWNWt8f64/s640/Aud+07.PNG" width="640" height="328" /></a></div>
<div class="separator"><a href="http://2.bp.blogspot.com/-IS87K-aQEJk/UeqbNqGPToI/AAAAAAAAAi0/g1GFE0QCY28/s1600/Aud+08.PNG"><img src="http://2.bp.blogspot.com/-IS87K-aQEJk/UeqbNqGPToI/AAAAAAAAAi0/g1GFE0QCY28/s400/Aud+08.PNG" width="400" height="90" /></a></div>
<div class="separator"><a href="http://1.bp.blogspot.com/-xRJolue9Mbs/UeqbOKXi71I/AAAAAAAAAjI/dUUcTO2R8Dg/s1600/Aud+09.PNG"><img src="http://1.bp.blogspot.com/-xRJolue9Mbs/UeqbOKXi71I/AAAAAAAAAjI/dUUcTO2R8Dg/s400/Aud+09.PNG" width="400" height="90" /></a></div>
<div class="separator"><a href="http://1.bp.blogspot.com/-tHa7P45XVG0/UeqbOUIfVfI/AAAAAAAAAjE/\_zU96lg8qkI/s1600/Aud+10.PNG"><img src="http://1.bp.blogspot.com/-tHa7P45XVG0/UeqbOUIfVfI/AAAAAAAAAjE/\_zU96lg8qkI/s400/Aud+10.PNG" width="400" height="92" /></a></div>
</div>