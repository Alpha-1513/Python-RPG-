from time import sleep
import re
import time
import sys
import os
from os import system
import pyfiglet
from colorama import  Back, Style
import climage 
from colorama import Fore
from cfonts import render, say
import random


#clears console
def clear_console():
  # For Windows
  if os.name == 'nt':
      _ = os.system('cls')
  else:
      _ = os.system('clear')


#writes strings letter by letter
def writeFast(text, speed=.000001):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(speed)


#big intro sign
def intro():
  print("Welcome to \"", end="" )
  print(Fore.RED + "Python", end="")
  print(Style.RESET_ALL + " RPG\"")

  #PPC = "Python RPG"
  #ASCII = pyfiglet.figlet_format(PPC, font='rounded')
  #writeFast(ASCII)
  output = render('Python RPG', colors=['red', 'white'], align='center')
  writeFast(output)
  print("Made by ", end="")
  print(Fore.BLUE + "@YengnongXiong ", end="")
  print(Style.RESET_ALL + "and his team")
  #print()
  sleep(1)
  print("Welcome: " , end="")
  print(Fore.BLUE + "@"+ os.environ['REPL_OWNER'])
  print(Style.RESET_ALL)
  sleep(1)
  input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  print()
  clear_console()


#enter username
def username():
  username = input()
  return username


#choose your character with user stats
CharacterClass = ""
def character(stats):
  global CharacterClass
  
  print("Choose your Class:")
  print("1. Assassian")
  print("2. Giant")
  print("3. Barbarian")
  CharacterChoice = input()
  while CharacterChoice not in ["1", "2", "3"]:
    print()
    print("Invalid User Input, try again")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    clear_console()
    print("Welcome "+Fore.CYAN+username1+Style.RESET_ALL+"!")
    print()
    print("Choose your Class:")
    print("1. Assassian")
    print("2. Giant")
    print("3. Barbarian")
    CharacterChoice = input()

  #stats = [0,0,0]
  if(CharacterChoice == "1"):
    CharacterClass = "Assassian"
    print()
    print("You have chosen Assassian")
    print("You specialize in "+Fore.BLUE+"SPEED"+Style.RESET_ALL+".")
    stats = [6,5,8]
  
  if(CharacterChoice == "2"):
    CharacterClass = "Giant"
    print()
    print("You have chosen Giant")
    print("You specialize in "+Fore.GREEN+"HEALTH"+Style.RESET_ALL+".")
    stats = [6,8,5]
    
  
  if(CharacterChoice == "3"):
    CharacterClass = "Barbarian"
    print()
    print("You have chosen Barbarian")
    print("You specialize in "+Fore.RED+"STRENGTH"+Style.RESET_ALL+".")
    stats = [8,6,5]
  
  print()
  input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  print()
  clear_console();

  print("Your starting stats are:")
  y=1
  for x in stats:
  
    print(x, end =" ")
    if(y==1):
      print(Fore.RED+"Strength"+Style.RESET_ALL)
    
    if(y==2):
      print(Fore.GREEN+"Health"+Style.RESET_ALL)
   
    if(y==3):
      print(Fore.BLUE+"Speed"+Style.RESET_ALL)
    
    y=y+1
  
  input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  print()
  clear_console()
  return stats

#images
def Alien():
  output = climage.convert('Alien6.png') 
  print(output)
def Insect():
  output = climage.convert('Insect2.png') 
  print(output)
def Demon():
  output = climage.convert('Demon5.png') 
  print(output)
def Ghost():
  output = climage.convert('Ghost3.jpg')
  print(output)
def Reaper():
  output = climage.convert('Reaper4.jpg')
  print(output)
def Slime():
  output = climage.convert('Slime1.webp')
  print(output)
def MerchantImage():
  output = climage.convert('merchant.jpg')
  print(output)
def CompanionImage():
  output = climage.convert('tree.jpg')
  print(output)

#rolling dice animation
def rollingdice():
  h = 0
  f = 0
  while h < 1:
      f = 0
      h += 1
      print("")

      while f < 1:
          print("R")
          time.sleep(.5)
          print("O")
          time.sleep(.5)
          print("L")
          time.sleep(.5)
          print("L")
          time.sleep(.5)
          print("I")
          time.sleep(.5)
          print("N")
          time.sleep(.5)
          print("G")
          time.sleep(.5)
          print(".")
          time.sleep(.5)
          print(".")
          time.sleep(.5)
          print(".")
          time.sleep(.5)

          if f == 6:
              time.sleep(0.5)  # Sleep for 500 milliseconds

          time.sleep(0.5)  # Sleep for 500 milliseconds
          f += 1

      print("\33[2K\r")


#choose and defeat bosses
bossdefeats=0
gold = 0
turn = 0
game=True
boss1Death=False
boss2Death=False
boss3Death=False
boss4Death=False
boss5Death=False
#boss6Death=False


def Boss(stats):
  global bossdefeats
  global gold
  global turn
  global game
  global boss1Death
  global boss2Death
  global boss3Death
  global boss4Death
  global boss5Death
  #global boss6Death
  
  if(boss1Death==True):
    bossdefeats=1
  if(boss2Death==True):
    bossdefeats=2
  if(boss3Death==True):
    bossdefeats=3
  if(boss4Death==True):
    bossdefeats=4
  if(boss5Death==True):
    bossdefeats=5
  
  
  print("Choose your boss:")
  print()

  bosses = ["1. Slime", "2. Insect", "3. Ghost", "4. Reaper", "5. Demon", "6. Alien"]

  if(bossdefeats<6):

    counter=0
    while(counter<=bossdefeats):
      print(bosses[counter])
      counter=counter+1

    while(counter<6):
      print("LOCKED --- (DEFEAT PREVIOUS BOSS)")
      counter=counter+1


  print()
  #input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  print(Fore.YELLOW+"Enter "+Style.RESET_ALL+"to Exit")
  print()

  BossChoice = input("Who would you like to fight? ")
    
  while BossChoice not in ["1", "2", "3", "4", "5", "6",""]:
    print()
    print("Invalid User Input, try again")
    print()
    BossChoice = input("Who would you like to fight? ")

  
  if(BossChoice==("")):
    clear_console()
    return

  
  turn = turn + 1
  dead=False
  
  if(BossChoice=="1"):
      
      clear_console()
      Slime()
      print("You have chosen Slime.")
      print("Slime Stats: 7" +Fore.RED+" Strength"+Style.RESET_ALL+" - 7"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 7 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
      print()
      startingHealth = stats[1]
      boss1=[7,7,7]
      count = 0
      while(dead==False):
        #boss1=[10,10,10]
        #startingHealth = stats[1]
        if (count >= 1):
          clear_console()
          Slime()
        #print("You have chosen Slime.")
        
        input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
        print()
        rollingdice()
        number = random.randint(1, 6)
        
        bossnumber = random.randint(1, 6)
        

        clear_console()
        Slime()
        
        print("You rolled a " + str(number) + "!")
        print("The boss rolled a " + str(bossnumber) + "!")
        
        #stength, health, speed
        damage = number * stats[0]
        damage = damage - (bossnumber * boss1[2])
        bossdamage = bossnumber * boss1[0]
        bossdamage = bossdamage - (number * stats[2])

        if(damage<0):
          damage=0
        if(bossdamage<0):
          bossdamage=0
        
        boss1[1]=boss1[1]-damage
        
        print()
        print("You do " + str(damage) + " damage to the Slime.")
        
        if(boss1[1]<=0):
          print("You have defeated the Slime!")
          boss1Death = True
          bossdefeats=1
          dead=True
          
          increaseStr=random.randint(1,3)
          increaseSpd=random.randint(1,3)
          increaseHlth=random.randint(1,3)
          
          stats[0]=stats[0]+increaseStr
          stats[1]=startingHealth+increaseHlth
          stats[2]=stats[2]+increaseSpd

          print()
          print("Your stats have increased!")
          print("You have gained " + str(increaseStr)+Fore.RED+" Strength"+Style.RESET_ALL+", "+ str(increaseHlth) +Fore.GREEN+" Health"+Style.RESET_ALL+", and "+ str(increaseSpd) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")

          gold = gold + 5
          print("You have gained 5 gold!")
          print()
          
          input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
          print()
          clear_console()
          return
        
        
        
        if(boss1[1]>=1):
          stats[1]=stats[1]-bossdamage
          print("The Slime does " + str(bossdamage) + " damage to you.")

        if(stats[1]<=0):
          print("You have died.")
          stats[1]=startingHealth
          dead=True

          input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
          print()
          clear_console()
          return

        if(boss1[1]>=1 and dead==False):     
          count = count + 1
          #print("You have done" + str(damage) + " to the Slime.")
         # print("The Slime has done" + str(bossdamage) + " to you.")

          print()

          print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
          print("The Slime has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")

          print()

          input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
          print()
          clear_console()

  if(BossChoice=="2" and bossdefeats>=1):

    clear_console()
    Insect()
    print("You have chosen Insect.")
    #print("Insect Stats: 25 strength - 35 health - 30 speed")
    print("Insect Stats: 25" +Fore.RED+" Strength"+Style.RESET_ALL+" - 35"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 30 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
    print()
    startingHealth = stats[1]
    boss1=[25,35,30]
    count = 0
    while(dead==False):
      #boss1=[10,10,10]
      #startingHealth = stats[1]
      if (count >= 1):
        clear_console()
        Insect()
      #print("You have chosen Slime.")

      input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
      print()
      rollingdice()
      number = random.randint(1, 6)
      
      bossnumber = random.randint(1, 6)


      clear_console()
      Insect()

      print("You rolled a " + str(number) + "!")
      print("The boss rolled a " + str(bossnumber) + "!")

      #stength, health, speed
      damage = number * stats[0]
      damage = damage - (bossnumber * boss1[2])
      bossdamage = bossnumber * boss1[0]
      bossdamage = bossdamage - (number * stats[2])

      if(damage<0):
        damage=0
      if(bossdamage<0):
        bossdamage=0

      boss1[1]=boss1[1]-damage

      print()
      print("You do " + str(damage) + " damage to the Insect.")

      if(boss1[1]<=0):
        print("You have defeated the Insect!")
        boss2Death = True
        bossdefeats=2
        dead=True

        increaseStr=random.randint(5,10)
        increaseSpd=random.randint(5,10)
        increaseHlth=random.randint(5,10)

        stats[0]=stats[0]+increaseStr
        stats[1]=startingHealth+increaseHlth
        stats[2]=stats[2]+increaseSpd

        print()
        print("Your stats have increased!")
        print("You have gained " + str(increaseStr)+Fore.RED+" Strength"+Style.RESET_ALL+", "+ str(increaseHlth) +Fore.GREEN+" Health"+Style.RESET_ALL+", and "+ str(increaseSpd) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")

        gold = gold + 10
        print("You have gained 10 gold!")
        print()

        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return



      if(boss1[1]>=1):
        stats[1]=stats[1]-bossdamage
        print("The Insect does " + str(bossdamage) + " damage to you.")

      if(stats[1]<=0):
        print("You have died.")
        stats[1]=startingHealth
        dead
        
        print("You lose 5 gold (can't go into negatives).")
        gold=gold-5
        if(gold<0):
          gold=0

        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()  
        return

      
      if(boss1[1]>=1 and dead==False):     
        count = count + 1
        #print("You have done" + str(damage) + " to the Slime.")
       # print("The Slime has done" + str(bossdamage) + " to you.")

        print()

        #print("You have " + str(stats[1]) + " health left.")
        #print("The Insect has " + str(boss1[1]) + " health left.")
        print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
        print("The Insect has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")

        print()

        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()

  if(BossChoice=="2" and bossdefeats<1):
    print()
    print("You haven't unlocked this boss.")
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return


  if(BossChoice=="3" and bossdefeats>=2):

    clear_console()
    Ghost()
    print("You have chosen Ghost.")
    #print("Ghost Stats: 55 strength - 55 health - 45 speed")
    print("Ghost Stats: 55" +Fore.RED+" Strength"+Style.RESET_ALL+" - 55"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 45 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
    print()
    startingHealth = stats[1]
    boss1=[55,55,45]
    count = 0
    while(dead==False):
      #boss1=[10,10,10]
      #startingHealth = stats[1]
      if (count >= 1):
        clear_console()
        Ghost()
      #print("You have chosen Slime.")
    
      input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
      print()
      rollingdice()
      number = random.randint(1, 6)
      
      bossnumber = random.randint(1, 6)
    
    
      clear_console()
      Ghost()
    
      print("You rolled a " + str(number) + "!")
      print("The boss rolled a " + str(bossnumber) + "!")
    
      #stength, health, speed
      damage = number * stats[0]
      damage = damage - (bossnumber * boss1[2])
      bossdamage = bossnumber * boss1[0]
      bossdamage = bossdamage - (number * stats[2])
    
      if(damage<0):
        damage=0
      if(bossdamage<0):
        bossdamage=0
    
      boss1[1]=boss1[1]-damage
    
      print()
      print("You do " + str(damage) + " damage to the Ghost.")
    
      if(boss1[1]<=0):
        print("You have defeated the Ghost!")
        boss3Death = True
        bossdefeats=3
        dead=True
    
        increaseStr=random.randint(7,12)
        increaseSpd=random.randint(7,12)
        increaseHlth=random.randint(7,12)
    
        stats[0]=stats[0]+increaseStr
        stats[1]=startingHealth+increaseHlth
        stats[2]=stats[2]+increaseSpd
    
        print()
        print("Your stats have increased!")
        print("You have gained " + str(increaseStr)+Fore.RED+" Strength"+Style.RESET_ALL+", "+ str(increaseHlth) +Fore.GREEN+" Health"+Style.RESET_ALL+", and "+ str(increaseSpd) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
    
        gold = gold + 15
        print("You have gained 15 gold!")
        print()
    
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return
    
    
      if(boss1[1]>=1):
        stats[1]=stats[1]-bossdamage
        print("The Ghost does " + str(bossdamage) + " damage to you.")
    
      if(stats[1]<=0):
        print("You have died.")
        stats[1]=startingHealth
        dead
        
        print("You lose 10 gold (can't go into negatives).")
        gold=gold-10
        if(gold<0):
          gold=0
    
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()   
        return

      
      if(boss1[1]>=1 and dead==False):     
        count = count + 1
        #print("You have done" + str(damage) + " to the Slime.")
       # print("The Slime has done" + str(bossdamage) + " to you.")
    
        print()
    
        #print("You have " + str(stats[1]) + " health left.")
        #print("The Ghost has " + str(boss1[1]) + " health left.")
        print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
        print("The Ghost has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
    
        print()
    
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()

  if(BossChoice=="3" and bossdefeats<2):
    print()
    print("You haven't unlocked this boss.")
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  
  if(BossChoice=="4" and bossdefeats>=3):

    clear_console()
    Reaper()
    print("You have chosen Reaper.")
    #print("Reaper Stats: 115 strength - 180 health - 80 speed")
    print("Reaper Stats: 115" +Fore.RED+" Strength"+Style.RESET_ALL+" - 180"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 80 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
    print()
    startingHealth = stats[1]
    boss1=[115,180,80]
    count = 0
    while(dead==False):
      #boss1=[10,10,10]
      #startingHealth = stats[1]
      if (count >= 1):
        clear_console()
        Reaper()
      #print("You have chosen Slime.")
  
      input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
      print()
      rollingdice()
      number = random.randint(1, 6)
      
      bossnumber = random.randint(1, 6)
  
  
      clear_console()
      Reaper()
  
      print("You rolled a " + str(number) + "!")
      print("The boss rolled a " + str(bossnumber) + "!")
  
      #stength, health, speed
      damage = number * stats[0]
      damage = damage - (bossnumber * boss1[2])
      bossdamage = bossnumber * boss1[0]
      bossdamage = bossdamage - (number * stats[2])
  
      if(damage<0):
        damage=0
      if(bossdamage<0):
        bossdamage=0
  
      boss1[1]=boss1[1]-damage
  
      print()
      print("You do " + str(damage) + " damage to the Reaper.")
  
      if(boss1[1]<=0):
        print("You have defeated the Reaper!")
        boss4Death = True
        bossdefeats=4
        dead=True
  
        increaseStr=random.randint(15,20)
        increaseSpd=random.randint(15,20)
        increaseHlth=random.randint(15,20)
  
        stats[0]=stats[0]+increaseStr
        stats[1]=startingHealth+increaseHlth
        stats[2]=stats[2]+increaseSpd
  
        print()
        print("Your stats have increased!")
        print("You have gained " + str(increaseStr)+Fore.RED+" Strength"+Style.RESET_ALL+", "+ str(increaseHlth) +Fore.GREEN+" Health"+Style.RESET_ALL+", and "+ str(increaseSpd) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
  
        gold = gold + 35
        print("You have gained 35 gold!")
        print()
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return
  
  
  
      if(boss1[1]>=1):
        stats[1]=stats[1]-bossdamage
        print("The Reaper does " + str(bossdamage) + " damage to you.")
  
      if(stats[1]<=0):
        print("You have died.")
        stats[1]=startingHealth
        dead=True
        
        print("You lose 20 gold (can't go into negatives).")
        gold=gold-20
        if(gold<0):
          gold=0
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()       
        return

      
      if(boss1[1]>=1 and dead==False):     
        count = count + 1
        #print("You have done" + str(damage) + " to the Slime.")
       # print("The Slime has done" + str(bossdamage) + " to you.")
  
        print()
  
        #print("You have " + str(stats[1]) + " health left.")
        #print("The Reaper has " + str(boss1[1]) + " health left.")
        print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
        print("The Reaper has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
  
        print()
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
  
  if(BossChoice=="4" and bossdefeats<3):
    print()
    print("You haven't unlocked this boss.")
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  if(BossChoice=="5" and bossdefeats>=4):

    clear_console()
    Demon()
    print("You have chosen Demon.")
    #print("Demon Stats: 200 strength - 280 health - 180 speed")
    print("Demon Stats: 200" +Fore.RED+" Strength"+Style.RESET_ALL+" - 280"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 180 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
    print()
    startingHealth = stats[1]
    boss1=[200,280,180]
    count = 0
    while(dead==False):
      #boss1=[10,10,10]
      #startingHealth = stats[1]
      if (count >= 1):
        clear_console()
        Demon()
      #print("You have chosen Slime.")
  
      input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
      print()
      rollingdice()
      number = random.randint(1, 6)
      
      bossnumber = random.randint(1, 6)
  
  
      clear_console()
      Demon()
  
      print("You rolled a " + str(number) + "!")
      print("The boss rolled a " + str(bossnumber) + "!")
  
      #stength, health, speed
      damage = number * stats[0]
      damage = damage - (bossnumber * boss1[2])
      bossdamage = bossnumber * boss1[0]
      bossdamage = bossdamage - (number * stats[2])
  
      if(damage<0):
        damage=0
      if(bossdamage<0):
        bossdamage=0
  
      boss1[1]=boss1[1]-damage
  
      print()
      print("You do " + str(damage) + " damage to the Demon.")
  
      if(boss1[1]<=0):
        print("You have defeated the Demon!")
        boss5Death = True
        bossdefeats=5
        dead=True
  
        increaseStr=random.randint(25,35)
        increaseSpd=random.randint(25,35)
        increaseHlth=random.randint(25,35)
  
        stats[0]=stats[0]+increaseStr
        stats[1]=startingHealth+increaseHlth
        stats[2]=stats[2]+increaseSpd
  
        print()
        print("Your stats have increased!")
        print("You have gained " + str(increaseStr)+Fore.RED+" Strength"+Style.RESET_ALL+", "+ str(increaseHlth) +Fore.GREEN+" Health"+Style.RESET_ALL+", and "+ str(increaseSpd) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
  
        gold = gold + 50
        print("You have gained 50 gold!")
        print()
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return
  
  
  
      if(boss1[1]>=1):
        stats[1]=stats[1]-bossdamage
        print("The Demon does " + str(bossdamage) + " damage to you.")
  
      if(stats[1]<=0):
        print("You have died.")
        stats[1]=startingHealth
        dead=True
        
        print("You lose 35 gold (can't go into negatives).")
        gold=gold-35
        if(gold<0):
          gold=0
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return

      
      if(boss1[1]>=1 and dead==False):     
        count = count + 1
        #print("You have done" + str(damage) + " to the Slime.")
       # print("The Slime has done" + str(bossdamage) + " to you.")
  
        print()
  
        #print("You have " + str(stats[1]) + " health left.")
        #print("The Demon has " + str(boss1[1]) + " health left.")
        print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
        print("The Demon has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
  
        print()
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
  
  if(BossChoice=="5" and bossdefeats<4):
    print()
    print("You haven't unlocked this boss.")
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  if(BossChoice=="6" and bossdefeats>=5):
  
    clear_console()
    Alien()
    print("You have chosen Alien.")
    #print("Alien Stats: 500 strength - 600 health - 650 speed")
    print("Alien Stats: 500" +Fore.RED+" Strength"+Style.RESET_ALL+" - 600"+Fore.GREEN+" Health" + Style.RESET_ALL+ " - 650 " +Fore.BLUE+"Speed"+Style.RESET_ALL)
    print()
    startingHealth = stats[1]
    boss1=[500,600,650]
    count = 0
    while(dead==False):
      #boss1=[10,10,10]
      #startingHealth = stats[1]
      if (count >= 1):
        clear_console()
        Alien()
      #print("You have chosen Slime.")
  
      input("Press"+Fore.YELLOW+" Enter"+Style.RESET_ALL+" to roll dice...")
      print()
      rollingdice()
      number = random.randint(1, 6)
      
      bossnumber = random.randint(1, 6)
  
  
      clear_console()
      Alien()
  
      print("You rolled a " + str(number) + "!")
      print("The boss rolled a " + str(bossnumber) + "!")
  
      #stength, health, speed
      damage = number * stats[0]
      damage = damage - (bossnumber * boss1[2])
      bossdamage = bossnumber * boss1[0]
      bossdamage = bossdamage - (number * stats[2])
  
      if(damage<0):
        damage=0
      if(bossdamage<0):
        bossdamage=0
  
      boss1[1]=boss1[1]-damage
  
      print()
      print("You do " + str(damage) + " damage to the Alien.")
  
      if(boss1[1]<=0):
        print("You have defeated the Alien!")
        bossdefeats=6
        dead=True
        game=False
  
        print()
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return
  
  
  
      if(boss1[1]>=1):
        stats[1]=stats[1]-bossdamage
        print("The Alien does " + str(bossdamage) + " damage to you.")
  
      if(stats[1]<=0):
        print("You have died.")
        stats[1]=startingHealth
        dead=True
        print("You lose 70 gold (can't go into negatives).")
        gold=gold-70
        if(gold<0):
          gold=0
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
        return
      
      if(boss1[1]>=1 and dead==False):     
        count = count + 1
        #print("You have done" + str(damage) + " to the Slime.")
       # print("The Slime has done" + str(bossdamage) + " to you.")
  
        print()
  
        #print("You have " + str(stats[1]) + " health left.")
        #print("The Alien has " + str(boss1[1]) + " health left.")
        print("You have " + str(stats[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
        print("The Alien has " + str(boss1[1]) +Fore.GREEN+" health "+Style.RESET_ALL+"left.")
  
        print()
  
        input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
        print()
        clear_console()
  
  if(BossChoice=="6" and bossdefeats<5):
    print()
    print("You haven't unlocked this boss.")
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return
    

      

#creates menu for user
def menu(username,stats,armour,companion): 
  print("Username: " +Fore.CYAN+username+Style.RESET_ALL+" | Class: " + CharacterClass)
  print("Stats --- " , end="")
  print(Fore.RED+"Strength"+Style.RESET_ALL+":"+str(stats[0]), end=" ")
  print(Fore.GREEN+"Health"+Style.RESET_ALL+":"+str(stats[1]), end=" ")
  print(Fore.BLUE+"Speed"+Style.RESET_ALL+":"+str(stats[2]))
  print()
  print("Gold:" + str(gold))
  print("Weapon: " + armour[0])
  print("Armour: " + armour[1])
  print("Relic: " + armour[2])
  print("Companion: " + companion)
  print()
  print(Back.YELLOW+"Goal: level up and beat the final boss in the least amount of time"+Style.RESET_ALL)
  print("--------------------------------------------")

#prompts user for a choice
def choice():
  
  print("1. Fight a Boss  --- ", end = " ")
  print("2. Go to the Merchant  --- ", end = " ")
  print("3. Find a Companion --- ", end = " ")
  print("4. Beginner Manual")
  choice = input()
  while choice not in ["1", "2", "3", "4"]:
    print()
    print("Invalid User Input, try again")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    clear_console()
    menu(username1,stats,inventory,companion)
    print("1. Fight a Boss  --- ", end = " ")
    print("2. Go to the Merchant  --- ", end = " ")
    print("3. Find a Companion --- ", end = " ")
    print("4. Beginner Manual")
    choice = input()
    
  return choice


#weapons, armours, relics 

WeaponArray = ( ["Infinity Gauntlet", 500, 150, 25, 100], ["Excalibur", 110, 50, 20, 20], ["Zeus's Thunderbolt", 250, 75, 10, 40], ["Titanium Shield", 200, 25, 300, 30], ["Energy Sword",75, 40, 15, 15], ["Master Sword", 35, 9, 8, 9], ["Assassin's Hidden Blade", 65, 15, 10, 70], ["Gunblade", 100, 75, 10, 5], ["Axe of Kratos", 250, 170, 35, 5], ["Steve's Pickaxe", 25, 10, 10, 10], ["Magician's Deck of Cards", 75, 25, 25, 25], ["Samurai Katana", 50, 25, 10, 15], ["Athena's Spear", 360, 200, 120, 30], ["Warrior's Bow", 25, 15, 5, 5], ["Unearthed Dagger", 55, 20, 10, 20], ["Cursed Scythe", 80, 45, 20, 20], ["Supernatural Double-Edged Sword", 100, 60, 5, 5], ["Sorcerer's Staff", 45, 20, 10, 5], ["One-Handed Greatsword", 50, 30, 20, 5], ["Blessed Greatsword", 60, 40, 25, 10] )

ArmourArray = ( ["Begger's Cloak", 25, 10, 5, 15], ["Eternal Leather", 180, 20, 50, 60], ["Chimera's Crest", 40, 10, 25, 10], ["Shiny Chestplate", 35, 10, 25, 5], ["Hunter's Leather", 35, 10, 25, 20], ["Plate of the Wounded", 100, 25, 60, 5], ["Ironman's Suit", 600, 350, 150, 150], ["Robes of Absorption", 200, 25, 150, 10], ["Bands of the Weak", 45, 60, 5, 5], ["Prodigy's Garments", 100, 35, 35, 35], ["Chestplate of Ares", 370, 110, 200, 125], ["Cloth of Security", 35, 5, 20, 10], ["Dreamer's Defense", 150, 5, 100, 25], ["Second Skin", 400, 25, 400, 25], ["Salamander's Scale", 320, 105, 85, 155], ["Uniform of Honor", 50, 10, 35, 20], ["Deathwalker's Plate", 170, 70, 10, 100], ["Eternal Chains", 300, 10, 200, 10], ["Wyvern's Hide", 190, 55, 120, 30], ["Coward's Clothing", 45, 5, 5, 100] )

RelicArray = ( ["Ring of Justice", 35, 15, 10, 5], ["Book of Enchantments", 100, 30, 30, 30], ["Mirror of Truth", 65, 55, 10, 5], ["Harmony Harp", 65, 35, 5, 40], ["Hourglass of Seconds", 145, 20, 15, 110], ["Lunar Compass", 20, 6, 6, 6], ["Spectral Lantern", 45, 5, 5, 5], ["Amulet of the Eclipse", 95, 25, 50, 10], ["Aetherian Crystal", 200, 150, 30, 10], ["Cursed Pearl", 150, 10, 120, 60], ["Dragon's Scale", 350, 100, 205, 10], ["Emperor's Locket", 100, 40, 55, 5], ["Time Stone", 180, 35, 5, 160], ["Elixar Vial", 400, 200, 100, 65], ["Olympic Medallion", 240, 15, 200, 60], ["Totem of Undying", 400, 5, 500, 10], ["Magician's Mask", 50, 15, 30, 5], ["Pandora's Box", 450, 155, 155, 155], ["Ring of Protection", 55, 10, 50, 10], ["Vlad's Blood Vial", 225, 105, 25, 70],)



RandWeapon=random.randint(0,len(WeaponArray)-1)
RandArmour=random.randint(0,len(ArmourArray)-1)
RandRelic=random.randint(0,len(RelicArray)-1)
turn2=0
SavedW=random.randint(0,len(WeaponArray)-1)
SavedA=random.randint(0,len(ArmourArray)-1)
SavedR=random.randint(0,len(RelicArray)-1)
Weapon1=0
Weapon2=0
Weapon3=0
Armour1=0
Armour2=0
Armour3=0
Relic1=0
Relic2=0
Relic3=0

def merchant(inventory):
  global turn2
  global RandWeapon
  global RandArmour
  global RandRelic
  global SavedW
  global SavedA
  global SavedR
  global gold
  global Weapon1
  global Weapon2
  global Weapon3
  global Armour1
  global Armour2
  global Armour3
  global Relic1
  global Relic2
  global Relic3
  

  MerchantImage()
  print("Welcome to the Merchant!")
  print("*shop reloads every time you fight a boss*")
  print()

  if(turn2!=turn):
    RandWeapon=random.randint(0,len(WeaponArray)-1)
    RandArmour=random.randint(0,len(ArmourArray)-1)
    RandRelic=random.randint(0,len(RelicArray)-1)
    SavedW=RandWeapon
    SavedA=RandArmour
    SavedR=RandRelic
    turn2=turn

  if(turn==turn):
    RandWeapon=SavedW
    RandArmour=SavedA
    RandRelic=SavedR

  print("1. Weapon  --- " + WeaponArray[RandWeapon][0] + " --- " + str(WeaponArray[RandWeapon][1]) + " gold")
  print("2. Armour  --- " + ArmourArray[RandArmour][0] + " --- " + str(ArmourArray[RandArmour][1]) + " gold")
  print("3. Relic  --- " + RelicArray[RandRelic][0] + " --- " + str(RelicArray[RandRelic][1]) + " gold")
  print()
  print(Fore.YELLOW+"Enter "+Style.RESET_ALL+"to Exit")
  
  
  print()
  UserChoice=input("What would you like to buy? ")
  while UserChoice not in ["1", "2", "3", ""]:
    print()
    print("Invalid User Input, try again")
    print()
    UserChoice=input("What would you like to buy? ")
    
  
  print()
  OverallChoice=0
  

  
  if(UserChoice==""):
    clear_console()
    return
  if(UserChoice=="1"):
    OverallChoice=RandWeapon
  if(UserChoice=="2"):
    OverallChoice=RandArmour
  if(UserChoice=="3"):
    OverallChoice=RandRelic
    

  if(UserChoice=="1" and gold>=WeaponArray[OverallChoice][1]):
    gold=gold-WeaponArray[OverallChoice][1]
    inventory[0]=WeaponArray[OverallChoice][0]
    
    stats[0]=stats[0]-Weapon1
    Weapon1=WeaponArray[OverallChoice][2]
    stats[0]=stats[0]+Weapon1
    stats[1]=stats[1]-Weapon2
    Weapon2=WeaponArray[OverallChoice][3]
    stats[1]=stats[1]+Weapon2
    stats[2]=stats[2]-Weapon3
    Weapon3=WeaponArray[OverallChoice][4]
    stats[2]=stats[2]+Weapon3
    
    print("You have bought the " + WeaponArray[OverallChoice][0] + "!")
    print()
    print("Your stats have increased!")
    print("You have gained " + str(WeaponArray[OverallChoice][2]) +Fore.RED+" Strength"+Style.RESET_ALL+".")
    print("You have gained " + str(WeaponArray[OverallChoice][3]) +Fore.GREEN+" Health"+Style.RESET_ALL+".")
    print("You have gained " + str(WeaponArray[OverallChoice][4]) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    clear_console()
    return
    
  if(UserChoice=="1" and gold<WeaponArray[OverallChoice][1]):
    print("You do not have enough gold!")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  if(UserChoice=="2" and gold>=ArmourArray[OverallChoice][1]):
    gold=gold-ArmourArray[OverallChoice][1]
    inventory[1]=ArmourArray[OverallChoice][0]

    stats[0]=stats[0]-Armour1
    Armour1=ArmourArray[OverallChoice][2]
    stats[0]=stats[0]+Armour1
    stats[1]=stats[1]-Armour2
    Armour2=ArmourArray[OverallChoice][3]
    stats[1]=stats[1]+Armour2
    stats[2]=stats[2]-Armour3
    Armour3=ArmourArray[OverallChoice][4]
    stats[2]=stats[2]+Armour3

    print("You have bought the " + ArmourArray[OverallChoice][0] + "!")
    print()
    print("Your stats have increased!")
    print("You have gained " + str(ArmourArray[OverallChoice][2]) +Fore.RED+" Strength"+Style.RESET_ALL+".")
    print("You have gained " + str(ArmourArray[OverallChoice][3]) +Fore.GREEN+" Health"+Style.RESET_ALL+".")
    print("You have gained " + str(ArmourArray[OverallChoice][4]) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    clear_console()
    return

  if(UserChoice=="2" and gold<ArmourArray[OverallChoice][1]):
    print("You do not have enough gold!")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  if(UserChoice=="3" and gold>=RelicArray[OverallChoice][1]):
    gold=gold-RelicArray[OverallChoice][1]
    inventory[1]=RelicArray[OverallChoice][0]
    stats[0]=stats[0]-Relic1
    Relic1=RelicArray[OverallChoice][2]
    stats[0]=stats[0]+Relic1
    stats[1]=stats[1]-Relic2
    Relic2=RelicArray[OverallChoice][3]
    stats[1]=stats[1]+Relic2
    stats[2]=stats[2]-Relic3
    Relic3=RelicArray[OverallChoice][4]
    stats[2]=stats[2]+Relic3

    print("You have bought the " + RelicArray[OverallChoice][0] + "!")
    print()
    print("Your stats have increased!")
    print("You have gained " + str(RelicArray[OverallChoice][2]) +Fore.RED+" Strength"+Style.RESET_ALL+".")
    print("You have gained " + str(RelicArray[OverallChoice][3]) +Fore.GREEN+" Health"+Style.RESET_ALL+".")
    print("You have gained " + str(RelicArray[OverallChoice][4]) +Fore.BLUE+" Speed"+Style.RESET_ALL+".")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    clear_console()
    return

  if(UserChoice=="3" and gold<RelicArray[OverallChoice][1]):
    print("You do not have enough gold!")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    return

  
    
    

  #print()
  #input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  #print()
  clear_console()

  


#companions 
CompanionsArray = ( ["Pikachu", 45, 7, 5, 10], ["Merlin the Magician", 30, 9, 5, 7], ["Dark Phoniex", 50, 11, 8, 6], ["Nick the Knight", 30, 10, 5, 6], ["Otto the Monk", 35, 5, 15, 4], ["Witch of Genieva", 50, 11, 6, 8], ["Orion the Oracle", 70, 15, 8, 5], ["Enigma", 85, 17, 8, 20], ["Aang the Last Airbender", 150, 50, 50, 50], ["Kane the Pyromancer", 35, 9, 3, 7], ["Tasmanian Trader", 60, 55, 0, 0], ["A.K.Y.", 500, 500, 500, 500], ["Jack the Ripper", 105, 55, 20, 15], ["Raiden the Swordsman", 45, 15, 7, 9], ["Apollo the Sun", 200, 65, 40, 90], ["Adam the First", 190, 20, 80, 55], ["White Eyed Dragon", 300, 100, 35, 20], ["Exodius", 200, 75, 30, 40], ["Medusa", 110, 70, 25, 10], ["Water Serpent", 150, 70, 20, 25])

#CompanionsArray = ( ["Dog", 0, 1, 2, 3], ["Cat", 0, 4, 5, 6], ["Bird", 0, 7, 8, 9] )
#print(array[0][3]) #this prints 3
turn1=0
saved1=random.randint(0, len(CompanionsArray) - 1)
saved2=random.randint(0, len(CompanionsArray) - 1)
saved3=random.randint(0, len(CompanionsArray) - 1)
randomChoice1=0
randomChoice2=0
randomChoice3=0
Companion1=0
Companion2=0
Companion3=0
companion = "None"

def FindCompanion():
  global turn1
  global turn
  global saved1
  global saved2
  global saved3
  global randomChoice1
  global randomChoice2
  global randomChoice3
  global Companion1
  global Companion2
  global Companion3
  global companion
  global gold 

  CompanionImage()
  print("You have traveled through the woods and found companions!")
  print("*companions reloads every time you fight a boss*")
  print()

  if(turn==turn1):
    
    randomChoice1=saved1
    randomChoice2=saved2
    randomChoice3=saved3

  if(turn!=turn1):
  
    randomChoice1 = random.randint(0, len(CompanionsArray) - 1)
    randomChoice2 = random.randint(0, len(CompanionsArray) - 1)
    randomChoice3 = random.randint(0, len(CompanionsArray) - 1)
    saved1=randomChoice1
    saved2=randomChoice2
    saved3=randomChoice3
    turn1=turn
    
  
  #randomChoice1 = random.randint(0, len(CompanionsArray) - 1)
  #randomChoice2 = random.randint(0, len(CompanionsArray) - 1)
  #randomChoice3 = random.randint(0, len(CompanionsArray) - 1)
  
  
  #CompanionImage()
  print("1. " + CompanionsArray[randomChoice1][0] + " --- " + str(CompanionsArray[randomChoice1][1]) + " gold")
  print("2. " + CompanionsArray[randomChoice2][0] + " --- " + str(CompanionsArray[randomChoice2][1]) + " gold")
  print("3. " + CompanionsArray[randomChoice3][0] + " --- " + str(CompanionsArray[randomChoice3][1]) + " gold")
  print()
  print(Fore.YELLOW+"Enter "+Style.RESET_ALL+"to Exit")
  
  print()
  choice = 0
  choice = input("What would you like to buy? ")
  while choice not in ["1", "2", "3", ""]:
    print()
    print("Invalid User Input, try again")
    print()
    choice=input("What would you like to buy? ")
  #print()
  
  #print("1. " + CompanionsArray[randomChoice1][0] + " --- " + str(CompanionsArray[randomChoice1][1]) + " gold")
  #print("2. " + CompanionsArray[randomChoice2][0] + " --- " + str(CompanionsArray[randomChoice2][1]) + " gold")
  #print("3. " + CompanionsArray[randomChoice3][0] + " --- " + str(CompanionsArray[randomChoice3][1]) + " gold")

  RandomChoiceOverall=0
  
  if(choice=="1"):
    RandomChoiceOverall=randomChoice1
  if(choice=="2"):
    RandomChoiceOverall=randomChoice2
  if(choice=="3"):
    RandomChoiceOverall=randomChoice3
  if(choice==""):
    clear_console()
    return

  
  print()
  
  
  if((choice=="1" or choice =="2" or choice =="3") and gold>=CompanionsArray[RandomChoiceOverall][1]):
    gold=gold-CompanionsArray[RandomChoiceOverall][1]
    print("You have bought " + CompanionsArray[RandomChoiceOverall][0] + "!")
    print("You have gained " + str(CompanionsArray[RandomChoiceOverall][2]) +Fore.RED+" Strength"+Style.RESET_ALL+".")
    stats[0]=stats[0]-Companion1
    Companion1=CompanionsArray[RandomChoiceOverall][2]
    stats[0]=stats[0]+Companion1
    print("You have gained " + str(CompanionsArray[RandomChoiceOverall][3])+Fore.GREEN+" Health"+Style.RESET_ALL+".")
    stats[1]=stats[1]-Companion2
    Companion2=CompanionsArray[RandomChoiceOverall][3]
    stats[1]=stats[1]+Companion2
    print("You have gained " + str(CompanionsArray[RandomChoiceOverall][4])+Fore.BLUE+" Speed"+Style.RESET_ALL+".")
    stats[2]=stats[2]-Companion3
    Companion3=CompanionsArray[RandomChoiceOverall][4]
    stats[2]=stats[2]+Companion3
    
    companion=CompanionsArray[RandomChoiceOverall][0]
    
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
  else:
    print("You do not have enough gold!")
    print()
    input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
    print()
    clear_console()
    
    #return CompanionsArray[randomChoice1][1], CompanionsArray[randomChoice1][2], CompanionsArray[randomChoice1][3], CompanionsArray[randomChoice1][4]
    
    
  
  #input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  #print()
  clear_console()


def BeginnerManual():
  print("This is the Beginner's Manual. It contains basic information that can help you beat the game faster.")
  print()
  print(" ---this game is a timed based game so you should try to beat the game in the least amount of time")
  print(" ---use your gold to buy weapons, armour, relics, and a companion")
  print(" ---when you buy a new item, you lose your previous item's stats, and gain your new item's stats")
  print(" ---companion and merchant shop reloads everytime you fight a boss")
  print(" ---when fighting a boss, your damage is most heavily dependant on your dice roll, then your strength, then your speed")
  print(" ---damage is based off strength multiplied by your dice roll and then gets subtracted by boss's speed multiplied by their dice roll")
  print(" ---user input should only require your number keys(1,2,3,etc) and the enter key")
  
  print()
  input("Press " +Fore.YELLOW+"Enter " +Style.RESET_ALL+"to continue...")
  print()
  clear_console()
  
  
  

  
  
#-----------------------------Functions Above--------------------------------------------


stats = [0,0,0]
inventory = ["None","None","None"]
#companion = "None"
#gold = 0

#-----------------------------Variables Above--------------------------------------------
#-----------------------------Main Code Below--------------------------------------------

#def main():

  
intro()
print("Enter your username: " , end="")
username1 = username()
print("Welcome "+Fore.CYAN+username1+Style.RESET_ALL+"!")
print()
stats=character(stats)
#print(stats)

start_time = int(time.time())
#game=True
while(game==True):
  menu(username1,stats,inventory,companion)
  userChoice = choice()
  if(userChoice=="1"):
    clear_console()
    Boss(stats)
  if(userChoice=="2"):
    clear_console()
    merchant(inventory)
  if(userChoice=="3"):
    clear_console()
    FindCompanion()
    #Companion1,Companion2,Companion3=FindCompanion(companion)
  if(userChoice=="4"):
    clear_console()
    BeginnerManual()
  
  


#main()
clear_console()
end_time = int(time.time())
finish_time = end_time - start_time
print("You beat the game!")
print("Username: " +Fore.CYAN+username1+Style.RESET_ALL)
print("Replit Username: " , end="")
print(Fore.BLUE + "@"+ os.environ['REPL_OWNER']+Style.RESET_ALL)
print("Time:", finish_time,"seconds") 
PPC = "CONGRATS"
ASCII = pyfiglet.figlet_format(PPC, font='epic')
writeFast(ASCII)


