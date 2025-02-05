# Instalar certificado via GPO

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** GPO, certificado, digital‏

**Última modificação:** 2015-04-29 13:07

**Autor:** Claudio Junior

---

<p>Ola pessoal, depois de muita pesquisa e ajuda de alguns amigos, vou compartilhar esta solução, que para mim resolveu, usei a GPO apenas para rodar os scripts.</p>
<p>Eu coloquei primeiro o certificado.pfx em um compartilhamento de rede (por exemplo,% LOGONSERVER% \ netlogon \ certificates \ vendorcertificate.pfx).</p>
<p> </p>
<p>Em seguida eu criei uma importação e certificado.bat  que executa esse comando:</p>
<p><code>certutil -f -user -p "senhadocertificado" -importpfx "%LOGONSERVER%\netlogon\certificates\certificado.pfx"</code></p>
<p>Criei então um script .VBS chamados de silenciosa.vbs que irá executar o script de certificado.bat silenciosamente (para que o usuário não vê um flash da janela do CMD, quando este é executado):</p>
<p><code>Set oShell = CreateObject ("Wscript.Shell") <br />Dim strArgs <br />strArgs = "cmd /c %LOGONSERVER%\netlogon\certificates\import-certificate.bat" <br />oShell.Run strArgs, 0, false</code></p>
<p>Os caminhos dos scripts ficam por conta de vocês, <code>aplique o arquivo silenciosa.vbs, por GPO para um grupo ou para o Domínio inteiro que vocês desejaram que será replicado para todas as estações. <br /></code></p>
<p><code>Muito obrigado pela atencao de todos e marquem como resposta para ajudar a outros!</code></p>
<p>abraços!!<code><br /></code></p>
<hr class="ecxsig" />
<p>Administrador de Redes - MCP</p>