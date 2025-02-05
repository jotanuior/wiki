# Usar configurações de política de grupo para configurar e gerenciar o Windows Defender Antivirus

**Categoria:** Base de Conhecimento >> Windows >> Server Edition

**Palavras-chave:** windows, GPO, Defender

**Última modificação:** 2019-07-16 17:20

**Autor:** Claudio Junior

---

<h1 id="usar-configurações-de-política-de-grupo-para-configurar-e-gerenciar-o-windows-defender-antivirus">Usar configurações de política de grupo para configurar e gerenciar o Windows Defender Antivirus</h1>
<p><strong>Aplica-se a:</strong></p>
<ul>
<li><a href="https://go.microsoft.com/fwlink/p/?linkid=2069559" data-linktype="external">Proteção avançada contra ameaças do Microsoft defender (Microsoft defender ATP)</a></li>
</ul>
<p>Você pode usar <a href="https://msdn.microsoft.com/library/ee663280(v=vs.85).aspx" data-linktype="external">Política de grupo</a> para configurar e gerenciar o Windows Defender Antivírus em seus pontos de extremidade.</p>
<p class="">Em geral, você pode usar o procedimento a seguir para configurar ou alterar as configurações de política de grupo do Windows Defender Antivirus:</p>
<ol>
<li>
<p>Em sua máquina de gerenciamento de Política de Grupo, abra o <a href="https://technet.microsoft.com/library/cc731212.aspx" data-linktype="external">Console de Gerenciamento de Política de Grupo</a>, clique com botão direito do mouse no Objeto de política de grupo (GPO) que você deseja configurar e clique em <strong>Editar</strong>.</p>
</li>
<li>
<p>No <strong>Editor de Gerenciamento de Política de Grupo</strong>, acesse <strong>Configuração do computador</strong>.</p>
</li>
<li>
<p>Clique em <strong>modelos administrativos</strong>.</p>
</li>
<li>
<p>Expanda a árvore para <strong>Componentes do Windows > Windows Defender Antivírus ou END POINT PROTECTION</strong>.</p>
</li>
<li>
<p class="">Expanda a seção (conhecida como <strong>Local</strong> na tabela neste tópico) que contém a configuração que você deseja definir, clique duas vezes nela para abri-la e faça as alterações na configuração.</p>
</li>
<li>
<p><a href="https://msdn.microsoft.com/library/ee663280(v=vs.85).aspx" data-linktype="external">Implante o GPO atualizado de forma normal</a>.</p>
</li>
</ol>
<p class="">A tabela a seguir neste tópico lista as configurações de Política de grupo disponíveis no Windows 10, versão 1703 e fornece links para o tópico apropriado nesta biblioteca de documentação (quando aplicável).</p>
<div class="table-scroll-wrapper">
<table>
<thead>
<tr>
<th>Localização</th>
<th>Configuração</th>
<th>Documentados no tópico</th>
</tr>
</thead>
<tbody>
<tr>
<td>Interface do cliente</td>
<td>Habilitar o modo de interface do usuário sem periféricos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/prevent-end-user-interaction-windows-defender-antivirus" data-linktype="relative-path">Impedir que os usuários vejam ou interajam com a interface do usuário do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Interface do cliente</td>
<td>Exibir texto adicional aos clientes quando eles precisam executar uma ação</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-notifications-windows-defender-antivirus" data-linktype="relative-path">Configure as notificações que aparecem em pontos de extremidade</a></td>
</tr>
<tr>
<td>Interface do cliente</td>
<td>Suprimir todas as notificações</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-notifications-windows-defender-antivirus" data-linktype="relative-path">Configure as notificações que aparecem em pontos de extremidade</a></td>
</tr>
<tr>
<td>Interface do cliente</td>
<td>Suprime notificações de reinicialização</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-notifications-windows-defender-antivirus" data-linktype="relative-path">Configure as notificações que aparecem em pontos de extremidade</a></td>
</tr>
<tr>
<td>Exclusões</td>
<td>Exclusões de extensão</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-exclusions-windows-defender-antivirus" data-linktype="relative-path">Configurar e validar exclusões nas verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Exclusões</td>
<td>Exclusões de caminho</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-exclusions-windows-defender-antivirus" data-linktype="relative-path">Configurar e validar exclusões nas verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Exclusões</td>
<td>Exclusões de processo</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-exclusions-windows-defender-antivirus" data-linktype="relative-path">Configurar e validar exclusões nas verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Exclusões</td>
<td>Desativar as exclusões automáticas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-exclusions-windows-defender-antivirus" data-linktype="relative-path">Configurar e validar exclusões nas verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>MAPS</td>
<td>Configurar o recurso "Bloquear à primeira vista"</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-block-at-first-sight-windows-defender-antivirus" data-linktype="relative-path">Habilitar bloqueio à primeira vista</a></td>
</tr>
<tr>
<td>MAPS</td>
<td>Ingressar no Mapas Microsoft</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/enable-cloud-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar a proteção entregue na nuvem</a></td>
</tr>
<tr>
<td>MAPS</td>
<td>Enviar amostras de arquivo quando outra análise for necessária</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/enable-cloud-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar a proteção entregue na nuvem</a></td>
</tr>
<tr>
<td>MAPS</td>
<td>Configurar a substituição de configuração local para relatar para a Microsoft MAPS</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>MpEngine</td>
<td>Configurar a verificação estendida na nuvem</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-cloud-block-timeout-period-windows-defender-antivirus" data-linktype="relative-path">Configurar o período de tempo limite de bloqueio da nuvem</a></td>
</tr>
<tr>
<td>MpEngine</td>
<td>Selecionar o nível de proteção de nuvem</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/specify-cloud-protection-level-windows-defender-antivirus" data-linktype="relative-path">Especificar o nível de proteção entregue na nuvem</a></td>
</tr>
<tr>
<td>Sistema de Inspeção de rede</td>
<td>Especificar conjuntos de definição adicional para inspeção de tráfego de rede</td>
<td>Não usada</td>
</tr>
<tr>
<td>Sistema de Inspeção de rede</td>
<td>Ativar a aposentadoria de definição</td>
<td>Não usada</td>
</tr>
<tr>
<td>Sistema de Inspeção de rede</td>
<td>Ativar o reconhecimento de protocolo</td>
<td>Não usada</td>
</tr>
<tr>
<td>Colocar em quarentena</td>
<td>Configurar a substituição de configuração local para a remoção dos itens da pasta de quarentena</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Colocar em quarentena</td>
<td>Configurar a remoção de itens da pasta de quarentena</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Configurar a substituição de configuração local para monitorar a atividade de arquivos e programas no seu computador</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Configurar a substituição de configuração local para o monitoramento de atividade de entrada e saída de arquivo</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Definir a configuração local de substituição para verificar todos os arquivos baixados tudo e anexos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Configurar a substituição de configuração local para ativar o monitoramento do comportamento</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Configurar a substituição de configuração local para ativar a proteção em tempo real</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Definir o tamanho máximo de arquivos baixados e anexos a serem verificados</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Monitorar a atividade de arquivos e programas no computador</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Verificar todos os arquivos baixados e anexos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Desativar a proteção em tempo real</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Ativar o monitoramento do comportamento</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Ativar o processo de verificação sempre que a proteção em tempo real estiver habilitada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Ativar as notificações de gravação de volume bruto</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Proteção em tempo real</td>
<td>Configurar o monitoramento de atividade de entrada e saída de arquivo e programa</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Correção</td>
<td>Configurar a substituição de configuração local para o horário do dia para executar uma verificação completa agendada para concluir a correção</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Correção</td>
<td>Especifique o dia da semana para executar uma verificação completa agendada para correção completa</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações programadas do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Correção</td>
<td>Especificar a hora do dia a fim de executar uma verificação completa agendada para correção completa</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações programadas do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Relatórios</td>
<td>Configurar eventos Watson</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Configurar componentes pré-processados de rastreamento de software do Windows</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Configurar nível de rastreamento WPP</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Definir o tempo limite para detecções no estado de falha crítica</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Configurar o tempo limite para detecções no estado de falha não crítica</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Definir i tempo limite para detecções no estado remediado recentemente</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Definir tempo limite para detecções que exigem uma ação adicional</td>
<td>Não usada</td>
</tr>
<tr>
<td>Relatórios</td>
<td>Desativar notificações aprimoradas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-notifications-windows-defender-antivirus" data-linktype="relative-path">Configure as notificações que aparecem em pontos de extremidade</a></td>
</tr>
<tr>
<td>Root</td>
<td>Desativar o Windows Defender Antivírus</td>
<td>Não usado (Esta configuração deve ser definida como <strong>Não configurado</strong> para garantir que todos os aplicativos antivírus de terceiros instalados estejam funcionando corretamente)</td>
</tr>
<tr>
<td>Root</td>
<td>Definir endereços para ignorar o servidor proxy</td>
<td>Não usada</td>
</tr>
<tr>
<td>Root</td>
<td>Definir a configuração automática do proxy (.pac) para conectar-se à rede</td>
<td>Não usada</td>
</tr>
<tr>
<td>Root</td>
<td>Definir o servidor proxy para conectar-se à rede</td>
<td>Não usada</td>
</tr>
<tr>
<td>Root</td>
<td>Configurar o comportamento de mesclagem de administrador local para listas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Raiz</td>
<td>Permitir que o serviço antimalware inicialize com prioridade normal</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Root</td>
<td>Permitir que o serviço antimalware permaneça em execução sempre</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Root</td>
<td>Desativar a correção rotineira</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Root</td>
<td>Horários de tarefa agendada organizados aleatoriamente</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Permitir que os usuários pausem a verificação</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/prevent-end-user-interaction-windows-defender-antivirus" data-linktype="relative-path">Impedir que os usuários vejam ou interajam com a interface do usuário do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Verifique as definições de vírus e spyware mais recentes antes de executar uma verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-event-based-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações forçadas com base em evento</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Definir a quantidade de dias após a qual uma verificação de atualização é forçada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Ativar a verificação de atualização completa</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Ativar a verificação rápida de atualização</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Configurar a substituição de configuração local para porcentagem máxima de utilização da CPU</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Configurar a substituição de configuração local para o dia de verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Configurar a substituição de configuração local para hora agendada de verificação rápida</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Configurar a substituição de configuração local para hora agendada de verificação</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Configurar a substituição de configuração local para o tipo de verificação a ser usada para uma verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-local-policy-overrides-windows-defender-antivirus" data-linktype="relative-path">Impedir ou permitir que os usuários modifiquem localmente as configurações de política</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Criar um ponto de restauração do sistema</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Ative a remoção de itens da pasta de histórico de verificação</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificar</td>
<td>Ativar a heurística</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-real-time-protection-windows-defender-antivirus" data-linktype="relative-path">Habilitar e configurar o monitoramento e a proteção do Windows Defender Antivirus sempre ativas</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Ativar a verificação de e-mail</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Ativar a verificação do ponto de nova análise</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Executar a verificação completa em unidades de rede mapeadas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Pesquisar arquivos mortos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Verificar os arquivos de rede</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Verificar executáveis compactados</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Verificar unidades removíveis</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especificar a profundidade máxima de verificação de arquivos mortos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especificar o percentual máximo de utilização da CPU durante uma verificação</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especificar a profundidade máxima de verificação de arquivos mortos</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-advanced-scan-types-windows-defender-antivirus" data-linktype="relative-path">Configurar opções de verificação no Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especifique o dia da semana para executar uma verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especifique o intervalo para executar verificações rápidas por dia</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especifique o tipo de verificação a ser usado para uma verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especifique o horário de uma verificação rápida diária</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Especifique a hora do dia para executar uma verificação agendada</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Verificação</td>
<td>Inicia a verificação agendada somente quando o computador está ligado, mas não está em uso</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Permitir atualizações de definição do Microsoft Update</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-updates-mobile-devices-vms-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para dispositivos móveis e VMs (máquinas virtuais)</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Permitir atualizações de definição quando ligado na bateria</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-updates-mobile-devices-vms-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para dispositivos móveis e VMs (máquinas virtuais)</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Permitir notificações para desabilitar relatórios com base em definições para Mapas Microsoft</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-event-based-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações forçadas com base em evento</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Permitir atualizações de definição em tempo real com base nos relatórios para Mapas Microsoft</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-event-based-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações forçadas com base em evento</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Procurar as definições de vírus e spyware mais recentes na inicialização</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-event-based-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações forçadas com base em evento</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Definir compartilhamentos de arquivos para baixar atualizações de definição</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-protection-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações de definição e de proteção do Windows Defender Antivírus</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Definir a quantidade de dias após a qual uma atualização de definição é necessária</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Definir a quantidade de dias antes das definições de spyware serem consideradas desatualizadas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Definir a quantidade de dias antes das definições de vírus serem consideradas desatualizadas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-outdated-endpoints-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações para pontos de extremidade que estejam desatualizados</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Definir a ordem das origens para baixar atualizações de definições</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-protection-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações de definição e de proteção do Windows Defender Antivírus</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Iniciar atualização de definição durante a inicialização</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-event-based-updates-windows-defender-antivirus" data-linktype="relative-path">Gerenciar atualizações forçadas com base em evento</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Especificar o dia da semana para verificar se há atualizações de definição</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-protection-update-schedule-windows-defender-antivirus" data-linktype="relative-path">Gerenciar quando as atualizações de proteção devem ser baixadas e aplicadas</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Especificar o intervalo para verificar se há atualizações de definição</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-protection-update-schedule-windows-defender-antivirus" data-linktype="relative-path">Gerenciar quando as atualizações de proteção devem ser baixadas e aplicadas</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Especificar o horário para verificar se há atualizações de definição</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/manage-protection-update-schedule-windows-defender-antivirus" data-linktype="relative-path">Gerenciar quando as atualizações de proteção devem ser baixadas e aplicadas</a></td>
</tr>
<tr>
<td>Atualizações de inteligência de segurança</td>
<td>Ativar o exame após a atualização do Security Intelligence</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/scheduled-catch-up-scans-windows-defender-antivirus" data-linktype="relative-path">Configurar verificações agendadas para o Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Ameaças</td>
<td>Especifique os níveis de alerta de ameaça em que a ação padrão não deve ser tomada quando detectado</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
<tr>
<td>Ameaças</td>
<td>Especificar ameaças após as quais a ação padrão não deve ser tomada quando detectadas</td>
<td><a href="https://docs.microsoft.com/pt-br/windows/security/threat-protection/windows-defender-antivirus/configure-remediation-windows-defender-antivirus" data-linktype="relative-path">Configurar a correção para verificações do Windows Defender Antivirus</a></td>
</tr>
</tbody>
</table>
</div>