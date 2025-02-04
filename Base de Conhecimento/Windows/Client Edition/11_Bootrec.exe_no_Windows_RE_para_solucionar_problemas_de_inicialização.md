# Bootrec.exe no Windows RE para solucionar problemas de inicialização

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** boot windows bootrec

**Última modificação:** 2015-02-03 11:08

**Autor:** Claudio Junior

---

<p>Ao usar o Ambiente de Recuperação (Windows RE) para solucionar problemas de inicialização, experimente primeiro a opção <strong>Reparo de Inicialização</strong> na caixa de diálogo <strong>Opções de Recuperação do Sistema</strong>. Se isso não resolver o problema ou se for necessário solucionar problemas adicionais manualmente, use a ferramenta Bootrec.exe. Esse artigo fala sobre como usar a ferramenta Bootrec.exe no Windows RE para solucionar problemas e reparar os itens a seguir no Windows Vista ou Windows 7:</p>
<ul>
<li>Um Registro mestre de inicialização (MBR)</li>
<li>Um setor de inicialização</li>
<li>Um armazenamento de Dados de Configuração da Inicialização (BCD)</li>
</ul>
<p>Você também pode usar a ferramenta Bootrec.exe solucionar um erro de <a title="http://support.microsoft.com/kb/927391/pt-br" href="http://support.microsoft.com/kb/927391/pt-br">Arquivo de dados de configuração da inicialização do Windows necessário ausente</a>.</p>
<div id="kb\_section" class="section briefView">
<h2 id="tocHeadRef" class="subTitle">Como executar a ferramenta Bootrec.exe</h2>
<div id="MT1" class="sbody">Para executar a ferramenta Bootrec.exe, primeiro inicie o Windows RE:<ol>
<li>Coloque a mídia do Windows Vista ou do Windows 7 na unidade de DVD e inicie o computador.</li>
<li>Pressione uma tecla quando solicitado.</li>
<li>Selecione um idioma, uma hora, uma moeda, um teclado ou um outro método de entrada e clique em <strong class="uiterm">Avançar</strong>.</li>
<li>Clique em <strong class="uiterm">Reparar o computador</strong>.</li>
<li>Selecione o sistema operacional que deseja reparar e clique em <strong class="uiterm">Próximo</strong>.</li>
<li>Na caixa de diálogo <strong class="uiterm">Opções de recuperação do sistema</strong>, clique em <strong class="uiterm">Prompt de comando</strong>.</li>
<li>Digite Bootrec.exe e pressione Enter.</li>
</ol>
<div class="kb\_nowrapper">
<div class="kb\_nowrapper"> </div>
<div class="kb\_nowrapper"> </div>
<img class="graphic" title="" src="http://support.microsoft.com/library/images/2683283.jpg" alt="" /></div>
<strong>Observação</strong> Para iniciar o computador a partir do DVD do Windows Vista ou Windows 7, o computador deve estar configurado para iniciar a partir da unidade de DVD. Para obter informações sobre como fazer isso, consulte a documentação incluída com o computador ou contate o fabricante do computador.</div>
<div id="MT2" class="sbody norollup"><br />
<h4 id="tocHeadRef"><a class="accessibilityanchor" title="resolution">Opções do Bootrec.exe</a></h4>
<div id="MT4" class="sbody subSection">A ferramenta Bootrec.exe suporta as seguintes opções. Use a opção adequada para o seu caso.<br /><br />
<h3 id="tocHeadRef">/FixMbr</h3>
Essa opção grava um MBR compatível com o Windows 7 ou Windows Vista na partição do sistema. Ela não substitui a tabela de partição existente. Use essa opção quando você precisar resolver problemas de corrupção do MBR ou precisar remover código não padrão do MBR.
<h3 id="tocHeadRef">/FixBoot</h3>
Essa opção grava um novo setor de inicialização na partição do sistema usando um setor de inicialização compatível com o Windows Vista ou Windows 7. Use essa opção se uma das seguintes condições for verdadeira:
<ul>
<li>O setor de inicialização foi substituído por um setor de inicialização não padrão do Windows Vista ou Windows 7.</li>
<li>O setor de inicialização está danificado.</li>
<li>Um sistema operacional Windows anterior foi instalado após a instalação do Windows Vista ou Windows 7. Nessa situação, o computador é iniciado utilizando o Windows NT Loader (NTLDR) em vez do Gerenciador de Inicialização do Windows (Bootmgr.exe).</li>
</ul>
<h3 id="tocHeadRef">/ScanOs</h3>
Essa opção examina todos os discos em busca de instalações que são compatíveis com o Windows Vista ou o Windows 7. Ela também exibe as entradas que não estão no repositório BCD. Use essa opção quando houver instalações do Windows Vista ou do Windows 7 não listadas pelo Gerenciador de Inicialização.
<h3 id="tocHeadRef">/RebuildBcd</h3>
Essa opção examina todos os discos em busca de instalações compatíveis com o Windows Vista ou o Windows 7. Além disso, ela permite que você selecione as instalações que deseja adicionar o repositório BCD. Use essa opção quando você precisar recriar completamente o repositório BCD.<br /><br />
<div class="kb\_nowrapper">
<div class="kb\_nowrapper"> </div>
<div class="kb\_nowrapper"> </div>
<img class="graphic" title="" src="http://support.microsoft.com/library/images/2683283.jpg" alt="" /></div>
<strong>Observação </strong>Use a ferramenta Bootrec.exe para solucionar um erro de "Bootmgr ausente". Se a recriação do repositório BCD não resolver o problema de inicialização, você poderá exportar e excluir o repositório BCD e executar essa opção novamente. Fazendo isso, é possível ter certeza de que o repositório BCD está completamente reconstruído. <br /><br />Para fazer isto, digite os seguintes comandos no prompt de comando do Windows RE:
<ul>
<li>bcdedit /export C:\BCD\_Backup</li>
<li>c:</li>
<li>cd boot</li>
<li>attrib bcd -s -h -r</li>
<li>ren c:\boot\bcd bcd.old</li>
<li>bootrec /RebuildBcd</li>
</ul>
</div>
</div>
</div>