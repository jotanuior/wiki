# Imapsync dicas para selecionar mensagens

**Categoria:** Base de Conhecimento >> Linux

**Palavras-chave:** imap, imapsync

**Última modificação:** 2018-01-07 17:26

**Autor:** Claudio Junior

---

<pre>================================================== =====================
 Imapsync dicas para selecionar mensagens.
================================================== =====================

As perguntas apresentadas neste FAQ são:

P. Que mensagens imapsync sincronizam por padrão?

P. Existe uma maneira de especificar um intervalo de datas para sincronizar e-mails? 
 Se sim, você pode compartilhar um exemplo?

P. Existe uma maneira de especificar uma idade para sincronizar e-mails? 
 Se sim, você pode compartilhar alguns exemplos?

P. Eu quero sincronizar mensagens com base em seu UID.

P. Posso migrar apenas emails com anexos?

P. Como posso mover mensagens marcadas? Excluídas de todas as pastas para
 uma pasta dedicada?

P. Quais os critérios de seleção disponíveis com a opção - search?


================================================== =====================
P. Que mensagens imapsync sincronizam por padrão?

R. Por padrão, o Imapsync sincroniza todas as mensagens, exceto as duplas.

================================================== =====================
P. Existe uma maneira de especificar um intervalo de datas para sincronizar e-mails? 
 Se sim, você pode compartilhar um exemplo?

R. Sim, é possível um intervalo de datas com a opção --search.

 imapsync ... --search "SENTSINCE 1-Jan-2010" 
 
ou 
 
 imapsync ... --search "SENTBEFORE 31-Dec-2010"

ou
 
 imapsync ... --search "SENTSINCE 1-Jan-2010 SENTBEFORE 31-Dec-2010"

 Os meses são especificados como este:
 
 Janeiro
 Fev
 Mar
 Abril
 Pode 
 Jun
 Jul 
 Ago
 Setembro
 Outubro 
 Novembro
 Dezembro

================================================== =====================
P. Existe uma maneira de especificar uma idade para sincronizar e-mails? 
 Se sim, você pode compartilhar alguns exemplos?

R. Sim, com a opção --maxage ou --minage.

E.1 Sincronizar apenas mensagens com menos de 2 dias de idade:

 imapsync ... --maxage 2

E.2 Sincronizar apenas mensagens com mais de 2 dias de idade:

 imapsync ... --minagem 2

E.3 Sincronizar apenas mensagens com mais de 30 dias de idade e menos de 365 dias:

 imapsync ... --minagem 30 --maxage 365

E.4 Sincronizar apenas mensagens com menos de 30 dias de idade ou mais de 365 dias:

 imapsync ... --maxage 30 - minage 365

Explicação completa:

--maxage <int>: Ignorar mensagens anteriores a <int> dias.
 estatísticas finais (ignoradas) não contam mensagens antigas
 veja também - minage
--minage <int>: Ignorar mensagens mais recentes do que <int> dias.
 as estatísticas finais (ignoradas) não contam mensagens mais recentes
 Você pode fazer (+ são as mensagens selecionadas):
 passado | ---- maxage +++++++++++++++> agora
 passado | +++++++++++++++ minage ----> agora
 passado | ---- maxage +++++ minage ----> agora (interseção)
 past | ++++ minage ----- maxage ++++> now (union)

C.1 Por padrão,

 A opção --maxage é implementada como uma - search SENTSINCE 
RFC 3501 diz: SENTSINCE <date>
Mensagens cujo [RFC-2822] Data: cabeçalho (desconsiderando o tempo e
fuso horário) está dentro ou depois da data especificada.

 Opção - minage é implementada como uma - search SENTBEFORE
RFC 3501 diz: SENTBEFORE <data>
Mensagens cujo [RFC-2822] Data: cabeçalho (desconsiderando o tempo e
fuso horário) é anterior à data especificada.

Se a pesquisa --noable estiver ativada - minas e
com as datas internas dadas por um comando FETCH imap, mas 
não o Date: header. A data interna é a data de chegada
na caixa de correio. A mesma observação para --noable toearch1 and
- não é possível pesquisar2, mas apenas para um lado.

================================================== =====================
P. Eu quero sincronizar mensagens com base em seu UID.

R. Primeiro, tenha em mente que os UIDs são únicos apenas por pasta, então trabalhe isso
 apenas com uma pasta por vez, com a opção --folder.

Para mostrar UIDs, existe o parâmetro --debugLIST.

 imapsync ... --debugLIST

Para sincronizar apenas uma parte de todas as mensagens, selecionadas por UIDs 
de 10000 a 11000:

 imapsync ... --search1 "UID 10000: 11000" 

Para sincronizar do INBOX apenas 3 mensagens UIDs 20000 20002 20004:

 imapsync ... --search1 'OU OU UID 20000 UID 20002 UID 20004' - pasta INBOX

Para sincronizar todas as mensagens do INBOX, exceto 3 mensagens 
UIDs 20000 20002 20004:

 imapsync ... --search1 'NÃO E OU UID 20000 UID 20002 UID 20004' - pasta INBOX

Se você pesquisar UIDs, então você deve colocar n-1 OU na linha de pesquisa,
Isso é IMAP.

================================================== =====================
P. Posso migrar apenas emails com anexos?

R. Use:

 imapsync ... --search "HEADER Content-Type multipart / mixed" 

ou mais geralmente:

 imapsync ... --search "OU HEADER Conteúdo-Disposição anexo HEADER Content-Type multipart / mixed" 


================================================== =====================
P. Como posso mover mensagens marcadas? Excluídas de todas as pastas para
 uma pasta dedicada?

R. Para mover \ Mensagens excluídas de todas as pastas para uma pasta específica, 
 vamos chamá-lo de lixo, use:

 imapsync ... --search DELETED --regextrans2 "s /.*/ Trash /" 

================================================== =====================
P. Quais os critérios de seleção disponíveis com a opção - search?

R. A lista de critérios de pesquisa está listada abaixo, um excerto da RFC3501.

http://www.faqs.org/rfcs/rfc3501.html

6.4.4. Comando SEARCH
...
 TODOS
 Todas as mensagens na caixa de correio; a chave inicial padrão para
 ANDING.

 RESPONDIDAS
 Mensagens com o conjunto de sinalizadores respondidos.

 BCC <string>
 Mensagens que contêm a string especificada no envelope
 campo BCC da estrutura.

 ANTES <data>
 Mensagens cuja data interna (desconsiderando o tempo e o fuso horário)
 é anterior à data especificada.

 CORPO <string>
 Mensagens que contêm a string especificada no corpo do
 mensagem.

 CC <string>
 Mensagens que contêm a string especificada no envelope
 campo CC da estrutura.

 DEVIDO
 Mensagens com o conjunto de sinalizadores \ Deleted.

 ESBOÇO, PROJETO
 Mensagens com o flag \ Draft flag set.

 FLAGGED
 Mensagens com o conjunto de sinalizadores marcados.

 FROM <string>
 Mensagens que contêm a string especificada no envelope
 campo FROM da estrutura.

 HEADER <field-name> <string>
 Mensagens que têm um cabeçalho com o nome de campo especificado (como
 definido em [RFC-2822]) e que contém a string especificada
 no texto do cabeçalho (o que vem depois dos dois pontos). Se o
 A string to search é zero-length, corresponde a todas as mensagens que
 tenha uma linha de cabeçalho com o nome de campo especificado independentemente de
 o conteúdo.

 KEYWORD <flag>
 Mensagens com o sinalizador de palavras-chave especificado definido.

 MAIS GRANDE <n>
 Mensagens com um [RFC-2822] tamanho maior que o especificado
 número de octetos.

 NOVO
 Mensagens que têm o sinalizador \ Recent marcado, mas não o sinalizador \ Seen.
 Isso é funcionalmente equivalente a "(RECENT UNSEEN)".

 NÃO <tecla de pesquisa>
 Mensagens que não correspondem à chave de pesquisa especificada.

 VELHO
 Mensagens que não têm o sinalizador \ Recent marcado. Isto é
 funcionalmente equivalente a "NOT RECENT" (em oposição a "NOT"
 NOVO").

 ON <data>
 Mensagens cuja data interna (desconsiderando o tempo e o fuso horário)
 está dentro da data especificada.

 OU <search-key1> <search-key2>
 Mensagens que correspondem a qualquer tecla de pesquisa.

 RECENTE
 Mensagens que têm o sinalizador \ Recent marcado.

 VISTO
 Mensagens que têm o sinalizador \ Seen marcado.

 SENTBEFORE <data>
 Mensagens cujo [RFC-2822] Data: cabeçalho (desconsiderando o tempo e
 fuso horário) é anterior à data especificada.

 SENTON <data>
 Mensagens cujo [RFC-2822] Data: cabeçalho (desconsiderando o tempo e
 fuso horário) está dentro da data especificada.

 SENTSINCE <data>
 Mensagens cujo [RFC-2822] Data: cabeçalho (desconsiderando o tempo e
 fuso horário) está dentro ou depois da data especificada.

 DESDE <data>
 Mensagens cuja data interna (desconsiderando o tempo e o fuso horário)
 está dentro ou depois da data especificada.

 Menor <n>
 Mensagens com um tamanho [RFC-2822] menor que o especificado
 número de octetos.

 ASSUNTO <string>
 Mensagens que contêm a string especificada no envelope
 campo SUBJECT da estrutura.

 TEXTO <string>
 Mensagens que contêm a string especificada no cabeçalho ou
 corpo da mensagem.

 PARA <string>
 Mensagens que contêm a string especificada no envelope
 campo TO da estrutura.

 UID <conjunto de sequências>
 Mensagens com identificadores únicos correspondentes ao especificado
 conjunto de identificadores exclusivos. Os intervalos de setas de seqüência são permitidos.

 DESEMPREGADO
 Mensagens que não possuem o sinalizador \ Respondido definido.

 DESLIGADO
 Mensagens que não possuem o sinalizador \ Deleted definido.

 UNDRAFT
 Mensagens que não possuem o sinalizador de rascunho definido.

 DESFASTADO
 Mensagens que não possuem o sinalizador Flagado.

 UNKEYWORD <flag>
 Mensagens que não possuem o sinalizador de palavras-chave especificado definido.

 DESPERCEBIDAS
 Mensagens que não têm o sinalizador \ Seen marcado. 

================================================== =====================
================================================== ====================</pre>
