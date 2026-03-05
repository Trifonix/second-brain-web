# HTML кнопки и обработка клика

## Что я узнал

Тег `<button>` используется для создания интерактивных кнопок на веб-странице. Кнопки могут выполнять разные действия: быть отключёнными, открывать ссылки или запускать JavaScript-функции при нажатии.

Атрибут `disabled` делает кнопку неактивной — пользователь не может нажать на неё. Это полезно, когда действие временно недоступно.

Кнопку можно поместить внутрь тега `<a>`, чтобы при нажатии происходил переход по ссылке. В этом случае кнопка выступает как визуальный элемент для навигации.

С помощью атрибута `style` можно применять **inline CSS** для изменения внешнего вида кнопки. Например, можно задать цвет фона (`background-color`), цвет текста (`color`) и скругление углов (`border-radius`).

Атрибут `onclick` позволяет выполнять JavaScript-код при нажатии на кнопку. В примере вызывается функция `doSomething()`. Эта функция использует `document.getElementById()` для поиска элемента по `id` и изменяет его содержимое через свойство `innerHTML`.

Таким образом, при нажатии на кнопку текст внутри параграфа `<p id="test">` меняется с `HELLO` на `Goodbye!`.

### Пример
```javascript
<h1>Buttons</h1>

<button disabled>click me</button>

<a href="https://google.com">
    <button style="background-color: #333333; color: #00ff00; border-radius: 5px;">click me</button>
</a>

<button style="background-color: #114488; color: #ffffff; border-radius: 15px;" onclick="doSomething()">click me</button>

<p id="test">HELLO</p>

<script>
    function doSomething() {
        document.getElementById("test").innerHTML = "Goodbye!";
    }
</script>
```

#### Связи

[[HTML кнопки]]
[[JavaScript события]]
[[DOM]]
[[document.getElementById]]
[[Inline CSS]]

