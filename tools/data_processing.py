s = "wtttttwlwwtwwwttlwtllwlwtlwtlttwtwltllltllwlllllwtwlttwtwltwltlllttltlllllllttwwwtllttwttwttttltlltt"

wins = 0
losses = 0

for c in s:
    if c == 'w':
        wins += 1
    elif c == 'l':
        losses += 1
    else:
        pass

print(f"Wins: {wins/len(s)}")
print(f"Losses: {losses/len(s)}")    
