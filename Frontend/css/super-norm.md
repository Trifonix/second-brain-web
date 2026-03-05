# Нормализация CSS и блочная модель

## Что я узнал

Для стабильного и предсказуемого отображения элементов на всех браузерах используют нормализацию CSS. Основные подходы включают:

- **box-sizing** – установка `border-box` для всех элементов и их псевдоэлементов упрощает расчёт ширины и высоты блоков.  
- **Удаление стандартных отступов и маркеров** – body, списки, заголовки и параграфы с атрибутом `class` сбрасываются до 0.  
- **Списки** – у ul[class] убираются маркеры через `list-style: none`.  
- **Изображения** – `display: block` и `max-width: 100%` предотвращают выход за пределы контейнера.  
- **Формы** – поля ввода наследуют шрифты от родителя через `font: inherit`.  
- **Вертикальное заполнение страницы** – html и body растягиваются на всю высоту (`height: 100%`, `min-height: 100%`) для удобного позиционирования футеров и блоков.  
- **Плавная прокрутка** – через `scroll-behavior: smooth`.  
- **Уменьшение анимаций для предпочтений пользователя** – медиа-запрос `prefers-reduced-motion: reduce` обнуляет анимации и переходы.  

Эти приёмы помогают сделать CSS более предсказуемым, особенно при разработке адаптивных и сложных интерфейсов.

### Пример
```javascript
/* Нормализация блочной модели */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Убираем отступы у списков с классом */
:where(ul, ol):where([class]) {
  padding-left: 0;
}

/* Сбрасываем внешние отступы body и блоков с классом */
body,
:where(blockquote, figure):where([class]) {
  margin: 0;
}

/* Убираем отступы у заголовков, параграфов и списков с классом */
:where(h1,h2,h3,h4,h5,h6,p,ul,ol,dl):where([class]) {
  margin-bottom: 0;
}

/* Убираем левый отступ у dd с классом */
:where(dd[class]) {
  margin-left: 0;
}

/* Убираем маркеры у ul с классом */
:where(ul[class]) {
  list-style: none;
}

/* Изображения адаптивные */
img {
  display: block;
  max-width: 100%;
}

/* Наследуем шрифты для форм */
input,
textarea,
select,
button {
  font: inherit;
}

/* Вертикальное заполнение страницы и плавный скролл */
html {
  height: 100%;
  scroll-behavior: smooth;
}

body {
  min-height: 100%;
  line-height: 1.5;
}

/* Минимизируем анимации для пользователей, предпочитающих reduced motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

#### Связи

[[CSS Reset]]
[[Box-sizing]]
[[Forms Styling]]
[[Responsive Images]]
[[Accessibility]]
[[Prefers Reduced Motion]]
