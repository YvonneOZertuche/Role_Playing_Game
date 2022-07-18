# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#&----------Character Class----------#
class Character:
  def __init__(self, health, power):
    self.health = health
    self.power = power
    
  def alive(self):
    if self.health > 0:
      return True
    else:
      return False    


#&----------Hero Class----------#
class Hero(Character):
  def __init__ (self, health, power):
    self.health = health
    self.power = power
    
  def attack(self, enemy):
    #Hero attacks goblin
    enemy.health -= self.power
    print(f'You do {self.power} damage to the goblin.')  
    
  # def alive(self):
  #   if self.health > 0:
  #     return True
  #   else:
  #     return False
    
  def print_status(self, enemy): 
    if enemy.health <= 0:
      print("The enemy is dead.")
        
 #&----------Goblin Class----------#   
class Goblin(Character):
  def __init__(self, health, power):
    self.health = health
    self.power = power    
    
  def attack(self, enemy):
    #Goblin attacks hero
      enemy.health -= self.power
      print(f"The goblin does {self.power} damage to you.")
      
  # def alive(self):
  #   if self.health > 0:
  #     return True
  #   else:
  #     return False
    
  def print_status(self, enemy): 
    if enemy.health <= 0:
      print("You are dead.")    
             
    
    
hero = Hero(10, 5)
goblin = Goblin(6, 2)


#&----------Logic----------
def main():
    while goblin.alive() and hero.alive(): 
        print()
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()        
        if raw_input == "1":
          hero.attack(goblin)            
          hero.print_status(goblin)   
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        
        #Goblin attacks hero    
        if goblin.alive() == True:  
          goblin.attack(hero)
          goblin.print_status(hero)
          
      
     
              
            
   

        
       

main()