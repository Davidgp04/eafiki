import sys
def getTrans(value):
    if value==1:
        return "O"
    elif value==-1:
        return "X"
    else:
        return ""
def validarTablero(board):
    if len(board)>4:
        return False
    for row in board:
        if len(row)>4:
            return False
    return True
def score(board,turno):
    score=0
    gameOver=False
    gameWin=False
    for i in range(3):
        for j in range(3):
            cadena=getTrans(board[i][j]*turno)+getTrans(board[i+1][j]*turno)+getTrans(board[i+1][j+1]*turno)
            if cadena=="OOO":
                gameWin=True
                score+=100
            elif cadena=="XXX":
                gameOver=True
                score-=100
            elif cadena=="OO":
                score+=10
            elif cadena=="XX":
                score-=10
            elif cadena=="O":
                score+=1
            elif cadena=="X":
                score-=1
    return score,gameOver,gameWin
def minimax(board,level,alpha,beta,maximizer:bool,turno):
    bestRow=None
    bestCol=None
    puntos,gameOver,gameWin=score(board,turno)
    if gameOver or level==0 or gameWin:
        return puntos,None,None
    #print(maximizer)
    if maximizer:
        maxVal=-sys.maxsize
        for i in range(4):
            for j in range(4):
                if board[i][j]==0:
                    board[i][j]=turno
                    value,col,row=minimax(board,level-1,alpha,beta,False,turno)
                    board[i][j]=0
                    if value>maxVal:
                        maxVal=value
                        bestRow=i
                        bestCol=j
                    alpha=max(maxVal,alpha)
                    if alpha>=beta:
                        break
        #print(maxVal,"maxVal")
        return maxVal,bestCol,bestRow
    else:
        minVal=sys.maxsize
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    board[i][j] = -turno
                    value,row,col=minimax(board,level-1, alpha,beta,True,turno)
                    board[i][j]=0
                    if value <minVal:
                        minVal = value
                        bestRow = i
                        bestCol = j
                    beta=min(beta,minVal)
                    if alpha>=beta:
                        break
        return minVal,bestCol,bestRow



tablero=[[0,0,0,0],
         [-1,-1,1,0],
         [0,1,1,-1],
         [0,1,0,0]]
while True:
    contador=0
    for row in tablero:
        contador+=row.count(0)
        print(row)
    if contador==0:
        break
    print("Sugerir mejor jugada -> 1")
    print("Jugar -> 2")
    answer=int(input())
    if answer==1:
        bestVal, bestCol, bestRow = minimax(tablero, 3, -sys.maxsize, sys.maxsize, True, -1)
        tablero[bestRow][bestCol] = -1
    elif answer==2:
        col=int(input("Ingrese la columna"))
        row=int(input("Ingrese la fila"))
        if (col>4 or col<1) or row>4 or row<1:
            print("Coordenadas inválidas")
            continue
        tablero[row-1][col-1]=-1
    else:
        print("Oops,No contamos con esa opción")
        continue
    score, gameOver, gameWin = score(tablero, 1)
    if gameWin or gameOver:
        break
    bestVal, bestCol, bestRow = minimax(tablero, 3, -sys.maxsize, sys.maxsize, True, 1)
    tablero[bestRow][bestCol] = 1
    score,gameOver,gameWin=score(tablero,1)
    if gameWin or gameOver:
        break
for row in tablero:
    print(row)
print("Fin del juego")
