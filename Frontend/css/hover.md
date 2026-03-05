# CSS Псевдоклассы и состояния элементов

## Что я узнал

CSS псевдоклассы позволяют выбирать элементы по их состоянию, порядку или атрибутам без добавления дополнительных классов в HTML. Они широко применяются для стилизации списков, текста, форм, кнопок и интерактивных элементов. Основные моменты:

- `:nth-child()` и `:nth-last-child()` дают возможность выбирать элементы по их порядковому номеру.
- `:first-child`, `:last-child`, `:only-child` позволяют стилизовать элементы, основываясь на их позиции внутри родителя.
- `:not()` используется для исключения определенных элементов из выбора.
- `:hover`, `:focus`, `:focus-visible`, `:active` применяются для интерактивных эффектов при наведении, фокусе или клике.
- `:disabled`, `:checked` дают доступ к состоянию форм и элементов управления.
- `visually-hidden` и похожие техники используются для скрытия элементов визуально, но оставляя их доступными для скринридеров.
- Сочетание псевдоклассов и CSS-свойств позволяет создавать эффекты, такие как подсветка, тени, изменение фона, рамок и текста без JS.

### Пример
```javascript
/* Селекторы по порядку */
li:nth-child(2) { color: red; }
p:first-child { color: red; }
p:last-child { color: blue; }
p:nth-child(odd) { color: green; }
p:nth-child(even) { color: yellow; background-color: black; }
p:nth-child(4) { color: whitesmoke; }
p:nth-last-child(2) { text-decoration: underline; }
p:nth-child(3n) { font-size: 22px; }
p:nth-child(3n + 5) { font-style: italic; }
p:nth-child(-n + 4) { border: 1px dotted; }
p:nth-last-child(-n + 4) { border: 2px dashed; }

/* Исключения и уникальные элементы */
li:only-child { background-color: brown; color: whitesmoke; }
li:not(:last-child) { margin-bottom: 10px; }

/* Состояние модального окна и тултипа */
.modal:not(.is-active) { display: none; }
.tooltip:not(.is-active) { display: none; }

/* Состояния кнопок */
button {
  background-color: whitesmoke;
  padding: 20px;
  border-radius: 10px;
  font-weight: 700;
}
.hover-effect:hover { background-color: pink; }
.focus-effect:focus { box-shadow: 0 0 10px 10px rgb(255 0 0 / 0.5); }
.focus-visible-effect:focus-visible { box-shadow: 0 0 10px 10px rgb(0 255 0 / 0.5); }
.active-effect:active { color: indigo; background-color: yellow; }
button:disabled { color: red; }

/* Состояние чекбоксов и input */
input:checked { box-shadow: 0 0 0 4px gold; }

/* Визуально скрытые элементы */
.visually-hidden {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  margin: -1px !important;
  border: 0 !important;
  padding: 0 !important;
  white-space: nowrap !important;
  clip-path: inset(100%) !important;
  clip: rect(0 0 0 0) !important;
  overflow: hidden !important;
}

/* Кастомные чекбоксы */
.checkbox {
  display: flex;
  column-gap: 0.5em;
  user-select: none;
}
.checkbox-control:not(:checked) + .checkbox-emulator::after { display: none; }
.checkbox-emulator {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 1em;
  height: 1em;
  border: 2px solid lightskyblue;
  border-radius: 5px;
  background-color: paleturquoise;
}
.checkbox-emulator::after {
  content: "✔";
  color: green;
}
```

#### Связи

[[CSS Pseudo-classes]]
[[CSS Forms]]
[[Interactive UI]]
[[Accessibility]]
[[Lists Styling]]
