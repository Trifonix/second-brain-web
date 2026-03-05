# Паттерн Factory Method

## Что я узнал

Factory Method (Фабричный метод) — это шаблон проектирования, который позволяет создавать объекты разных типов, не указывая конкретные классы при их создании напрямую. В практике, например, в файлах `Character.js` и `CharacterFactory.js`, используется фабрика для генерации различных типов персонажей (маг, воин, лучник) на основе входных данных. Это упрощает расширение приложения новыми типами персонажей и изолирует клиентский код от конкретных реализаций классов.

### Пример
```javascript
// Character.js
class Character {
  constructor(name) {
    this.name = name;
  }
  attack() {
    console.log(`${this.name} атакует!`);
  }
}

class Warrior extends Character {
  attack() {
    console.log(`${this.name} наносит удар мечом!`);
  }
}

class Mage extends Character {
  attack() {
    console.log(`${this.name} применяет магию!`);
  }
}

// CharacterFactory.js
class CharacterFactory {
  static create(type, name) {
    switch(type) {
      case 'warrior':
        return new Warrior(name);
      case 'mage':
        return new Mage(name);
      default:
        return new Character(name);
    }
  }
}

// Использование
const hero1 = CharacterFactory.create('warrior', 'Aragorn');
const hero2 = CharacterFactory.create('mage', 'Gandalf');

hero1.attack(); // Aragorn наносит удар мечом!
hero2.attack(); // Gandalf применяет магию!
```

#### Связи

[[Паттерны проектирования]]
[[Классы и объекты]]
