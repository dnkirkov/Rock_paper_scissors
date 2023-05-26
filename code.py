import random
green = '\033[92m'
reset = '\033[0m'
line_marker = f"{green}-------------------------------------------{reset}"
bug_flag = False
player_score = 0
ai_score = 0
ai_play_word = ''
win_conditions = [('r', 's'), ('p', 'r'), ('s', 'p')]
print('Lets play rock paper scissors!')
print(line_marker)
while 1:
    player_play = input("Choose a play: [r]ock, [p]aper, [s]cissors:")
    if player_play not in ['r', 'p', 's']:
        bug_flag = True
    if bug_flag:
        break
    ai_play = random.choice(['r', 'p', 's'])
    if ai_play == 'r':
        ai_play_word = 'rock'
    elif ai_play == 'p':
        ai_play_word = 'paper'
    elif ai_play == 's':
        ai_play_word = 'scissors'
    print(f'Computer chose {ai_play_word}!')
    if (player_play, ai_play) in win_conditions:
        print('You win!')
        print(line_marker)
        player_score += 1
    elif (ai_play, player_play) in win_conditions:
        print('You lose!')
        print(line_marker)
        ai_score += 1
    elif player_play == ai_play:
        print('Draw!')
        print(line_marker)
    else:
        bug_flag = True
    if bug_flag:
        break
    print('Current score:')
    print(f'You: {player_score}')
    print(f'Computer: {ai_score}')
    print(line_marker)
    decision = input('Do you want to play again?([y]es, [n]o):')
    print(line_marker)
    if decision == 'y':
        continue
    elif decision == 'n':
        break
    else:
        bug_flag = True
        break
if not bug_flag:
    print('Thanks for playing!')
    print(line_marker)
else:
    print('Program executed unsuccessfully.')
    print(line_marker)
