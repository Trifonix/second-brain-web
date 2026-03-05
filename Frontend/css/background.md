# Фоны и градиенты в CSS

## Что я узнал

CSS предоставляет мощные возможности для работы с фонами и градиентами. Можно комбинировать:
- Цвета (`background-color`) и изображения (`background-image`) в одном свойстве `background`.
- Управлять повторением изображений (`repeat`, `repeat-x`, `no-repeat`) и их позицией (`background-position`).
- Масштабировать изображения через `background-size` (`cover`, `contain`, фиксированные размеры).
- Контролировать область отображения изображения с помощью `background-clip`.
- Фиксировать фон относительно окна или контента с `background-attachment` (`fixed`, `local`).
- Использовать различные типы градиентов: линейные (`linear-gradient`), радиальные (`radial-gradient`), конические (`conic-gradient`) и их повторяющиеся варианты (`repeating-linear-gradient`, `repeating-radial-gradient`, `repeating-conic-gradient`).
- Применять градиенты к тексту через `background-clip: text` и `-webkit-background-clip: text`.

Эти методы позволяют создавать визуально выразительные блоки, баннеры и декоративные элементы без использования графических редакторов.

### Пример
```javascript
.box {
  width: 500px;
  height: 500px;
  background: lightcoral url('https://png.pngtree.com/png-clipart/20230511/ourmid/pngtree-isolated-cat-on-white-background-png-image_7094927.png') repeat-x 0 0/300px fixed padding-box;
}

.box2 {
  width: 600px;
  height: 600px;
  background-image: url('https://png.pngtree.com/png-clipart/20230511/ourmid/pngtree-isolated-cat-on-white-background-png-image_7094927.png');
}

.box3 {
  width: 500px;
  height: 500px;
  background-color: lightskyblue;
  background-image: 
    url('https://png.pngtree.com/png-clipart/20230511/ourmid/pngtree-isolated-cat-on-white-background-png-image_7094927.png'),
    url('https://t3.ftcdn.net/jpg/02/36/99/22/360_F_236992283_sNOxCVQeFLd5pdqaKGh8DRGMZy7P4XKm.jpg'),
    url('https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?s=612x612&w=0&k=20&c=6yvVxdufrNvkmc50nCLCd8OFGhoJd6vPTNotl90L-vo=');
}

.box4 {
  width: 1000px;
  height: 1060px;
  background-color: lightcyan;
  background-image: url('https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?s=612x612&w=0&k=20&c=6yvVxdufrNvkmc50nCLCd8OFGhoJd6vPTNotl90L-vo=');
  background-repeat: round;
}

.box5 {
  width: 500px;
  height: 500px;
  background-image: url('https://t3.ftcdn.net/jpg/02/36/99/22/360_F_236992283_sNOxCVQeFLd5pdqaKGh8DRGMZy7P4XKm.jpg');
  background-repeat: repeat-x;
  background-color: lightyellow;
}

.box9 {
  font-size: 2em;
  font-weight: 900;
  width: 500px;
  height: 500px;
  padding: 50px;
  color: transparent;
  border: 20px dashed salmon;
  background-image: url('https://ybis.ru/wp-content/uploads/2023/09/krasota-prirody-10.webp');
  background-position: center;
  background-size: cover;
  background-clip: text;
  -webkit-background-clip: text;
}

.box11 {
  background-image: linear-gradient(indianred, cornflowerblue);
}

.box12 {
  background-image: radial-gradient(slateblue, darkorange);
}

.box13 {
  background-image: conic-gradient(deepskyblue, lightpink);
}

.box14 {
  background-image: repeating-linear-gradient(
    indianred 0,
    indianred 10px,
    cornflowerblue 10px,
    cornflowerblue 20px
  );
}

.box15 {
  background-image: repeating-radial-gradient(
    slateblue 0,
    slateblue 10px,
    darkorange 10px,
    darkorange 20px
  );
}

.box16 {
  background-image: repeating-conic-gradient(
    deepskyblue 8deg 15deg,
    lightpink 15deg 30deg,
    deepskyblue 30deg 45deg
  );
}

.box17 {
  width: 500px;
  height: 500px;
  background-image: linear-gradient(0.75turn, indianred, cornflowerblue, palegreen);
}

.box18 {
  background-image: linear-gradient(to top, indianred, cornflowerblue);
}

.box19 {
  background-image: linear-gradient(to top right, indianred, cornflowerblue);
}

.box20 {
  background-image: linear-gradient(to right, indianred, cornflowerblue);
}

.box21 {
  background-image: linear-gradient(to right bottom, indianred, cornflowerblue);
}

.box22 {
  background-image: linear-gradient(to bottom, indianred, cornflowerblue);
}

.box23 {
  background-image: linear-gradient(to bottom left, indianred, cornflowerblue);
}

.box24 {
  background-image: linear-gradient(to left, indianred, cornflowerblue);
}

.box25 {
  background-image: linear-gradient(to left top, indianred, cornflowerblue);
}

.box26 {
  width: 400px;
  height: 400px;
  background-image: linear-gradient(
    indianred 30%,
    cornflowerblue 30% 50%,
    lightgreen 80%
  );
}
```

#### Связи

[[CSS Backgrounds]]
[[CSS Gradients]]
[[Linear Gradient]]
[[Radial Gradient]]
[[Conic Gradient]]
[[Background Images]]
[[Background Clip]]
