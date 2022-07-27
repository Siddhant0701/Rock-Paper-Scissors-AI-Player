import random

dict = {1:"Rock", 2:"Paper", 3:"Scissors"}
win_dict = {"Scissors":1, "Rock":2, "Paper":3}

player_data = []
computer_data = []
win_data = ""

GAMES = 500

for i in range(GAMES):
    try:
        computer_choice = random.randint(1,3)
        player_choice = int(input("Rock (1), Paper (2) or Scissors (3)? "))
        
        print("Computer:", dict[computer_choice])
        print("Player:", dict[player_choice])
        
        if computer_choice == player_choice:
            print("Tie!")
            win_data += 't'
            player_data.append(player_choice)
        elif computer_choice == win_dict[dict[player_choice]]:
            print("Computer wins!")
            win_data += 'l'
            player_data.append(player_choice)
        else:
            print("Player wins!")
            win_data  += 'w'
            player_data.append(player_choice)
    except:
        continue



print(("").join(list(map(str,player_data))))
print(win_data)
    
