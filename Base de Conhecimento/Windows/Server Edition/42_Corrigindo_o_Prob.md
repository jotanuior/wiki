# Corrigindo o Problema de Conexão RDP (Não há suporte para a função solicitada)

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** wts, rdesktop, remote

**Última modificação:** 2018-10-05 01:44

**Autor:** Claudio Junior

---

<p>Referência: Atualizações de CredSSP para a CVE-2018-0886 <a class="yt-simple-endpoint style-scope yt-formatted-string" href="https://www.youtube.com/redirect?v=D8CKYahr\_Hs&event=video\_description&q=https%3A%2F%2Fsupport.microsoft.com%2Fpt-br%2Fhelp%2F4093492%2Fcredssp-updates-for-cve-2018-0886-march-13-2018&redir\_token=UTWZu\_Bzpv\_rQzo6\_AiwL0Ss8118MTUzODc4Mjc3NUAxNTM4Njk2Mzc1" rel="nofollow">https://support.microsoft.com/pt-br/h...</a></p>
<p>Comando para Executar no Pronpt (Do micro local):</p>
<p>REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters\ /v AllowEncryptionOracle /t REG\_DWORD /d 2</p>