# Windows 10 – Múltiplas Sessões de RDP com RDPWrapper

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** rdp, windows, 10, multiuser 

**Última modificação:** 2019-08-06 15:03

**Autor:** Claudio Junior

---

<p>Nativamente o Windows não permite que você estabeleça uma conexão RDP com múltiplas sessões e depois de algumas pesquisas e testes com a ferramenta RDPWrapper constatei que isso é possível. Na minha avaliação este é um recurso que pode ser útil em diversas situações do dia a dia.</p>
<p>Download: www.100security.com.br/downloads/RDPWrapper.zip</p>
<p>01 Passo</p>
<p>Após o download do RDPWrapper execute o script install.dat</p>
<p> </p>
<p>02 Passo</p>
<p>Após a execução do script execute o arquivo RDPConf.exe para visualizar o painel de configurações.</p>
<p> </p>
<p>03 Passo</p>
<p>No RDP Wrapper Configuration você pode certificar que o Wrapper foi instalado</p>
<p> </p>
<p>04 Passo</p>
<p>Realize a conexão RDP (mstsc /console) para o host alvo se logando com uma das contas, no meu exemplo utilizei o usuário: Marcos</p>
<p> </p>
<p>05 Passo</p>
<p>Nesta sessão estou utilizando a conta de Administrador e como pode ser visto no Gerenciador de Tarefas existem 2 conexões ativas sendo uma com o usuário Administrador e outra com o usuário Marcos.</p>
<p> </p>
<p> </p>