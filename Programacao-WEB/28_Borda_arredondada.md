# Borda arredondada CSS

**Categoria:** Programação WEB

**Palavras-chave:** borda, arredondada, css

**Última modificação:** 2016-06-01 15:05

**Autor:** Claudio Junior

---

<h1>Bordas Arredondadas CSS3: Estilizando bordas</h1>
<p>Neste artigo iremos aprender a criar elementos com bordas arredondadas por meio de css 3. Iremos ver como é possível atribuir diferentes valores para diferentes bordas.</p>
<div class="article">
<p>Olá Pessoal, neste tutorial iremos ver como arredondar os cantos das bordas por meio de CSS3 e fazer funcionar em todos os navegadores.</p>
<p>Antes do CSS3, para criarmos bordas arredondadas era preciso escrever bastante código css e usar diversas imagens, mas com a chegava do novo css esse trabalho ficou muito mais fácil, em apenas 3 linhas é possível fazer um Box com cantos arredondados aparecer em todos os principais navegadores e ainda poder definir o quanto arredondado ficará a borda.</p>
<p>Vamos à parte prática, que é o que interessa:</p>
<p>Primeiro criamos um documento HTML que será onde ficará o nosso Box.</p>
<p><strong>Listagem1</strong>: Código completo</p>
<div>
<div id="highlighter\_825158" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
<div class="line number14 index13 alt1">14</div>
<div class="line number15 index14 alt2">15</div>
<div class="line number16 index15 alt1">16</div>
<div class="line number17 index16 alt2">17</div>
<div class="line number18 index17 alt1">18</div>
<div class="line number19 index18 alt2">19</div>
<div class="line number20 index19 alt1">20</div>
<div class="line number21 index20 alt2">21</div>
<div class="line number22 index21 alt1">22</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><!DOCTYPE html PUBLIC </code><code class="js string">"-//W3C//DTD XHTML 1.0 Transitional//EN"</code></div>
<div class="line number2 index1 alt1"><code class="js string">"<a href="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd</a>"</code><code class="js plain">></code></div>
<div class="line number3 index2 alt2"><code class="js plain"><html xmlns=</code><code class="js string">"<a href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>"</code><code class="js plain">></code></div>
<div class="line number4 index3 alt1"><code class="js plain"><head></code></div>
<div class="line number5 index4 alt2"><code class="js plain"><meta http-equiv=</code><code class="js string">"Content-Type"</code> <code class="js plain">content=</code><code class="js string">"text/html; charset=utf-8"</code> <code class="js plain">/></code></div>
<div class="line number6 index5 alt1"><code class="js plain"><title>Bordas Arredondadas</title></code></div>
<div class="line number7 index6 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number8 index7 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#666;</code></div>
<div class="line number12 index11 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px;</code></div>
<div class="line number13 index12 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number14 index13 alt1"> </div>
<div class="line number15 index14 alt2"><code class="js plain"></style></code></div>
<div class="line number16 index15 alt1"><code class="js plain"></head></code></div>
<div class="line number17 index16 alt2"> </div>
<div class="line number18 index17 alt1"><code class="js plain"><body></code></div>
<div class="line number19 index18 alt2"><code class="js plain"><!-- iremos criar nossa div onde ficará o box arredondado --></code></div>
<div class="line number20 index19 alt1"><code class="js plain"><div id=</code><code class="js string">"box"</code><code class="js plain">></div></code></div>
<div class="line number21 index20 alt2"><code class="js plain"></body></code></div>
<div class="line number22 index21 alt1"><code class="js plain"></html></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>Note que usamos o css para estilizar a div criada pelo HTML, nela colocamos largura e altura que desejamos e também colocamos uma propriedade nova, chamada <strong>border-radius</strong>. Com ela é possível arredondar todas as bordas sem precisar de usar imagens para fazer isso.</p>
<p><strong>Listagem 2</strong>: Propriedade border-radius</p>
<div>
<div id="highlighter\_367479" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#666;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number12 index11 alt1"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>Como podemos ver na imagem a seguir, o nosso Box terá 10px de bordas arredondadas, isso quer dizer que todas as 4 bordas terá o valor de 10px.</p>
<img src="http://videos.web-03.net/artigos/Ricardo\_Arrigoni/Bordas\_Arredondadas\_com\_html\_e\_css\_3/imagem1.jpg" alt="Bordas com 10px de arredondamento" /><br />
<p>Figura 1: Bordas com 10px de arredondamento.</p>
<p>Assim como as propriedades margin, padding e border, é possível definir valores diferentes para cada canto, irei mostrar alguns exemplos e como deverá ficar exibido após:</p>
<p><strong>Listagem 3</strong>: border-radius: 10px 20px;</p>
<div>
<div id="highlighter\_919087" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#6495ed;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px 20px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number12 index11 alt1"> </div>
<div class="line number13 index12 alt2"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>O exemplo anterior ficará da seguinte forma:</p>
<img src="http://videos.web-03.net/artigos/Ricardo\_Arrigoni/Bordas\_Arredondadas\_com\_html\_e\_css\_3/imagem2.jpg" alt="border-radius: 10px 20px;" /><br />
<p>Figura 2. border-radius: 10px 20px 30px;</p>
<p><strong>Listagem 4</strong>: border-radius: 10px 20px 30px;</p>
<div>
<div id="highlighter\_704016" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#6495ed;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px 20px 30px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number12 index11 alt1"> </div>
<div class="line number13 index12 alt2"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>O exemplo anterior ficará da seguinte forma:</p>
<img src="http://videos.web-03.net/artigos/Ricardo\_Arrigoni/Bordas\_Arredondadas\_com\_html\_e\_css\_3/imagem3.jpg" alt="border-radius: 10px 20px 30px;" /><br />
<p>Figura 3. border-radius: 10px 20px 30px;</p>
<p><strong>Listagem 5</strong>: border-radius: 10px 20px 30px 40px;</p>
<div>
<div id="highlighter\_155313" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#6495ed;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px 20px 30px 40px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number12 index11 alt1"> </div>
<div class="line number13 index12 alt2"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>O exemplo ficará assim:</p>
<img src="http://videos.web-03.net/artigos/Ricardo\_Arrigoni/Bordas\_Arredondadas\_com\_html\_e\_css\_3/imagem4.jpg" alt="border-radius: 10px 20px 30px 40px;" /><br />
<p>Figura 4. border-radius: 10px 20px 30px 40px;</p>
<p>Caso você queira arredondar os cantos separadamente, também é possível. Abaixo as opções de alteração separadamente e você pode testar e ver quais são os resultados.</p>
<ul>
<li>border-radius-topleft para o canto superior esquerdo</li>
<li>border-radius-topright para o canto superior direito</li>
<li>border-radius-bottomright para o canto inferior direito</li>
<li>border-radius-bottomleft para o canto inferior esquerdo</li>
</ul>
<br />
<h3>Exibir no Firefox</h3>
<p>Para exibir no Firefox é praticamente a mesma coisa, a única diferença é que usamos o prefixo “-moz-“ antes de “border-radius”, ficando “-moz-border-radius: X px;</p>
<p><strong>Listagem 6</strong>: Exibindo no Firefox também</p>
<div>
<div id="highlighter\_298694" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
<div class="line number14 index13 alt1">14</div>
<div class="line number15 index14 alt2">15</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#6495ed;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js comments">/* Declaração para aparecer no Firefox */</code></div>
<div class="line number12 index11 alt1"><code class="js spaces">    </code><code class="js plain">-moz-border-radius: 10px;</code></div>
<div class="line number13 index12 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number14 index13 alt1"> </div>
<div class="line number15 index14 alt2"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>Assim como o Firefox, os outros navegadores, como Chrome, Safari, Opera, IE precisam de um prefixo para funcionarem também, para isso é usado o “-webkit-“ antes de “border-radius”, ficando “-webkit-border-radius”.</p>
<p><strong>Listagem 7 :</strong> Exibindo em todos os navegadores</p>
<div>
<div id="highlighter\_700527" class="syntaxhighlighter js">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1</div>
<div class="line number2 index1 alt1">2</div>
<div class="line number3 index2 alt2">3</div>
<div class="line number4 index3 alt1">4</div>
<div class="line number5 index4 alt2">5</div>
<div class="line number6 index5 alt1">6</div>
<div class="line number7 index6 alt2">7</div>
<div class="line number8 index7 alt1">8</div>
<div class="line number9 index8 alt2">9</div>
<div class="line number10 index9 alt1">10</div>
<div class="line number11 index10 alt2">11</div>
<div class="line number12 index11 alt1">12</div>
<div class="line number13 index12 alt2">13</div>
<div class="line number14 index13 alt1">14</div>
<div class="line number15 index14 alt2">15</div>
<div class="line number16 index15 alt1">16</div>
<div class="line number17 index16 alt2">17</div>
</td>
<td class="code">
<div class="container">
<div class="line number1 index0 alt2"><code class="js plain"><style type=</code><code class="js string">"text/css"</code><code class="js plain">></code></div>
<div class="line number2 index1 alt1"><code class="js preprocessor">#box{</code></div>
<div class="line number3 index2 alt2"><code class="js spaces">    </code><code class="js comments">/*definimos a largura do box*/</code></div>
<div class="line number4 index3 alt1"><code class="js spaces">    </code><code class="js plain">width:300px;</code></div>
<div class="line number5 index4 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a altura do box */</code></div>
<div class="line number6 index5 alt1"><code class="js spaces">    </code><code class="js plain">height:100px;</code></div>
<div class="line number7 index6 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos a cor de fundo do box */</code></div>
<div class="line number8 index7 alt1"><code class="js spaces">    </code><code class="js plain">background-color:</code><code class="js preprocessor">#6495ed;</code></div>
<div class="line number9 index8 alt2"><code class="js spaces">    </code><code class="js comments">/* definimos o quão arredondado irá ficar nosso box */</code></div>
<div class="line number10 index9 alt1"><code class="js spaces">    </code><code class="js plain">border-radius: 10px;</code></div>
<div class="line number11 index10 alt2"><code class="js spaces">    </code><code class="js comments">/* Declaração para aparecer no Firefox */</code></div>
<div class="line number12 index11 alt1"><code class="js spaces">    </code><code class="js plain">-moz-border-radius: 10px;</code></div>
<div class="line number13 index12 alt2"><code class="js spaces">    </code><code class="js comments">/* Para exibir nos outros navegadores como Chrome, safari, opera*/</code></div>
<div class="line number14 index13 alt1"><code class="js spaces">    </code><code class="js plain">-webkit-border-radius: 10px;</code></div>
<div class="line number15 index14 alt2"><code class="js spaces">    </code><code class="js plain">}</code></div>
<div class="line number16 index15 alt1"> </div>
<div class="line number17 index16 alt2"><code class="js plain"></style></code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="spacesyntax"> </div>
<p>Agora sabemos como arredondas cada canto de qualquer elemento HTML por meio de css3, de maneira muito mais fácil e mais leve do que com css2. Um abraço e até o próximo artigo.</p>
<p>Espero que tenham gostado e até o próximo artigo.</p>
</div>
<p><span id="ContentPlaceHolder1\_lblTexto" class="artigo"></span><br /><br />Read more: <a href="http://www.linhadecodigo.com.br/artigo/3611/bordas-arredondadas-css3-estilizando-bordas.aspx#ixzz4AKfOSwEh">http://www.linhadecodigo.com.br/artigo/3611/bordas-arredondadas-css3-estilizando-bordas.aspx#ixzz4AKfOSwEh</a></p>