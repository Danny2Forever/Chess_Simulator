running = True
board = [['bR','bH','bB','bK','bQ','bB','bH','bR']
        ,['bP','bP','bP','bP','bP','bP','bP','bP']
        ,['  ','  ','  ','  ','  ','  ','  ','  ']
        ,['  ','  ','  ','  ','  ','  ','  ','  ']
        ,['  ','  ','  ','  ','  ','  ','  ','  ']
        ,['  ','  ','  ','  ','  ','  ','  ','  ']
        ,['wP','wP','wP','wP','wP','wP','wP','wP']
        ,['wR','wH','wB','wK','wQ','wB','wH','wR']]

ROW = 0
COL = 0
ROWED = 0
COLED = 0
Turn = "WHITE"

col = {
    'a' : 0,'b' : 1,
    'c' : 2,'d' : 3,
    'e' : 4,'f' : 5,
    'g' : 6,'h' : 7
}
row = {
    '1' : 7,'2' : 6,
    '3' : 5,'4' : 4,
    '5' : 3,'6' : 2,
    '7' : 1,'8' : 0,
}

def check_piece(ROW,ROWED):
    Pawn_move(ROW, ROWED)

def Pawn_move(ROW, ROWED):
    first_move = True
    if Turn == "WHITE":
        if first_move == True :
            if ROWED == ROW + 2 or ROWED == ROW + 1:
                first_move = False
            else:
                print("Invalid move ไอควาย")
                Destination(starter_move)
        
        elif first_move == False :
            if ROWED == ROW + 1:
                first_move = False
            else:
                print("Invalid move ไอควาย")
                Destination(starter_move)
    else:
        if first_move == True :
            if ROWED == ROW - 2 or ROWED == ROW - 1:
                first_move = False
            else:
                print("Invalid move ไอควาย")
                Destination(starter_move)
        
        elif first_move == False :
            if ROWED == ROW - 1:
                first_move = False
            else:
                print("Invalid move ไอควาย")
                Destination(starter_move)

def print_board():
    for i in board:
        print(i)
        
def Destination(starter_move):
    global destination_move ,ROW ,COL
    try:
        destination_move = input("Input destination col , row : ")
        ROW = row[destination_move[1]]+1
        Pawn_move(ROW,ROWED)
        print(ROWED)
        print(ROW)
        board[row[destination_move[1]]][int(col[destination_move[0]])] = piece
        board[row[starter_move[1]]][int(col[starter_move[0]])] = '  '
    except:
        print('Invalid choose again!')
        Destination(starter_move)

def Swap_turn(Turn):
    if Turn == "WHITE":
        Turn = "BLACK"
    else:
        Turn = "WHITE"

def Move():
    global piece ,starter_move ,ROWED ,COLED
    try: 
        starter_move = input("Input start col , row : ")
        if len(starter_move) > 2 :
            Move()
        else:
            piece = board[row[starter_move[1]]][int(col[starter_move[0]])]
        ROWED = row[starter_move[1]]+1
        COLED = int(col[starter_move[0]])+1
        print(ROWED)

    except:
        print('Invalid choose again!')
        Move()

    print(piece)
    while piece == '  ':
        print('Invalid choose again!')
        Move()

    Destination(starter_move)
    print(f"{starter_move}{destination_move}")
    Swap_turn(Turn)
    print_board()
    print("")

def main():
    while running :
        Move()

if __name__ == "__main__" :
    main()