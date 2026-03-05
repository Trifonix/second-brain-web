# Паттерн Singleton

## Что я узнал

Singleton (Одиночка) — это шаблон проектирования, который гарантирует существование только одного экземпляра класса в системе и предоставляет глобальную точку доступа к этому экземпляру. В практике, например в файле `GameStats.js`, реализован класс, который хранит статистику игры и не позволяет создавать новые объекты, обеспечивая единое состояние данных по всей программе. Этот паттерн полезен для логирования, управления конфигурацией или хранения глобальных состояний, где дублирование объектов недопустимо.

### Пример
```javascript
class GameStats {
  constructor() {
    if (GameStats.instance) {
      return GameStats.instance;
    }
    this.score = 0;
    this.level = 1;
    GameStats.instance = this;
  }

  increaseScore(points) {
    this.score += points;
  }

  nextLevel() {
    this.level += 1;
  }
}

// Все экземпляры будут ссылаться на один объект
const stats1 = new GameStats();
const stats2 = new GameStats();

stats1.increaseScore(10);
console.log(stats2.score); // 10, так как stats1 и stats2 — один объект
```

#### Связи

[[Паттерны проектирования]]
[[Классы и объекты]]
