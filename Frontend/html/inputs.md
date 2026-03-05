# Продвинутые формы и атрибуты ввода в HTML

## Что я узнал

HTML формы позволяют не только собирать базовую информацию, но и использовать **расширенные элементы и атрибуты** для улучшения пользовательского опыта и точной валидации данных.

**Новые элементы и возможности:**
- `<optgroup>` — используется для **группировки опций** внутри выпадающего списка `<select>`, что делает длинные списки более удобными для пользователя.
  
**Специфические атрибуты input:**
- `inputmode="numeric"` — при фокусе на поле вызывается **цифровая клавиатура** на мобильных устройствах.
- `autofocus` — элемент автоматически получает фокус при загрузке страницы.
- `maxlength` — ограничивает максимальное количество вводимых символов.
- `multiple` — позволяет выбирать несколько файлов (`<input type="file">`) или несколько опций (`<select multiple>`).

**Расширенные типы ввода:**
- `search` — поле для поиска с браузерной стилизацией.
- `datetime-local` — выбор даты и времени.
- `week` — выбор недели года.
- `range` — ползунок для выбора значения в диапазоне.

Эти функции делают формы более **интерактивными, адаптивными и удобными для пользователей**, особенно на мобильных устройствах, и позволяют избежать лишнего JavaScript для базовой проверки и интерфейса.

### Пример
```javascript
<form>
    <label for="fruit">Choose a fruit:</label>
    <select id="fruit" name="fruit">
        <optgroup label="Citrus">
            <option value="orange">Orange</option>
            <option value="lemon">Lemon</option>
        </optgroup>
        <optgroup label="Berries">
            <option value="strawberry">Strawberry</option>
            <option value="blueberry">Blueberry</option>
        </optgroup>
    </select>

    <br><br>

    <label for="age">Enter your age:</label>
    <input type="text" id="age" name="age" inputmode="numeric" maxlength="3" autofocus>

    <br><br>

    <label for="files">Upload files:</label>
    <input type="file" id="files" name="files" multiple>

    <br><br>

    <label for="search">Search:</label>
    <input type="search" id="search" name="search">

    <br><br>

    <label for="appointment">Appointment time:</label>
    <input type="datetime-local" id="appointment" name="appointment">

    <br><br>

    <label for="week">Select week:</label>
    <input type="week" id="week" name="week">

    <br><br>

    <label for="range">Choose a number:</label>
    <input type="range" id="range" name="range" min="0" max="100">
</form>
```

#### Связи

[[HTML формы]]
[[HTML input]]
[[HTML optgroup]]
[[Атрибуты input]]
[[Продвинутые элементы формы]]
