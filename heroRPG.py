#!/usr/bin/env python

# In this simple RPG game, the hero fights randomly generated enemies. 

import random

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
        if self.name == "Revive Tonic":
            addMessage = " Automatically used in battle when health drops below 1 HP"
        else:
            addMessage = ""
        print(f"{self.name}, Cost: {self.cost} gold, Action: +{self.heal_amount} health{addMessage}")
class Armor(Item):
    def __init__(self, name, cost, armor_amount):
        super().__init__(name, cost)
        self.armor_amount = armor_amount
    def use(self, person):
        person.armor += self.armor_amount
        print(f"Your new armor amount is {person.armor}")
        
    def list_info(self):
        print(f"{self.name}, Cost: {self.cost} gold, Action: +{self.armor_amount} armor")
class Swap(Item):
    def __init__(self, name, cost):
        super().__init__(name, cost)
    def use(self, person_1, person_2):
        print(f"{person_1.name}'s previous power of {person_1.power}")
        print(f"{person_2.name}'s previous power of {person_2.power}")
        temp_cont = person_1.power
        person_1.power = person_2.power
        person_2.power = temp_cont
        print(f"{person_1.name}'s swapped power of {person_1.power}")
        print(f"{person_2.name}'s swapped power of {person_2.power}")
    def list_info(self):
        print(f"{self.name}, Cost: {self.cost} gold, Action: Swaps Hero and Enemy Power for 1 turn")
class Magic(Item):
    def __init__(self, name, cost, damage_amount):
        super().__init__(name, cost)
        self.damage_amount = damage_amount
        self.type = "Magic"
    def use(self, person):
        person.currenthealth -= self.damage_amount
        print(f"You used {self.name} Magic, and did {self.damage_amount} to enemy")
    def list_info(self):
        print(f"{self.name} Magic, Cost: {self.cost} gold, Action: +{self.damage_amount} damage to enemy")
class Store:
    def __init__(self):
        self.items = []
    def create_magic(self, name, cost, damage_amount):
        temp = Magic(name, cost, damage_amount)
        self.items.append(temp)
    def create_tonic(self, name, cost, heal_amount):
        temp = Tonic(name, cost, heal_amount)
        self.items.append(temp)
        # print("tonic created with these values")
        # print(f"{temp.name} {temp.cost} {temp.heal_amount}")
    def create_armor(self, name, cost, armor_amount):
        temp = Armor(name, cost, armor_amount)
        self.items.append(temp)
    def create_swap(self, name, cost):
        temp = Swap(name, cost)
        self.items.append(temp)
    def list_items(self, person):
        for i in range(len(self.items)):
            print(f"{i + 1}.)")
            self.items[i].list_info()
        print(f"{len(self.items) + 1}. Quit")
        print("Please enter number of item you would like to buy\n")

        while True:
            try:
                chosen_item = int(input(">>> "))
                break
            except ValueError:
                print("Please enter a valid number")
        if chosen_item == len(self.items) + 1:
            print(">>  LEAVING STORE.... <<")
            pass
        else:                
            chosen_store_item = self.items[chosen_item - 1]
            if person.gold >= chosen_store_item.cost:
                person.gold -= chosen_store_item.cost
                print(f"You purchased {chosen_store_item.name}")
                if chosen_store_item.name == "Revive Tonic":
                    hero.revive = True
                else:    
                    hero.items.append(chosen_store_item)
            else:
                print(f"You do not have enough gold! You only have {person.gold}")

store = Store()
store.create_armor("Armor", 2, 2)
store.create_tonic("Super Tonic", 2, 10)
store.create_tonic("Revive Tonic", 2, 20)
store.create_swap("Swap", 2)
store.create_magic("Fire", 2, 6)


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.currenthealth = health
        self.evade = 0
        self.armor = 0
        self.swapped = False
    def attack(self,enemy):
        ranNum = random.randint(1,20)
        if ranNum <= enemy.evade:
            print(f"{self.name}'s attack missed!")
        else:
            
            totalAttack = self.power - enemy.armor
            if totalAttack < 0:
                totalAttack = 0
            enemy.currenthealth -= totalAttack
            print("The enemy does {} damage to you.".format(totalAttack))
    def swap(self, person):
        print(f"{person.name}'s previous power of {person.power}")
        print(f"{self.name}'s previous power of {self.power}")
        temp_cont = self.power
        self.power = person.power
        person.power = temp_cont
        print(f"{person.name}'s swapped power of {person.power}")
        print(f"{self.name}'s swapped power of {self.power}")



        
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
        self.evade = 2
        self.items = []
        self.revive = False
        self.current_enemy = None
        


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
            chosen_item = self.items[user_choice - 1]
            if(chosen_item.name == "Swap"):
                self.swapped = True
                
                print(f"Used Swap item, swap will take place next turn {self.swapped}")
            elif chosen_item.type == "Magic":
                chosen_item.use(self.current_enemy)
            else:
                chosen_item.use(hero)
            # print(f"health is {self.currenthealth}")
            del self.items[user_choice - 1]
    def print_stats(self):
        print(f"""
        Health: {self.currenthealth}
        Power: {self.power}
        Evade: {self.evade}
        Armor: {self.armor}
        Gold: {self.gold}
        Have Revive: {self.revive}
        """)
    def use_revive(self):
        if self.revive == True:
            self.currenthealth = 20
            print("Your Revive Tonic has been used")
            print(f"Your health has been restored to {self.currenthealth}")
            self.revive = False
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
hero = Hero("hero", 20, 4)
zombie = Zombie("zombie", 10, 1)
medic = Medic("medic", 10, 3)
shadow = Shadow("shadow", 1, 2)
giant = Giant("giant", 15, 5)
mage = Mage("mage", 8, 4)
enemies = [goblin,medic,giant,mage]

def main():

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
            store.list_items(hero)
        elif user_choice == "3":
            # Line needs to be refactored incase swap item is used
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
    hero.current_enemy = enemy
    

    while enemy.alive() and hero.alive():
        # print(f"{hero.swapped}")
        if hero.swapped:
            hero.swap(enemy) 
            
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
            if hero.currenthealth < 1 and hero.revive == True:
                hero.use_revive()


            if not hero.alive():
                print("You are dead.")
        if hero.swapped:
            hero.swap(enemy) 
            hero.swapped = False
            
main()
