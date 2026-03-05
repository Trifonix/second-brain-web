# HTML элементы span и div

## Что я узнал

Теги `<span>` и `<div>` используются для **структурирования и стилизации контента** в HTML, но имеют разные назначения.

**`<span>`** — это **инлайн-элемент**, который применяется для выделения или форматирования отдельного текста или небольшой части документа. Он не создаёт нового блока на странице, а лишь позволяет применить стили, классы или идентификаторы к тексту внутри существующего блока.

**`<div>`** — это **блочный элемент**, который определяет отдельный раздел документа. Он часто используется для группировки нескольких элементов (параграфов, изображений, списков) для последующего применения стилей, позиционирования или логической организации страницы. В примере `<div>` имеет серый фон, который визуально отделяет содержимое от остальной страницы.

Комбинирование `<div>` и `<span>` позволяет гибко структурировать контент: `<div>` создаёт блоки, а `<span>` выделяет отдельные части текста внутри этих блоков.

### Пример
```javascript
<!--span    = adds markup to text or portion of a document-->
<!--div     = defines a division of a document-->

<h1>Hello!!!</h1>

<div style="background-color: #aaa">
    <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit sequi quasi repudiandae est nisi ipsum odit quos sint. Odio error modi hic ipsam atque optio est aspernatur dolores debitis repudiandae.
    </p>
    <p>
        <span style="color: red;">Lorem ipsum dolor sit, amet consectetur adipisicing elit</span>. Ipsa, inventore iusto? Officia quibusdam iusto quam, provident exercitationem ducimus odit ipsa asperiores culpa obcaecati, aliquam facere, officiis autem eveniet expedita veritatis.
    </p>
    <p>
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Numquam ipsum illum dolore officiis, exercitationem laboriosam suscipit magni earum adipisci commodi delectus mollitia a excepturi consequuntur accusamus veritatis eius aut pariatur!
    </p>
</div>
```

#### Связи

[[HTML div]]
[[HTML span]]
[[Стилизация текста]]
[[Блочные и инлайн элементы]]
