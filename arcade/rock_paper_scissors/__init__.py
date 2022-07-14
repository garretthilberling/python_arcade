import random, os, time
user = ''
def play():
    os.system('cls')
    global user
    user = input("What's your choice? 'r' for rock, 'p' for paper, or 's' for scissors ('q' to quit):\n").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie!'

    if user == 'q':
        return 'Goodbye!'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

if __name__ == '__main__':
    while user != 'q':
        print(play())
        time.sleep(0.8)