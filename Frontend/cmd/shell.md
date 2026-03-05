# Командные оболочки: CMD, PowerShell и Bash

## Что я узнал

Современная работа с файловой системой и процессами может выполняться через разные оболочки:

- **CMD (Windows Command Prompt)** — классическая командная строка Windows. Поддерживает базовые команды для создания, удаления и переименования файлов и папок.
- **PowerShell** — расширенная оболочка Windows с поддержкой объектов, скриптов и более мощной работы с файловой системой и процессами.
- **Bash (Linux / macOS)** — стандартная оболочка Unix-подобных систем, поддерживает цепочки команд, скрипты и работу с переменными окружения.

В PowerShell ключевые команды включают:

- `gl` / `pwd` / `get-location` — отображает текущий рабочий каталог.
- `cd` — изменяет текущий каталог:
  ```text
  cd desktop
  cd ..
  cd d:
```

* `dir` / `ls` — вывод всех файлов и папок.
* `clear` / `cls` — очистка экрана.
* `mkdir` — создание директорий:

  ```text
  mkdir img
  mkdir css, js
  ```
* `ren` — переименование файлов или папок:

  ```text
  ren css scss
  ```
* `rmdir` — удаление папок и файлов:

  ```text
  rmdir js
  rmdir new.txt
  rmdir css, html
  ```
* `help` — просмотр справки по команде (выход из справки `CTRL + C`).
* `ni` — создание файлов:

  ```text
  ni text.txt
  ```
* `cp` — копирование файлов или папок:

  ```text
  cp index.html fonts
  cd fonts
  ls
  ```
* `mv` — перемещение или переименование файлов и папок:

  ```text
  mv index.html ..\
  ```
* `ps` — получение списка процессов, после чего можно завершить процесс с помощью `kill <id>`:

  ```text
  Open notepad.exe
  ps -> запомнить id процесса
  kill 7488
  ```

Примеры создания структуры сайта и файлов:

```javascript
mkdir mySite, mySite\css, mySite\js, mySite\img
ni mySite\index.html, mySite\css\style.css, mySite\css\media.css, mySite\js\main.js
```

Использование этих команд позволяет полностью управлять файловой системой, создавать проекты и работать с процессами как в Windows, так и в Linux через Bash или PowerShell.

### Пример

```javascript
// PowerShell: создание проекта и файлов
mkdir mySite
mkdir mySite\css, mySite\js, mySite\img
ni mySite\index.html
ni mySite\css\style.css
ni mySite\css\media.css
ni mySite\js\main.js
```

#### Связи

[[PowerShell]]
[[CMD]]
[[Bash]]
[[Файловая система]]
