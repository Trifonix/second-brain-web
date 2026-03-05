# HTML ссылки, медиа и взаимодействие с пользователем

## Что я узнал

HTML позволяет создавать интерактивные страницы, включая **ссылки, изображения, аудио и видео**.  

Тег `<a>` создаёт ссылку на другую страницу, адрес электронной почты или внешний ресурс. Атрибут `href` задаёт адрес ссылки:
- Локальная страница: `href="index.html"`  
- Email: `href="mailto:fake123@gmail.com"`  
- Внешний сайт: `href="https://en.wikipedia.org/wiki/Shrek"`

Внутри ссылки можно вставлять **текст** или **изображение** через тег `<img>`. Атрибуты изображения:
- `src` — путь к файлу изображения  
- `alt` — альтернативный текст, показывается если изображение не загрузилось  
- `height` — высота изображения  
- `title` — подсказка при наведении на изображение  

HTML позволяет добавлять аудио через тег `<audio>`. Атрибут `controls` добавляет стандартные кнопки управления (play, pause, volume), а `src` указывает путь к файлу.  

Для видео используется тег `<video>`. Атрибуты `width` и `controls` управляют размером и отображением кнопок. Дополнительно можно использовать:
- `autoplay` — воспроизведение сразу после загрузки  
- `muted` — без звука  
- `loop` — зацикливание  
- `<source>` — задаёт путь к видеофайлу и поддерживаемый формат (`mp4`, `webm`, `ogg`)  

Эти элементы делают страницу более интерактивной и мультимедийной, позволяя пользователям не только просматривать текст, но и слушать и смотреть медиа прямо на сайте.

### Пример
```javascript
<h1>This is page 2</h1>

<a href="index.html">Go to page 1</a>

<a href="mailto:fake123@gmail.com">Email me!!!</a>

<a href="https://en.wikipedia.org/wiki/Shrek">
    <img src="https://m.media-amazon.com/images/S/pv-target-images/dbf6812f59e5080cf420f1056bfceb66f7d6a43a8df19ace503ea70596afc0ff.jpg" 
         alt="Shrek" height="120" title="Shrek is shrexy">
</a>

<br>
<p>You can put music file here in 'src'</p>
<audio src="" controls></audio>

<br>
<!--mp4, webm, ogg-->
<video width="400" controls autoplay muted loop>
    <source src="https://videos.pexels.com/video-files/31381823/13390461_1920_1080_30fps.mp4">
</video>
```

#### Связи

[[HTML ссылки]]
[[HTML изображения]]
[[HTML аудио]]
[[HTML видео]]
[[Интерактивный контент]]
