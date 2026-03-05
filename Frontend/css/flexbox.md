# Flexbox в CSS: основы и свойства

## Что я узнал

Flexbox — это современный способ управления расположением элементов в контейнере. Он позволяет легко выравнивать, упорядочивать и масштабировать блоки как по основной оси, так и по поперечной. Основные моменты:

- **Контейнеры и элементы**: задаем `display: flex` или `display: inline-flex` для родителя, а дочерние элементы становятся flex-элементами.
- **Направление**: `flex-direction` определяет основную ось (`row`, `row-reverse`, `column`, `column-reverse`).
- **Перенос**: `flex-wrap` управляет переносом элементов (`nowrap`, `wrap`, `wrap-reverse`).
- **Рост и сжатие**: `flex-grow`, `flex-shrink`, `flex-basis` позволяют элементам изменять размеры пропорционально.
- **Порядок элементов**: свойство `order` изменяет визуальное расположение без изменения HTML.
- **Выравнивание**: `justify-content` управляет расположением вдоль основной оси, `align-items` — вдоль поперечной оси, `align-content` — для нескольких строк.
- **Промежутки**: `gap`, `row-gap`, `column-gap` создают пространство между элементами без использования маргинов.
- **Комбинации**: `flex-flow` объединяет направление и перенос.

Flexbox упрощает создание адаптивных макетов, особенно когда элементы должны масштабироваться или располагаться в разных направлениях без сложных вычислений.

### Пример
```javascript
/* Основной контейнер и элементы */
.flex-container {
  display: flex;
  column-gap: 10px;
  padding: 10px;
  background-color: lightskyblue;
}
.flex-element {
  background-color: lightgreen;
  padding: 10px;
}

/* Направление и порядок */
.flex-row-reverse { flex-direction: row-reverse; }
.flex-column { flex-direction: column; }
.flex-column-reverse { flex-direction: column-reverse; }
.order-first { order: -1; }
.order-last { order: 1; }

/* Перенос элементов */
.flex-wrap { flex-wrap: wrap; }
.flex-wrap-reverse { flex-wrap: wrap-reverse; }

/* Рост и сжатие элементов */
.wide { flex-grow: 1; }
.real-size { flex-shrink: 0; }
.flex-element6 { flex-basis: 100px; }
.fixed-sizes { flex: 0 0 50%; }

/* Выравнивание и распределение */
.justify-content-flex-start { justify-content: flex-start; }
.justify-content-center { justify-content: center; }
.justify-content-space-between { justify-content: space-between; }
.align-items-center { align-items: center; }
.align-content-space-around { align-content: space-around; }

/* Промежутки между элементами */
.gap-50 { gap: 50px 50px; }
.column-gap-50 { column-gap: 50px; }
.row-gap-50 { row-gap: 50px; }
```

#### Связи

[[CSS Layout]]
[[Flexbox]]
[[Align Items]]
[[Justify Content]]
[[Flex Wrap]]
[[Flex Grow and Shrink]]
[[Responsive Design]]
[[Gap Property]]
