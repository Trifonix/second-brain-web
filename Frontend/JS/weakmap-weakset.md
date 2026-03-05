# JavaScript: WeakMap и WeakSet

## Что я узнал

`WeakMap` и `WeakSet` — это «слабые» коллекции в JavaScript, которые отличаются от обычных `Map` и `Set` тем, что хранят **слабые ссылки** на объекты. Это значит, что если объект больше нигде не используется, сборщик мусора может его удалить, даже если он находится в WeakMap или WeakSet.  

- **WeakMap** — коллекция пар «ключ-значение», где **ключи должны быть объектами**. Значения могут быть любыми. WeakMap не поддерживает итерацию и не имеет свойства `size`. Это делает WeakMap удобным для хранения приватных данных объектов и предотвращения утечек памяти.  
- **WeakSet** — коллекция уникальных объектов. Все элементы должны быть объектами. Как и WeakMap, WeakSet не поддерживает итерацию и не имеет свойства `size`.  

Основное преимущество этих структур — автоматическое удаление объектов, на которые больше нет ссылок, что помогает управлять памятью в больших приложениях.

### Пример
```javascript
// ===== WeakMap =====
const wm = new WeakMap();

let obj1 = { name: 'Neo' };
let obj2 = { name: 'Trinity' };

wm.set(obj1, 'admin');
wm.set(obj2, 'editor');

console.log(wm.get(obj1));   // "admin"
console.log(wm.has(obj2));   // true

obj1 = null; // obj1 теперь может быть удален сборщиком мусора

// ===== WeakSet =====
const ws = new WeakSet();

let user1 = { name: 'Morpheus' };
let user2 = { name: 'Oracle' };

ws.add(user1);
ws.add(user2);

console.log(ws.has(user1));  // true

user1 = null; // user1 теперь может быть удален сборщиком мусора
```

#### Связи

[[JavaScript Collections]]
[[Map]]
[[Set]]
[[Memory Management]]
[[Weak References]]
