# Позиционирование элементов и управление слоями

## Что я узнал

В CSS для управления положением элементов на странице используются свойства `position` и `z-index`. Основные типы позиционирования:

- **static** – значение по умолчанию, элемент располагается в потоке документа, свойства `top`, `left`, `z-index` игнорируются.  
- **relative** – элемент остаётся в потоке, но его можно сдвигать относительно исходного положения с помощью `top`, `left`, `bottom`, `right`.  
- **absolute** – элемент удаляется из потока и позиционируется относительно ближайшего предка с `position` отличным от `static`.  
- **fixed** – элемент фиксируется относительно окна просмотра и не двигается при прокрутке.  
- **sticky** – комбинирует поведение `relative` и `fixed`; элемент остаётся в потоке, но «прилипает» к указанной позиции при прокрутке.

Свойство **z-index** задаёт порядок наложения слоёв. Элементы с большим значением отображаются выше. Для удобства часто используют CSS-переменные (`--layer-tooltip`, `--layer-menu`, `--layer-modal`), которые упрощают управление слоями.  

Также важно понимать взаимодействие блочных и строчных элементов в контейнерах (`flex`, `grid`) и использование `inset` для абсолютного позиционирования внутри родителя. Для модальных окон и tooltip-элементов применяется комбинация `position` и `z-index` для корректного отображения поверх других элементов.  

### Пример
```javascript
/* Пример диалогового окна с backdrop и кнопкой закрытия */
dialog {
  position: fixed;
  margin: auto;
  padding: 50px;
}
dialog::backdrop {
  background-color: rgb(0 0 0 / 0.5);
}
dialog button {
  position: absolute;
  top: 10px;
  right: 10px;
}

/* Контейнер с различными позициями блоков */
.wrap {
  height: 800px;
  position: relative;
}

.box1 { background-color: cornflowerblue; position: static; }
.box2 { background-color: lightpink; position: relative; top: 50px; left: 100px; }
.box3 { background-color: palegreen; position: absolute; top: 100px; left: 250px; z-index: 100; }
.box5 { background-color: goldenrod; position: sticky; top: 0; left: 20px; }

/* Пример абсолютного элемента внутри родителя */
.wrap2 .inner {
  background-color: gold;
  position: absolute;
  bottom: 0;
  left: 0;
}

/* Управление слоями через переменные */
:root {
  --layer-tooltip: 100;
  --layer-menu: 200;
  --layer-modal: 300;
  --layer-admin-panel: 1000;
}
.tooltip {
  z-index: var(--layer-tooltip);
}
.between-tooltip-and-menu {
  z-index: calc((var(--layer-modal) + var(--layer-menu)) / 2);
}

/* Пример комбинированного flex и grid */
main { display: flex; column-gap: 20px; }
section { width: 100%; }
.grid { display: grid; }
.grid > div { width: 150px; height: 150px; }
```

#### Связи

[[CSS Position]]
[[Z-index]]
[[Flexbox]]
[[Grid Layout]]
[[Modal Windows]]
[[Tooltip]]
[[Sticky Elements]]
