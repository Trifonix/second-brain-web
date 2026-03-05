# JavaScript: Классы и прототипы

## Что я узнал

В JavaScript классы являются синтаксическим сахаром над прототипной системой. Все объекты наследуют свойства и методы через прототипное наследование.  

Ключевое слово `extends` позволяет создавать классы-наследники. Методы класса добавляются в его прототип, а статические свойства и методы доступны только на самом классе, а не на экземплярах.  

Абстракция реализуется через создание методов и конструктора в классе-наследнике, которые используют родительские методы через `super()`.  

Прототипированная цепочка позволяет экземплярам классов получать доступ к методам родительских классов, а статические свойства — только через сам класс.

### Пример
```javascript
class Human {
    static isHuman = true;

    humanGreet() {
        console.log("Greet from human!");
    }

    toString() {
        console.log('to string!!!');
    }
}

class Person extends Human {
    constructor(name, age) {
        super();
        this.name = name ?? 'Undefined name';
        this.age = age ?? 'Undefined age';
    }

    sayHello() {
        console.log('Hello from = ', this.name);
    }
}

const newPerson1 = new Person('Neo', 28);
const newPerson2 = new Person('Smith', 33);

newPerson1.sayHello(); // Hello from = Neo
newPerson2.sayHello(); // Hello from = Smith

// Доступ к методам родителя через прототип
newPerson1.humanGreet();  // Greet from human!

// Статические свойства доступны только на классе
console.log(Human.isHuman);  // true
console.log(Person.isHuman); // true
// console.log(newPerson1.isHuman); // undefined
```

#### Связи

[[JavaScript Classes]]
[[Prototypes]]
[[Inheritance]]
