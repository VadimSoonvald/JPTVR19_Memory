import random # Import random
import datetime # Impressing time

# Information about the author of the work
print(60*"=")
print("Game: rock, scissors, paper.")
now_date = datetime.date.today ()
print("Date: ", now_date)
print(60*"=")
print("The author of the work: Vadim Soonvald")
print("Specialty: Tarkvaraarendaja")
print("Group: JPTVR19")
print(60*"=")

player_score = 0 # Player points
computer_score = 0 # Computer points
choices = ["1", "2", "3"] # Item selection
print("Rules:\nStone crushes scissors. Scissors cut the paper. The paper covers the stone")
player = input("Choose number:\n1 - rock\n2 - scissors\n3 - paper\n4 - go out")
while player != "4":
    computer = random.choice(choices)
    print("Your choice " +player+ ", computer took " +computer+ ".")
    if player == computer:
        print("Draw!")
    elif player == "1":
        if computer == "2":
            print("You win!")
            player_score = player_score + 1
        else:
            print("The computer won!")
            computer_score = computer_score + 1
        print ("Total score: you have ", player_score, "at the computer ", computer_score)
    elif player == "3":
        if computer == "1":
            print("You win!")
            player_score = player_score + 1
        else:
            print("The computer won!")
            computer_score = computer_score + 1
        print ("Total score: you have ", player_score, "at the computer ", computer_score)
    elif player == "2":
        if computer == "3":
            print("You win!")
            player_score = player_score + 1
        else:
            print("The computer won!")
            computer_score = computer_score + 1
        print ("Total score: you have", player_score, "at the computer", computer_score)
    else:
        print("An error occurred ...")
    print()                             
    player = input("Choose number:\n1 - rock\n2 - scissors\n3 - paper\n4 - go out")