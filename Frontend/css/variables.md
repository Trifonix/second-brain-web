# CSS-переменные (Custom Properties)

## Что я узнал

CSS-переменные (или **Custom Properties**) позволяют хранить значения в переменных и повторно использовать их в стилях. Они объявляются с помощью префикса `--` и обычно размещаются в селекторе `:root`, чтобы быть доступными во всём документе.

Использование переменных делает код **гибким, поддерживаемым и масштабируемым**, потому что значения можно менять в одном месте, и изменения автоматически применяются ко всем элементам, где используется переменная.

### Объявление переменных

Переменные объявляются внутри любого селектора:

```css
body {
  --color-main: red;
}
```

Использование происходит через функцию `var()`:

```css
color: var(--color-main);
```

Название переменной может содержать:

* латинские символы
* дефисы
* цифры
* даже эмодзи или символы других языков

Но на практике обычно используют **kebab-case** (`--color-main`, `--border-radius`), чтобы код оставался читаемым.

### Область видимости

CSS-переменные работают по принципу **наследования**.

Это означает:

* переменная доступна **внутри текущего элемента**
* и **во всех его дочерних элементах**

Если переменная объявлена внутри одного блока, она **недоступна вне него**.

Также переменные можно **переопределять в более вложенных элементах**, создавая локальные значения.

### Фоллбэк (резервное значение)

Функция `var()` поддерживает **резервное значение**, если переменная не определена:

```css
box-shadow: var(--undefined-variable, 2px 2px 2px green);
```

Если переменная отсутствует, используется значение после запятой.

### Глобальные переменные

Чаще всего переменные объявляют в `:root`, чтобы они были доступны во всём документе:

```css
:root {
  --color-main: lightskyblue;
  --color-accent: #ffc67c;
}
```

Так можно хранить:

* цвета
* размеры
* шрифты
* анимации
* уровни `z-index`
* тени
* отступы

### Практическое применение

CSS-переменные часто используют для:

* **дизайн-систем**
* **темизации интерфейса**
* **управления цветами**
* **создания гибких компонентов**

Например, кнопка может менять внешний вид просто через переопределение переменных.

### Пример

```javascript
body {
  --color-main: #20855e;
  --color-accent: #ffc67c;
  --border-radius: 4px;
}

.button3 {
  color: var(--color-main);
  background-color: var(--color-accent);
  border-radius: var(--border-radius);

  /* Фоллбэк если переменной нет */
  box-shadow: var(--undefined-variable, 2px 2px 2px green);
}

/* Локальная переменная */
.box-2 {
  --custom-border: 2px solid red;
  border: var(--custom-border);
}

/* Переопределение переменной */
.box-22 {
  --custom-border: 5px solid blue;
  border: var(--custom-border);
}

/* Глобальные переменные */
:root {
  --color-light: #FFFFFF;
  --color-dark: #171717;
  --color-main: lightskyblue;
  --color-accent: #ffc67c;

  --font-family-base: 'Roboto', sans-serif;

  --container-width: 1200px;
  --section-gap-y: 80px;

  --transition-duration: 0.2s;

  --layer-modal: 100;
  --layer-overlay-menu: 200;
}

/* Компонент кнопки */
.button {
  --buttonTextColor: var(--color-main);
  --buttonBgColor: var(--color-accent);
  --buttonBorderColor: transparent;

  padding: 10px;
  border-radius: 5px;
  color: var(--buttonTextColor);
  background-color: var(--buttonBgColor);
  border: 4px solid var(--buttonBorderColor);
}

/* Модификатор */
.button.yellow {
  --buttonBgColor: var(--color-secondary);
}

.button.transparent {
  --buttonTextColor: var(--color-dark);
  --buttonBgColor: transparent;
  --buttonBorderColor: var(--color-dark);
}
```

#### Связи

[[CSS]]
[[Архитектура CSS]]
