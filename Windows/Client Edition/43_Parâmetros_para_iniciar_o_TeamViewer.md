# Parâmetros para iniciar o TeamViewer

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** teamviewer, vpn, cmd, linha de comando

**Última modificação:** 2018-10-09 12:46

**Autor:** Claudio Junior

---

<h3 id="sites-page-title-header"><span id="sites-page-title" dir="ltr">Parâmetros para iniciar o TeamViewer</span></h3>
<div id="sites-canvas-main" class="sites-canvas-main">
<div id="sites-canvas-main-content">
<table class="sites-layout-name-one-column sites-layout-hbox">
<tbody>
<tr>
<td class="sites-layout-tile sites-tile-name-content-1">
<div dir="ltr">
<div dir="ltr">
<p>TeamViewer pode ser executado via linha de comando usando diferentes parâmetros que têm de ser precedido por um "-" (por exemplo  --Password 123.456 ). </p>
<p>Alternativamente, você também pode utilizar a forma abreviada, que é executado com um "-" no início (por exemplo, --P 123456 ).</p>
<p>Abaixo você pode ver um exemplo de uma linha de comando em que o TeamViewer está se conectando a uma identificação específica, usando uma senha pré-definida e um modo de conexão pré-estabelecida:</p>
<p><code><span style="font-size: xx-small;">C:\Program Files\TeamViewer7\teamviewer.exe -i 192.168.0.1 --Password test -m fileTransfer</span></code></p>
ou 
<p><code><span style="font-size: xx-small;">C:\Program Files\TeamViewer\TeamViewer7\teamviewer.exe -i 18876347 --Password test</span></code></p>
<p><strong>Os modos de conexão disponíveis são:</strong></p>
<div> </div>
</div>
</div>
<ul>
<li><strong>Remote-Control:</strong><br /><code>teamviewer.exe -i <ID> --Password <Password></code></li>
</ul>
<div dir="ltr">
<div dir="ltr">
<div> </div>
</div>
</div>
<ul>
<li><strong>FileTransfer:</strong><br /><code>teamviewer.exe -i <ID> --Password <Password> -m fileTransfer</code></li>
</ul>
<div dir="ltr">
<div dir="ltr">
<div> </div>
</div>
</div>
<ul>
<li><strong>VPN:</strong><br /><code>teamviewer.exe -i <ID> --Password <Password> -m vpn</code></li>
</ul>
<div dir="ltr">
<div><span style="color: #006000;"><br /></span>
<div><span style="font-family: verdana, sans-serif;"><strong><span style="font-size: small;"><code>FONTE: </code> </span></strong><a href="http://www.teamviewer.com/pt/kb/91-Are-there-parameters-to-start-TeamViewer.aspx" rel="nofollow">http://www.teamviewer.com/pt/kb/91-Are-there-parameters-to-start-TeamViewer.aspx</a></span></div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>