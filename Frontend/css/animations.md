# CSS Анимации: @keyframes и animation

## Что я узнал

CSS-анимации позволяют изменять свойства элементов со временем без использования JavaScript. Основой таких анимаций является правило `@keyframes`, которое описывает ключевые этапы изменения свойств элемента.

Внутри `@keyframes` задаются промежуточные состояния анимации в процентах (`0%`, `50%`, `100%`) или с помощью ключевых слов `from` и `to`. Браузер автоматически интерполирует значения между этими точками.

Свойство `animation` управляет запуском анимации и может быть записано краткой формой или через отдельные свойства:

- `animation-name` — имя анимации из `@keyframes`
- `animation-duration` — длительность анимации
- `animation-delay` — задержка перед стартом
- `animation-iteration-count` — количество повторений
- `animation-direction` — направление воспроизведения
- `animation-timing-function` — скорость изменения анимации
- `animation-play-state` — состояние анимации (играет или остановлена)

Например, `animation-direction: alternate-reverse` означает, что анимация будет чередовать направление и начинать воспроизведение с обратной стороны.

Скорость анимации можно контролировать через `animation-timing-function`. Популярные варианты:

- `ease` — плавное начало и конец (по умолчанию)
- `ease-in` — медленный старт
- `ease-out` — плавное завершение
- `ease-in-out` — плавный старт и конец
- `linear` — равномерная скорость
- `cubic-bezier()` — пользовательская кривая ускорения

Анимацию можно ставить на паузу через `animation-play-state`. Например, при наведении курсора можно остановить движение элемента.

### Пример
```javascript
@keyframes move-to-right {
  50% {
    rotate: 45deg;
  }
  100% {
    translate: 75vw;
  }
}

@keyframes move-to-right2 {
  0% {
    translate: 0;
  }
  100% {
    translate: 100vw;
  }
}

.box {
  width: 100px;
  height: 100px;
  border: 2px solid black;

  animation-name: move-to-right;
  animation-duration: 1000ms;
  animation-delay: 0.5s;
  animation-iteration-count: 6;
  animation-direction: alternate-reverse;
}

.box1 {
  width: 50px;
  height: 50px;
  background-color: lightskyblue;

  translate: -100%;
  animation-name: move-to-right2;
  animation-duration: 5s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

.ease-in {
  animation-timing-function: ease-in;
}

.ease-out {
  animation-timing-function: ease-out;
}

.ease-in-out {
  animation-timing-function: ease-in-out;
}

.linear {
  animation-timing-function: linear;
}

.cubic-bezier {
  animation-timing-function: cubic-bezier(0.1, 0.7, 0.165, 1);
}

.line:hover .box1 {
  animation-play-state: paused;
}
```

#### Связи

[[CSS]]
[[CSS Анимации]]
