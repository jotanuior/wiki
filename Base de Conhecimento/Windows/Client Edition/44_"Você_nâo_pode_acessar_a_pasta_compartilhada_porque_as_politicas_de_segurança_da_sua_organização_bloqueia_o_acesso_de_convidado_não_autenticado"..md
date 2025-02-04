# "Você nâo pode acessar a pasta compartilhada porque as politicas de segurança da sua organização bloqueia o acesso de convidado não autenticado".

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** compartilhada, segurança 

**Última modificação:** 2018-11-21 21:25

**Autor:** Claudio Junior

---

<p>Pessoal, depois de muita pesquisa sobre os mais variados assuntos, consegui uma solução:<br /> <br /> Vão até o editor de políticas locais (gpedit.msc);<br /> <br /> Navegue até Configuração do Computador>Modelos Administrativos>Rede>Estação de trabalho LANMAN;<br /> <br /> Habilite a configuração Habilitar logons de convidados não seguros;<br /> <br /> Reinicie.<br /> <br /> Fonte: https://support.microsoft.com/en-us/help/4046019/guest-access-smb2-disabled-by-default-in-windows-10-server-2016<br /> <br /> Ao que indica essa nova atualização visa impossibilitar acesso à ambientes sem autenticação, o que até é legal, mas nesses casos onde você tem um storage que não requer autenticação você fica rendido.</p>