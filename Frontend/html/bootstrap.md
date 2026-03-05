# Внешние фреймворки и библиотеки: Bootstrap 5

## Что я узнал

Помимо чистого HTML и JavaScript, в веб-разработке часто используют **внешние фреймворки и библиотеки**, которые ускоряют создание интерфейсов и упрощают стилизацию элементов. Один из самых популярных — **Bootstrap**.  

Bootstrap предоставляет готовые стили и компоненты, позволяя быстро создавать адаптивные страницы без написания большого количества CSS. Для подключения Bootstrap можно использовать **CDN** — ссылку на внешние файлы стилей и скриптов, которые загружаются напрямую с сервера Bootstrap.

Основные возможности Bootstrap:
- **Сетки (grid system)**: с помощью классов `container`, `row` и `col-*` можно создавать адаптивные макеты. Например, `col-lg-6` создаёт колонку, занимающую половину ширины экрана на больших устройствах.
- **Навигационные панели (navbar)**: готовые меню, которые автоматически адаптируются под мобильные устройства.
- **Кнопки (btn, btn-primary, btn-secondary и т.д.)**: готовые стилизованные кнопки с разными цветами и эффектами при наведении.
- **Карточки (card)**: контейнеры для контента с заголовком, текстом, изображением и кнопками.

Использование Bootstrap позволяет фокусироваться на логике и структуре страницы, не тратя время на мелкие детали дизайна и стилизации.

### Пример
```javascript
<!-- Подключение Bootstrap через CDN -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet">

<div class="container">
    <div class="row">
        <div class="col-lg-6">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">This is a card using Bootstrap classes.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Another card</h5>
                    <p class="card-text">Bootstrap grid helps make responsive layouts easily.</p>
                    <a href="#" class="btn btn-secondary">Click me</a>
                </div>
            </div>
        </div>
    </div>
</div>
```

#### Связи

[[Bootstrap]]
[[CSS фреймворки]]
[[Grid system]]
[[HTML компоненты]]
[[Веб-разработка]]
