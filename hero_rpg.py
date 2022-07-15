class Hero:
    def __init__(self, health, power): 
        self.health = health
        self.power = power
        
    def attack(self, enemy):  
        # Hero attacks Goblin
        enemy.health -= self.power  
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False    
        
class Goblin:
    def __init__(self, health, power):    
        self.health = health        
        self.power = power
        
    def attack(self, enemy):  
        # Goblin attacks Hero
        enemy.health -= self.power    
    
    def alive(self):
        if self.health > 0:
            return 'False'
        else:
            return 'True'         
        
hero = Hero(10, 5)
goblin = Goblin(6, 2)
# 



while goblin.alive() and hero.alive():
    print("Hero has {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    
    raw_input = input()
    if raw_input == "1":
        hero.attack(goblin)
        print("Hero does {} damage to the goblin.".format(hero.power))
    if not goblin.alive():
        print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
             
    else:
       print("Please play again...this time enter either a 1, 2 or 3 only.")
    break  

    if goblin.alive():
       goblin.attack(hero)
       print("The goblin does {} damage to you.".format(goblin.power))
       
    if not goblin.alive():
        print("You are dead.")



# # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def greet(self, other_person):
# #  return(f'Hello {other_person.name}, I am {self.name}!')
      
# # print(sonny.greet(jordan))      
# # print(jordan.greet(sonny))
