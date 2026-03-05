# Бордеры, радиусы и тени в CSS

## Что я узнал

CSS позволяет детально управлять внешним видом блоков через свойства границ (border), радиусов углов (border-radius), контуров (outline) и теней (box-shadow).  

- **Границы (border)**: можно задавать одновременно ширину, стиль и цвет через `border`, либо отдельно через `border-width`, `border-style` и `border-color`.  
- **Стороны и направления**: используются `border-top`, `border-right`, `border-bottom`, `border-left`, а также логические свойства `border-block` и `border-inline`.  
- **Контур (outline)**: похож на border, но не влияет на размеры элемента. Можно контролировать ширину, стиль, цвет и смещение (`outline-offset`).  
- **Скругление углов (border-radius)**: поддерживает простые значения для всех углов или сложные через слэши для эллиптической формы.  
- **Box-sizing**: `border-box` учитывает границы и padding в размерах элемента.  
- **Тени и фильтры**: `box-shadow` позволяет создавать внутренние (`inset`) и внешние тени, а `filter` — применять визуальные эффекты к изображениям, включая sepia, drop-shadow, blur и др.  

Эти свойства дают большой контроль над визуальной композицией элементов на странице.

### Пример
```javascript
.box1 {
  width: 100px;
  height: 100px;
  background-color: lightpink;
  border-inline: 20px solid deepskyblue;
}

.box2 {
  width: 120px;
  height: 120px;
  background-color: salmon;
  border-style: solid;
  border-color: deepskyblue;
  border-width: 16px 8px 42px 30px;
}

.box3 {
  width: 80px;
  height: 80px;
  background-color: lightgreen;
  border-width: 6px;
  border-color: dimgray;
  border-style: outset;
}

.box4 {
  width: 160px;
  height: 160px;
  background-color: lightsalmon;
  border-width: 6px;
  border-color: brown;
  border-block-style: outset;
  border-inline-style: groove;
}

.box5 {
  width: 100px;
  height: 200px;
  background-color: whitesmoke;
  border-width: 10px;
  border-style: solid;
  border-color: deepskyblue tomato slateblue cadetblue;
}

.box6 {
  width: 100px;
  height: 100px;
  background-color: pink;
  border-width: 10px;
  border-style: solid;
  border-block-color: red;
  border-inline-color: blue;
}

.box7 {
  width: 120px;
  height: 140px;
  background-color: grey;
  border: 10px solid magenta;
  box-sizing: border-box;
}

.box8 {
  width: 120px;
  height: 100px;
  background-color: darkred;
  border: 10px solid deepskyblue;
  outline: 5px solid goldenrod;
}

.box9 {
  width: 100px;
  height: 100px;
  background-color: lightpink;
  border: 10px solid deepskyblue;
  outline: 5px solid gold;
  outline-offset: -25px;
}

.box10 {
  width: 120px;
  height: 120px;
  background-color: lightpink;
  border-radius: 15px;
}

.box11 {
  width: 100px;
  height: 100px;
  background-color: cornflowerblue;
  border-radius: 0 30px 80% 30px;
}

.box12 {
  width: 120px;
  height: 120px;
  background-color: crimson;
  border-radius: 60% 20% / 10% 50%;
}

.box13 {
  width: 100px;
  height: 100px;
  background-color: lightseagreen;
  outline: 5px solid deeppink;
  border-radius: 15px;
}

.box14 {
  margin-left: 20px;
  margin-bottom: 20px;
  width: 120px;
  height: 120px;
  background-color: lawngreen;
  box-shadow: -5px 10px 5px -5px rgb(0 0 255 / 0.5) inset, 5px 5px 5px red;
}

body {
  background-color: lightyellow;
}

img {
  filter: sepia(0.8) drop-shadow(15px 15px 15px rgb(60, 30, 233));
}
```

#### Связи

[[CSS Borders]]
[[Border-radius]]
[[Box-shadow]]
[[Outline]]
[[CSS Filters]]
[[Box-sizing]]
