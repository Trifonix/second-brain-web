# JavaScript: Map и Set

## Что я узнал

`Map` и `Set` — это встроенные структуры данных в JavaScript, которые расширяют возможности работы с коллекциями по сравнению с обычными объектами и массивами.  

- **Map** — коллекция пар «ключ-значение», где ключи могут быть любого типа (объекты, функции, примитивы). Map сохраняет порядок добавления элементов и предоставляет методы `set`, `get`, `has`, `delete` и `clear`.  
- **Set** — коллекция уникальных значений. Значения в Set не повторяются, и порядок их добавления сохраняется. Методы включают `add`, `has`, `delete` и `clear`.

Map и Set полезны, когда нужно хранить уникальные элементы, работать с произвольными ключами, выполнять быстрый поиск или итерироваться по коллекции в определенном порядке.

### Пример
```javascript
// ===== Map =====
const userRoles = new Map();
userRoles.set('Neo', 'admin');
userRoles.set('Trinity', 'editor');
userRoles.set('Morpheus', 'moderator');

console.log(userRoles.get('Neo'));       // "admin"
console.log(userRoles.has('Smith'));    // false

userRoles.delete('Morpheus');
console.log(userRoles.size);            // 2

for (const [user, role] of userRoles) {
  console.log(user, role);
}

// ===== Set =====
const uniqueNumbers = new Set([1, 2, 3, 3, 2, 4]);
console.log(uniqueNumbers);             // Set { 1, 2, 3, 4 }

uniqueNumbers.add(5);
console.log(uniqueNumbers.has(3));      // true

uniqueNumbers.delete(2);
console.log(uniqueNumbers.size);        // 4

// Итерирование по Set
for (const number of uniqueNumbers) {
  console.log(number);
}

// Применение Set для удаления дубликатов из массива
const numbersArray = [1, 2, 2, 3, 4, 4, 5];
const uniqueArray = [...new Set(numbersArray)];
console.log(uniqueArray);               // [1, 2, 3, 4, 5]
```

#### Связи

[[JavaScript Collections]]
[[JavaScript Iterators]]
[[Data Structures]]
[[Map]]
[[Set]]
