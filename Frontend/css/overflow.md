# Свойства overflow, opacity, visibility и clip-path

## Что я узнал

CSS предоставляет несколько способов управлять видимостью и обрезкой элементов. Свойство `overflow` контролирует, что происходит с контентом, выходящим за границы блока: `visible` (по умолчанию), `hidden`, `scroll`, `auto` или `clip`. Свойство `opacity` управляет прозрачностью элемента от 0 (полностью прозрачный) до 1 (полностью видимый). Свойство `visibility` скрывает элемент, но сохраняет его место в макете. Для обрезки сложных форм используется `clip-path`, позволяющий создавать круги, эллипсы, полигоны и SVG-пути для масок элементов.

Применение этих свойств позволяет создавать интерактивные кнопки, стилизованные изображения и управлять видимостью элементов на странице без изменения структуры документа.

### Пример
```javascript
/* Контейнеры с разными overflow */
.box, .box2 {
  width: 100px;
  height: 100px;
  border: 2px solid indianred;
  overflow: clip;
  margin-bottom: 10px;
}
.box2 {
  overflow: hidden;
}

.box3 {
  width: 100px;
  height: 100px;
  border: 3px solid purple;
  overflow: visible clip; /* по оси X видимый, по оси Y обрезанный */
}

/* Прозрачность и видимость */
.box21, .box22, .box23 {
  margin-bottom: 5px;
  color: yellowgreen;
  background-color: darkblue;
  font-weight: 700;
}
.box22 {
  opacity: 0; /* полностью прозрачный */
}

.btn1 {
  height: 30px;
  padding-inline: 20px;
  color: pink;
  font: inherit;
  background-color: black;
  border: none;
  border-radius: 10px;
  visibility: visible; /* можно сделать hidden для скрытия */
}
.btn1:active {
  background-color: lemonchiffon;
  color: black;
}

/* Сложная обрезка изображений */
.img {
  width: 400px;
  clip-path: path('M253.1,6.7c-32.4-14.4-73.7,1.4-97.7,26.6c-24-25.2-65.3-41-97.7-26.6c-33.2,15.7-45.2,49-32.2,75.1c12.9,26.1,43.6,43.3,68.3,64.4c23.5,19.8,46.3,37.4,46.3,37.4s22.8-17.6,46.3-37.4c24.7-21.1,55.4-38.3,68.3-64.4c13-26.1,0.9-59.4-32.2-75.1z');
}

.img1 {
  width: 400px;
  clip-path: url(#shape); /* использование SVG-маски */
}
```

#### Связи

[[CSS Overflow]]
[[CSS Opacity]]
[[CSS Visibility]]
[[CSS Clip-path]]
[[Стилизация кнопок]]
[[Стилизация изображений]]
