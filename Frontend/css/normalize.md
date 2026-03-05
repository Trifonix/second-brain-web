# Normalize.css v8.0.1

## Что я узнал

**Normalize.css** — это современный CSS-файл для **нормализации стилей браузеров**, который сохраняет полезные дефолтные стили, устраняя при этом различия между браузерами. В отличие от CSS Reset, normalize не убирает все стили, а корректирует их для **более предсказуемого отображения**.

**Основные моменты:**
- **Документ и базовые стили:** корректировка `line-height` и `-webkit-text-size-adjust` для правильного масштабирования текста на iOS.
- **Секции и заголовки:** обнуление отступов `margin` для `body`, единое отображение блока `main`, исправление размера шрифтов заголовков `h1`.
- **Группировка контента:** `hr`, `pre`, `code`, `kbd`, `samp` получают корректные размеры и шрифты.
- **Текстовые элементы:** стили для ссылок `a`, аббревиатур `<abbr>`, тегов `<b>`, `<strong>`, `<small>`, `<sub>` и `<sup>`.
- **Встроенный контент:** `img` без границ, `audio` и `video` корректно отображаются.
- **Формы:** унификация стилей для `<button>`, `<input>`, `<textarea>`, `<select>`, включая устранение внутренних отступов и наследование шрифтов.
- **Интерактивные элементы:** `<details>` и `<summary>` получают корректное отображение.
- **Разное:** `<template>` и `[hidden]` корректно скрываются в поддерживаемых браузерах.

Использование normalize.css помогает **поддерживать кросс-браузерную совместимость**, сохраняя естественный вид элементов, и является отличной базой для последующей стилизации сайта.

### Пример
```javascript
/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */

html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
}

body {
  margin: 0;
}

main {
  display: block;
}

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible;
}

pre {
  font-family: monospace, monospace;
  font-size: 1em;
}

a {
  background-color: transparent;
}

abbr[title] {
  border-bottom: none;
  text-decoration: underline dotted;
}

b,
strong {
  font-weight: bolder;
}

code,
kbd,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}

small {
  font-size: 80%;
}

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub { bottom: -0.25em; }
sup { top: -0.5em; }

img {
  border-style: none;
}

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  line-height: 1.15;
  margin: 0;
}

button,
input {
  overflow: visible;
}

button,
select {
  text-transform: none;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring {
  outline: 1px dotted ButtonText;
}

fieldset { padding: 0.35em 0.75em 0.625em; }

legend {
  box-sizing: border-box;
  color: inherit;
  display: table;
  max-width: 100%;
  padding: 0;
  white-space: normal;
}

progress { vertical-align: baseline; }

textarea { overflow: auto; }

[type="checkbox"],
[type="radio"] { box-sizing: border-box; padding: 0; }

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button { height: auto; }

[type="search"] { -webkit-appearance: textfield; outline-offset: -2px; }

[type="search"]::-webkit-search-decoration { -webkit-appearance: none; }

::-webkit-file-upload-button {
  -webkit-appearance: button;
  font: inherit;
}

details { display: block; }
summary { display: list-item; }

template { display: none; }
[hidden] { display: none; }
```

#### Связи

[[normalize.css]]
[[CSS кросс-браузер]]
[[HTML базовые стили]]
[[CSS стандартизация]]
[[CSS reset vs normalize]]
