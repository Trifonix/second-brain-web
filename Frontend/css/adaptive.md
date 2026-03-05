# CSS Медиа-запросы и адаптивная вёрстка

## Что я узнал

Адаптивная вёрстка позволяет интерфейсу корректно отображаться на разных устройствах: телефонах, планшетах, ноутбуках и больших мониторах. Основной инструмент для этого — **медиа-запросы (`@media`)**.

Медиа-запросы позволяют применять CSS-правила только при выполнении определённых условий: ширины экрана, высоты, ориентации устройства, типа устройства или даже возможностей ввода.

Чаще всего используются условия:

- `max-width` — правила применяются **если ширина экрана меньше или равна указанной**
- `min-width` — правила применяются **если ширина экрана больше или равна указанной**
- `max-height` / `min-height` — ограничения по высоте
- `orientation` — ориентация экрана (`portrait` или `landscape`)
- `hover` — поддерживает ли устройство наведение курсора
- `print` — стили для печати

Существует два распространённых подхода к адаптивной разработке:

**Desktop First**

Сначала создаётся дизайн для больших экранов, затем через `max-width` добавляются правила для меньших экранов.

**Mobile First**

Сначала пишется базовый CSS для мобильных устройств, а затем через `min-width` добавляются стили для более широких экранов. Этот подход считается более современным.

Медиа-запросы позволяют:

- изменять количество колонок в grid
- уменьшать размер текста
- менять ориентацию текста
- адаптировать интерфейс под сенсорные устройства
- задавать отдельные стили для печати

Также часто используются **относительные единицы измерения**, такие как:

- `%` — процент от родительского элемента
- `vw` — процент ширины окна браузера
- `vh` — процент высоты окна браузера

Это помогает интерфейсу гибко масштабироваться.

### Пример
```javascript
.box {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 48px;
  background-color: tomato;
  height: 100px;
  width: 50%;
  min-width: 200px;
  max-width: 500px;
}

.banner {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: salmon;
  min-height: 100vh;
}

.catalog-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.catalog-item {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: lightskyblue;
  min-height: 100px;
}

@media (max-width: 700px) {
  .catalog-title {
    font-size: 36px;
  }

  .catalog-list {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 400px) {
  .catalog-list {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 401px) {
  .catalog-list1 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 701px) {
  .catalog-title1 {
    font-size: 64px;
  }

  .catalog-list1 {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (orientation: portrait) {
  .banner-title1 {
    writing-mode: vertical-lr;
  }
}

@media print {
  body {
    font-size: 36px;
  }

  a {
    color: black;
    text-decoration: underline;
  }
}

@media (hover: hover) {
  button:hover {
    background-color: crimson;
  }
}
```

#### Связи

[[CSS]]
[[Адаптивная верстка]]
