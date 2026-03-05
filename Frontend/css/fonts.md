# Подключение шрифтов и управление текстом в CSS

## Что я узнал

В CSS можно подключать внешние шрифты через `@import` или `<link>` из Google Fonts или других источников. После подключения шрифта его можно применять через свойство `font-family` или использовать сокращённое свойство `font`, которое объединяет несколько параметров:  
- `font-style` (normal, italic)  
- `font-variant` (small-caps и др.)  
- `font-weight` (100–900)  
- `font-stretch` (normal, condensed, expanded)  
- `font-size/line-height` (например, `16px/1.6`)  
- `font-family` (название шрифта и fallback-список)

Также можно управлять размером текста через классы, например `.small-text` и `.big-text`.

### Пример
```javascript
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

/* body {
  font-family: Inter;
} */

body {
  font: 700 italic normal normal 16px/1.6 Inter, Arial, sans-serif;
  line-height: 1.2;
}

.small-text {
  font-size: 12px;
}

.big-text {
  font-size: 32px;
}
````

#### Связи

[[CSS Fonts]]
[[Google Fonts]]
[[Font Shorthand]]
[[Font Weight]]
[[Font Size]]
