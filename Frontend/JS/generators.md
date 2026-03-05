# JavaScript: Генераторы (Generators)

## Что я узнал

Генераторы в JavaScript — это особый тип функций, которые могут приостанавливать свое выполнение и возобновлять его позже. Они объявляются с помощью `function*` вместо обычного `function`. Генераторы возвращают объект-итератор, у которого есть методы `next()`, `return()` и `throw()`.  

Основная идея генераторов — управлять последовательностью выполнения кода и значениями, которые возвращаются шаг за шагом. Это особенно полезно для ленивых вычислений, обработки больших данных, асинхронного кода (до появления `async/await`) и создания пользовательских итераторов.  

При вызове генератора функция не выполняется сразу. Она выполняется только при вызове метода `next()`, который возвращает объект `{ value, done }`, где `value` — текущее значение, а `done` — булевое значение, показывающее, завершен ли генератор.

### Пример
```javascript
// Создание генератора
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id; // приостанавливает выполнение и возвращает id
    id++;
  }
}

const gen = idGenerator();

console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }

// Генератор с ограниченным числом шагов
function* range(start, end) {
  for (let i = start; i <= end; i++) {
    yield i;
  }
}

const numbers = range(1, 5);
console.log([...numbers]); // [1, 2, 3, 4, 5]

// Генераторы и функции с передачей значения внутрь
function* greeting() {
  const name = yield "Hello, what is your name?";
  yield `Nice to meet you, ${name}!`;
}

const greetGen = greeting();
console.log(greetGen.next().value);          // "Hello, what is your name?"
console.log(greetGen.next("Neo").value);     // "Nice to meet you, Neo!"
```

#### Связи

[[JavaScript Functions]]
[[JavaScript Iterators]]
[[Async Programming]]
[[Lazy Evaluation]]
