# Instalando um Domain Controller em Windows Server 2016 Core

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** 

**Última modificação:** 2019-04-23 15:28

**Autor:** Claudio Junior

---

<header class="entry-header">
<h1 class="entry-title">Instalando um Domain Controller em Windows Server 2016 Core</h1>
</header>
<div class="entry-content">
<p>Fala pessoal, boa tarde.</p>
<p>Antes de qualquer coisa, agradeço ao <a href="https://vfava.wordpress.com/">Vitor Fava</a> pela ideia e inspiração para esse vídeo!</p>
<p>Neste video mostro pra vocês o passo a passo para instalar um Windows Server 2016 Core – Sem interface Gráfica – e configurar nele um Controlador de Domínio (DC ou AD Server).</p>
<p>Para isso utilizei o  Windows Server 2016 Evaluation Edition (Expira em 180 dias) sobre o VMWARE Workstation.</p>
<p><iframe src="https://www.youtube.com/embed/tJY-jSAVrfA?feature=oembed" width="840" height="473" data-mce-fragment="1"></iframe></p>
<p>Aqui estão as referências que usei:</p>
<p><a href="https://blogs.technet.microsoft.com/chadcox/2016/10/25/chads-quick-notes-installing-a-domain-controller-with-server-2016-core/">https://blogs.technet.microsoft.com/chadcox/2016/10/25/chads-quick-notes-installing-a-domain-controller-with-server-2016-core/</a></p>
<p><a href="https://technet.microsoft.com/en-us/library/hh831453(v=ws.11).aspx">https://technet.microsoft.com/en-us/library/hh831453(v=ws.11).aspx</a></p>
<p><a href="https://www.microsoft.com/en-us/download/details.aspx?id=45520">https://www.microsoft.com/en-us/download/details.aspx?id=45520</a></p>
<p>E os passos que executei via Powershell:</p>
<p>[powershell]<br />#Renomeie o servidor:</p>
<p>Rename-computer -newname 2016-DC01</p>
<p>#Altere o endereço IP, coloque de acordo com o seu ambiente:</p>
<p>$ipaddress = "10.0.0.2"<br />$dnsaddress = "127.0.0.1"<br />New-NetIPAddress -InterfaceAlias Ethernet -IPAddress $ipaddress -AddressFamily IPv4 -PrefixLength 24<br />Set-DnsClientServerAddress -InterfaceAlias Ethernet1 -ServerAddresses $dnsaddress</p>
<p>#Reinicie o Servidor:<br />Restart-Computer</p>
<p>#Verifique o timezone e se necessário troque-o:<br />get-timezone<br />Set-TimeZone -Id "UTC-02"</p>
<p>#Instale a Feature de AD:<br />Install-WindowsFeature AD-Domain-Services -IncludeManagementTools</p>
<p>#Crie uma nova floresta de AD e promova o Servidor atual a DC:<br />Install-ADDSForest -DomainName ONOMEDOSEUADAQUI.ad<br />#No seu host físico, comando para adicionar o DC virtual à lista de Servidores Confiáveis:<br />Set-Item wsman:\localhost\Client\TrustedHosts SEUADAQUI -Concatenate -Force</p>
<p>#No seu servidor virtual para verificar o uso de memória:<br />Get-WmiObject win32\_OperatingSystem |%{"Total Physical Memory: {0}KB`nFree Physical Memory : {1}KB`nTotal Virtual Memory : {2}KB`nFree Virtual Memory : {3}KB" -f $\_.totalvisiblememorysize, $\_.freephysicalmemory, $\_.totalvirtualmemorysize, $\_.freevirtualmemory}</p>
<p>[/powershell]</p>
</div>