# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
#?Hero Class
class Hero:
  def __init__(hero, health, power):   
    hero.health = health
    hero.power = power
    hero.attack = " "

#?Hero Methods  
    def attack(hero):
        goblin.health -= hero.power
        print(f'You do {hero.power} damage to the goblin.')
        if goblin.health <= 0:
            print("The goblin is dead.")
          
    def print_alive(hero):  
        while hero.alive > 0: 
            print(f'You have {hero.health} and {hero.power}.')
            break
        
    def print_status(hero):  
        if hero.health <= 0:
            print('You are dead.')
#              
#*Goblin Class
class Goblin:
    def __init__(goblin, health, power):
        goblin.health = health
        goblin.power = power
  
#*Goblin Methods       
    def attack(goblin):
        if goblin.health > 0:
#       # Goblin attacks hero
            hero.health -= goblin.power 
            print(f'The goblin does {goblin.power} damage to you.')    
        if hero.health <= 0:
            print('Your are dead.')             

    def print_alive(goblin):      
        while goblin.alive > 0:
            print(f'You have {goblin.health} and {goblin.power}.')
            break    

    def print_status(goblin):    
        if goblin.health <= 0:
            print('Your are dead.')



#&----------------code starts here---------------------
Link = Hero(10, 20)
print(f'Link -->  Health: {Link.health} Power: {Link.power}')

Harry = Goblin( 5, 10)
print(f'Harry -->  Health: {Harry.health} Power: {Harry.power}')
 
# Hero.attack(Goblin)
# hero.attack(goblin) 
    
   
###########################################################################    
# # Hero.main(hero)
# Hero.attack(Goblin)
# Hero.choices(Hero)
# print(Hero.menu(Hero))
##########################################################################


 # def main():
    #     hero.health = 10
    #     hero.power = 5
    #     goblin.health = 6
    #     goblin.power = 2
    
#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":

  #        elif raw_input == "2":
#             pass
#          elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()
    



 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def greet(self, other_person):
#  return(f'Hello {other_person.name}, I am {self.name}!')
      
# print(sonny.greet(jordan))      
# print(jordan.greet(sonny))