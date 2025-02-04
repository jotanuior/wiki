# Problema de rede?

**Categoria:** Base de Conhecimento >> PFsense

**Palavras-chave:** pfsense problema rede backup

**Última modificação:** 2015-03-12 19:41

**Autor:** Luiz Carlos

---

<p> </p>
<p>O primeiro passo é descobrir o problema e isso significa monitorar o que está acontecendo:</p>
<p> - Status / Dashboard: Logs do firewall, status e tráfego das redes interna e externas</p>
<p> - Status / Traffic Graph: com Interface LAN, Filter Local e Display Hostname, descobre quem está usando a rede local. Necessário bater com redes externas (Interfaces de internet)</p>
<p> - Diagnostics / pfTop: com Label e Rules, descobre regras que estão atuando</p>
<p> - Diagnostics / States: conexões ativas e possibilidade de resetar todas conexões</p>
<p> - Status / System Logs: o nome diz tudo</p>
<p> </p>
<p>Outros:</p>
<p> - Status / Gateways</p>
<p> - Status / Interfaces</p>
<p> - Status / Proxy report</p>
<p> - Status / Services</p>
<p> </p>
<p>Caso não seja possível descobrir a causa do problema, o jeito é restaurar algum backup.</p>
<p>Os backups do PFsense são enviadas para alertas@tecmen.com.br em texto cru, bem como notificações e mensagens de alerta.</p>
<p>Deve-se analisar as notificações e alertas a fim de escolher o dia em que o backup representa uma configuração estável.</p>
<p>Então, é necessário salvar o conteúdo do e-mail de backup para um arquivo XML antes de restaurar o backup no PFsense, em Diagnostics / Backup/Restore.</p>
<p>Após clicar em Restore Configuration, o servidor vai rebootar para efetivamente restaurar o backup.</p>
<p>Após o reboot, os pacotes/aplicativos do PFsense serão reinstalados e, antes desse processo terminar, nenhuma alteração deve ser feita no servidor via interface gráfica.</p>