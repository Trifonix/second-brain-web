# JavaScript: Функции, замыкания и таймеры

## Что я узнал

В JavaScript функции можно объявлять разными способами: через **Function Declaration (FD)**, **Function Expression (FE)** и **Arrow Functions**. Каждая форма имеет свои особенности вызова и области видимости.  

- **Function Declaration** можно вызывать до объявления функции.  
- **Function Expression** нельзя вызывать до объявления, так как она присваивается переменной.  
- **Arrow Functions** имеют краткий синтаксис и не создают собственный `this`.  
- **Параметры функции** могут иметь значения по умолчанию, а также использовать **rest-параметры** для передачи неограниченного числа аргументов.  
- **Замыкания (closures)** позволяют функции помнить окружение, в котором она была создана. Это полезно для хранения состояния и создания приватных переменных.  
- **Таймеры**: `setTimeout` и `setInterval` используются для отложенного выполнения кода и повторяющихся операций. `clearTimeout` и `clearInterval` позволяют останавливать таймеры.

### Пример
```javascript
// Function Declaration
const name = "user";
function greet(name) {
  console.log("Hello,", name, "!");
}
greet(name);

// Function Expression
const greet2 = function (name) {
  console.log("2 Hello", name);
};
greet2("Smith");

// Проверка типов
console.log(typeof greet);   // function
console.log(typeof greet2);  // function

// Таймеры
setTimeout(greet, 1500);
setTimeout(() => console.log("TimeOut!"), 2500);
setTimeout(() => greet2(name), 3000);

let counter = 0;
const interval = setInterval(() => {
  if (counter === 5) {
    console.log("it was 5");
    clearInterval(interval);
  } else {
    console.log(++counter);
  }
}, 1000);

// Arrow Functions
const arrow = (name, age) => console.log('Hello - ', name, age);
arrow('Megauser', 25);

const arrow2 = name2 => console.log('qhello, ', name2);
arrow2('hacker');

const pow2 = (num, exp) => Math.pow(num, exp);
console.log(pow2(2, 3));

// Default parameters
const sum = (a = 20, b = a / 2) => a + b;
console.log(sum(40, 2));
console.log(sum(40));

// Rest parameters
function sumAll(...numbers) {
  return numbers.reduce((acc, cur) => acc + cur, 0);
}
console.log('sum was ===', sumAll(1, 2, 3, 4, 5, 6));

// Closures
function createPerson(name) {
  return function(lastName) {
    console.log(name + ' ' + lastName);
  }
}
const addLastName = createPerson('agent');
addLastName('Smith');
addLastName('Neo');
```

#### Связи

[[JavaScript Functions]]
[[Closures]]
[[Arrow Functions]]
[[Timers]]
