# CSS Grid и Layout

## Что я узнал

CSS Grid — это мощный инструмент для создания сложных макетов страниц с помощью сетки. С его помощью можно управлять как строками и колонками, так и позиционированием отдельных элементов внутри контейнера. Основные возможности:

- `display: grid` или `inline-grid` превращает контейнер в сетку.
- `grid-template-columns` и `grid-template-rows` задают размеры колонок и строк.
- `grid-auto-columns` и `grid-auto-rows` управляют автоматически создаваемыми треками.
- `gap`, `row-gap`, `column-gap` задают промежутки между элементами сетки.
- `grid-template-areas` позволяет именовать области сетки и позиционировать элементы по именам.
- Свойства `justify-content`, `align-items`, `place-items` управляют выравниванием элементов внутри сетки.
- Элементы сетки могут занимать несколько строк и колонок с помощью `grid-column` и `grid-row`.
- Можно комбинировать с `flex-grow`, `flex-shrink`, `minmax()` и `repeat()` для адаптивного дизайна.
- Grid позволяет создавать как простые каталоги и карточки, так и сложные макеты с меню, контентом и рекламой.

### Пример
```javascript
/* Основная структура страницы */
body {
  flex-direction: column;
  font-family: 'Arial', sans-serif;
}

.header { background-color: lightblue; }
.content {
  flex-grow: 1;
  display: grid;
  grid-template-columns: 25% auto;
  background-color: palegoldenrod;
}
.aside-menu { background-color: lawngreen; }
.catalog-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}
.catalog-item {
  list-style-type: none;
  background-color: burlywood;
  padding: 20px;
}
.footer { background-color: lightcoral; }

/* Простая сетка с равными колонками */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
.grid-element { min-height: 50px; background-color: lightslategray; color: whitesmoke; padding: 5px; }

/* Сетка с auto-flow и inline-grid */
.grid-container2, .inline-grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
.inline-grid-container { display: inline-grid; }
.grid-element2 { background-color: lightcoral; }

/* Гибкая настройка колонок с minmax и repeat */
.grid-container3 {
  display: grid;
  gap: 10px;
  grid-template-columns: minmax(200px, 35%) 1fr 50px;
}
.grid-element3 { background-color: lightsteelblue; }

/* Определение сетки с явными строками и авто-строками */
.grid-container4 {
  display: grid;
  gap: 10px;
  grid-template-columns: 100px auto;
  grid-template-rows: 40px 80px;
  grid-auto-rows: 42px 24px;
}
.grid-element4 { background-color: lightgoldenrodyellow; border: 1px solid; padding: 4px; }

/* Сетка с авто-колонками и flow по колонкам */
.grid-container5 {
  display: grid;
  gap: 10px;
  grid-template-columns: 30%;
  grid-auto-columns: 50px 100px;
  grid-auto-flow: column;
}
.grid-element5 { background-color: lightseagreen; }

/* Grid с именованными областями */
.content1 {
  min-height: 50vh;
  display: grid;
  grid-template-columns: 25% auto 15%;
  grid-template-areas: 
    "menu catalog advertisement"
    "menu catalog advertisement"
    "menu catalog ."
    "menu order order";
  gap: 50px;
}
.menu1 { grid-area: menu; background-color: lightskyblue; }
.catalog { grid-area: catalog; background-color: lightpink; }
.advertisement { grid-area: advertisement; background-color: palevioletred; }
.order { grid-area: order; background-color: cadetblue; }

/* Выравнивание и позиционирование элементов */
.grid-container6 {
  display: grid;
  gap: 10px;
  grid-template-columns: auto auto auto;
  grid-template-rows: repeat(5, 50px);
  border: 1px solid;
  place-items: center;
}
.grid-element6 { background-color: lightsalmon; }

/* Использование именованных линий и span */
.grid-container7 {
  display: grid;
  gap: 10px;
  grid-template-columns: [start] 1fr [middle-before] 1fr [middle-after] 1fr [end];
  grid-auto-rows: 50px;
  align-items: normal;
}
.grid-element7 { background-color: lightskyblue; }
.big { grid-column: span 2; grid-row: 1 / 3; }

/* Простая сетка с повторением и order */
.grid-container8 {
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(3, 1fr);
  align-items: normal;
}
.grid-element8 { background-color: plum; }
.wide { grid-column: -1 / 1; order: 1; }
```

#### Связи

[[CSS Grid]]
[[Layout]]
[[Responsive Design]]
[[Web Layout Patterns]]
[[Grid Areas]]
