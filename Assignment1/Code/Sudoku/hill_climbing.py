from asyncio import constants
from datetime import datetime
import itertools
import random
import sys


def printBroad(board):
    for i  in range(len(board)): 
        if i == 0:
            print("Hang\Cot",end="")
            print("   1 2 3    4 5 6    7 8 9 ")
            print(" - - - - - - - - - - - - - ")
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j == 0: 
                print(i+1, end ="");
                print("        | ", end = "")
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8: 
                print(board[i][j])
            else: print(str(board[i][j]) + " ",end ="")


def checkValid(board, num , pos):
    # Check column
    res = 0
    for i  in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i and num != 0:
            res += 1
    # Check row
    for i  in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i and num != 0:
            res += 1 
        
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
         for j in range(box_x * 3, box_x * 3 + 3):
             if board[i][j] == num and (i,j) != pos and num != 0:
                 res += 1
             
    return res
def findEmpty(board):
    res =[]
    
    for i in range(len(board)):
        minires = []
        for j in range(len(board[0])):
            if board[i][j] == 0:
               minires += [j]
        res.append(minires)
    return res

def findSol_list(bo):
    res =[]
    for i in range(len(bo)):
        res.append(findNum(bo[i]))
    
    return res
def checkPoint(bo):
    res = 0
    for i in range(len(bo)):
        for j in range(len(bo_test1)):
            res += checkValid(bo,bo[i][j],(i,j)) 
            
    return res

def solve1(bo):
    prob = bo
    pos_list = findEmpty(bo)
    for i in range(0,9):
        
        for j in pos_list[i]:
            bo[i][j]= random.randint(1,9)
            z = 0
        while checkPoint(bo) != 0:
            if z > 200: break
            for j in pos_list[i]:
                bo[i][j]= random.randint(1,9)
            for j in pos_list[i]:
                for l in range (9,0,-1):
                    if l != bo[i][j]:
                        temp = checkPoint(bo)
                        temp1 = bo[i][j]
                        bo[i][j] = l
                        if checkPoint(bo) > temp:
                            bo[i][j] = temp1
                            print("So ",end="")
                            print(l,end="")
                            print(" khong phu hop tai ",end="")
                            print("hang ",end="")
                            print(i,end="")
                            print(" cot ",end="")
                            print(j)                          
                            printBroad(bo)
                            print("\n")
                        else:  
                            print("Thay hang ",end="")
                            print(i,end="")
                            print(" cot ",end="")
                            print(j,end="")
                            print(" = ",end="")
                            print(l)
                            printBroad(bo)
                            print("\n")
            z = z+1
    # print(bo[0])
    if z == 201:
        print("Last answer:")
    else: print("The answer: ")    
    printBroad(bo)
def findNum(col):
    res =[]
    for i in range (1,10):
        if i not in col:
            res += [i] 
    return res

bo_test1 = [ [0,0,3,5,1,0,6,2,8],
    [2,9,0,0,0,3,7,0,0],
    [0,0,0,0,4,0,0,0,5],
    [0,4,7,0,3,8,2,0,0],
    [5,1,2,6,0,7,0,4,0],
    [6,0,0,0,0,5,0,9,0],
    [7,8,0,0,0,0,0,6,0],
    [0,0,6,9,0,0,5,0,1],
    [1,0,4,2,7,0,3,0,0]]

bo_test2 = [ [2,3,0,1,0,0,4,0,8],
    [7,0,5,0,0,2,0,6,0],
    [0,1,0,0,8,9,0,5,0],
    [0,0,6,3,0,7,0,0,2],
    [0,7,3,0,4,8,0,0,1],
    [8,4,0,0,9,0,0,0,5],
    [4,6,8,0,0,3,0,0,7],
    [0,0,1,5,7,0,9,0,0],
    [9,0,0,0,0,6,3,2,0]]
bo_test3 =  [ [0,9,0,2,0,0,7,1,4],
    [0,0,8,7,0,6,0,0,3],
    [0,2,5,0,4,3,0,9,0],
    [2,0,0,0,0,0,8,6,0],
    [3,5,0,9,7,0,1,0,0],
    [0,4,1,0,5,2,0,0,7],
    [0,3,0,8,1,4,5,0,6],
    [1,0,0,0,0,0,0,2,9],
    [0,6,7,3,0,0,0,0,0]]

bo_test4 =  [ [0,5,6,8,0,7,3,0,0],
    [0,2,0,3,0,0,9,0,0],
    [0,0,4,0,6,2,0,7,1],
    [0,8,0,0,2,5,1,0,7],
    [3,0,0,0,4,0,0,6,0],
    [0,7,0,1,0,0,2,9,4],
    [5,0,1,0,3,6,0,8,0],
    [8,9,3,0,7,1,0,2,5],
    [0,0,0,9,0,0,4,0,0]]

bo_test5 =  [ [8,0,1,0,3,0,2,0,0],
    [3,0,0,9,1,0,0,5,7],
    [5,0,0,4,0,6,9,1,0],
    [6,3,0,0,0,0,4,0,2],
    [0,0,5,0,2,0,0,8,9],
    [0,8,0,3,7,9,1,0,0],
    [9,0,0,1,0,7,6,0,8],
    [2,4,0,5,6,0,0,0,0],
    [0,7,0,0,0,8,0,3,0]]

bo_test6 =  [ [0,5,7,0,0,9,0,8,0],
    [6,0,8,0,3,2,0,7,0],
    [9,4,0,0,0,6,1,0,5],
    [0,7,0,1,0,3,5,0,0],
    [4,0,0,8,0,0,6,0,0],
    [0,2,5,0,7,0,0,9,3],
    [2,6,1,0,4,7,3,0,8],
    [0,0,0,0,6,1,0,2,4],
    [0,3,0,0,5,0,9,0,0]]

bo_test7 =  [ [0,2,3,7,0,0,0,6,0],
    [6,0,0,0,2,0,0,3,0],
    [1,0,4,0,9,6,0,7,0],
    [0,0,5,0,0,2,4,0,0],
    [0,7,0,0,0,0,0,0,8],
    [0,0,9,1,8,0,0,2,0],
    [3,1,0,6,0,0,0,0,0],
    [0,0,6,0,0,0,9,4,0],
    [0,0,0,5,7,1,0,0,0]]

bo_test8 =  [ [6,1,5,0,4,0,0,3,0],
    [2,0,4,0,8,6,1,0,9],
    [8,0,9,1,0,7,0,4,0],
    [0,0,6,0,7,8,0,2,0],
    [0,5,2,0,6,0,9,0,8],
    [3,0,8,9,0,2,0,7,0],
    [9,0,1,7,3,0,2,0,0],
    [0,2,7,8,0,5,0,0,1],
    [0,8,0,6,0,0,7,0,4]]

bo_test9 =  [ [0,6,0,0,7,4,0,0,8],
    [0,7,5,0,3,0,0,0,1],
    [4,0,2,9,6,0,0,0,3],
    [2,0,8,0,0,5,4,0,0],
    [0,0,7,2,9,0,0,1,5],
    [0,3,1,0,0,8,9,6,0],
    [0,0,0,3,2,9,0,0,6],
    [0,0,9,1,0,6,5,7,0],
    [8,1,0,4,0,0,0,2,0]]

bo_test10 =  [ [0,1,0,0,4,0,0,8,5],
    [3,0,6,2,0,0,0,9,0],
    [0,2,0,0,1,0,0,3,0],
    [0,0,4,0,0,2,6,0,0],
    [1,0,0,0,0,5,0,0,9],
    [0,0,0,8,0,0,7,0,4],
    [0,6,0,0,0,0,8,0,1],
    [0,9,0,7,3,0,0,0,2],
    [0,0,5,6,0,0,0,0,0]]

bo_test11 =  [ [0,5,0,1,3,0,4,0,8],
    [0,8,9,0,5,2,0,6,0],
    [3,0,6,9,7,0,1,0,0],
    [9,0,0,0,8,0,0,5,4],
    [0,7,2,0,0,4,0,0,1],
    [0,1,0,6,0,3,8,7,0],
    [7,0,0,0,1,5,9,0,0],
    [0,0,0,8,0,0,3,0,2],
    [4,3,1,0,6,0,0,0,7]]

bo_test12 =  [ 
    [0,8,6,0,0,1,0,0,0],
    [7,0,0,5,0,0,0,9,2],
    [0,0,9,0,7,0,3,0,0],
    [1,9,0,0,2,0,4,0,0],
    [0,0,0,0,3,0,0,0,9],
    [0,7,0,8,4,0,0,5,0],
    [4,2,0,0,0,6,0,8,0],
    [0,5,7,0,0,0,1,0,0],
    [6,0,0,9,0,3,0,7,0]]
bo_test13 =  [ 
    [0,0,0,0,0,0,0,8,5],
    [0,0,6,0,0,2,0,0,4],
    [0,0,9,3,7,0,0,0,0],
    [3,7,0,0,1,9,0,0,0],
    [2,1,0,0,0,0,6,3,0],
    [0,0,0,4,0,0,5,0,0],
    [8,0,1,0,6,0,9,0,0],
    [0,5,0,8,4,0,2,0,0],
    [7,0,0,0,3,0,0,0,1]]

bo_test14 =  [ 
    [0,7,5,9,0,3,8,0,1],
    [3,8,0,0,2,0,0,4,0],
    [1,0,6,5,0,7,9,0,0],
    [0,2,7,0,0,8,4,5,0],
    [0,0,3,7,0,0,6,0,8],
    [9,1,0,4,6,0,3,7,0],
    [7,0,2,3,5,0,0,8,0],
    [0,9,1,0,7,4,0,3,6],
    [5,0,4,8,1,0,2,0,7]]

bo_test15 =  [ 
    [0,0,2,0,3,4,0,0,7],
    [6,0,0,8,0,0,5,0,0],
    [0,3,0,0,1,0,0,9,0],
    [0,0,3,0,0,0,9,7,8],
    [0,4,9,0,7,0,2,0,0],
    [8,0,0,0,0,0,0,1,0],
    [0,9,4,0,0,0,0,2,0],
    [0,0,0,0,6,5,0,0,0],
    [7,0,8,2,0,0,0,3,5]]


print ("Testcase 3")           # khi chay co the thay doi bo_test1 = bo_testn voi n la so testcase tuong ung 
a = solve1(bo_test3)
print("Mem memorry usage = ",end="")
print(sys.getsizeof(a))


    