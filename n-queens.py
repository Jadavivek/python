import numpy as np
n = 8
res = np.arange(1,65).reshape(-1, n)
board = [[(i*8 + j) for i in range(8)] for j in range(8)]
print ( res)
def attack(i,j):
    for k in range (0,65):
        if board[i][j]==k+(n+1)*8 or board[i][j]==k+(n-1)*8 or board[i][j]==k-(n+1)*8 or board[i][j]==k-(n-1)*8:
            return True
    for i in range(n):
        i=i+1
        if board[i][j]==k+i or board[i][j]==k-i:
            return True
    for k in range(0,65):
        if board[i][j]==k+(n+1)*9 or board[i][j]==k+(n-1)*9 or board[i][j]==k-(n+1)*9 or board[i][j]==k-(n-1)*9:
            return True
    return False
def N_queens(n1):
    if n1==0:
        return True
    for k in range(0,65):
        i = k//8
        j = k % 8
        if(not(attack(i, j))) and (board[i][j]!=0):
            board[i][j]=0
            if N_queens(n-1)==True:
                return True
            board[i][j]= k
        return False
N_queens(n)
for l in res:
    print(l)
    
        

 


