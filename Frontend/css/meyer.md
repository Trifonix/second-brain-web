# CSS Reset (Meyer Reset v2.0)

## Что я узнал

CSS Reset — это набор правил, который **сбрасывает стандартные стили браузера** для всех HTML-элементов. Разные браузеры применяют собственные стили по умолчанию к тегам, что может вызывать **непредсказуемое отображение** элементов. Reset помогает создать **однородную базу** для дальнейшей стилизации.

**Основные моменты:**
- Убираются **отступы (`margin`, `padding`)** и границы (`border`) у всех элементов.
- Шрифты и размер текста приводятся к базовым значениям (`font-size: 100%; font: inherit`).
- Блоки HTML5 (`article`, `section`, `nav` и др.) явно выставляются как `display: block`, чтобы корректно работали в старых браузерах.
- Списки (`ul`, `ol`) очищаются от маркеров (`list-style: none`).
- Цитаты (`blockquote`, `q`) очищаются от автоматических кавычек.
- Таблицы (`table`) сбрасывают `border-spacing` и включают `border-collapse: collapse`.

Использование CSS Reset помогает **избежать неожиданностей при кросс-браузерной разработке** и упростить дальнейшее создание дизайна сайта.

### Пример
```javascript
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
```

#### Связи

[[CSS Reset]]
[[Meyer Reset]]
[[Кросс-браузерная разработка]]
[[HTML базовые стили]]
[[Начальная стилизация]]
