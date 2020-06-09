#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self,enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
        print("The goblin has {} health and {} power.".format(
            goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

class Goblin(Character):
    pass
class Hero(Character):
    pass
goblin = Goblin(6, 2)
hero = Hero(10, 5)
def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2


    while goblin.alive() and hero.alive():
        
        hero.print_status()
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if not goblin.alive():
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if not hero.alive():
                print("You are dead.")


main()
