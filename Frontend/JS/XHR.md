# JavaScript: Legacy-методы запросов (XHR и Ajax)

## Что я узнал

Раньше для работы с сервером использовались **XMLHttpRequest (XHR)** и подходы, называемые **Ajax**, которые позволяли делать асинхронные запросы без перезагрузки страницы. Несмотря на то, что современная практика смещается к `fetch` и `async/await`, знание этих методов полезно для поддержки старого кода и понимания истории веб-разработки.

Основные моменты:

- `XMLHttpRequest` создается через `new XMLHttpRequest()`.  
- Можно отслеживать состояние запроса через `onreadystatechange`.  
- Метод `open(method, url)` задает тип запроса и адрес.  
- Метод `send()` отправляет запрос.  
- Ajax позволяет обновлять части страницы без полной перезагрузки.  
- Есть методы `setRequestHeader` для настройки заголовков и `responseText` / `responseXML` для получения данных.  

### Пример
```javascript
// Создаем объект запроса
const xhr = new XMLHttpRequest();

// Настраиваем GET-запрос
xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1', true);

// Отслеживаем изменение состояния
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log('Ответ от сервера:', JSON.parse(xhr.responseText));
  }
};

// Отправляем запрос
xhr.send();
```

#### Связи

[[JavaScript Fetch API]]
[[Async/Await]]
[[AJAX]]
[[XMLHttpRequest]]
