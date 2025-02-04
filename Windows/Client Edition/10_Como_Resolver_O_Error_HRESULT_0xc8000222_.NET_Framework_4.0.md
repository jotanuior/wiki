# Como Resolver O Error HRESULT 0xc8000222 .NET Framework 4.0

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** 0xc8000222 .NET Framework

**Última modificação:** 2014-10-28 16:33

**Autor:** Claudio Junior

---

1°Procure o cmd no iniciar e execute como administrador!<br />
2°Coloque net stop WuAuServ!<br />
3°feche o cmd e aperte Win(inicar)+R!<br />
4° digita %windir% e da enter!<br />
5°Procure a pasta SoftwareDistribution<br />
6°Renomeie SoftwareDistribution para SDold<br />
Eu ja renomiei<br />
7°depois feche a pasta e abra o cmd<br />
8°digite net start WuAuServ<br />
9°Intale o net framework 4.0