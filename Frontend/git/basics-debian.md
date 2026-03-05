# Основы GIT в Linux (Debian)

## Что я узнал

GIT в Linux (Debian) используется через терминал и предоставляет те же возможности контроля версий, что и в Windows, но с особенностями командной оболочки и путей к файлам.

Основные шаги и команды:

1. **Установка GIT**
   ```bash
   sudo apt update
   sudo apt install git
   git --version
```

Проверка установки и версии GIT.

2. **Настройка пользователя**

   ```bash
   git config --global user.name "Ваше Имя"
   git config --global user.email "email@example.com"
   ```

   Устанавливает имя и email для всех коммитов.

3. **Инициализация репозитория**

   ```bash
   git init
   ```

   Создаёт новый локальный репозиторий в текущей папке.

4. **Добавление файлов и создание коммита**

   ```bash
   git add .
   git commit -m "Первый коммит"
   ```

   `git add .` добавляет все изменения, `git commit` сохраняет их с сообщением.

5. **Работа с удалённым репозиторием**

   ```bash
   git remote add origin https://github.com/username/repo.git
   git push -u origin main
   ```

   Привязывает удалённый репозиторий и отправляет изменения.

6. **Просмотр состояния и истории**

   ```bash
   git status
   git log --oneline
   ```

   Проверка текущего состояния и истории коммитов.

7. **Работа с ветками**

   ```bash
   git branch feature-branch
   git checkout feature-branch
   git merge feature-branch
   ```

   Создание ветки, переключение на неё и слияние с основной.

GIT в Linux особенно удобно использовать вместе с редакторами кода и shell-скриптами, что делает процесс контроля версий более гибким и автоматизируемым.

### Пример

```bash
# Создание репозитория и коммит
git init
git add .
git commit -m "Инициализация проекта в Debian"
```

#### Связи

[[GIT]]
[[Linux Terminal]]
[[Контроль версий]]
[[Командная строка Linux]]
