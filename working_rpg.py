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
    
  def rounds(self, hero):    
    round = hero.health/self.power
    
    
#&-----------Zombie Class----------#
class Zombie:
  def __init__(self, name, health, power):
    self.name = name
    self.health = health
    self.power = power
    
 print(round)         
def main():
  
    hero = Hero(10, 5)
    goblin = Goblin( 6, 2)   
    zombie = Zombie("Brains",10000,10)
    
    while goblin.alive() and hero.alive(): 
        print()
        hero.print_status(goblin)
        goblin.print_status(hero)
        print()     
        print("What do you want to do?")
        print("1. Fight")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        
        raw_input = input()        
        if raw_input == "1":
          hero.attack(goblin)            
        elif raw_input == "2":
          print("Really?!!")
          goblin.round(hero)
          count = 0       
          for i in round: 
              print("Don't just stand there...")
              count +=1 
                
        elif raw_input == "3":
            print("Goodbye Chicken!")
            break
        else:
            print(f"You didn't select a 1, 2 or 3")
            answer = input("Play again...Yes?")
            if answer.lower() == 'y':
              main()
            else:
              print("See you on the flip side - Bye!")  
            break
        
        #enemy attacks hero    
        if goblin.alive() == True:  
          goblin.attack(hero)
          
        if hero.health <= 0:
          print("You are dead.")
          
        if goblin.health <= 0:
            print(f"The Goblin is dead.")   
               
      
     
              
            
   

        
       

main()