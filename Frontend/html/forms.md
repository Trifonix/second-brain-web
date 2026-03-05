# ФОРМЫ в HTML

## Что я узнал

HTML-формы используются для сбора данных от пользователя и их отправки на сервер.  
Главный контейнер — `<form>`. Именно он объединяет поля ввода и управляет отправкой данных.

Форма может отправлять данные двумя способами:
- `GET` — данные передаются в URL (подходит для поиска, фильтров)
- `POST` — данные отправляются в теле запроса (используется для регистрации, авторизации и передачи чувствительных данных)

Ключевые элементы формы:

- `<input>` — поле ввода (имеет разные типы)
- `<label>` — подпись для поля (связывается через `for` и `id`)
- `<textarea>` — многострочный ввод
- `<select>` — выпадающий список
- `<button>` — кнопка отправки
- `<fieldset>` и `<legend>` — логическая группировка полей

Основные типы `<input>`:
- text
- email
- password
- number
- checkbox
- radio
- file
- date

Важные атрибуты:
- `name` — имя поля (по нему данные отправляются на сервер)
- `id` — связывает input с label
- `required` — обязательное поле
- `placeholder` — подсказка
- `value` — значение по умолчанию
- `checked` — выбранный вариант (checkbox, radio)
- `disabled` — отключённое поле

Важно понимать:
- Без `name` поле не отправляется
- `<label>` увеличивает кликабельную область и улучшает доступность
- Кнопка внутри формы по умолчанию имеет тип `submit`

Форма — это не просто верстка. Это механизм взаимодействия пользователя с приложением.

---

### Пример
```javascript
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Пример формы</title>
</head>
<body>
  <form action="/submit" method="POST">
    
    <label for="email">Email</label>
    <input 
      type="email" 
      id="email" 
      name="email" 
      required 
      placeholder="Введите email"
    />

    <label for="password">Пароль</label>
    <input 
      type="password" 
      id="password" 
      name="password" 
      required
    />

    <fieldset>
      <legend>Выберите роль</legend>

      <label>
        <input type="radio" name="role" value="user" checked />
        Пользователь
      </label>

      <label>
        <input type="radio" name="role" value="admin" />
        Администратор
      </label>
    </fieldset>

    <label>
      <input type="checkbox" name="agree" required />
      Я согласен с условиями
    </label>

    <button type="submit">Отправить</button>
  </form>
</body>
</html>
```

#### Связи

[[HTML]]
[[Семантический HTML]]
[[Доступность (A11Y)]]
[[HTTP методы GET и POST]]
[[Валидация форм]]