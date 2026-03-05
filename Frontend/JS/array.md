# JavaScript: Массивы, Объекты и Методы работы с данными

## Что я узнал

В этой заметке рассматриваются основные возможности работы с **массивами** и **объектами** в JavaScript, а также методы их обработки и фильтрации данных:

- **Создание массивов:** литералы `[]`, конструктор `new Array()`.
- **Доступ к элементам:** индексация, `array.length`, последний элемент `array[array.length - 1]`.
- **Изменение массива:** `push`, `pop`, `shift`, `unshift`, `splice`, `slice`, `reverse`, `sort`, `map`, `filter`, `reduce`, `with`, `toReversed`, `toSorted`, `toSpliced`.
- **Особенности поиска:** `indexOf`, `includes`, `find`, `findIndex`.
- **Работа с объектами:** создание объектов, доступ через `obj.key` или `obj['key']`, изменение свойств, методы объектов.
- **Рендеринг списков в DOM:** `insertAdjacentHTML`, динамическое обновление контента через `innerHTML`.
- **Обработка событий:** `onclick`, использование `event.target` для управления списками.
- **Комбинированная обработка данных:** фильтрация, маппинг и редьюс для суммирования значений или преобразования данных.
- **Манипуляции со строками:** `split`, `join`, `toReversed`, `filter`.
- **Отображение состояния:** через CSS классы (`text-decoration-line-through`) для пометки завершённых заметок.

Практика на примере заметок показывает, как массивы и объекты интегрируются с интерфейсом, как создавать интерактивные списки и управлять состоянием элементов.

### Пример
```javascript
const notes = [
  { title: "записать блок про массивы", completed: false },
  { title: "рассказать теорию объектов", completed: true }
];

const inputElement = document.getElementById("title");
const createBtn = document.getElementById("create");
const listElement = document.getElementById("list");

function getNoteTemplate(note, index) {
  return `
    <li class="list-group-item d-flex justify-content-between align-items-center">
      <span class="${note.completed ? "text-decoration-line-through" : ""}">${note.title}</span>
      <span>
        <span class="btn btn-small btn-${note.completed ? "warning" : "success"}" data-index=${index} data-type="toggle">&check;</span>
        <span class="btn btn-small btn-danger" data-index=${index} data-type="remove">&times;</span>
      </span>
    </li>
  `;
}

function render() {
  listElement.innerHTML = "";
  if (notes.length === 0) {
    listElement.innerHTML = '<p>Список пуст...</p>';
  }
  notes.forEach((note, i) => listElement.insertAdjacentHTML("beforeend", getNoteTemplate(note, i)));
}

createBtn.onclick = () => {
  if (!inputElement.value) return;
  notes.push({ title: inputElement.value, completed: false });
  render();
  inputElement.value = "";
};

listElement.onclick = (event) => {
  const index = parseInt(event.target.dataset.index);
  const type = event.target.dataset.type;
  if (type === "toggle") notes[index].completed = !notes[index].completed;
  else if (type === "remove") notes.splice(index, 1);
  render();
};

render();
```

#### Связи

[[JavaScript Basics]]
[[Arrays]]
[[Objects]]
[[DOM Manipulation]]
[[Event Handling]]
[[Array Methods]]
