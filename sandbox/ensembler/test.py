from strategy import *
from ensembler import *



perf =[]
obj = Ensembler()
for i in range(25):
    computer_choice = obj.predict()
    my_choice = int(input("What is your choice? 1(Rock), 2(Paper), 3(Scissors) ")) - 1
    
    if(my_choice == 42):
        break

    if(computer_choice == my_choice):
        print("Tie!")
        s = 0
        perf.append('t')

    elif(computer_choice == win(my_choice)):
        print("Computer wins!")
        s = -1
        perf.append('w')

    else:
        print("Player wins!")
        s = 1
        perf.append('l')
    
    obj.update(my_choice, computer_choice, s)
    obj.update_weights()

wins = len(list(filter(lambda x: x =='w', perf)))
losses = len(list(filter(lambda x: x =='l', perf)))
draws = len(list(filter(lambda x: x =='t', perf)))

print(f'Winrate: {wins*4}%')
print(f'Lossrate: {losses*4}%')
print(f'Drawrate: {draws*4}%')
