# HTML списки: unordered, ordered и description

## Что я узнал

HTML предоставляет несколько типов списков для структурирования информации на веб-странице. Списки помогают организовать данные, сделать текст более читаемым и логически разделённым.

**Ненумерованный список** создаётся с помощью тега `<ul>` (unordered list). Каждый элемент списка помещается в тег `<li>` (list item). Такой список обычно отображается с маркерами (точками). Внутри элемента списка можно создавать **вложенные списки**, чтобы показать подкатегории или детали.

**Нумерованный список** создаётся с помощью тега `<ol>` (ordered list). Элементы также задаются через `<li>`. В отличие от `<ul>`, элементы автоматически нумеруются. Атрибут `type` позволяет изменить формат нумерации, например:
- `1` — обычные числа  
- `A` — заглавные буквы  
- `a` — строчные буквы  
- `I` — римские цифры  

**Список описаний** создаётся с помощью `<dl>` (description list). Он используется для определения терминов и их объяснений.  
Внутри него используются два тега:
- `<dt>` — термин (definition term)
- `<dd>` — описание термина (definition description)

Этот тип списка часто применяется для глоссариев, словарей терминов или объяснения понятий, например HTML, CSS и JavaScript.

Использование разных типов списков помогает лучше структурировать информацию на странице и улучшает её читаемость.

### Пример
```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h4>Unordered List</h4>
    <ul>
        <li>pizza dough</li>
        <li>tomato sauce</li>
        <li>cheese</li>
        <li>toppings
            <ul>
                <li>pepperoni</li>
                <li>mushrooms</li>
                <li>peppers</li>
            </ul>
        </li>
    </ul>

    <h4>Ordered List</h4>
    <ol type="A">
        <li>eat breakfast</li>
        <li>take shower</li>
        <li>leave for work</li>
    </ol>

    <h4>Description List</h4>
    <dl>
        <dt>HTML</dt>
        <dd>This adds scructure to a webpage</dd>

        <dt>CSS</dt>
        <dd>This adds style to a webpage</dd>

        <dt>JavaScript</dt>
        <dd>This adds functionality to a webpage</dd>
    </dl>
</body>
</html>
```

#### Связи

[[HTML списки]]
[[Unordered List]]
[[Ordered List]]
[[Description List]]
[[HTML структура страницы]]
