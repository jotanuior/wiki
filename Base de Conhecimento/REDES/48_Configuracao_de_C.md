# Configuração de Cliente PPPoE em Roteadores Cisco

**Categoria:** Base de Conhecimento >> REDES

**Palavras-chave:** 

**Última modificação:** 2019-06-06 20:58

**Autor:** Claudio Junior

---

<h3 class="post-title entry-title">Configuração de Cliente PPPoE em Roteadores Cisco</h3>
<div class="post-header">
<div class="post-header-line-1"> </div>
</div>
<div id="post-body-6813028536322442349" class="post-body entry-content">
<div>Olá Pessoal.</div>
<div> </div>
<div>Um dos novos tópicos adicionados ao novo currículo CCNA R&S no que tange às tecnologias de longa distância é a configuração de <strong>PPPoE (<em>Point-to-Point Protocol over Ethernet</em>)</strong> no lado cliente, uma prática comum entre algumas operadoras que ofertam conexões à Internet via xDSL.</div>
<div> </div>
<div>A tecnologia PPPoE é bastante utilizada com DSL porque o protocolo PPP é a opção natural para permitir a <strong><u>autenticação do usuário</u></strong> e o transporte das mais diversas tecnologias através das redes de transporte das operadoras, de forma que, por exemplo, quadros Ethernet encapsulados dentro de quadros PPP podem trafegar através das redes legadas ATM (<em>Asynchronous Transfer Mode</em>) que ainda possam existir em virtude do alto custo de implantação. Atualmente o maior motivador para uso do PPPoE é a possibilidade de autenticar o usuário com CHAP, um sub-protocolo nativo do PPP.</div>
<div> </div>
<div>Nessas situações é comum a operadora disponibilizar um software de autenticação no lado do cliente, através do qual o usuário fornece suas credenciais (login e senha) para estabelecer a conexão com a Internet. Em pequenas empresas ou mesmo em ambientes residenciais que tenham várias máquinas ligadas em rede é mais conveniente transferir a responsabilidade de autenticação para um dispositivo central, de forma que o processo de conexão fica totalmente transparente para o usuário final. Esse dispositivo responsável pela autenticação pode ser o próprio roteador. Para exemplificar como seria o processo de configuração de uma conexão cliente PPPoE em roteadores Cisco estaremos considerando o cenário apresentado na figura abaixo.</div>
<div> </div>
<div class="separator"><a href="http://1.bp.blogspot.com/-ufGBqlB3IaU/Uhw1SnwUQwI/AAAAAAAAA\_I/uoMxcTNhkV8/s1600/PPPoE.png"><img src="https://1.bp.blogspot.com/-ufGBqlB3IaU/Uhw1SnwUQwI/AAAAAAAAA\_I/uoMxcTNhkV8/s400/PPPoE.png" width="400" height="153" /></a></div>
<div> </div>
<div>A interface f0/0 está conectada na rede local (LAN), sendo que seu IP 192.168.0.254 será configurado como gateway da rede. A interface f0/1 está diretamente conectada ao modem da operadora instalado na casa do usuário, também chamado de CPE (<em>Customer Premises Equipment</em>). No lado da operadora existe um dispositivo chamado DSLAM que faz a agregação de vários modens DSL dos clientes e que, por sua vez, está conectado à rede da operadora que possui saída para a Internet. A seguir são apresentados os comandos para configurar o roteador como cliente PPPoE e, em seguida, são feitas algumas observações relevantes.</div>
<div> </div>
<div>01. Router# conf t</div>
<div>02. Router(config)# interface f0/0</div>
<div>03. Router(config-if)# ip address 192.168.0.254 255.255.255.0</div>
<div>04. Router(config-if)# ip nat inside</div>
<div>05. Router(config-if)# no shut</div>
<div>06. Router(config-if)# interface f0/1</div>
<div>07. Router(config-if)# pppoe-client dial-pool-number 1</div>
<div>08. Router(config-if)# exit</div>
<div>09. Router(config)# interface dialer1</div>
<div>10. Router(config-if)# mtu 1492</div>
<div>11. Router(config-if)# encapsulation ppp</div>
<div>12. Router(config-if)# ip address negotiated</div>
<div>13. Router(config-if)# ppp authentication chap </div>
<div>14. Router(config-if)# ppp chap hostname LOGIN</div>
<div>15. Router(config-if)# ppp chap password SENHA</div>
<div>16. Router(config-if)# dialer pool 1 </div>
<div>17. Router(config-if)# ip nat outside</div>
<div>18. Router(config-if)# dialer-group 1</div>
<div>19. Router(config-if)# exit</div>
<div>20. Router(config)# dialer-list 1 protocol ip permit</div>
<div>21. Router(config)# ip nat inside source list 1 interface dialer1 overload</div>
<div>22. Router(config)# access-list 1 permit 192.168.0.0 0.0.0.255</div>
<div>23. Router(config)# ip route 0.0.0.0 0.0.0.0 dialer 1</div>
<div> </div>
<div>A configuração do PPPoE em roteadores consiste em criar e vincular uma nova interface virtual do tipo <em><strong>dialer</strong></em> à interface ethernet que está fisicamente conectada ao modem da operadora, processo realizado nas linhas 07, 09 e 16 da configuração anterior. Todas as demais configurações relacionadas ao PPP propriamente dito são realizadas na interface virtual <em>dialer, </em>já que esse tipo de interface tem suporte ao encapsulamento PPP. Ou seja, esse processo não passa de um mecanismo de tunelamento...</div>
<div> </div>
<div>Em conexões DSL é comum a operadora atribuir dinamicamente os endereços dos usuários através de um servidor DHCP, no entanto é necessário o uso do protocolo IPCP (<em>IP Configuration Protocol</em>) no contexto do link PPP para que essa atribuição funcione. Por isso na linha 12 foi utilizado o comando "ip address negotiated" para habilitar o IPCP. </div>
<div> </div>
<div>Outra configuração extremamente importante é setar o tamanho máximo do quadro (MTU) para 1492 bytes (linha 10), uma vez que o novo cabeçalho PPP possui 8 bytes e o limite máximo do quadro Ethernet é 1500 bytes. Logo, para não estourar o limite do quadro Ethernet é necessário <u><strong>subtrair</strong></u> esses 8 bytes do PPP para que os quadros Ethernet não ultrapassem 1492 bytes antes de receber o cabeçalho PPP de 8 bytes. Todo processo de resolução de problemas em conexões PPPoE deve começar por essa observação, para assegurar que o MTU foi configurado para 1492, caso contrário a comunicação não é estabelecida.</div>
<div> </div>
<div>Por fim, nas linhas 13, 14 e 15 são configuradas as credenciais de autenticação do usuário. Reparem que também já estamos fazendo a configuração do NAT, considerando a interface f0/0 como o lado <em>inside</em>e a interface <em>dialer1</em> como o lado <em>outside</em>. O objetivo desse artigo não é mostrar o processo de configuração do NAT, por isso os leitores que tiverem dúvida nessa configuração podem consultar o Lab10 do livro <strong>"Laboratórios de Tecnologias Cisco em Infraestrutura de Redes"</strong>.</div>
<div> </div>
<div>Como complemento, as linhas 18 e 20 trazem uma configuração adicional de segurança que restringe o tráfego na interface <em>dialer</em> para aceitar apenas conteúdo IP, uma prática que não é cobrada no novo exame CCNA R&S (por isso não há destaque em amarelo). A linha 23 cria uma rota padrão apontando que todo o conteúdo direcionado à Internet deve sair através dessa interface virtual que tem conectividade com a operadora.</div>
<div> </div>
<div>A título de informação, recentemente criei uma nova categoria no blog com a palavra-chave 200-120, onde estou agrupando todos os artigos relacionados aos tópicos adicionados no novo exame CCNA R&S. Recomendo aos leitores interessados no novo exame CCNA R&S que façam uma busca pela palavra-chave 200-120 porque em outras oportunidades já escrevi vários artigos falando sobre tópicos que foram acrescentados recentemente, a saber: SSH, SNMP, Syslog, NTP, NetFlow, IOS 15, etc.</div>
<div> </div>
<div>Abraço.</div>
<div> </div>
<div>Samuel.</div>
</div>