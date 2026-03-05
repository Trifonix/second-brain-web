# JavaScript: Proxy

## Что я узнал

В JavaScript `Proxy` позволяет перехватывать и изменять поведение объектов, функций и классов. Он создается с двумя аргументами: целевой объект (`target`) и объект с ловушками (`handler`), которые перехватывают различные операции, такие как чтение свойств, запись, вызов функции или создание экземпляра класса.  

Использование Proxy полезно для валидации данных, логирования, мемоизации, защиты объектов и создания реактивных структур. Кроме объектов, Proxy можно применять к функциям, чтобы перехватывать вызовы, а также к классам для контроля за созданием экземпляров и доступом к статическим методам.

### Пример
```javascript
// Proxy для объекта
const person = { name: 'Neo', age: 29 };
const proxyPerson = new Proxy(person, {
  get(target, prop) {
    console.log(`Читаем свойство: ${prop}`);
    return target[prop];
  },
  set(target, prop, value) {
    console.log(`Устанавливаем ${prop} = ${value}`);
    target[prop] = value;
    return true;
  }
});

console.log(proxyPerson.name); // "Читаем свойство: name"
proxyPerson.age = 30;          // "Устанавливаем age = 30"

// Proxy для функции
function greet(name) {
  return `Hello, ${name}!`;
}
const proxyGreet = new Proxy(greet, {
  apply(target, thisArg, args) {
    console.log(`Вызываем функцию с аргументами: ${args}`);
    return target(...args).toUpperCase();
  }
});

console.log(proxyGreet('Smith')); // "HELLO, SMITH!"

// Proxy для класса
class Person {
  constructor(name) {
    this.name = name;
  }
  sayHello() {
    return `Hello from ${this.name}`;
  }
}

const proxyPersonClass = new Proxy(Person, {
  construct(target, args) {
    console.log(`Создаем экземпляр с аргументами: ${args}`);
    return new target(...args);
  },
  get(target, prop) {
    console.log(`Доступ к статическому свойству: ${prop}`);
    return target[prop];
  }
});

const p = new proxyPersonClass('Neo');
console.log(p.sayHello());
```

#### Связи

[[JavaScript Objects]]
[[JavaScript Functions]]
[[JavaScript Classes]]
[[Reactivity]]
