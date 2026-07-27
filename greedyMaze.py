import numpy as np
import pygame as pg
pg.init()

def printToScreen(x,y,text,colour, size):
    timesnewroman = pg.font.SysFont('Arial', size) #fontType, size
    text = str(text)
    label = timesnewroman.render(text, False, colour)
    screen.blit(label,(x,y))

def convert_text_to_array(file):
    with open(file, "r") as f:
        text = f.read()
        print(text)

    textRows = text.split("\n")
    
    nr = len(textRows)
    nc = len(textRows[1])
    startPoint = None
    endPoint = None

    mazeArray = np.zeros((nr,nc), dtype=np.uint8)
    for rowNum, row in enumerate(textRows):
        for colNum, c in enumerate(row):
            if c == "A":
                mazeArray[rowNum, colNum] = 2
                startPoint = (rowNum, colNum)
            if c == "B":
                mazeArray[rowNum, colNum] = 3
                endPoint = (rowNum, colNum)
            if c == " ":
                mazeArray[rowNum, colNum] = 1

    mazeArrayScores = np.zeros((nr,nc), dtype=np.uint8)
    for rowNum, row in enumerate(textRows):
        for colNum, c in enumerate(row):
            if c == "A" or c == " ":
                score = abs(endPoint[0] - rowNum) + abs(endPoint[1]- colNum)
                mazeArrayScores[rowNum, colNum] = score
    
    return mazeArray, startPoint, endPoint, mazeArrayScores

def display_maze(mazeArray, explored_set = None):

    screen.fill("white")
    for c, x in enumerate(range(0, w, gridSize)):
        for r, y in enumerate(range(0, h, gridSize)):
            if (r, c) in explored_set:
                pg.draw.rect(screen, "yellow", (x, y, gridSize, gridSize))
                printToScreen(x+int(gridSize/3), y+int(gridSize/3), mazeArrayScores[r, c], "black", 20)
            elif mazeArray[r, c] == 0:
                pg.draw.rect(screen, "black", (x, y, gridSize, gridSize))
            elif mazeArray[r, c] == 1:
                pg.draw.rect(screen, "white", (x, y, gridSize, gridSize))
                printToScreen(x+int(gridSize/3), y+int(gridSize/3), mazeArrayScores[r, c], "black", 20)
            elif mazeArray[r, c] == 2:
                pg.draw.rect(screen, "green", (x, y, gridSize, gridSize))
            elif mazeArray[r, c] == 3:
                pg.draw.rect(screen, "red", (x, y, gridSize, gridSize))

        
            
    pg.display.flip()

class node:
    def __init__(self, state, parent, action, score):
        self.state = state
        self.parent = parent
        self.action = action
        self.score = score

class Stack:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
       self.frontier.append(node)
    
    def remove(self):
        nodeToRemove = self.frontier.pop()
        return nodeToRemove

    def contains(self, node):
        return node in self.frontier

class Queue:
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
       self.frontier.append(node)
    
    def remove(self):
        nodeToRemove = self.frontier.pop(0)
        return nodeToRemove

    def contains(self, node):
        return node in self.frontier
    
def getPossiblePositions(currentPos):
    all_pos = {}
    all_pos["L"] = (currentPos[0], currentPos[1]-1)
    all_pos["R"] = (currentPos[0], currentPos[1]+1)
    all_pos["U"] = (currentPos[0]-1, currentPos[1])
    all_pos["D"] = (currentPos[0]+1, currentPos[1])
    
    valid_moves = []

    for action, pos in all_pos.items():
        if 0<=pos[0]<nr-1 and 0<=pos[1]<nc-1 and mazeArray[pos[0], pos[1]] != 0:
            valid_moves.append((action, pos))
    return valid_moves

#Main Code
gridSize = 50
mazeFilePath = "maze2.txt"

mazeArray, start, end, mazeArrayScores = convert_text_to_array(mazeFilePath)
print(mazeArrayScores)
print(mazeArray)
nr, nc = mazeArray.shape
h, w = mazeArray.shape
h, w = h*gridSize, w*gridSize
screen = pg.display.set_mode((w, h))

# maze solving
explored_set = set()
myFrontier = Stack()
temp = node(state=start, parent = None, action = None, score = mazeArrayScores[start[0], start[1]])
myFrontier.add(temp)
numExplored = 0

while True:
    display_maze(mazeArray, explored_set)
    currentNode = myFrontier.remove()
    numExplored += 1
    if currentNode.state == end:
        resultAction = []
        resultState = []
        while not currentNode.parent is None:
            resultAction.append(currentNode.action)
            resultAction.append(currentNode.state)
            #resultAction.append(currentNode.state)
            currentNode = currentNode.parent
        
        resultState.reverse()
        resultAction.reverse()
        print(resultAction)
        break

    explored_set.add(currentNode.state)

    for action, state in getPossiblePositions(currentNode.state):
        if not myFrontier.contains(state) and state not in explored_set:
            temp = node(state=state, parent = currentNode, action = action, score = mazeArrayScores[state[0], state[1]])
            myFrontier.add(temp)

    myFrontier.frontier.sort(reverse=True, key=lambda x: x.score)

    pg.time.wait(250)

print(end)
