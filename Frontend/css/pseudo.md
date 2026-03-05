# CSS Псевдоэлементы и псевдоклассы

## Что я узнал

Псевдоэлементы (`::before`, `::after`, `::first-letter`, `::first-line`, `::selection`, `::marker`, `::file-selector-button`) и псевдоклассы позволяют добавлять стиль и контент к элементам без изменения HTML. Они полезны для декоративных эффектов, выделения текста, кастомизации форм и интерактивных элементов. Основные моменты:

- `::before` и `::after` вставляют контент до или после содержимого элемента.
- `::first-letter` и `::first-line` позволяют стилизовать первую букву или первую строку текста.
- `::selection` задает стиль текста при выделении пользователем.
- `::marker` управляет маркерами списков.
- `::placeholder` позволяет стилизовать текст подсказки в полях ввода.
- `::file-selector-button` настраивает кнопку выбора файла.
- `attr()` позволяет вставлять значение атрибута в контент псевдоэлемента.
- Псевдоэлементы могут быть объединены с декоративными эффектами, например тенями, фоном, границами и даже изображениями.

Использование этих инструментов упрощает создание визуально интересных и интерактивных элементов без лишнего HTML.

### Пример
```javascript
/* Добавление символов до и после элемента */
.with-before::before {
  content: "(-:";
  color: cornflowerblue;
}
.with-after::after {
  content: ":-)";
  color: green;
}

/* Стилизация плейсхолдера и кнопки выбора файла */
.with-red-placeholder::placeholder { color: red; }
.with-file-selector-button::file-selector-button {
  background-color: lawngreen;
  font-weight: 700;
  border: 2px solid darkblue;
}

/* Первая буква и первая строка */
.with-first-letter::first-letter { font-size: 3em; }
.with-first-line::first-line { text-decoration: underline; }

/* Стили выделенного текста */
.with-selection::selection { background-color: pink; }

/* Маркеры списков */
#marked::marker { color: gold; }
.red-marker::marker { color: red; }
.smile-marker::marker { content: "😂 "; }

/* Кастомные кнопки */
.with-custom-file-button::file-selector-button {
  height: 32px;
  padding-inline: 12px;
  color: teal;
  background-color: goldenrod;
  border: 3px dashed #132954;
  border-radius: 10px;
}

/* Декоративные эффекты первой буквы и строки */
.special-first-letter::first-letter {
  margin-right: 15px;
  padding: 12px 24px;
  font-size: 3em;
  color: indianred;
  background-color: skyblue;
  border: 3px solid cadetblue;
  border-radius: 10px;
  box-shadow: 0 0 10px 0 rgb(0 0 0 / 0.75);
}
.special-first-line::first-line {
  text-transform: uppercase;
  color: indianred;
  background-color: skyblue;
  box-shadow: 0 0 10px 0 rgb(0 0 0 / 0.75);
}

/* Выделение текста с эффектами */
.custom-selection::selection {
  color: whitesmoke;
  background-color: coral;
  text-shadow: 2px 2px 2px black;
  text-decoration: underline;
}

/* Эмодзи и декоративные псевдоэлементы */
.emoji-pseudo::before { content: "👉"; }
.emoji-pseudo::after { content: "👈"; }

/* Псевдоэлементы с позиционированием */
.gray-box-pseudo {
  position: relative;
  width: 100px;
  height: 100px;
  background-color: lightskyblue;
}
.gray-box-pseudo::after {
  content: "";
  position: absolute;
  left: 90%;
  top: 10px;
  width: 100%;
  height: 100%;
  background-color: greenyellow;
}

/* Псевдоэлемент с изображением */
.image-pseudo::after {
  content: url('https://images.stockcake.com/public/6/0/f/60f007a6-743e-4fe4-9b64-7765295c43b0_medium/playful-kitten-playing-stockcake.jpg');
}

/* Вставка атрибута в контент */
.attr-pseudo::after { content: attr(data-example); color: red; }

/* Цитата через псевдоэлемент */
.quote-pseudo::before { content: open-quote; }
```

#### Связи

[[CSS Pseudo-elements]]
[[CSS Pseudo-classes]]
[[Decorative CSS]]
[[Form Styling]]
[[Text Effects]]
