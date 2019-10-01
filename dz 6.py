# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

'''class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed != 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, side):
        if side == 1:
            print('Машина поворачивает налево')
        if side == 2:
            print('Машина поворачивает направо')


TownCar = Car(60, 'green', 'zhiguli', '')
SportCar = Car(220, 'black', 'ferrari', '')
WorkCar = Car(80, 'yellow', 'kia', '')
PoliceCar = Car(80, 'blue', 'lada', '...')'''

#medium

'''class Person:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def _calculate_damage(self, enemy):
        return self.damage / enemy.armor

    def attack(self, enemy):
        enemy.health -= self._calculate_damage(enemy)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:

    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.health > 0 and self._enemy.health > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player
        if player.health > 0:
            print('вы победили.')
        else:
            print('you died.')


player = Player('Max', 100, 1.2, 10)
enemy = Enemy('Megadeath', 100, 1.1, 10)
game = Game(player, enemy)

game.start() '''