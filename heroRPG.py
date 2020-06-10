#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
def store():
    def super_tonic():
        return 10
    def armor():
        return
    def evade():
        pass
    store = [
        {"Super Tonic" : super_tonic},
        {"Armor" : armor},
        {"Evade" : evade}
    ]

    
    
    
    for item in range(len(store)):
        for key in store[item].keys():
            print(f"{item + 1}. {key}")
        

    print("Please enter number of item you would like to buy")
    chosen_item = int(input(">>> "))
    return store[chosen_item - 1]


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self,enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False    
    def print_status(self, enemy):
        print("You have {} health and {} power.".format(self.health, self.power))
        print("The {} has {} health and {} power.".format(
            enemy.name, enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')

class Enemy(Character):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power)
        self.bounty = bounty

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.coins = 0
        self.items = []


    def attack(self,enemy):
        ranNum = random.randint(1,5)
        totalAttack = self.power
        print(ranNum)
        if ranNum == 1:
            totalAttack *= 2
            enemy.health -= totalAttack 
        else:
            enemy.health -= totalAttack
        return totalAttack
    def go_to_shop(self):
        item = store()
        self.items.append(item)
        for key in item.keys():
            print(f"You purchased {key}")
        # print(self.items[0]["Super Tonic"]())
    def use_item(self):
        print("Which item would you like to use")
        for item in self.items:
            for key in item.keys():
                print(key)
class Medic(Enemy):
    def __init__(self, name, health, power):
        super().__init__(name, health, power, 3)
    
    def afterAttacked(self, damagedTaken):
        ranNum = random.randint(1,5)
        if ranNum == 1:
            self.health += 2
            print(f"{self.name} used heal and gained +2 health")

class Zombie(Enemy):
    def __init__(self, name, health, power,):
        super().__init__(name, health, power, 6)
    def alive(self):
        return True
class Goblin(Enemy):
    def __init__(self, name, health, power,):
        super().__init__(name, health, power, 2)
        
class Shadow(Enemy):
    def __init__(self, name, health, power,):
        super().__init__(name, health, power, 3)
    def afterAttacked(self, damagedTaken):
        ranNum = random.randint(1,10)
        if ranNum >= 1:
            print(self.health)
            print("Your attack missed!")
            self.health += damagedTaken
class Giant(Enemy):
    def __init__(self, name, health, power,):
        super().__init__(name, health, power, 7)
class Mage(Enemy):
    def __init__(self, name, health, power,):
        super().__init__(name, health, power, 5)

goblin = Goblin("goblin", 6, 2)
hero = Hero("hero", 10, 5)
zombie = Zombie("zombie", 10, 1)
medic = Medic("medic", 10, 3)
shadow = Shadow("shadow", 1, 2)
giant = Giant("giant", 15, 6)
mage = Mage("mage", 8, 4)
enemies = [goblin]

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2
    while True:
        user_choice = input("""
        What would you like to do?
        1.  Shop Store
        2.  Fight Enemy
        """)
        if user_choice == "1":
            hero.go_to_shop()
        else:
            break 
        
    enemy = enemies[random.randint(0, len(enemies) -1)]
    print(f">>> Random enemy is the {enemy.name} <<<")
    while enemy.alive() and hero.alive():

            
        hero.print_status(enemy)
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            attackTotal = hero.attack(enemy)
            print("You do {} damage to the enemy.".format(attackTotal))
            try:
                enemy.afterAttacked(attackTotal)
            except:
                pass
                
            if not enemy.alive():
                print("The enemy is dead.")
                print(f"You collected {enemy.bounty} coins for defeating {enemy.name}")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # enemy attacks hero
            enemy.attack(hero)
            print("The enemy does {} damage to you.".format(enemy.power))
            if not hero.alive():
                print("You are dead.")


main()
