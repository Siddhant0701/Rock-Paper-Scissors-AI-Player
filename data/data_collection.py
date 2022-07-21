import random

dict = {1:"Rock", 2:"Paper", 3:"Scissors"}
win_dict = {"Scissors":1, "Rock":2, "Paper":3}

player_data = []
computer_data = []
win_data = ""

GAMES = 100

for i in range(GAMES):
    try:
        computer_choice = random.randint(1,3)
        player_choice = int(input("Rock (1), Paper (2) or Scissors (3)? "))
        player_data.append(player_choice)
        print("Computer:", dict[computer_choice])
        print("Player:", dict[player_choice])
        if computer_choice == player_choice:
            print("Tie!")
            win_data += 't'
        elif computer_choice == win_dict[dict[player_choice]]:
            print("Computer wins!")
            win_data += 'l'
        else:
            print("Player wins!")
            win_data  += 'w'
    except:
        continue



print(("").join(list(map(str,player_data))))
print(win_data)
    
