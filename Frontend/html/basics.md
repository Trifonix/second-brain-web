# Базовые HTML теги: заголовки, ссылки и форматирование текста

## Что я узнал

HTML предоставляет множество базовых тегов для структуры страницы, навигации и форматирования текста. Эти элементы являются фундаментом любой веб-страницы.

Комментарии в HTML создаются с помощью `<!-- комментарий -->`. Они не отображаются на странице и используются для пояснений внутри кода.

Заголовки создаются с помощью тегов `<h1>`–`<h6>`. `<h1>` — самый важный и крупный заголовок, а `<h6>` — самый маленький. Они помогают структурировать документ и важны для SEO и доступности.

Тег `<hr>` создаёт горизонтальную линию, которая используется для визуального разделения разделов страницы.  
Тег `<br>` добавляет перенос строки.

Параграфы создаются с помощью `<p>`. Это основной способ размещения текстовых блоков на странице.

Тег `<a>` используется для создания ссылок. Атрибут `href` указывает адрес страницы. Атрибут `target` определяет, где откроется ссылка:
- `_blank` — открывает страницу в новой вкладке
- `_self` — открывает ссылку в текущей вкладке

Атрибут `title` показывает всплывающую подсказку при наведении курсора на ссылку.

Ссылки могут вести как на внешние сайты (например Google), так и на другие страницы внутри проекта (например `page2.html`, `forms.html` и т.д.).

HTML также содержит теги для **форматирования текста**:
- `<b>` — жирный текст
- `<i>` — курсив
- `<big>` — увеличенный текст
- `<small>` — уменьшенный текст
- `<sub>` — нижний индекс
- `<sup>` — верхний индекс
- `<ins>` — вставленный текст (обычно подчёркнутый)
- `<del>` — удалённый текст (перечёркнутый)
- `<mark>` — выделенный текст

Эти теги помогают визуально подчеркнуть важные части текста и улучшить читаемость контента.

### Пример
```javascript
<!--This is the best website ever-->
<h1>I like pizza</h1>
<hr>
<h2>I like pizza</h2>
<h3>I like pizza</h3>
<h4>I like pizza</h4>
<h5>I like pizza</h5>
<h6>I like pizza</h6>

<br>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint tempora obcaecati at qui eaque tempore culpa, dolorum possimus facere perspiciatis distinctio quos nulla repudiandae id sunt temporibus molestias rerum porro?</p>
<p>Lorem ipsum dolor sit amet consectetur.</p>

<a href="https://google.com" target=_blank>GOOGLE</a>
<a href="https://google.com" target=_self title="This takes you to google">GOOGLE</a>

<a href="page2.html">Go to page 2</a><br>
<a href="lists.html">Go to page lists.html</a><br>
<a href="table.html">Go to page table.html</a><br>
<a href="colors.html">Go to page colors.html</a><br>
<a href="span-div.html">Go to page span-div.html</a><br>
<a href="metadata.html">Go to page metadata.html</a><br>
<a href="iframes.html">Go to page iframes.html</a><br>
<a href="buttons.html">Go to page buttons.html</a><br>
<a href="forms.html">Go to page forms.html</a><br>

<!--html text formatting tags-->
<p>This is normal text</p>
<p>This is <b>bold</b> text</p>
<p>This is <i>italic</i> text</p>
<p>This is <big>big</big> text</p>
<p>This is <small>small</small> text</p>
<p>This is <sub>subscript</sub> text</p>
<p>This is <sup>superscript</sup> text</p>
<p>This is <ins>inserted</ins> text</p>
<p>This is <del>deleted</del> text</p>
<p>This is <mark>marked</mark> text</p>
```

#### Связи

[[HTML]]
[[HTML заголовки]]
[[HTML ссылки]]
[[Форматирование текста HTML]]
[[Основы веб-разработки]]
