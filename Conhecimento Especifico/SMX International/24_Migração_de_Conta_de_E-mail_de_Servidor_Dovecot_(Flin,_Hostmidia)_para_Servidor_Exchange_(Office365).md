# Migração de Conta de E-mail de Servidor Dovecot (Flin, Hostmidia) para Servidor Exchange (Office365)

**Categoria:** Base de Conhecimento >> Conhecimento Especifico >> SMX International

**Palavras-chave:** e-mail office365 smxinternational dovecot migração

**Última modificação:** 2015-07-19 17:21

**Autor:** Luiz Carlos

---

<p> </p>
<p>Como a ferramenta de migração disponível no portal do Office365 não funcionou como esperado, foi necessário utilizar o imapsync.</p>
<p> </p>
<p>A grande diferença entre esses dois tipos de servidores para a utilização do imapsync é que o Dovecot usa . (ponto) como separador de pastas e o Exchange usa / (barra). Além disso, a ponto base da estrutura de pastas (análogo ao / no linux ou o C: no Windows) difere pois o Dovecot usa INBOX. e o Exchange não usa esse recurso. Ou seja, a pasta Documentos aparecerá no Dovecot como INBOX.Documentos e no Exchange simplesmente como Documentos na estrutura de pastas de e-mail.</p>
<p> </p>
<p>Por esses motivos, é necessário o uso do parâmetro --regextrans2 para compatibilizar a migração corretamente.</p>
<p> </p>
<p>EXEMPLO (da Flin - o ServidorAntigo - para Office365):</p>
<p>/usr/bin/imapsync --addheader --host1 webserver07.floripa.com.br --user1 paulo.seara@smxinternational.com.br --password1 <senha> --host2 132.245.60.2 --ssl2 --user2 paulo.seara@smxinternational.com.br --password2 <senha> --regextrans2 's#(.*)#ServidorAntigo/$1#' --dry --justfolders</p>
<p>Qualquer parâmetro adicional deve ser incluído após o parâmetro password2 e a respectiva senha.</p>
<p>O parâmetro --dry roda o comando como TESTE. Vai realizar apenas a simulação do que ocorreria se o comando sem o --dry for executado. Muito útil.</p>
<p>No exemplo acima, toda a estrutura de pastas do servidor antigo será copiado (ou seja, não é removido do servidor de origem) para a pasta ServidorAntigo dentro do servidor destino.</p>
<p> </p>
<p>FONTE:</p>
<p>http://www.seas.harvard.edu/computing-office/email/how-to-use-imapsync</p>
<p> </p>
<p>Lista de pastas criadas por padrão para novas contas do Office365 (útil para migração e restore futuro a partir da HostMidia para não bagunçar estrutura existente):</p>
<p> - Caixa de Entrada (Inbox)</p>
<p> - Anotações</p>
<p> - Rascunhos (Drafts)</p>
<p> - Lixo Eletrônico (Junk)</p>
<p> - Caixa de Saída (Outbox)</p>
<p> - Itens Enviados (Sent Items)</p>
<p> </p>