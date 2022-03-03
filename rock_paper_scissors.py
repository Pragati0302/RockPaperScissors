import random

def play():
    print("Your chance!")
    print('What\'s your choice?')
    player = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    print(f'Your choice is {player}\n')

    print("Opponnet's chance!")
    opponent = random.choice(['r', 'p', 's'])  #randomly chooses from a list
    # print("what's your choice?")
    # opponent =  input("'r' for rock, 'p' for paper, 's' for scissors\n")
    print(f'Opponent\'s choice is {opponent}\n')

    if player == opponent:
        return 'It\'s a tie'

    #r > s, s > p, p > r
    if is_win(player, opponent):
        return 'You Won!'
    else:
        return 'You lost!'


def is_win (player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
         or (player == 'p' and opponent == 'r'):
         return True

print(play())