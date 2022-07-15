class Character:
    def __init__(self, health, power):
      self.health = health
      self.power = power
  
    def print_status(self):  
        print(f'Hero has {hero.health} health and {hero.power} power.')
        print(f'The {self.character_name} has {self.health} and {self.power} power.')   
        
    def attack(self, enemy):         
        enemy.health -= self.power  
        # Hero attacks Goblin
        if (self.character_name == "hero"):
            print(f'You do {self.power} damage points to the {enemy.character_name}.') 
        # Goblin attacks Hero      
        elif (self.character_name == "goblin"): 
            print(f'The {self.character_name} does {self.power} damage points to you.')     
                       
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False 
                           
class Hero(Character):
    def __init__(self, health, power): 
        self.character_name = "hero"
        super(Hero, self).__init__(health, power)
        
   
        
class Goblin(Character):
    def __init__(self, health, power):  
        self.character_name = "Goblin"  
        super(Goblin,self).__init__(health,power)
        
    # def attack(self, enemy):  
    #     # Goblin attacks Hero
    #     enemy.health -= self.power    
    #     print(f'The {self.character_name} does {self.power} damage to you.')
        
                     
hero = Hero(10, 5)
goblin = Goblin(6, 2 )



while goblin.alive() and hero.alive():
    print(' ')
    hero.print_status()
    # goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end =' ')
    
    raw_input = input()
    if raw_input == "1" :
        hero.attack(goblin)
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
    if not hero.alive():
        print("You are dead.")



# # #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # def greet(self, other_person):
# #  return(f'Hello {other_person.name}, I am {self.name}!')
      
# # print(sonny.greet(jordan))      
# # print(jordan.greet(sonny))
