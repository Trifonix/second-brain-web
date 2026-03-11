# Циклы в JavaScript: while, do while, for, for of, for in

## Что я узнал

Циклы в JavaScript позволяют повторять выполнение кода определенное количество раз или до выполнения условия. Основные типы:

- **while** — проверяет условие перед выполнением тела цикла
- **do while** — выполняет тело хотя бы один раз, проверяет условие после
- **for** — классический цикл с инициализацией, условием и инкрементом
- **for...of** — для итерации по значениям итерируемых объектов (строки, массивы)
- **for...in** — для итерации по ключам/индексам объектов

### Пример
```javascript
let value = '';
let i = 10;

while(i--) {
  value += i + ' ';
}
document.body.innerHTML = value;
value += '<hr>';

let x = 0;
do {
  value += x + ' ';
  x++;
} while (x < 10);
document.body.innerHTML = value;
value += '<hr>';

let str = 'hello';
for (let y = 0; y < str.length; y++) {
  value += str[y] + '*';
}
document.body.innerHTML = value;
value += '<hr>';

let myObj = {
  name: 'Neo',
  age: 28
}

for (let key in myObj) {
  value += key + '<br>';
  value += myObj[key] + '<br><br>';
}
value += '<hr>';
document.body.innerHTML = value;
```

Связи

[[JavaScript]]
[[Циклы]]
[[Переменные]]
[[Объекты]]
