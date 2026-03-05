# Единицы измерения и масштабирование в CSS

## Что я узнал

В CSS размеры элементов можно задавать с использованием различных единиц измерения, которые влияют на адаптивность и масштабирование:

- **Абсолютные единицы**: `px`, `mm`, `cm`, `in` – фиксированные значения, которые не зависят от контекста.
- **Относительные единицы**: `em`, `rem`, `%`, `vw`, `vh` – изменяются в зависимости от шрифта родителя, корня документа или размеров окна. Например, `1em` = размер шрифта родителя, `1rem` = размер шрифта корневого элемента.
- **Процентные значения** (`%`) – часто используют для ширины/высоты внутри контейнера, чтобы элементы адаптировались к размерам родителя.

Шрифты и размеры блоков тесно связаны: при использовании `em` или `rem` изменение размера шрифта родителя автоматически масштабирует дочерние элементы.  
Медиа-запросы (`@media`) позволяют менять базовый размер шрифта или других свойств для разных экранов, делая дизайн адаптивным.  
Фиксированные блоки, такие как меню (`position: fixed`) или баннеры, позволяют создавать элементы, которые остаются на месте при прокрутке, а сочетание абсолютных и процентных размеров помогает точно позиционировать и масштабировать элементы внутри контейнеров.

### Пример
```javascript
/* Блоки с разными единицами измерения */
.box-1 { background-color: lightskyblue; width: 50vw; height: 100px; }
.box-2 { background-color: lightpink; font-size: 30px; width: 15em; height: 100px; }
.box-3 { background-color: lightgreen; width: 200px; height: 100px; }
.box-4 { background-color: lightsalmon; width: 30mm; height: 50px; }

/* Использование процентов внутри родителя */
.wrapper { height: 200px; background-color: lightpink; }
.box41 { background-color: limegreen; height: 50%; margin-top: 400px; }

/* Абсолютное позиционирование и фиксированные блоки */
.box51 { background-color: lightskyblue; height: 50%; position: absolute; }
.menu { position: fixed; top: 0; right: 0; width: 30vw; height: 100vh; background-color: cornsilk; }

/* Шрифты и масштабирование */
h1 { font-size: 40px; }
h1 span { font-size: 0.5em; }
.box61 { font-size: 24px; width: 4em; height: 3em; background-color: lightpink; }

.small-font-size { font-size: 0.75rem; }
.base-font-size { font-size: 1.6rem; }
.big-font-size { font-size: 2.5rem; }
.h1 { font-size: 10rem; } /* 100px */

/* Медиа-запрос для адаптивности */
@media (max-width: 480px) {
  html { font-size: 5px; }
}

/* Сброс отступов и баннер */
* { margin: 0; padding: 0; }
.banner { 
  height: 100vh; 
  background: url("https://png.pngtree.com/png-clipart/20220125/ourmid/pngtree-leaves-spring-green-decorative-border-png-image_4364434.png") center/cover no-repeat;
}
```

#### Связи

[[CSS Units]]
[[Responsive Design]]
[[Viewport]]
[[EM and REM]]
[[Fixed Elements]]
[[Absolute Positioning]]
[[Media Queries]]
[[Banner Backgrounds]]
