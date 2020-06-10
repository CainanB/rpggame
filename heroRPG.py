#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random
def store():
    def super_tonic():
        hero.currenthealth = 10
        print("Hero health restored to 10")
    def armor():
        hero.armor += 1
        print("Hero gained 1 Armor")
    def evade():
        if hero.evade < 10:
            hero.evade += 2
            print("Hero gained +2 evade")
        else:
            print("Cannot increase evade attribute any higher!")    
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




class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
class Tonic(Item):
    def __init__(self, name, cost, heal_amount):
        super().__init__(name, cost)
        self.heal_amount = heal_amount
    def use(self, person):
        print(f"Health before using {person.currenthealth}")
        if person.currenthealth + self.heal_amount > person.health:
            person.currenthealth = person.health
        else:
            person.currenthealth += self.heal_amount
        print(f"Health after using {person.currenthealth}")
    def list_info(self):
        print(f"{self.name}, Cost: {self.cost} gold, Aciton: +{self.heal_amount} health")
class Armor(Item):
    def __init__(self, name, cost, armor_amount):
        super().__init__(name, cost)
        self.armor_amount = armor_amount
    def use(self, person):
        upgradedArmor = person.armor + self.armor_amount
        return upgradedArmor
    def list_info(self):
        print(f"{self.name}, Cost: {self.cost} gold, Action: +{self.armor_amount} armor")

class Store:
    def __init__(self):
        self.items = []
    def create_tonic(self, name, cost, heal_amount):
        temp = Tonic(name, cost, heal_amount)
        self.items.append(temp)
        print("tonic created with these values")
        print(f"{temp.name} {temp.cost} {temp.heal_amount}")
    def create_armor(self, name, cost, armor_amount):
        temp = Armor(name, cost, armor_amount)
        self.items.append(temp)
    def list_items(self):
        for i in range(len(self.items)):
            print(f"{i + 1}.)")
            self.items[i].list_info()
        print("Please enter number of item you would like to buy")
        chosen_item = int(input(">>> "))
        chosen_store_item = self.items[chosen_item - 1]
        print(f"You purchased {chosen_store_item.name}")
        hero.items.append(chosen_store_item)


store = Store()
store.create_armor("Armor", 2, 2)
store.create_tonic("Super Tonic", 2, 10)
# store.list_items()


# super_tonic = Tonic("Super Tonic", 2, 10)
# tonic = Tonic("Tonic", 1, 3)


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.currenthealth = health
        self.evade = 0
        self.armor = 0
    def attack(self,enemy):
        ranNum = random.randint(1,20)
        if ranNum <= enemy.evade:
            print("Attack missed!")
        else:
            attackAmountLeft = abs(enemy.armor - self.power)
            totalAttack = self.power - enemy.armor
            enemy.currenthealth -= totalAttack
            print("The enemy does {} damage to you.".format(totalAttack))

        
    def alive(self):
        if self.currenthealth > 0:
            return True
        else:
            return False    
    def print_status(self, enemy):
        print("You have {} health and {} power.".format(self.currenthealth, self.power))
        print("The {} has {} health and {} power.".format(
            enemy.name, enemy.currenthealth, enemy.power))
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. use item")
        print("> ", end=' ')


class Enemy(Character):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power)
        self.bounty = bounty

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.gold = 0
        self.items = []
        


    def attack(self,enemy):
        ranNum = random.randint(1,5)
        totalAttack = self.power
        print(ranNum)
        if ranNum == 1:
            totalAttack *= 2
            enemy.currenthealth -= totalAttack 
        else:
            enemy.currenthealth -= totalAttack
        return totalAttack
    # def go_to_shop(self):
    #     item = store()
    #     self.items.append(item)
    #     for key in item.keys():
    #         print(f"You purchased {key}")
        # print(self.items[0]["Super Tonic"]())
    def use_item(self):
        if len(self.items) == 0:
            print("You have no items to use!\n")
        else:
            print("Which item would you like to use")
            for item in range(len(self.items)):
                print(f"{item + 1}. {self.items[item].name}")
                # for key in self.items[item].keys():
                #     print(f"{item + 1}. {key}")
            user_choice = int(input(">> "))
            
            # for itemUsed in self.items[user_choice - 1]:
            self.items[user_choice - 1].use(hero)
            # print(f"health is {self.currenthealth}")
            del self.items[user_choice - 1]
    def print_stats(self):
        print(f"""
        Health: {self.currenthealth}
        Power: {self.power}
        Evade: {self.evade}
        Armor: {self.armor}
        Gold: {self.gold}
        """)
class Medic(Enemy):
    def __init__(self, name, health, power):
        super().__init__(name, health, power, 3)
    
    def afterAttacked(self, damagedTaken):
        ranNum = random.randint(1,5)
        if ranNum == 1:
            self.currenthealth += 2
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
            print(self.currenthealth)
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
        3.  Use Item
        4.  Print Status
        """)
        if user_choice == "1":
            # hero.go_to_shop()
            store.list_items()
        elif user_choice == "3":
            hero.use_item()
        elif user_choice == "2":
            fight()
        elif user_choice == "4":
            hero.print_stats()
        else:
            pass 
        
    
def fight():
    enemy = enemies[random.randint(0, len(enemies) -1)]
    enemy.currenthealth = enemy.health
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
                print(f"You collected {enemy.bounty} gold for defeating {enemy.name}")
                hero.gold += enemy.bounty
                
                
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # enemy attacks hero
            enemy.attack(hero)
            
            if not hero.alive():
                print("You are dead.")

main()
