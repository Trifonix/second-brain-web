# JavaScript: Работа со строками и шаблонными литералами

## Что я узнал

В JavaScript строки — это последовательности символов, которые можно создавать с помощью одинарных `'...'`, двойных `"..."` или шаблонных литералов `` `...` ``. Основные моменты:

- **Шаблонные литералы** позволяют создавать многострочные строки и вставлять выражения через `${...}`.
- **Конкатенация строк** выполняется с помощью `+`, но шаблонные литералы делают код чище и удобнее.
- **Функции внутри шаблонных литералов** могут возвращать значения, которые вставляются прямо в строку.
- **Условные выражения** (тернарный оператор) можно использовать внутри `${...}`.
- **Экранирование символов** (`\'`, `\"`) используется для включения специальных символов в строку.
- **Методы строк**:
  - `length` — длина строки.
  - `toUpperCase()`, `toLowerCase()` — изменение регистра.
  - `charAt(index)` — символ по индексу.
  - `indexOf(substr)` — индекс первого вхождения подстроки.
  - `startsWith(substr)`, `endsWith(substr)` — проверка начала и конца строки.
  - `repeat(n)` — повтор строки.
  - `trim()` — удаление пробелов с начала и конца строки.

### Пример
```javascript
const myName = "Neo";
const age = "29";

// Многострочная строка
const output = `any
qwe
string`;
console.log(output);

// Конкатенация строк
const old = "Hello, I am " + myName + " and my age is " + age;
console.log(old);

// Шаблонные литералы
const newStr = `My name is ${myName}`;
console.log(newStr);

// Вставка функции
function getAge() {
  return age;
}
console.log(`it will be result of func: ${getAge()}`);

// Тернарный оператор внутри строки
console.log(`you can or not ? ${getAge() > 18 ? "yes" : "not"}`);

// Экранирование
console.log(`can\'t breathe`);

// Методы строк
console.log(myName);
console.log(myName.length);
console.log(myName.toUpperCase());
console.log(myName.toLowerCase());
console.log(myName.charAt(0));
console.log(myName.indexOf('e'));
console.log(myName.startsWith('Ne'));
console.log(myName.toLowerCase().startsWith('ne'));
console.log(myName.endsWith('o'));
console.log(myName.repeat(2));

// Удаление пробелов
const password = '    my super pass    ';
console.log(password);
console.log(password.trim());
```

#### Связи

[[JavaScript Basics]]
[[Strings]]
[[Template Literals]]
[[String Methods]]
