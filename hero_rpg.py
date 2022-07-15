class Character:
    def __init__(self, health, power):
      self.health = health
      self.power = power
             
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False 
               
class Hero(Character):
    def __init__(self, health, power): 
        super(Hero, self).__init__(health, power)
        
    def attack(self, enemy):  
        # Hero attacks Goblin
        enemy.health -= self.power  
        
    def print_status(self):    
        print(f'Hero has {self.health} health and {self.power} power.')
        
class Goblin(Character):
    def __init__(self, health, power):    
       super(Goblin,self).__init__(health,power)
        
    def attack(self, enemy):  
        # Goblin attacks Hero
        enemy.health -= self.power    
        
    def print_status(self):
        print(f'The goblin has {self.health} health and {self.power} power.')
             
        
hero = Hero(10, 5)
goblin = Goblin(6, 2)



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
        #TODO Hero attacks Goblin
        hero.attack(goblin) 
        print(f'Hero does {hero.power} damage to the goblin.')
    if not goblin.alive():
        print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
             
    # else:
    #    print("Please play again...this time enter either a 1, 2 or 3 only.")
    # break  

    if goblin.alive():
       goblin.attack(hero)
       print(f'The goblin does {goblin.power} damage to you.')
       
    if not hero.alive():
        print("You are dead.")



# # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def greet(self, other_person):
# #  return(f'Hello {other_person.name}, I am {self.name}!')
      
# # print(sonny.greet(jordan))      
# # print(jordan.greet(sonny))
