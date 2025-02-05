---
title: Tecmen
description: 
published: true
date: 2025-02-05T22:35:58.756Z
tags: 
editor: markdown
dateCreated: 2025-02-05T12:49:03.638Z
---

# 📂 Índice de Conhecimento

<script>
fetch('/api/pages')
  .then(response => response.json())
  .then(data => {
    let content = '<ul>';
    data.forEach(page => {
      content += `<li><a href="/${page.path}">${page.title}</a></li>`;
    });
    content += '</ul>';
    document.getElementById('page-list').innerHTML = content;
  });
</script>

<div id="page-list">
  <p>Carregando páginas...</p>
</div>

