# Основы JavaScript: Калькулятор и базовые конструкции

## Что я узнал

В этой заметке собраны базовые концепции **JavaScript**, продемонстрированные на примере простого калькулятора:

- **Переменные и константы:** `let` для изменяемых значений, `const` для констант. 
- **Типы данных:** `number`, `string`, `boolean`, `undefined`, `null`. Особенности проверки типов через `typeof`.
- **Комментарии:** однострочные `//` и многострочные `/* ... */`.
- **Имена переменных:** camelCase, PascalCase, snake_case, допустимые символы и запрещенные варианты.
- **Арифметические операции:** `+`, `-`, `*`, `/` и комбинированные `+=`, `-=`, `*=`, `/=`.
- **Приоритет операций:** скобки и порядок вычисления.
- **Сравнения:** `>`, `<`, `>=`, `<=`, `==` (с приведением типов), `===` (строгое сравнение).
- **Работа с DOM:** `document.getElementById`, `textContent`, `onclick`.
- **Функции:** создание для вычислений (`computeNumbersWithAction`) и отображения результата (`printResult`).
- **Управление стилями:** динамическая смена цвета текста в зависимости от значения (`resultElement.style.color`).
- **События:** обработчики кнопок для выбора действия и вычисления результата.
- **Bootstrap 5:** для быстрого создания интерфейса калькулятора с input, кнопками и блоком результата.

Пример показывает, как базовые конструкции JavaScript можно интегрировать с DOM и библиотеками UI для интерактивных приложений.

### Пример
```javascript
const resultElement = document.getElementById("result");
const input1 = document.getElementById("input1");
const input2 = document.getElementById("input2");
const submitBtn = document.getElementById("submit");
const plusBtn = document.getElementById("plus");
const minusBtn = document.getElementById("minus");

let action = '+';

plusBtn.onclick = () => { action = '+'; };
minusBtn.onclick = () => { action = '-'; };

function printResult(result) {
  resultElement.style.color = result < 0 ? 'red' : 'green';
  resultElement.textContent = result;
}

function computeNumbersWithAction(input1, input2, actionSymbol) {
  const value1 = +input1.value;
  const value2 = +input2.value;
  return actionSymbol === '+' ? value1 + value2 : value1 - value2;
}

submitBtn.onclick = () => {
  const result = computeNumbersWithAction(input1, input2, action);
  printResult(result);
};
```

#### Связи

[[JavaScript Basics]]
[[DOM Manipulation]]
[[Bootstrap 5]]
[[Functions]]
[[Data Types]]
