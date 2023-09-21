
#количество клеток
board_size=3
#игровое поле
board = [1,2,3,4,5,6,7,8,9]
#функция для выведения
def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[i*3+1], '|', board[i*3+2], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, char):
    #функция хода игрока
    if index > 9 or index < 1 or board[index-1] in ('X', 'O'):
        return False

    board[index-1] = char
    return True

def check_win():
    win = False

    win_comb = ((0,1,2), (3,4,5),(6,7,8),(0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for pos in win_comb:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win

def start_game():
    # текущий игрок
    current_player = 'X'
    #номер шага
    step = 1
    draw_board()

    while(step<10 and check_win() == False):
        index = input('ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')
        if index == '0':
            break
        # если получилось сделать шаг
        if game_step(int(index),current_player):
            print('удачный ход')

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            #увеличим номер хода
            step += 1
        else:
            print('Неверный номер! Повторите!')
    if step == 10:
        print("ничья!")
    else:
        print('Выиграл ' + check_win())


print('Привет!')
start_game()