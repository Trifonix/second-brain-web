# JavaScript: Object.create

## Что я узнал

Метод `Object.create` позволяет создавать новый объект с заданным прототипом. Это ключевой инструмент для работы с прототипным наследованием в JavaScript. В отличие от классов, где наследование задается через `extends`, `Object.create` дает прямой контроль над прототипом нового объекта, что полезно для создания объектов с общим поведением без необходимости использования конструкторов.

Основные моменты:

- `Object.create(proto)` создает объект с прототипом `proto`.  
- Можно дополнительно передавать дескрипторы свойств вторым аргументом.  
- Созданный объект наследует все свойства и методы прототипа.  
- Это удобный способ реализации прототипной цепочки без классов.  

### Пример
```javascript
const personProto = {
  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

const neo = Object.create(personProto);
neo.name = "Neo";
neo.greet(); // Hello, my name is Neo

const smith = Object.create(personProto, {
  name: { value: "Smith", writable: true, enumerable: true }
});
smith.greet(); // Hello, my name is Smith
```

#### Связи

[[JavaScript прототипы]]
[[Классы и прототипы]]
[[Object]]
