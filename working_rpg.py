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
    # if enemy.character_name != "Zombie":
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
      
  # def retorts(self, enemy):
  #   number = 0
    
  #   for number in retorts:
  #     number = (int(hero.health/enemy.power))
  #     if number == 1:
  #         print("Are you sure?")              
  #     elif number == 2 : 
  #         print("Don't just stand there...")
  #     elif number == 3:
  #         print("'You're killing me Smalls!'")   
  #     elif number == 4:
  #         print("The end is near.")  
  #     elif number == 5:
  #         print("RIP")   
  #     number +=1
  #     break     
              
   
                


#&----------Hero Class----------#
class Hero(Character):
  def __init__ (self, health, power):
    self.character_name = "Hero"
    super(Hero, self).__init__(health, power)
    
  def retorts(goblin):
    number = 0
    for i  in range(number):
      number = (int(hero.health/enemy.power))
      if number == 1:
          
          print("Are you sure?")   
          number = i           
      elif number == 2 : 
          print("Don't just stand there...")
          number = i
      elif number == 3:
          print("'You're killing me Smalls!'")   
          number = i
      elif number == 4:
          print("The end is near.")  
          number = i
      elif number == 5:
         number = i
         print("RIP")   
    number +=1
         
              
  # def attack(self, enemy):
  #   #Hero attacks enemy
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
    
 
    
    
#&-----------Zombie Class----------#
class Zombie(Character):
  def __init__(self, health, power):
    self.character_name = "Zombie"
    super(Zombie,self).__init__(health, power)
 
 
hero = Hero(10, 5)
goblin = Goblin( 6, 2)   
zombie = Zombie(10, 1)


       
def main():       
    while goblin.alive() and hero.alive(): 
        print()
        hero.print_status(goblin)
        goblin.print_status(hero)
        print()     
        print("What do you want to do?")
        print(f"1. Fight ")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        
        raw_input = input()        
        if raw_input == "1":
          hero.attack(goblin)            
        elif raw_input == "2":
          hero.retorts()
        
          
          # number = 0   
          # for i in range(5): 
          #     # if number == 1:
          #       print("Are you sure?")
          #       number+=1
          #     # elif number == 2 : 
          #       print("Don't just stand there...")
          #     # elif number == 3:
          #       print("'You're killing me Smalls!'")   
          #     # elif number == 4:
          #       print("The end is near.")  
          #     # elif number == 5:
          #       print("RIP")         
          # number +=1 
          # break
                
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
        elif goblin.health <= 0:
          print(f"The Goblin is dead.")  
            
main()       
     
             
               
      
     
              
            
   

        
       

