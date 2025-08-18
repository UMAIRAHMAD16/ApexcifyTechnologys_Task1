import random
play_again = ''
wins = 0
losses = 0
draw = 0

def rock_paper_scissors(wins, losses, draw):
    print("rock, paper, scissors, 1,2,3!")  
    player = input("Pick one! (r/p/s): ")  
    ai = random.randint(1,3)
    if ai == 1:
        ai_player = 'r'
    if ai == 2:
        ai_player = 'p'
    if ai == 3:
        ai_player = 's'


    print('Computer played:' + ai_player)
    print('You played:' + player)            
    
    if ai_player == player:
        print('draw!')
        draw += 1
        print('Wins: '+ str(wins) + 'Losses: '+ str(losses) + 'Draw: '+  str(draw))
        play_again_prompt = input('play again? (yes/no): ')

    elif (ai_player == 's' and player == 'p') or (ai_player == 'p' and player == 'r') or (ai_player == 'r' and player == 's'):
        print('loss!')
        losses += 1
        print('wins: ' +str(wins) + 'losses: ' +str(losses) + 'draw: ' + str(draw))
        play_again_prompt = input('play again? (yes/no): ')
    else:
        print('Win!')
        wins += 1
        print('wins: ' +str(wins) + 'losses: ' +str(losses) + 'draw: ' + str(draw))
        play_again_prompt = input('play again? (yes/no): ')
    return wins, losses, draw, play_again_prompt


    
while play_again != 'no':

    wins, losses, draw, play_again = rock_paper_scissors(wins, losses, draw)

print('Thanks for playing!')    











