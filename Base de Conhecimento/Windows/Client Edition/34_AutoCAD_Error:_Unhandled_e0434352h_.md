# AutoCAD Error: Unhandled e0434352h 

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** e0434352h, AutoCAD

**Última modificação:** 2018-01-21 14:57

**Autor:** Claudio Junior

---

Problema<br />
quando o cliente abria o AutoCAD, recebia a seguinte mensagem de erro: Error: Unhandled e0434352h <br />
<br />
Análise do Problema<br />
Depois de analisarmos o log de Evento e a base de conhecimento da AUTODESK, descobrimos que o problema estava relacionado com programas .NETs e Microsoft Visual C++. O Problema foi resolvido desinstalado o AutoCAD, todos os programas .NET e MS Visual C++.<br />
<br />
<br />
Solução<br />
Desativar o Antivírus, remover o AutoCAD, MS Visual C++ e todos os programas .NET.<br />
<br />
Passo a passo:<br />
1. Desinstalar o Antivírus;<br />
2. Remover o AutoCAD e todos os produtos relacionados ao mesmo;<br />
3. Remover todos os produtos relacionados ao Microsoft Visual C++;<br />
4. Remover todos os produtos relacionados ao .NET;<br />
5. Reinicializar o computador;<br />
6. Realizar a instalação do AautoCAD;<br />
7. Reinicializar o computador, novamente;<br />
8. Realizar os testes com o AutoCad e instalar o Antivírus.