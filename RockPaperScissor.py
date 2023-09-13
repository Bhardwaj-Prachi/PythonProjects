import random

options = ("rock","paper","scissors")
running = True

while running:

   player = None
   computer = random.choice(options)

   while player not in options:  
     player = input("Enter a choice(rock,paper,scissors): ")
  
   print(f"Player: {player}")
   print(f"Computer:{computer}")
 
   if player== computer:
      print("It's a Tie!")
   elif player=="rock" and computer=="scissor":
      print("You Win!")
   elif player =="scissor" and computer=="paper":
      print("You Win!")
   elif player =="paper" and computer=="rock":
      print("You Win!")
   else:
      print("Computer Win!")
      print("You Lose!")

   if not input("Play again? (y/n):") .lower()=="y":
        running= False

print("Thanks for Playing")