# JavaScript: LocalStorage

## Что я узнал

**LocalStorage** — это встроенное веб-хранилище в браузерах, которое позволяет сохранять данные на стороне клиента. Данные в LocalStorage сохраняются между сессиями браузера и доступны только для того же домена. В отличие от cookies, LocalStorage не отправляет данные на сервер при каждом запросе, а хранит их локально.  

Основные операции с LocalStorage:

- `setItem(key, value)` — сохраняет значение под ключом.  
- `getItem(key)` — получает значение по ключу.  
- `removeItem(key)` — удаляет ключ и связанное значение.  
- `clear()` — очищает всё хранилище.  
- `key(index)` — возвращает ключ по индексу.  
- `length` — количество элементов в хранилище.  

Для удобства часто используют сериализацию JSON, чтобы хранить объекты или массивы, а не только строки.

### Пример
```javascript
// Сохранение строки
localStorage.setItem('name', 'Neo');

// Получение значения
const userName = localStorage.getItem('name');
console.log(userName); // Neo

// Сохранение объекта
const settings = { theme: 'dark', fontSize: 16 };
localStorage.setItem('settings', JSON.stringify(settings));

// Получение объекта
const savedSettings = JSON.parse(localStorage.getItem('settings'));
console.log(savedSettings); // { theme: 'dark', fontSize: 16 }

// Удаление конкретного элемента
localStorage.removeItem('name');

// Очистка всего хранилища
// localStorage.clear();
```

#### Связи

[[Web Storage]]
[[JavaScript Objects]]
[[JSON]]
[[Client-side Storage]]
