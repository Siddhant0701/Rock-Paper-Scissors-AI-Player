import csv

win_dict = {'1':'3', '2':'1', '3':'2'}
lose_dict = {'1':'2', '2':'3', '3':'1'}

def get_string(player, wins):
    res = ""
    for(i,j) in zip(player, wins):
        if j == 't':
            res += i
        elif j == 'w':
            res += win_dict[i]
        else:
            res += lose_dict[i]
    print(len(res))
    return res



with open('collected.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    for row in reader:
        print(get_string(row[2], row[3]))
