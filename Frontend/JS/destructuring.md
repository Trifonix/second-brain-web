# JavaScript: Деструктуризация и работа с объектами

## Что я узнал

В JavaScript деструктуризация позволяет извлекать значения из объектов и массивов в отдельные переменные удобным синтаксисом. Можно задавать новые имена переменных через `name: newName` и устанавливать значения по умолчанию.  

Прототипное наследование объектов позволяет перебирать ключи через `for...in`, при этом `hasOwnProperty` помогает отличить собственные свойства от унаследованных.  

Методы `Object.keys()` и `Object.values()` позволяют получать массивы ключей и значений объекта. Методы `call`, `apply` и `bind` дают возможность менять контекст `this` при вызове функций, что особенно полезно при работе с объектами и методами, которые используют `this`.

### Пример
```javascript
const person = {
    age: 40,
    isAgent: true,
    languages: ['en', 'binary'],
    address: {
      city: 'New-York',
      street: 'Avenue'
    }
}

// Деструктуризация
const { age, name: firstname = 'TEST', languages } = person;
console.log(age);        // 40
console.log(firstname);  // TEST
console.log(languages);  // ['en', 'binary']

// Перебор собственных свойств объекта
for (let key in person) {
    if (person.hasOwnProperty(key)) {
        console.log(key, person[key]);
    }
}

// Методы для работы с ключами и значениями
const logger = {
    keys(withText = true) {
        if (withText) {
            console.log('Object keys: ', Object.keys(this));
        } else {
            console.log(Object.keys(this));
        }
    },

    keysAndValues() {
        Object.keys(this).forEach((key) => {
            console.log('Key: ', key);
            console.log('Value: ', this[key]);
        });
    }
};

// Изменение контекста this
const bound = logger.keys.bind(person);
bound(false);            // ключи объекта person без текста

logger.keys.call(person, false);       // ключи через call
logger.keys.apply(person, [true]);     // ключи через apply с текстом
```

#### Связи

[[JavaScript Objects]]
[[Destructuring]]
[[this, call, apply, bind]]
