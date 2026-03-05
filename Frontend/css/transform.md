# CSS Transform и Transition

## Что я узнал

Свойство `transform` позволяет изменять положение, размер и форму элементов без влияния на поток документа. С его помощью можно перемещать (`translate`), масштабировать (`scale`), вращать (`rotate`) и искажать (`skew`) элементы. Трансформации могут комбинироваться в одной строке и применяться последовательно. Также существуют отдельные свойства `translate`, `scale` и `rotate`, которые позволяют задавать трансформации более декларативно.

Свойство `transform-origin` определяет точку, относительно которой происходит трансформация элемента. По умолчанию это центр (`50% 50%`), но его можно изменить, например, на верхний левый угол (`0 0`).

Для создания анимационных эффектов используется свойство `transition`. Оно задаёт плавный переход между состояниями элемента при изменении CSS-свойств. Можно указать длительность анимации, задержку (`delay`) и функцию времени (`timing-function`), которая определяет скорость изменения. Среди популярных функций: `ease`, `ease-in`, `ease-out`, `ease-in-out`, `linear`, а также кастомные кривые `cubic-bezier()`.

Трансформации и transitions широко применяются для интерактивных интерфейсов, hover-эффектов, анимации кнопок, карточек и прогресс-баров.

### Пример
```javascript
.box-1, .box-2 {
  width: 100px;
  height: 100px;
  background-color: lightskyblue;
  border: 5px solid indianred;
  box-shadow: 4px -2px 12px 4px rgb(0 0 0 / 0.5);
}

.box-2 {
  transform: translate(30px, -30px) scale(1.5) skew(20deg, 5deg);
}

.box-3, .box-4 {
  width: 150px;
  height: 150px;
  background-color: lightgreen;
  border: 5px solid brown;
  padding: 10px;
  box-shadow: 4px -2px 12px 4px rgb(0 0 0 / 0.5);
}

.box-4 {
  translate: 30px;
  scale: 0.5;
  rotate: 135deg;
}

.box5 {
  width: 100px;
  height: 100px;
  background-color: salmon;
  border: 5px dotted purple;
}

.inner {
  width: 75px;
  height: 75px;
  background-color: palegreen;
  rotate: 30deg;
  transform-origin: 0 0;
}

.box6 {
  width: 50px;
  height: 50px;
  background-color: lightskyblue;
  border: 2px solid indianred;
  transition: 1s 2s;
}

.scale-on-hover:hover .box6 {
  scale: 2;
}

.rotate-on-hover:hover .box6 {
  rotate: 45deg;
}

.box7 {
  width: 100%;
  height: 50px;
  display: inline-block;
  border: 5px solid sandybrown;
}

.inner1 {
  width: 0;
  height: 100%;
  transition: 1s ease;
  background-color: aquamarine;
}

body:hover .inner1 {
  width: 100%;
}

.ease-in {
  transition-timing-function: ease-in;
}

.ease-out {
  transition-timing-function: ease-out;
}

.ease-in-out {
  transition-timing-function: ease-in-out;
}

.linear {
  transition-timing-function: linear;
}

.cubic-bezier {
  transition-timing-function:
    cubic-bezier(0.1, 0.7, 1.0, 0.1)
}
```

#### Связи

[[CSS Transform]]
[[CSS Transition]]
[[CSS Transform-origin]]
[[CSS Timing Functions]]
[[CSS Hover эффекты]]
