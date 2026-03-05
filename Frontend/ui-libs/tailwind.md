# Tailwind CSS: Практический пример веб-страницы

## Что я узнал

В этом примере показано, как с помощью **Tailwind CSS** можно создавать современную адаптивную веб-страницу с тёмной и светлой темой. Основные элементы включают:

- **Сетку страницы** с использованием `grid` и `max-w-screen-xl` для центрального контейнера.
- **Header** с навигацией и адаптивным меню для мобильных устройств.
- **Breadcrumbs** для навигации по разделам сайта.
- **Баннеры и карточки постов** с изображениями, градиентами и overlay для текста.
- **Сайдбар** с популярными темами и подпиской на рассылку.
- **Footer** с информацией о компании, контенте и контактами.
- Использование **тёмной темы** через `.dark` класс и пользовательский вариант `@custom-variant dark`.
- Настройка компонентов через `@layer components` и утилиты `@apply` для кнопок, ссылок и пагинации.
- **Анимации и переходы** через `transition-all duration-300` для плавного hover-эффекта.

Пример демонстрирует сочетание **utility-first подхода Tailwind** с HTML-структурой для быстрого создания адаптивного дизайна.

### Пример
```html
<header class="px-2 border-b flex items-center justify-between h-14">
  <a href="#" class="uppercase font-bold text-purple-800 dark:text-purple-400">webDev</a>
  <nav class="hidden md:flex items-center">
    <ul class="inline-flex items-center">
      <li><a href="#" class="header-link">Home</a></li>
      <li><a href="#" class="header-link">About</a></li>
      <li><a href="#" class="header-link">Contact</a></li>
    </ul>
    <ul class="inline-flex items-center">
      <li><button class="header-btn">Login</button></li>
      <li><button class="header-btn">Register</button></li>
    </ul>
  </nav>
</header>
```

```css
.header-link {
  @apply dark:text-slate-200 dark:hover:text-purple-400 dark:hover:border-purple-500 transition-all duration-300 inline-block py-3 px-2 border-b-2 border-transparent hover:text-purple-800 hover:border-purple-800 text-gray-500 font-semibold;
}

.header-btn {
  @apply dark:border-indigo-500 dark:text-indigo-500 dark:hover:bg-indigo-500 dark:hover:text-white transition-all duration-300 ml-2 py-1 px-3 border-2 rounded-full border-indigo-600 text-indigo-600 hover:text-white hover:bg-indigo-800 focus:outline-none focus:ring focus:ring-violet-300 cursor-pointer;
}
```

#### Связи

[[Tailwind CSS Utility-first]]
[[Адаптивный дизайн]]
[[Темная тема CSS]]
[[Grid layout]]
[[Компоненты UI]]
