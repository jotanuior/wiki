# Install AD DS, DNS, and DHCP using Powershell on Windows Server 2016

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** Windows, server, core, DNS, DHCP

**Última modificação:** 2019-05-30 23:14

**Autor:** Claudio Junior

---

<div class="section-inner sectionLayout--insetColumn">
<p id="2a79" class="graf graf--p graf-after--h3">This article serves as a guide to installing and configuring roles on Windows 2016 servers using powershell.</p>
<p id="cfe6" class="graf graf--p graf-after--p">To begin, right-click the Windows Powershell taskbar icon and select “Run as Administrator”. To view Windows features and statuses enter this command into the console:</p>
<pre id="0327" class="graf graf--pre graf-after--p">Get-WindowsFeature</pre>
<figure id="2c92" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*TcGCkZYngCsZ\_9q6Kg1AzA.png" data-width="910" data-height="387" data-is-featured="true" data-action="zoom" data-action-value="1*TcGCkZYngCsZ\_9q6Kg1AzA.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*TcGCkZYngCsZ\_9q6Kg1AzA.png" data-src="https://cdn-images-1.medium.com/max/800/1*TcGCkZYngCsZ\_9q6Kg1AzA.png" /></div>
</div>
</figure>
<p id="8ef1" class="graf graf--p graf-after--figure">To install an individual feature the following command syntax is used:</p>
<pre id="30ca" class="graf graf--pre graf-after--p"><strong class="markup--strong markup--pre-strong">Install-WindowsFeature -Name [feature\_name] -[Options]</strong></pre>
<h3 id="8406" class="graf graf--h3 graf-after--pre">Active Directory Role</h3>
<p id="e016" class="graf graf--p graf-after--h3">We will begin by installing the Active Directory role using the following:</p>
<pre id="4b6c" class="graf graf--pre graf-after--p">Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools</pre>
<figure id="67b9" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*nre49B6XwLeTQJmvQxyPmw.png" data-image-id="1*nre49B6XwLeTQJmvQxyPmw.png" data-width="918" data-height="100" data-action="zoom" data-action-value="1*nre49B6XwLeTQJmvQxyPmw.png" /></div>
</figure>
<p id="68c6" class="graf graf--p graf-after--figure">To view the available module commands related to AD DS use the following:</p>
</div>
<div class="section-inner sectionLayout--insetColumn">
<pre id="32aa" class="graf graf--pre graf-after--p">Get-Command -Module ADDSDeployment</pre>
<figure id="07fc" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*4agv-34r9vmPEnD-vRqfEA.png" data-width="868" data-height="234" data-action="zoom" data-action-value="1*4agv-34r9vmPEnD-vRqfEA.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*4agv-34r9vmPEnD-vRqfEA.png" data-src="https://cdn-images-1.medium.com/max/800/1*4agv-34r9vmPEnD-vRqfEA.png" /></div>
</div>
</figure>
<p id="3d59" class="graf graf--p graf-after--figure">First, the root domain is installed:</p>
<p class="graf graf--p graf-after--figure"><strong>Step 2</strong>: Import ADDSDeployment Module.</p>
<p class="graf graf--p graf-after--figure">C:\> Import-Module ADDSDeployment</p>
<p class="graf graf--p graf-after--figure">Install-ADDSForest  <br />-CreateDnsDelegation:$false `  <br />-DatabasePath "C:\Windows\NTDS" `  <br />-DomainMode "Win2016" `  <br />-DomainName "tecmen.corp" `  <br />-DomainNetbiosName "tecmen" `  <br />-ForestMode "Win2016" `  <br />-InstallDns:$true `  <br />-LogPath "C:\Windows\NTDS" `  <br />-NoRebootOnCompletion:$false `  <br />-SysvolPath "C:\Windows\SYSVOL" `  <br />-Force:$true</p>
<pre id="5e0f" class="graf graf--pre graf-after--p">Install-ADDSForest -DomainName “corp.momco.com”</pre>
<figure id="34bc" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*HQ78iU14r5gNGvBkWdUV-Q.png" data-width="967" data-height="123" data-action="zoom" data-action-value="1*HQ78iU14r5gNGvBkWdUV-Q.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*HQ78iU14r5gNGvBkWdUV-Q.png" data-src="https://cdn-images-1.medium.com/max/800/1*HQ78iU14r5gNGvBkWdUV-Q.png" /></div>
</div>
</figure>
<p id="9239" class="graf graf--p graf-after--figure">Note that you may see several error messages and this is okay. Watch the banner for update information regarding your domain forest. Once the root forest is successfully created you’ll see this message:</p>
<figure id="9697" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*ZZTz-EfVyDO9xDycUc6PzQ.png" data-width="869" data-height="223" data-action="zoom" data-action-value="1*ZZTz-EfVyDO9xDycUc6PzQ.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*ZZTz-EfVyDO9xDycUc6PzQ.png" data-src="https://cdn-images-1.medium.com/max/800/1*ZZTz-EfVyDO9xDycUc6PzQ.png" /></div>
</div>
</figure>
<p id="6788" class="graf graf--p graf-after--figure">The server will restart. Open Powershell again as Administrator and check to make sure the appropriate changes were made:</p>
<figure id="e621" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*rmmz2A9rAGa3fcsLzegzyg.png" data-width="476" data-height="150" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*rmmz2A9rAGa3fcsLzegzyg.png" data-src="https://cdn-images-1.medium.com/max/800/1*rmmz2A9rAGa3fcsLzegzyg.png" /></div>
</div>
</figure>
<p id="815e" class="graf graf--p graf-after--figure">Now we can join a computer connected to our vlan to our domain. In this instance I log onto a Windows 7 vm on the same VLAN as the Windows Server and join this box by changing the domain in the computer’s System Properties. To join the domain, you must authorize the client using an administrative username/password from the domain. In this example my username was “momco\administrator”. Upon successfully joining you should see a messagebox welcoming you to your domain:</p>
<figure id="37ae" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*cQ7eun8PZuib4hnVSahg2Q.png" data-width="437" data-height="235" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*cQ7eun8PZuib4hnVSahg2Q.png" data-src="https://cdn-images-1.medium.com/max/800/1*cQ7eun8PZuib4hnVSahg2Q.png" /></div>
</div>
</figure>
<p id="b100" class="graf graf--p graf-after--figure">Restart your client computer to apply the new changes. You should now be able to view this client on your Windows server domain controller (DC) using the following command:</p>
<pre id="becc" class="graf graf--pre graf-after--p">get-ADComputer | Format-Table DNSHostName, Enabled, Name, SamAccountName</pre>
<figure id="5b2d" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*54fY4bxEhHqmKWM-uU4YWg.png" data-width="911" data-height="188" data-action="zoom" data-action-value="1*54fY4bxEhHqmKWM-uU4YWg.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*54fY4bxEhHqmKWM-uU4YWg.png" data-src="https://cdn-images-1.medium.com/max/800/1*54fY4bxEhHqmKWM-uU4YWg.png" /></div>
</div>
</figure>
<p id="b9af" class="graf graf--p graf-after--figure">The client computer can be seen above as “WIN-BOB-01”. We can add a user to the Active Directory domain using the following command:</p>
<pre id="d2b7" class="graf graf--pre graf-after--p">New-ADUser -Name [Username] -AccountPassword(Read-Host -AsSecureString AccountPassword) -PassThru | Enable-ADAccount</pre>
<figure id="947b" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*xHuxHrQO4iXeqokIwltodQ.png" data-image-id="1*xHuxHrQO4iXeqokIwltodQ.png" data-width="1030" data-height="54" data-action="zoom" data-action-value="1*xHuxHrQO4iXeqokIwltodQ.png" /></div>
</figure>
<h3 id="78c3" class="graf graf--h3 graf-after--figure">DNS Role</h3>
<p id="c481" class="graf graf--p graf-after--h3">The DNS server was created when AD DS role installed the root forest. We can see that the DNS role is installed using the <strong class="markup--strong markup--p-strong">Get-WindowsFeature</strong> command:</p>
<pre id="e595" class="graf graf--pre graf-after--p">Get-WindowsFeature | where {($\_.name -like “DNS”)}</pre>
<figure id="378b" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*R69rtU3a-WD7Ylnmp57rGg.png" data-image-id="1*R69rtU3a-WD7Ylnmp57rGg.png" data-width="908" data-height="96" data-action="zoom" data-action-value="1*R69rtU3a-WD7Ylnmp57rGg.png" /></div>
</figure>
<p id="db32" class="graf graf--p graf-after--figure">If your DNS server is not installed, you can install it with this command:</p>
<pre id="8a48" class="graf graf--pre graf-after--p">Install-WindowsFeature DNS -IncludeManagementTools</pre>
<figure id="361f" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*EO3P21XukCfG2Sv2Xd-e4g.png" data-width="499" data-height="104" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*EO3P21XukCfG2Sv2Xd-e4g.png" data-src="https://cdn-images-1.medium.com/max/800/1*EO3P21XukCfG2Sv2Xd-e4g.png" /></div>
</div>
</figure>
<p id="8dc6" class="graf graf--p graf-after--figure">The DNS primary zone is created when the forest is generated. Next, the network ID and file entry is made:</p>
<pre id="401b" class="graf graf--pre graf-after--p">Add-DnsServerPrimaryZone -NetworkID 192.168.64.0/24 -ZoneFile “192.168.64.2.in-addr.arpa.dns”</pre>
<p id="3a3d" class="graf graf--p graf-after--pre">Next, the forwarder is added:</p>
<pre id="04ce" class="graf graf--pre graf-after--p">Add-DnsServerForwarder -IPAddress 8.8.8.8 -PassThru<br /><span class="hljs-pscommand">OPENDNS - CONTROLE DE ACESSO - 208.67.222.123 / 208.67.220.123<br /><br />Remove-DnsServerForwarder</span><span class="hljs-parameter"> -IPAddress</span> <span class="hljs-number">10.0</span>.<span class="hljs-number">0.8</span><span class="hljs-parameter"> -PassThru - Para REMOVER</span></pre>
<p id="873a" class="graf graf--p graf-after--pre">You should now be able to test your dns server:</p>
<pre id="25af" class="graf graf--pre graf-after--p">Test-DnsServer -IPAddress 192.168.64.2 -ZoneName "corp.momco.com"</pre>
<figure id="64f0" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*KQ\_l9YhgGrtdIWKPepHJvQ.png" data-image-id="1*KQ\_l9YhgGrtdIWKPepHJvQ.png" data-width="851" data-height="95" data-action="zoom" data-action-value="1*KQ\_l9YhgGrtdIWKPepHJvQ.png" /></div>
</figure>
<h3 id="796e" class="graf graf--h3 graf-after--figure">DHCP Role</h3>
<p id="79ba" class="graf graf--p graf-after--h3">We’ll begin by installing the DHCP role. To do this, the Windows 2016 Sever must be configured with a static IP address. The <strong class="markup--strong markup--p-strong">New-NetIpAddress</strong>command is used:</p>
<pre id="cc32" class="graf graf--pre graf-after--p">New-NetIPAddress -InterfaceIndex 2 -IPAddress 192.168.64.2 -PrefixLength 24 -DefaultGateway 192.168.64.1</pre>
<figure id="b5e8" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked"><img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*T0Hy2CO9qPkGqwyYnyq0IA.png" data-image-id="1*T0Hy2CO9qPkGqwyYnyq0IA.png" data-width="952" data-height="43" data-action="zoom" data-action-value="1*T0Hy2CO9qPkGqwyYnyq0IA.png" /></div>
</figure>
<p id="7658" class="graf graf--p graf-after--figure">You’ll need to know the ifIndex the network interface of which you are configuring the IP address. To view your available network interfaces, use the <strong class="markup--strong markup--p-strong">Get-Net-IPInterface </strong>command. Now that the server has been configured with an IP address the DHCP role can be installed:</p>
<pre id="f877" class="graf graf--pre graf-after--p">Install-WindowsFeature DHCP -IncludeManagementTools</pre>
<figure id="12aa" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*oDNa9laLxscCyW1fHcUxFg.png" data-width="774" data-height="106" data-action="zoom" data-action-value="1*oDNa9laLxscCyW1fHcUxFg.png" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*oDNa9laLxscCyW1fHcUxFg.png" data-src="https://cdn-images-1.medium.com/max/800/1*oDNa9laLxscCyW1fHcUxFg.png" /></div>
</div>
</figure>
<p id="cf7e" class="graf graf--p graf-after--figure">Next, a security group is created using the <strong class="markup--strong markup--p-strong">netsh </strong>command. The service is then restarted. When the following command is run, the DHCP Administrators and DHCP Users security groups are created in Local Users and Groups on the DHCP server.</p>
<figure id="eadb" class="graf graf--figure graf-after--p">
<div class="aspectRatioPlaceholder is-locked">
<div class="progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded" data-image-id="1*TT200gbkVU5jz8zxdRRCNw.png" data-width="634" data-height="173" data-scroll="native"><img class="progressiveMedia-image js-progressiveMedia-image" src="https://cdn-images-1.medium.com/max/800/1*TT200gbkVU5jz8zxdRRCNw.png" data-src="https://cdn-images-1.medium.com/max/800/1*TT200gbkVU5jz8zxdRRCNw.png" /></div>
</div>
</figure>
<p id="b4c3" class="graf graf--p graf-after--figure">Now that the DHCP role and security groups are installed, we need to configure the subnets, scope and exclusions. Configure the DHCP scope for the domain. This will be the addresses that are handed out the to network by DHCP.</p>
<pre id="182c" class="graf graf--pre graf-after--p">Add-DHCPServerv4Scope -Name “Employee Scope” -StartRange 192.168.64.10 -EndRange 192.168.64.30 -SubnetMask 255.255.255.0 -State Active</pre>
<p id="b8b4" class="graf graf--p graf-after--pre">The DHCP lease can be set to 1 day using the following command:</p>
<pre id="ba84" class="graf graf--pre graf-after--p">Set-DhcpServerv4Scope -ScopeId 192.168.64.0 -LeaseDuration 1.00:00:00</pre>
<p id="7b9e" class="graf graf--p graf-after--pre">Next, authorize the DHCP server to operate in the domain:</p>
<pre id="826a" class="graf graf--pre graf-after--p">Set-DHCPServerv4OptionValue -ScopeID 192.168.64.0 -DnsDomain corp.momco.com -DnsServer 192.168.64.2 -Router 192.168.64.1</pre>
</div>
<div class="section-inner sectionLayout--outsetColumn">
<figure id="cb4c" class="graf graf--figure graf--layoutOutsetCenter graf-after--pre" data-scroll="native">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"> </div>
<img class="graf-image" src="https://cdn-images-1.medium.com/max/1200/1*1xiYCB561ZAtOQNQ9qnczQ.png" data-image-id="1*1xiYCB561ZAtOQNQ9qnczQ.png" data-width="1115" data-height="33" data-action="zoom" data-action-value="1*1xiYCB561ZAtOQNQ9qnczQ.png" /></div>
</figure>
</div>
<div class="section-inner sectionLayout--insetColumn">
<p id="2401" class="graf graf--p graf-after--figure">Finally, the DHCP Server is added to the DC:</p>
<pre id="1295" class="graf graf--pre graf-after--p">Add-DhcpServerInDC -DnsName corp.momco.com -IpAddress 192.168.64.2</pre>
<figure id="725b" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"> </div>
<img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*3uFy8OkJtFZeDvvsESQfWg.png" data-image-id="1*3uFy8OkJtFZeDvvsESQfWg.png" data-width="847" data-height="27" data-action="zoom" data-action-value="1*3uFy8OkJtFZeDvvsESQfWg.png" /></div>
</figure>
<p id="d355" class="graf graf--p graf-after--figure">We can verify the DHCP Scope setting using this command:</p>
<pre id="c5ee" class="graf graf--pre graf-after--p">Get-DhcpServerv4Scope</pre>
<figure id="0c29" class="graf graf--figure graf-after--pre">
<div class="aspectRatioPlaceholder is-locked">
<div class="aspectRatioPlaceholder-fill"> </div>
<img class="graf-image" src="https://cdn-images-1.medium.com/max/800/1*oBWUZqBw3Y0UxwgprK6PhA.png" data-image-id="1*oBWUZqBw3Y0UxwgprK6PhA.png" data-width="919" data-height="98" data-action="zoom" data-action-value="1*oBWUZqBw3Y0UxwgprK6PhA.png" /></div>
</figure>
</div>