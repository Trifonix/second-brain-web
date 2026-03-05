# CSS Селекторы и приоритеты стилей

## Что я узнал

CSS предоставляет огромное количество способов **направленно стилизовать элементы** на странице — через теги, классы, идентификаторы, атрибуты и комбинированные селекторы. Разные селекторы имеют **разный приоритет (specificity)**, который определяет, какой стиль будет применён при конфликте.  

**Основные моменты:**
- **Селекторы по тегу** (`p`, `a`, `li`) задают базовые стили для всех элементов этого типа.
- **Классы** (`.my-super-text`, `.big`, `.blue`) позволяют применять стили к группе элементов, независимо от их места в DOM.
- **Идентификаторы** (`#my-first-unique-text`) имеют более высокий приоритет и перекрывают стили классов и тегов.
- **Атрибутные селекторы** (`[type="number"]`, `[href*="hh.ru"]`) позволяют применять стили к элементам с конкретными атрибутами или их значениями.
- **Комбинированные селекторы** (`section > h2`, `section p span`) задают стили элементам на основе их иерархии или соседства.
- **Псевдоклассы и порядок**: соседние элементы (`h2 + p`), потомки (`section p`), универсальный селектор `*`.
- **!important и inline** (не показаны в этом примере, но важно знать) — повышают приоритет стилей.  
- **Ошибки:** не рекомендуется перебивать универсальный селектор `*` для шрифтов несколько раз; правильная практика — один общий базовый стиль.

Использование этих методов позволяет **точно контролировать внешний вид страницы**, создавать визуальные эффекты для ссылок, кнопок, сообщений об ошибках, и управлять стилями динамических элементов.

### Пример
```javascript
/* Стили для текста и элементов */
p { color: red; }
a { color: peru; }
li { color: purple; }
.my-super-text { color: gold; font-size: 22px; }
.not-super-text { color: grey; }
.big { font-size: 24px; }
.small { font-size: 10px; }
.red { color: indianred; }
.blue { color: deepskyblue; }
.bold { font-weight: 700; }
.thin { font-weight: 100; }
#my-first-unique-text { color: indianred; }
#my-second-unique-text { color: seagreen; }
#my-third-unique-text { color: deepskyblue; }

/* Селекторы по атрибутам */
[placeholder] { border: 3px solid darkturquoise; }
[type="number"] { box-shadow: 3px 3px 3px 3px indianred; }
[type="tel"] { box-shadow: 3px 3px 3px 3px #5c7ccd; }
[type=email] { box-shadow: 3px 3px 3px 3px #7bf178; }
[href*="hh.ru"] { padding-left: 1.2em; background: url(https://upload.wikimedia.org/wikipedia/commons/7/79/HeadHunter_logo.png) 0 50%/1em no-repeat; }
[href*="habr.ru"] { padding-left: 1.2em; background: url(https://habrastorage.org/storage2/ebf/ded/334/ebfded3341c46c05625c8990cb4c5e8e.png) 0 50%/1em no-repeat; }
[href^="http://"] { color: red; }
[href^="https://"] { color: green; }

/* Комбинированные селекторы и псевдоклассы */
section p { color: seagreen; }
section p span { color: darkred; }
section > h2 { color: rgb(32, 255, 3); }
h2 + p { background-color: rgb(14, 14, 5); color: khaki; }

/* Стили для кнопок и активных состояний */
.button { background-color: lightgray; }
.button.is-active { background-color: coral; }

/* Стили для текста с уникальными id */
#my-super-text { color: rgb(0, 0, 0); background-color: #109910; }

/* Общие и визуальные эффекты */
* { border: 1px dotted black; font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; }

/* Скрытые и видимые элементы */
.error-message { color: red; visibility: hidden; }
.input.is-invalid + .error-message { visibility: visible; }
```

#### Связи

[[CSS селекторы]]
[[Specificity]]
[[Атрибутные селекторы]]
[[Комбинации селекторов]]
[[Визуальные эффекты]]
