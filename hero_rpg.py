# import random()

class Character:
    def __init__(self, health, power):
      self.health = health
      self.power = power
                             
    def attack(self, enemy):         
        enemy.health -= self.power  
        # Hero attacks Goblin
        if (self.character_name == "Hero"):
            print(f'You do {self.power} damage points to the {enemy.character_name}.') 
     # Goblin attacks Hero      
        elif(self.character_name == "Goblin"):             
            print(f'The {self.character_name} does {self.power} damage points to you.')     
                       
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False 
                           
class Hero(Character):
    def __init__(self, health, power): 
        self.character_name = "Hero"
        super(Hero, self).__init__(health, power)
       
            
    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False 
        
    def print_status(self):
        print(f'The {self.character_name} has {self.health} power points and {self.power} health points.') 
        
             
class Goblin(Character):
    def __init__(self, health, power):  
        self.character_name = "Goblin"  
        super(Goblin,self).__init__(health,power)

    # def attack(self, enemy):         
    #     enemy.health -= self.power  
    #     print(f'You do {self.power} damage points to the {enemy.character_name}.')         
        
    def print_status(self):
        print(f'The {self.character_name} has {self.health} power points and {self.power} health points.') 
        
    # def alive(self):
    #     if self.health > 0:
    #         return True        
    #     else:
    #         return False
        
hero = Hero(10, 5)
goblin = Goblin(6, 2 )



while goblin.alive() and hero.alive():
    print(' ')
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end =' ')
    
    raw_input = input()
    if raw_input == "1" :
        hero.attack(goblin)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break           
    else:
       print("Please play again...this time enter either a 1, 2 or 3 only.")
       break  
    
    if goblin.alive():
       goblin.attack(hero)     
    # if not hero.alive():
    #     print("You are dead.")



# # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def doublePointsAttack(self,enemy):
#         power_int = random.randint(1, 5)
#         if power_int == 5:
#             enemy.health -= self.power * 2
#             print("\nDouble damage points!")
#         else:
#             enemy.health -= self.power
#             print(f"{enemy.name} receives {self.power} damage points from {self.name} .")
#             if enemy.health <= 0:
#                 print(f"The {enemy.name} is dead.")