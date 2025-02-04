# Create USB UEFI

**Categoria:** Base de Conhecimento >> Windows >> Client Edition

**Palavras-chave:** windows, 10, pe, uefi

**Última modificação:** 2019-12-04 22:32

**Autor:** Claudio Junior

---

<p>DISKPART></p>
<p>DISKPART> list disk</p>
<p>Nº Disco Status Tam. Livre Din. GPT<br /> -------- ------------- ------- ------- --- ---<br /> Disco 0 Online 931 GB 0 B<br /> Disco 1 Online 7681 MB 0 B</p>
<p>DISKPART> select disk 1</p>
<p>O disco 1 é o disco selecionado.</p>
<p>DISKPART> clean</p>
<p>DiskPart está limpando o disco.</p>
<p>DISKPART> create partition primary</p>
<p>DiskPart criou com êxito a partição especificada.</p>
<p>DISKPART> active</p>
<p>O DiskPart marcou a partição atual como ativa.</p>
<p>DISKPART> format quick fs=FAT32</p>
<p>100 por cento concluído</p>
<p>O DiskPart formatou com êxito o volume.</p>
<p>DISKPART> assign</p>
<p>DiskPart atribuiu com êxito a letra de unidade ou o ponto de montagem.</p>
<p>DISKPART> exit</p>
<p>Descompactar iso do windows no drive USB</p>
<p>Copiar os arquivos da pasta "usb":\efi\microsoft\boot para a pasta "usb":\efi\boot</p>