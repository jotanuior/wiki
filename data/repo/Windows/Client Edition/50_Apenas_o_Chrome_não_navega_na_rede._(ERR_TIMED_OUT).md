# Apenas o Chrome não navega na rede. (ERR_TIMED_OUT)

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** Chrome, ERR_TIMED_OUT

**Última modificação:** 2019-07-17 23:29

**Autor:** Claudio Junior

---

<div>Faça o seguinte:</div>
<div> </div>
<div>
<div>1. Na área de trabalho, pressione as teclas Windows + R e digite CMD, clique sobre ele com o botão direito do mouse e selecione Executar como administrador;</div>
<div>2. Cole o comando: net stop cryptsvc [Enter] e feche a janela;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/ddc92441-7413-4cf4-b0c1-b481353c5549?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div> </div>
<div>3. Na área de trabalho, pressione as teclas Windows + R e digite: regedit, clique em OK;</div>
<div>4. Navegue até a chave: HKEY\_CURRENT\_USER\Software\Microsoft\SystemCertificates\Root;</div>
<div>5. Clique com o botão direito sobre a chave Root e selecione Exportar > Salve na área de trabalho;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/95e22871-1af4-4c8c-b068-6c30f78dfa9a?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div>6. Clique com o botão direito sobre a chave Root e selecione Permissões > Adicionar > Digite: Todos >Verificar nomes > OK > Na janela principal, selecione o usuário e marque a caixa Controle total;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/2968ab3d-94dd-49f6-ae9f-cba6994af47c?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div> </div>
<div>7. Ainda na janela de Permissões clique em Avançadas >A frente de Proprietário clique em Alterar > Digite:Todos > Verificar Nomes > OK;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/e33eff0f-c1d6-4bbf-8f7c-8ba0f914b477?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div> </div>
<div>8. Marque as opções Substituir o proprietário em subcontêineres e objetos e Substituir todas as entradas de permissão de objetivos filho por entradas de permissão herdáveis desse objeto e clique em Habilitar Herança > Aplicar;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/e771df20-0304-4c90-b2ed-28739588175f?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div> </div>
<div>9. Clique na guia Auditoria > Adicionar > Clique em Selecionar uma entidade de segurança > Digite: Todos> Verificar Nomes > Ok > Marque Controle Total e Aplicar estas entradas de auditoria apenas a objetos e/ou contêineres dentro deste contêiner > Ok;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/a0c025fa-5735-4115-8245-7f106a9d0115?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div><br />10. Na janela principal, clique em Aplicar e OK;</div>
<div>11. Após aplicar as permissões, clique com o botão direito do mouse sobre a chave Root e selecione Excluir;</div>
<div> </div>
<div><a href="https://filestore.community.support.microsoft.com/api/images/3f0c7ae4-4ce3-4468-b011-a22f1b877d83?upload=true" target="\_blank" rel="nofollow noopener noreferrer" data-auth="NotApplicable"><img data-imagetype="Empty" data-imageerror="SrcNullOrEmpty" /></a></div>
<div>12. Reinicie o equipamento.</div>
</div>
<div> </div>