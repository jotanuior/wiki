# Como configurar VLAN 802.1Q em Switches Easy Smart

**Categoria:** Base de Conhecimento >> REDES

**Palavras-chave:** vlan

**Última modificação:** 2020-02-14 17:04

**Autor:** Claudio Junior

---

<div class="title">
<h1>Como configurar VLAN 802.1Q em Switches Easy Smart?</h1>
</div>
<div class="visit-message clearfix">User Application Requirement
<div class="float-right"><span class="faq-updated">Updated 01-07-2016 16:37:46 PM</span><span class="faq-pageview"><img src="https://www.tp-link.com/res/images/icons/article-views.png" /><em>165987</em></span></div>
</div>
<div class="suit-for">
<div class="label"><strong>This Article Applies to:</strong><em> </em></div>
</div>
<div class="content">
<p>Uma Rede Virtual Local (VLAN)   é uma topologia de rede configurada de acordo com o esquema lógico ao invés do layout físico. Hosts na mesma VLAN comunicam-se entre si uma vez que estão em uma LAN. De qualquer forma, hosts em VLANs diferentes não podem se comunicar diretamente.</p>
<p>Aprenderemos agora como configurar a VLAN no Switch Web Smart através do exemplo a seguir:</p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage001.jpg" /></p>
<p><strong>Utilizamos aqui como exemplo os modelos TL-SG1016DE e TL-SG108E.                   </strong></p>
<p>O TL-SG10 conecta à Internet via TL-R480T+ na porta 9, e conecta ao TL-SG108E com um cabo Ethernet na porta 1.                                    </p>
<p>Os computadores do Grupo A conectam-se às portas 2-3 do TL-SG1016DE e portas 2-3 do TL-SG108E.                Já o Grupo B conecta-se às portas 4-8 destes.</p>
<p>Propósito：</p>
<p>1 Os computadores do Grupo A podem se comunicarem entre si.</p>
<p>2 Os computadores do Grupo B podem se comunicarem entre si.</p>
<p>3 Os computadores do Grupo A não podem se comunicar com computadores do Grupo B e vice-versa.</p>
<p>4 Ambos Grupos podem acessar a Internet através do TL-R480T+.    </p>
<p><strong>Parâmetros de Configuração VLAN:</strong></p>
<p> </p>
<table>
<tbody>
<tr>
<td>
<p> </p>
</td>
<td>
<p>VLAN         1                                              </p>
</td>
<td>
<p>VLAN           101                                              </p>
</td>
<td>
<p>VLAN           102                                              </p>
</td>
</tr>
<tr>
<td>
<p>TL-SG1016DE</p>
</td>
<td>
<p>1-9</p>
</td>
<td>
<p>1-3,9</p>
</td>
<td>
<p>1,4-9</p>
</td>
</tr>
<tr>
<td>
<p>TL-SG108E</p>
</td>
<td>
<p>1-8</p>
</td>
<td>
<p>1-3</p>
</td>
<td>
<p>1,4-8</p>
</td>
</tr>
</tbody>
</table>
<p> </p>
<p>Para cumprir com o Propósito 1, nós criamos a VLAN cujo ID é 101</p>
<p>Para cumprir com o Propósito 2, nós criamos a VLAN cujo ID é 102</p>
<p>Ao criar as VLANs 101 e 102, nós cumprimos com o Propósito3.</p>
<p>Para cumprir com o Propósito  4, utilizamos a VLAN 1 padrão para garantir que o TL-R480T+ posso se comunicar com todas as portas dos dois switches.  </p>
<p> </p>
<table>
<tbody>
<tr>
<td>
<p>Switch</p>
</td>
<td>
<p>TL-SG1016DE</p>
</td>
<td>
<p>TL-SG108E</p>
</td>
</tr>
<tr>
<td>
<p>                  Porta</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>2-3</p>
</td>
<td>
<p>4-8</p>
</td>
<td>
<p>9</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>2-3</p>
</td>
<td>
<p>4-8</p>
</td>
</tr>
<tr>
<td>
<p>Regra de Egresso</p>
</td>
<td>
<p>Marcar</p>
</td>
<td>
<p>Desmarcar</p>
</td>
<td>
<p>Desmarcar</p>
</td>
<td>
<p>Desmarcar</p>
</td>
<td>
<p>Marcar</p>
</td>
<td>
<p>Desmarcar</p>
</td>
<td>
<p>Desmarcar</p>
</td>
</tr>
<tr>
<td>
<p>PVID</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>101</p>
</td>
<td>
<p>102</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>101</p>
</td>
<td>
<p>102</p>
</td>
</tr>
</tbody>
</table>
<p> </p>
<p>A tabela abaixo mostra outros parâmetros.</p>
<p> </p>
<p><strong>Nota:</strong></p>
<p><strong>O TL-SG1016DE e o TL-SG108E são ambos Switches Easy Smart, a diferença é que o TL-SG1016DE possui interface web GUI, já o TL-SG108E pode ser configurado apenas pelo Utilitário de Configuração Easy Smart.                                                                                        </strong></p>
<p><strong>Neste texto apresentamos como configurar VLAN 802.1q no TL-SG1016DE através de web GUI, e como configurar o TL-SG108E através do Utilitário de Configuração Easy Smart, obviamente você consegue configurar o TL-SG1016DE através do utilitário também, é exatamente o mesmo que no TL-SG108E.                                                                                                                                                        </strong></p>
<p> </p>
<p>Agora, vamos iniciar a configuração do Switch TL-SG1016DE.           </p>
<p> </p>
<p><strong>Passo 1 </strong>Insira a interface web GUI do TL-SG1016DE, escolha “VLAN 802.1Q” no menu “VLAN”, e marque Enable (Habilitar) na direita “802.1Q VLAN Configuration”, clique em Apply (Aplicar) para iniciar a função VLAN 802.1Q, somente depois deste passo você poderá adicionar ou modificar a VLAN:    </p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage002.jpg" /></p>
<p><strong>Passo 2 </strong>Insira o ID VLAN que deseja criar, e então poderá nomear a VLAN que preferir. Aqui inserimos VLAN ID 101, deixe a porta 1 como marcada, porta 2-3, 9 como desmarcardas e clique então em Add/Modificar (Adicionar/Modificar):             </p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage003.png" /></p>
<p><strong>Passo 3 </strong>Assim como o passo 2, nós criamos a VLAN 102 com a porta 1 marcada, e as portas 4-9 desmarcadas</p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage004.png" /></p>
<p> </p>
<p><strong>Passo 4 </strong>Este passo nós devemos configurar o PVID da porta, aqui nós configuramos o PVID da porta 2-3 para 101, escolha "configurações 802.1q PVID" na esquerda no menu da VLAN, então esolha a porta que você quer configurar, digitando o valor do PVID então clique "Apply". </p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage005.png" /><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage006.png" /></p>
<p> </p>
<p><strong>Passo 5 </strong>Configure o PVID de todas as portas corretamente como no passo 4</p>
<p> </p>
<p>Agora a configuração no TL-SG1016DE foi concluída, veremos como configurar a VLAN 802.1q TL-SG108E via Utilitário de Configuração Easy Smart:                                                            </p>
<p> </p>
<p><strong>Passo 1 </strong>Escolha TL-SG108E através do utilitário, escolha então a página VLAN, 802.1Q VLAN na esquerda, você verá a janela da direita  monstrar somente "Global Config", por favor configure  o  "802.1q VLAN status" para "Enable" e clique em Apply (Aplicar), a configuração de VLAN 802.1q aparecerá da seguinte forma:                </p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage007.jpg" /></p>
<p><strong>Passo 2 </strong>Nós podemos encontrar diferenças entre configurar VLAN aqui ou através da wed GUI do TL-SG1016DE, neste utilitário utilizamos a seleção de porta gráfica, você apenas precisa clicar na porta que deseja escolher, é muito mais fácil. Configuramos a VLAN101 com a porta 1 marcada, portas 2-3 desmarcadas, clique então em Apply (Aplicar):    </p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage008.jpg" /></p>
<p><strong>Passo 3 </strong>Como o passo 2 mostra, configuramos a VLAN 102 com a porta 1 marcada, enquanto as portas 4-8 estão desmarcadas:</p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage009.jpg" /></p>
<p><strong>Passo 4</strong>Neste passo devemos configurar o PVID da porta, aqui configuramos o PVID das portas 2-3 até 101, escolha “Configuração 802.1q PVID” no menu do lado esquerdo, escolha então a porta que deseja configurar, digitando o valor PVID e clicando depois em Apply (Aplicar):</p>
<p><img src="https://static.tp-link.com/resources/UploadFiles/Images/How\_to\_configure\_802.1q\_VLAN\_on\_Easy\_Smart\_Switchesimage010.jpg" /></p>
<p><strong>Passo 5 </strong>Configure o PVID de todas as portas corretamente de acordo com o passo 4</p>
<p> </p>
<p>Agora que criamos com sucesso 2 VLANs operando juntas coma VLAN1 padrão, compreendendo          a sua necessidade de uso.</p>
<p> </p>
<p><strong>Nota:</strong></p>
<p>Somente quando uma VLAN específica for criada você poderá alterar o PVID da porta para VID nesta VLAN.                                           Os passos corretos para se construir várias VLANs no switch são:              1. Crie estas VLANs 2.Selecione Portas Membro 3. Configure PVID para estas portas.              </p>
<p>2.   Devido ao PVID da porta ser único mesmo que ele pertença a mais de uma VLAN, você pode escolher qualquer LAN para configurar o PVID.</p>
</div>