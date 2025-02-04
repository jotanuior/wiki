# Criando VPN entre empresa e Filial com Mikrotik

**Categoria:** Base de Conhecimento >> REDES >> Mikrotik

**Palavras-chave:** VPN, Mikrotik

**Última modificação:** 2020-04-02 20:25

**Autor:** Claudio Junior

---

<p><strong>criando VPN entre empresa e Filial com Mikrotik</strong></p>
<p>Criação de VPN entre matriz e filial de uma empresa usando servidores <em>Mikrotik</em> nas duas pontas. Levando em consideração a seguinte estrutura:          </p>
<p><strong>Matriz: ·</strong><br />Rede Local: 40.0.0.X/24          <br />Ip local do Servidor: 40.0.0.1         <br />Ip Internet do Servidor: 201.200.200.200  IP Publico ou Cloud<br /><br /><strong>Filial: ·         </strong><br />Rede Local: 192.168.1.X/24 ·         <br />Ip local do Servidor: 192.168.1.1 ·         <br />Ip Internet do Servidor: 189.50.1.200  IP Publico ou Cloud<br /><br /><strong>VPN: ·         </strong><br />Faixa IPs: 10.20.0.X/24 IPs para VPN usar a mesma faixa qdo criar o secret.<br /><br /></p>
<p><br /><strong>Configurações</strong> Partindo do ponto de que os dois servidores já estão devidamente configurados e navegando na Internet repassando a navegação para rede Interna e seus clientes via NAT, iremos configurar o Server VPN na matriz. <br /><br /></p>
<p><strong>WINBOX:</strong><br /><br />Ip > firewall > Service Ports, <br />clique com o botão direito e selecione enable em "GRE" e "PPTP". <br /><br />PPP > Interfaces > L2TP Server > marque a opção enable. <br /><br />Na segunda guia, "secrets", crie um usuário para conectar ao Server pela VPN: Usuário: teste <br />Senha: teste <br />Local address: 10.20.0.1 <br />Remote address: 10.20.0.2 <br /><br />Dessa forma seu servidor estará preparado para ouvir e autenticar requisições L2TP. Ainda falta configurar as rotas nesse servidor para que as máquinas internas possam ver a outra rede e vice-versa. <br /><br />Ip > routes e crie as duas rotas abaixo (na Matriz):  <br />Primeira Rota: 10.20.0.0/24 > gateway 40.0.0.1 <br />Segunda Rota: 192.168.1.0/24> Gateway 10.20.0.2 <br /><br />A rota 10.0.0.0/24 apontando para o gateway 40.0.0.1 indica que a rede usada pela vpn será roteada pelo ip 40.0.0.1 que é da placa interna do servidor e a rota 192.168.10.0/24 indica que a rede interna do servidor da filial será roteada pelo ip remoto que o servidor da filial receberá quando conectar. <br />Configuramos o servidor da matriz, agora vamos para o servidor da</p>
<p>Filial: <br />PPP > Interfaces crie o usuário para se conectar conforme abaixo: <br />Server: 201.200.200.200 <br />user: teste <br />password: teste <br /><br />Ip > routes e crie as duas rotas abaixo (na Filial):  <br />Primeira Rota: 10.20.0.0/24 > gateway 192.168.1.1 <br />Segunda Rota: 40.0.0.0/24> Gateway 10.20.0.1 <br />Terceira Rota: 192.168.25.0/24 (caso tenha mais de um range de ip)> GTW 10.20.0.1 <br /><br />Bom pessoal, com isso estaremos com a vpn funcionando nos dois pontos caso queiram adicionar mais pontos é só seguir o mesmo raciocínio. Outra coisa, você pode também criar um usuário para acessar de qualquer máquina Windows diretamente em rede assistente para novas conexões e marcar a opção conectar-me a uma vpn.</p>