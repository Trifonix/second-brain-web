# JavaScript: Работа с датой и временем

## Что я узнал

В JavaScript объект **Date** используется для работы с датой и временем. С его помощью можно получать текущую дату, компоненты даты (год, месяц, день, часы, минуты, секунды, миллисекунды) и изменять их через методы `setFullYear`, `setMonth` и другие.  

Методы форматирования позволяют выводить дату и время в удобочитаемом виде: `toDateString()`, `toTimeString()`, `toLocaleDateString()`, `toLocaleTimeString()`.  

Для динамического отображения времени на странице используют таймеры: `setInterval` для обновления текста, `onclick` для переключения режимов отображения. Создание **чистых функций (Pure Functions)**, таких как `format`, помогает отделить логику форматирования от состояния интерфейса.

### Пример
```javascript
const now = new Date();
console.log(now.getFullYear());   // год
console.log(now.getMonth());      // месяц (0-11)
console.log(now.getDate());       // день месяца
console.log(now.getHours());      // часы
console.log(now.getMinutes());    // минуты
console.log(now.getSeconds());    // секунды
console.log(now.getMilliseconds());// миллисекунды

now.setFullYear(2055);
console.log(now.toDateString());
console.log(now.toTimeString());
console.log(now.toLocaleDateString());
console.log(now.toLocaleTimeString());

// Динамическое отображение даты/времени
let mode = "full";
const output = document.getElementById("output");
const fullBtn = document.getElementById("full");
const dateBtn = document.getElementById("date");
const timeBtn = document.getElementById("time");

function bindMode(name) {
  return function () {
    mode = name;
    update();
  };
}

fullBtn.onclick = bindMode("full");
dateBtn.onclick = bindMode("date");
timeBtn.onclick = bindMode("time");

setInterval(update, 100);

function update() {
  output.textContent = format(mode);
}

function format(formatMode) {
  const now = new Date();
  switch (formatMode) {
    case "time":
      return now.toLocaleTimeString() + '.' + now.getMilliseconds();
    case "date":
      return now.toLocaleDateString();
    case "full":
      return now.toLocaleDateString() + " " + now.toLocaleTimeString();
    default:
      return now.toLocaleTimeString();
  }
}
```

#### Связи

[[JavaScript Date]]
[[Timers]]
[[Pure Functions]]
