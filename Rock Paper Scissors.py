print("Made by Ritesh Kumar Mohapatra")
import time
loose = ("The computer wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []
while True:
    print("To begin fill in the below information.")
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
                print("Access Granted")
                time.sleep(0.5)
                print("Loading.")
                time.sleep(0.5)
                print("Loading..")
                time.sleep(0.5)
                print("Loading...")
                time.sleep(0.5)
                start_menu = """
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    
¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
 \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /
                                                                                                                                                                 /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Live Rules
You start with 5 lives.
If you win you get a extra live.
If you loose you loose a live.
If you draw the lives stay the same.
-----------------------------------------
To see a list of rules type rules.
-----------------------------------------
At any point type exit to leave the game.
-----------------------------------------
The computer has lives aswell.
Can you beat the computer?
Good Luck!!
-----------------------------------------
"""
                print(start_menu)
                while True:
                    rps = input("Rock, Paper, Scissors?   ")
                    rps = rps.title()
                    import random
                    computer = ("rock", "paper", "scissors")
                    computer = random.choice(computer)
                    #rock if statments
                    if rps == "Rock" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    if rps == "Rock" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        print("")
                        print("")
                        score+=1
                  #paper if statements
                    if rps == "Paper" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if rps == "Paper" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #scissor if statements
                    if rps == "Scissors" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if rps == "Scissors" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #duplicates
                    if rps == "Rock" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1               
                    if rps == "Paper" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    if rps == "Scissors" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    #system
                    if rps == "rules":
                        print("**********************************************")
                        print("Rules")
                        print("**********************************************")
                        print("-Rock looses against Paper")
                        print("-Rock beats Scissors")
                        print("-Paper beats Rock")
                        print("-Paper looses against Scissors")
                        print("-Scissors beats Paper")
                        print("-Scissors looses against Rock")
                        print("**********************************************")
                    if rps == "display lives":
                        print(lives)
                    if rps == "display score":
                        print(score)
                    if rps == "display drew":
                        print(drew)
                    #lives
                    if lives == 0 or rps == "test":
                        print("Thanks for playing.")
                        print("You have run out of lives")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        exit()
                    if computer_lives == 0:
                        print("Thanks for playing.")
                        print("The computer lost all it's lives. You Win.")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        exit()
                    #exit
                    if rps == "exit":
                        break
        if password in line and password != line:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
