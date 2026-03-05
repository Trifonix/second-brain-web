# JavaScript: Числа, BigInt и Math

## Что я узнал

В JavaScript числа представлены в виде типа **Number**, который охватывает как целые числа, так и числа с плавающей точкой (float). Основные моменты:

- **Типы чисел:** integer (`42`), float (`42.42`), экспоненциальная запись (`10e3`).
- **Большие числа:** можно использовать `_` для читаемости (`1_000_000_000`). Для чисел больше `Number.MAX_SAFE_INTEGER` используется `BigInt`.
- **Безопасные границы:** `Number.MAX_SAFE_INTEGER` и `Number.MIN_SAFE_INTEGER` показывают безопасный диапазон целых чисел.
- **Infinity и NaN:** бесконечность (`Infinity`), отрицательная бесконечность (`-Infinity`), проверка через `Number.isFinite()` и `Number.isNaN()`.
- **Преобразование строк в числа:** `Number()`, `parseInt()`, `parseFloat()`, унарный плюс `+`.
- **Проблемы точности float:** например, `0.1 + 0.2` даёт не совсем `0.3`. Для исправления используется `toFixed()` и `parseFloat()`.
- **BigInt:** для целых чисел произвольной длины (`42n`, `BigInt()`), поддерживает арифметику, но нельзя смешивать с Number без явного преобразования.
- **Math объект:** предоставляет математические функции: `Math.sqrt`, `Math.pow`, `Math.abs`, `Math.max`, `Math.min`, `Math.floor`, `Math.ceil`, `Math.round`, `Math.trunc`, `Math.random`.
- **Генерация случайных чисел в диапазоне:** `Math.random()` + `Math.floor()`.

### Пример
```javascript
// Number и преобразования
const num = 42;
const float = 42.42;
const pow = 10e3;
console.log(pow);

const big = 1_000_000_000;
console.log(big);

// Проверка Infinity и NaN
console.log(Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY);
const weird = 23 / undefined;
console.log(Number.isNaN(weird));

// Преобразование строк
const strInt = '42';
const strFloat = '42.42';
console.log(Number(strInt), Number(strFloat));
console.log(parseInt(strFloat), parseFloat(strFloat));
console.log(+strInt, +strFloat);

// Точность float
console.log(0.1 + 0.2);
const fixed = (0.1 + 0.2).toFixed(10);
console.log(parseFloat(fixed));

// BigInt
console.log(BigInt(Number.MAX_SAFE_INTEGER) + 1246987n);
console.log(5n / 2n); // целочисленное деление
console.log(5 / 2);   // обычное деление

// Math функции
console.log(Math.sqrt(25));
console.log(Math.pow(2, 3));
console.log(Math.max(2,5,42,199,0));
console.log(Math.min(2,5,42,199,0));
console.log(Math.floor(4.9), Math.ceil(4.9), Math.round(4.4), Math.trunc(4.5));

// Случайное число в диапазоне
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
console.log(getRandomNumber(10, 100));
```

#### Связи

[[JavaScript Basics]]
[[Number]]
[[BigInt]]
[[Math Object]]
[[Random Numbers]]
