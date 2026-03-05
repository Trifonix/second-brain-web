# JavaScript: Event Loop и Асинхронность

## Что я узнал

В JavaScript асинхронные операции обрабатываются через Event Loop. Функции типа `setTimeout` и `setInterval` ставят задачи в очередь макротасков, которые выполняются после завершения текущего стека вызовов.  

Промисы (`Promise`) создают микротаски, которые выполняются перед следующей итерацией Event Loop. Метод `then` позволяет цепочками обрабатывать результаты асинхронных операций, а `catch` и `finally` обрабатывают ошибки и финальные действия.  

Синтаксис `async/await` упрощает работу с промисами, позволяя писать асинхронный код в синхронном стиле, при этом ошибки ловятся через `try/catch`.  

Event Loop обеспечивает неблокирующее выполнение кода, позволяя JavaScript работать эффективно даже с долгими асинхронными задачами.

### Пример
```javascript
// Пример промиса с задержкой
const delay = (time = 1000) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // resolve([1, 2, 3]);
      reject("Error in delay");
    }, time);
  });
};

// Чейнинг промисов
const getData = () => new Promise(resolve => resolve([1, 2, 3, 4, 5]));
getData().then(array => console.log(array)); // [1,2,3,4,5]

// Async/await пример
async function asyncExample() {
  try {
    await delay(3000);
    const data = await getData();
    console.log(data);
  } catch (err) {
    console.log(err); // ловим ошибку из delay
  } finally {
    console.log("Finally"); // всегда выполняется
  }
}

asyncExample();
```

#### Связи

[[JavaScript Asynchronous]]
[[Event Loop]]
[[Promises]]
[[Async Await]]
