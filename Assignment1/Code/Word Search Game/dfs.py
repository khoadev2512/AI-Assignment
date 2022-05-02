from pickle import TRUE
import random 
import string
import sys
from copy import deepcopy
import os, psutil
import time

# Use for window
time_start = time.perf_counter()

# Initiate dictionary from dictionary.txt
with open('dictionary.txt', 'r') as f:
    DICTIONARY = [line.strip() for line in f]

# User uppercase for game
dictionary = [x.upper() for x in DICTIONARY]

# Check and create Log folder
MYDIR = "Log"
PATHDIR = "./"

PATH = os.path.join(PATHDIR, MYDIR)

if os.path.isdir(PATH):
    for file in os.listdir(MYDIR):
                os.remove(os.path.join(MYDIR, file))
else:
    os.makedirs(PATH)
    print("Created {} folder".format(MYDIR))

# Initia global variable
couter = 0
store = ""
result = []
step = 0

class boggle:

    def __init__(self, size):
        self.size = size
        self.board = [0]*self.size
        self.dictionary = dictionary
        for i in range(self.size):
            tmpBoggle = [0]*self.size
            for j in range(self.size):
                tmpBoggle[j] = random.choice(string.ascii_letters).upper()
            self.board[i] = tmpBoggle

    # To run example
    # def __init__(self, boggle, dictionary):
    #     self.size = len(boggle)
    #     self.board = boggle
    #     self.dictionary = dictionary

    # Visualize board
    def printBoard(self, board):
        result = ""
        def print_horiz_line():
            return " -----" * self.size

        def print_vert_line(row):
            display = ""
            for i in range(len(row)):
                display += ("|  {x}  ").format(x = row[i])
            display += "|"
            return display

        for index in range(self.size):
            result += print_horiz_line()
            result += '\n'
            result += print_vert_line(board[index])
            result += '\n'
        result += print_horiz_line()
        result += '\n'
        return result

    # Visualize step of process
    def printStep(self, history):
        tmp = deepcopy(history)
        for i in range(self.size):
            for j in range(self.size):
                if tmp[i][j] == -1:
                    tmp[i][j] = self.board[i][j]
        return self.printBoard(tmp)

    # Check neightbor of current position [x][y] 
    # If it's connected and increase by order 1
    def getNeighbors(self, x, y):
        """Returns the neighbors for a given co-ordinates"""
        direction = [
            (-1,-1, "↖"),
            (-1, 0, "↑"),
            (-1, 1, "↗"),
            (0, -1, "←"),
            (0,  1, "→"),
            (1, -1, "↙"),
            (1,  0, "↓"),
            (1,  1, "↘"),
        ]
        listOfNeighbor = []
        for neighbor in direction:
            nextX = x + neighbor[0]
            nextY = y + neighbor[1]

            if (nextX >= self.size) or (nextY >= self.size) or (nextX < 0) or (nextY < 0):
                continue
            listOfNeighbor.append((nextX, nextY, neighbor[2]))
        return listOfNeighbor

    # Check if Str is a word and is contained dictionary
    def isWord(self, Str):
        str_match = list(filter(lambda x: Str in x, self.dictionary))
        return Str in str_match

    # A recursive function to print all words present on boggle
    def findWords(self, visited, i, j, Str, state, log, history):
        # Mark current cell as visited and
        # Append current character to str
        global step
        global couter
        global result

        if visited[i][j]:
            return True

        # Check if current Str is a sub String which contained in dictionary
        matching = [word for word in dictionary if Str in word]
        if len(matching) == 0:
            return

        # Mark state number 
        history[i][j] = state 

        # Mark visited -> true
        visited[i][j] = True
        Str = Str + self.board[i][j]

       # If use option log -> create file txt each case in Log folder
        if log == 1:
            global store
            store += '    ' * (int(len(self.board[0])/2) + 1) + 'Step {step}'.format(step = step) + '    ' * (int(len(self.board[0])/2) + 1) + '\n'
            store += self.printStep(history) 
            store += 'Current String: ' + Str + '\n'
            store += ('----' * (len(self.board[0]) + 3)) + '\n'
        state += 1
        step += 1

        # Check if neighbor is Invalid

        # If str is present in DICTIONARY
        if (self.isWord(Str) and Str not in result):
            store += '\n' + Str 
           
            # Save log in Log folder 
            if log == 1 and Str not in result:
                fileName = str(str(couter) + ".txt")
                fileName = os.path.join(MYDIR, fileName)
                with open(fileName, 'w+') as textFile:
                    textFile.write(store)
                    textFile.close()
            if Str not in result:
                print('Word {couter}:'.format(couter = couter) ,Str)
                result.append(Str)
                couter += 1

            # Reset state and step
            state = -1
            step = 0
            


        # Check condition and call recursion
        # row = i - 1
        # while row <= i + 1 and row < self.size:
        #     col = j - 1 - 1
        #     while col <= j + 1 and col < self.size:
        #         if (row >= 0 and col >= 0 and not visited[row][col]):
        #             self.findWords(visited, row, col, Str, state, log, history)
        #         col+=1
        #     row+=1
        listOfNeighbor = self.getNeighbors(i, j)
        for neighbor in listOfNeighbor:
            self.findWords(visited, neighbor[0], neighbor[1], Str, state, log, history)

        
        # Erase current character from string and
        # mark visited of current cell as false
        Str = "" + Str[-1]
        visited[i][j] = False
        history[i][j] = -1

    # Print board on console
    def display(self):
        print(self.printBoard(self.board))

    # Prints all words present in DICTIONARY.
    def run(self, log=0):
        state = 0
        # Mark all characters as not visited
        visited = [[False for i in range(self.size)] for j in range(self.size)]
        history = [[-1 for i in range(self.size)] for j in range(self.size)]
        # Initialize current string
        Str = ""
        
        # Consider every character and look for all words
        # starting with this character
        for i in range(self.size):
            for j in range(self.size):
                self.findWords(visited, i, j, Str, state, log, history)
                
        # Log result on console
        if len(result) == 0:
            print('Not found any words')
        else:
            print('Found total {couter} words: {result}'.format(couter = len(result), result = [x for x in result]))


def introduction():
    print('How to run ?')
    print('python heuristics.py size save')
    print('Example: ', 'python heuristics.py 3 0', '-> Run program with board size 3x3 and doesn`t save Log')
    print('Example: ', 'python heuristics.py 3 1', '-> Run program with board size 3x3 and save Log')


if __name__=="__main__":

    # Example    
    # dictionary = ["TPHCM", "DHBK", "MIC", "NMAI", "TIC"]

    # x =      [['T', 'I', 'M', 'N'],
    #           ['P', 'C', 'K', 'A'],
    #           ['D', 'H', 'B', 'I'],
    #           ['N', 'O', 'T', 'H']]

    # root Node of trie
    if len(sys.argv) == 3:
        # wordSearchGame = boggle(x, dictionary)
        wordSearchGame = boggle(int(sys.argv[1]))
        wordSearchGame.display()
        wordSearchGame.run(int(sys.argv[2]))
    else:
        introduction()

# Use for Unix os


# Use for window os
time_elapsed = (time.perf_counter() - time_start)
process = psutil.Process(os.getpid())
print ("%5.1f secs %5.1f KByte" % (time_elapsed, process.memory_info().rss/1024.0))

