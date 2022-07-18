# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
  def __init__ (self, health, power):
    self.health = health
    self.power = power
    
  def attack(self):
    #Hero attacks goblin
    goblin.health -= hero.power
    print(f'You do {self.power} damage to the goblin.')
    if goblin.health <= 0:
      print("The goblin is dead.")
        
    
    
class Goblin:
  def __init__(self, health, power):
    self.health = health
    self.power = power    
    
  def attack(self):
    if goblin.health > 0:
    # Goblin attacks hero
      hero.health -= goblin.power
      print(f"The goblin does {goblin.power} damage to you.")
      if hero.health <= 0:
        print("You are dead.")    
    
    

hero = Hero(10, 5)
goblin = Goblin(6, 2)











def main():

 

    while goblin.health > 0 and hero.health > 0:
        print()
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin {goblin.health} health and {goblin.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        
        if raw_input == "1":
          hero.attack()       
          goblin.attack()  
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

       

main()