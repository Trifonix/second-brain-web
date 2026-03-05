# CSS Box Model и Display

## Что я узнал

В CSS **блочная модель и свойства отображения** (`display`) определяют, как элементы занимают пространство на странице и взаимодействуют с другими элементами. Понимание этих основ важно для верстки и управления размерами блоков.

**Основные моменты:**

- **Box Model** включает:
  - `width` и `height` — размеры контента.
  - `padding` — внутренние отступы между контентом и границей.
  - `border` — граница вокруг элемента.
  - `margin` — внешние отступы от других элементов.
  - `box-sizing` — определяет, включается ли `padding` и `border` в общую ширину и высоту (`border-box`) или нет (`content-box`).

- **Типы отображения (`display`)**:
  - `block` — элемент занимает всю ширину строки (`div` по умолчанию).
  - `inline` — элемент занимает только ширину содержимого (`span` по умолчанию), свойства `width` и `height` не применяются.
  - `inline-block` — комбинация: элементы расположены в одну линию, но `width` и `height` работают.
  - `none` — элемент скрыт, не занимает место на странице.

- **Примеры влияния `display` и box-model**:
  - Блочные элементы можно размерно настраивать (`width`, `height`).
  - Строчные элементы игнорируют `width` и `height`, но реагируют на `padding` и `border`.
  - `inline-block` позволяет задавать размеры и располагаться в линии с другими элементами.
  - Использование `box-sizing: border-box` облегчает контроль над общей шириной блока с учётом `padding` и `border`.

### Пример
```javascript
.box {
  width: 100px;
  height: 100px;
  margin: 20px;
  padding: 30px;
  border: 5px solid indianred;
}

.box2 {
  border: 5px solid goldenrod; /* display:block по умолчанию */
}

.box3 {
  width: 200px;
  border: 5px solid green;
}

span {
  border: 5px solid rebeccapurple;
  width: 200px; /* не работает с inline */
  height: 500px; /* не работает с inline */
}

.span2 {
  display: inline-block;
  width: 100px;
  height: 100px;
  border: 5px solid firebrick;
}

.box-1 { display: block; background-color: palevioletred; }
.box-2 { display: inline; background-color: darkturquoise; }
.box-3 { display: inline-block; background-color: tomato; }
.box-4 { display: none; }

.box5 {
  width: 200px;
  height: 200px;
  padding: 15px 40px;
  background-color: moccasin;
  border: 10px solid red;
}

.normal-size {
  box-sizing: border-box;
}
```

#### Связи

[[CSS Box Model]]
[[Display]]
[[Block vs Inline vs Inline-Block]]
[[Padding & Margin]]
[[box-sizing]]
