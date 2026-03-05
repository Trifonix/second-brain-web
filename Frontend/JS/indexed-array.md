# IndexedArray с Proxy

## Что я узнал

IndexedArray — это паттерн, реализуемый через Proxy, который позволяет автоматически создавать индекс по уникальному ключу, например `id`, для объектов в массиве. Это ускоряет поиск элементов: вместо полного перебора массива (`O(n)`) можно мгновенно получать объект по его `id` (`O(1)`). Такая конструкция полезна для оптимизации работы с коллекциями данных, где часто выполняются запросы по идентификатору.

### Пример
```javascript
// Создаем Proxy для массива с индексом по id
function createIndexedArray(array = []) {
  const index = {};
  array.forEach(item => {
    if(item.id !== undefined) index[item.id] = item;
  });

  return new Proxy(array, {
    get(target, prop) {
      if(prop === 'findById') {
        return (id) => index[id];
      }
      return target[prop];
    },
    set(target, prop, value) {
      if(typeof prop === 'string' && !isNaN(prop)) {
        if(value.id !== undefined) index[value.id] = value;
      }
      target[prop] = value;
      return true;
    }
  });
}

// Использование
const users = createIndexedArray([
  {id: 1, name: 'Neo'},
  {id: 2, name: 'Trinity'}
]);

console.log(users.findById(1)); // {id: 1, name: 'Neo'}

users.push({id: 3, name: 'Morpheus'});
console.log(users.findById(3)); // {id: 3, name: 'Morpheus'}
```

#### Связи

[[Proxy]]
[[Массивы и коллекции]]
