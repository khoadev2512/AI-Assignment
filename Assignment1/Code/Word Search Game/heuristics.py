import random 
import string
import sys
import os, psutil
import time

time_start = time.perf_counter()
with open('dictionary.txt', 'r') as f:
    DICTIONARY = [line.strip() for line in f]

dictionary = [x.upper() for x in DICTIONARY]
# dictionary = ["TPHCM", "DHBK", "MIC", "NMAI"]


# Create Log folder 
MYDIR = "Log"
PATHDIR = "./"
PATH = os.path.join(PATHDIR, MYDIR)

# Delete all file if it's exist in Log
if os.path.isdir(PATH):
    for file in os.listdir(MYDIR):
                os.remove(os.path.join(MYDIR, file))
else:
    os.makedirs(PATH)
    print("Created {} folder".format(MYDIR))




# Lets get the delta to find all the nighbors
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

class Boggle:

    def __init__(self, size):
        self.size = size
        self.board = [0]*self.size
        # Initialize dictionary
        self.dictionary = dictionary
        # Initialize trie datastructure
        self.trieNode = {'valid': False, 'next': {}}
        for i in range(self.size):
            tmpBoggle = [0]*self.size
            for j in range(self.size):
                tmpBoggle[j] = random.choice(string.ascii_letters).upper()
            self.board[i] = tmpBoggle
            
    # def __init__(self, size, board, dictionary):
    #     self.size = size
    #     self.board = board
    #     # Initialize dictionary
    #     self.dictionary = dictionary
    #     # Initialize trie datastructure
    #     self.trieNode = {'valid': False, 'next': {}}
    #     # for i in range(self.size):
    #     #     tmpBoggle = [0]*self.size
    #     #     for j in range(self.size):
    #     #         tmpBoggle[j] = random.choice(string.ascii_letters).upper()
    #     #     self.board[i] = tmpBoggle

    def genTrieTree(self, word, node):
        """udpates the trie datastructure using the given word"""
        if not word:
            return

        if word[0] not in node:
            node[word[0]] = {'valid': len(word) == 1, 'next': {}}

        # Recursively build trie
        self.genTrieTree(word[1:], node[word[0]])

    # Insert words from dictionary to trie tree 
    def buildTrieTree(self, dictionary, trie):
        """Builds trie data structure from the list of dictionary given"""
        for word in dictionary:
            self.genTrieTree(word, trie)
        return trie

    # Get neighbors of current posision [x][y]
    def getNeighbors(self, x, y):
        """Returns the neighbors for a given co-ordinates"""
        listOfNeighbor = []
        for neighbor in direction:
            nextX = x + neighbor[0]
            nextY = y + neighbor[1]

            if (nextX >= self.size) or (nextY >= self.size) or (nextX < 0) or (nextY < 0):
                continue
            listOfNeighbor.append((nextX, nextY, neighbor[2]))
        return listOfNeighbor

    # Search word method with recursion
    def findWords(self, x, y, visited, trie, currentStr, direction, log=[]):
        """Scan the graph using DFS"""
        if (x, y) in visited:
            return

        letter = self.board[x][y]
        visited.append((x, y))

        if letter in trie:
            currentStr += letter

            if trie[letter]['valid']:
                log.append('Found "{}" {}'.format(currentStr, direction))
                
            listOfNeighbor = self.getNeighbors(x, y)
            for neighbor in listOfNeighbor:
                self.findWords(neighbor[0], neighbor[1], visited[::], trie[letter], currentStr, direction + " " + neighbor[2], log)

    # Visualize the board
    def getBoard(self):
        result = ""
        def print_horiz_line():
            return (" -----" * self.size)

        def print_vert_line(row):
            display = ""
            for i in range(len(row)):
                display += ("|  {x}  ").format(x = row[i])
            display += "|"
            return (display)

        for index in range(self.size):
            result += print_horiz_line()
            result += '\n'
            result += print_vert_line(self.board[index])
            result += '\n'
        result += print_horiz_line()
        result += '\n'
        return result

    def run(self, save=0):
        """Initiate the search for words in boggle"""
        self.trieNode = self.buildTrieTree(dictionary, self.trieNode)

        # Visualize the board
        print("Given board")
        board = self.getBoard()
        print(board)
        log = []

        # Traveser the board with recursion
        for x in range(self.size):
            for y in range(self.size):
                letter = self.board[x][y]
                self.findWords(x, y, [], self.trieNode, '', 'directions from ({},{})({}) go '.format(x, y, letter), log)

        # Save log into Log folder
        if save:
            for index in range(len(log)):
                fileName = str(str(index) + ".txt")
                fileName = os.path.join(MYDIR, fileName)
                with open(fileName, 'w+', encoding='utf-8') as textFile:
                    print(log[index])
                    textFile.write("    " * int(self.size / 2) + 'Case {}:'.format(index) + "    " * int(self.size / 2) + '\n' )
                    textFile.write(str(self.getBoard()))
                    textFile.write("----" * int(self.size + 2) + '\n')
                    textFile.write(log[index])
                    textFile.close()
        else:
            for index in range(len(log)):
                print(log[index])

def introduction():
    print('How to run ?')
    print('python heuristics.py size save')
    print('Example: ', 'python heuristics.py 4 0', '-> Run program with board size 4x4 and doesn`t save Log')
    print('Example: ', 'python heuristics.py 4 1', '-> Run program with board size 4x4 and save Log')


if __name__ == '__main__':
    # Test 
    # dictionary = ["TPHCM", "DHBK", "MIC", "NMAI", "TIC"]

    # x =      [['T', 'I', 'M', 'N'],
    #           ['P', 'C', 'K', 'A'],
    #           ['D', 'H', 'B', 'I'],
    #           ['N', 'O', 'T', 'H'],]

    if len(sys.argv) == 3:
        tmp = Boggle(int(sys.argv[1]))
        # tmp = Boggle(4, x, dictionary)
        tmp.run(int(sys.argv[2]))
    else:
        introduction()

time_elapsed = (time.perf_counter() - time_start)
process = psutil.Process(os.getpid())
print ("%5.1f secs %5.1f KByte" % (time_elapsed, process.memory_info().rss/1024.0))
