# CSS Padding и Margin

## Что я узнал

В CSS **padding** и **margin** управляют внутренними и внешними отступами элементов:

- **Padding** — внутренний отступ между содержимым элемента и его границей. Можно задавать отдельные стороны:
  - `padding-top`, `padding-right`, `padding-bottom`, `padding-left`
  - `padding-block` (верх/низ), `padding-inline` (лево/право в зависимости от направления текста)

- **Margin** — внешний отступ между элементом и соседними элементами. Аналогично можно использовать:
  - `margin-top`, `margin-right`, `margin-bottom`, `margin-left`
  - Короткая запись: `margin: 10px 20px 30px 40px;` (top, right, bottom, left)
  - `margin-inline` и `margin-block` для логических направлений

- Центрирование блоков возможно через `margin-inline: auto` для горизонтального выравнивания.

- Отрицательные значения margin позволяют «сдвигать» элементы за пределы их обычного положения.

Использование этих свойств важно для контроля пространства между элементами, создания визуальных блоков и компоновки макета страницы.

### Пример
```javascript
div {
  width: 200px;
  height: 200px;
}

.box-1 {
  padding: 30px;
  background-color: palevioletred;
  margin: 30px;
}

.box-2 {
  padding: 10px 50px;
  background-color: sandybrown;
  margin: 10px 50px;
}

.box-3 {
  margin: 50px 100px 150px;
  background-color: lightseagreen;
}

.box-4 {
  margin: 50px 100px 150px 200px;
  background-color: blueviolet;
}

.box-5 { padding-top: 60px; background-color: forestgreen; }
.box-6 { padding-right: 60px; background-color: cornflowerblue; }
.box-7 { padding-bottom: 60px; background-color: bisque; }
.box-8 { padding-left: 60px; background-color: darkcyan; }
.box-9 { padding-block: 100px; background-color: grey; }
.box-10 { padding-inline: 100px; background-color: darkolivegreen; }

body { font-family: Arial, Helvetica, sans-serif; }

.bordered-wrapper { width: 300px; border: 2px dashed black; }
.box { width: 200px; height: 200px; margin-inline: auto; background-color: seagreen; }

.box-11 { width: 200px; height: 200px; background-color: palevioletred; }
.box-12 { width: 150px; height: 150px; margin-top: -50px; background-color: sandybrown; }

.box-21 { margin-bottom: 50px; background-color: coral; }
.box-22 { margin-top: 100px; background-color: lightblue; }

.box31 { margin-bottom: 100px; padding: 50px; background-color: coral; }
.box32 { background-color: purple; color: white; }
```

#### Связи

[[CSS Padding]]
[[CSS Margin]]
[[Margin-Top-Bottom-Left-Right]]
[[Padding-Top-Bottom-Left-Right]]
[[Margin-Auto]]
[[Box Model]]
