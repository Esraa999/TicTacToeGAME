from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    
    print (board[8] + ' | ' + board[7] + ' | ' + board[6])

    print (board[5] + ' | ' + board[4] + ' | ' + board[3])

    print (board[2] + ' | ' + board[1] + ' | ' + board[0])
def player_input():

  marker = ''

  while marker != 'X' and marker != 'O':
    marker = input('\n Player : Do you want to be X or O ? ').upper()

    if marker == 'X':
      return('X','O')
    else:
      return('O','X')
def place_marker(board, marker, position):
    
     board[position] = marker
def win_check(board, mark):
    if (board[6] == mark and board[7] == mark and board[8] == mark) or (board[5] == mark and board[4] == mark and board[3] == mark) or (board[2] == mark and board[1] == mark and board[0] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[6] == mark and board[3] == mark and board[0] == mark) or (board[6] == mark and board[4] == mark and board[2] == mark) or (board[8] == mark and board[4] == mark and board[0] == mark):
      return True
    else:
      return False


def choose_first():
     if random.randint(0, 1) == 0:
        return 'Player 2 (0)'
     else:
        return 'Player 1 (X)'
def space_check(board, position):
    
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(0,8):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
      # Using strings because of raw_input
    position = ' '
    while position not in '0 1 2 3 4 5 6 7 8'.split() or not space_check(board, int(position)):
        
        position = input('Choose your next position: (0-8) so that 0 is the lower right cell and 8 is the upper left cell ')
        if position not in range(0,8):
           continue
           print("Please choose a range between 0 and 8")
           position = input('Choose your next position: (0-8) so that 0 is the lower right cell and 8 is the upper left cell ')
          

    return int(position)
def replay():
    
     return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
     


print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True
    while game_on:
      if turn == 'Player 1 (X)':
          # Player1's turn.
          
          display_board(theBoard)
          position = player_choice(theBoard)
          place_marker(theBoard, player1_marker, position)

          if win_check(theBoard, player1_marker):
              display_board(theBoard)
              print('Congratulations! Player 1 (X) won the game!')
              game_on = False
          else:
              if full_board_check(theBoard):
                  display_board(theBoard)
                  print('The game is a draw!')
                  break
              else:
                  turn = 'Player 2 (O)'

      else:
          # Player2's turn.
          
          display_board(theBoard)
          position = player_choice(theBoard)
          place_marker(theBoard, player2_marker, position)

          if win_check(theBoard, player2_marker):
              display_board(theBoard)
              print('Congratulations! Player 2 (O) won the game!')
              game_on = False
          else:
              if full_board_check(theBoard):
                  display_board(theBoard)
                  print('The game is a tie!')
                  break
              else:
                  turn = 'Player 1 (X)'

    if not replay():
        break 


  
