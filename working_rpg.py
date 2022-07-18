# In this simple RPG game, the hero fights the enemy. He has the options to:

# 1. fight enemy
# 2. do nothing - in which case the enemy will attack him anyway
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
  
  def attack(self, enemy):
    enemy.health -= self.power   
    if (self.character_name == "Hero"):
      print(f'You do {self.power} damage points to the {enemy.character_name}.')  
    elif(self.character_name == "Goblin"):         
      print(f"The {self.character_name} does {self.power} damage to you.")
    
  def print_status(self, enemy): 
    if(self.character_name == "Hero"):
      print(f'You have {self.health} power points and {self.power} health points.') 
    elif(self.character_name == "Goblin"):  
      print(f"The {self.character_name} has {self.health} power point(s) and {self.power} health points.") 
   
                


#&----------Hero Class----------#
class Hero(Character):
  def __init__ (self, health, power):
    self.character_name = "Hero"
    super(Hero, self).__init__(health, power)
    
  # def attack(self, enemy):
  #   #Hero attacks Goblin
  #   enemy.health -= self.power
  #   print(f'You do {self.power} damage to the enemy.')  
    
    
  # def alive(self):
  #   if self.health > 0:
  #     return True
  #   else:
  #     return False
    
  # def print_status(self, enemy): 
  #   if enemy.health <= 0:
  #     print(f"The {enemy.character_name} is dead.") 
      
        
 #&----------Goblin Class----------#   
class Goblin(Character):
  def __init__(self, health, power):
    self.character_name = "Goblin"
    super(Goblin, self).__init__(health, power)
    
          
def main():
  
    hero = Hero(10, 5)
    goblin = Goblin( 6, 2)   
    
    while goblin.alive() and hero.alive(): 
        print()
        hero.print_status(goblin)
        goblin.print_status(hero)
             
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()        
        if raw_input == "1":
          hero.attack(goblin)            
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")
        
        #enemy attacks hero    
        if goblin.alive() == True:  
          goblin.attack(hero)
          
        if hero.health <= 0:
          print("You are dead.")
          
        if goblin.health <= 0:
            print(f"The Goblin is dead.")   
               
      
     
              
            
   

        
       

main()