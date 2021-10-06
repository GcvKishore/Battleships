"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["Number of rows"] = 10
    data["Number of cols"] = 10
    data["Board Size"] = 500
    data["Cell Size"] = data["Board Size"]/data["Number of rows"]
    data["num Of Ships"] = 5
    data["computer Board"] = emptyGrid(data["Number of rows"],data["Number of cols"])
    data["user Board"] = emptyGrid(data["Number of rows"],data["Number of cols"])
    # data["user Board"] = test.testGrid()
    data["computer Board"] = addShips(data["computer Board"],data["num Of Ships"]) 
    data["temporary Ship"] = []
    data["numOfShips"] = 0
    data["winner"] = None
    data["max Turns"] = 50
    data["current Turns"] = 0
    return 

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user Board"],True)
    drawGrid(data,compCanvas,data["computer Board"],False)
    drawShip(data,userCanvas,data["temporary Ship"])
    if(data["winner"]=="user"):
        drawGameOver(data,userCanvas) 
    elif(data["winner"]=="comp"):
        drawGameOver(data,compCanvas) 
    elif data["winner"]=="draw": 
        drawGameOver(data,userCanvas) 
        drawGameOver(data,compCanvas)
    return

'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if(event):
        makeModel(data)
    return


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    click=getClickedCell(data,event)
    if board == "user":
        clickUserBoard(data,click[0],click[1])
    elif board == "comp":
        runGameTurn(data,click[0],click[1]) 
    return

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for i in range(rows):
        list = []  
        for j in range(cols):
            list.append(EMPTY_UNCLICKED)
        grid.append(list) 
    return grid

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip(): 
    row = random.randint(1,8)
    col = random.randint(1,8)
    edge = random.randint(0,1)
    ship = [[],[],[]]  
    if edge == 0:
       ship = [[row,col-1],[row,col],[row,col+1]] 
    else:
        ship = [[row-1,col],[row,col],[row+1,col]] 
    return ship 
#Its a createShip function. 
'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count = 0
    for every in ship:
        row=every[0]
        col=every[1]
        if grid[row][col]!=EMPTY_UNCLICKED:
            return False
    return True 
# checkShip Function
'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    num=0
    while num<numShips:
        ship=createShip()
        if checkShip(grid,ship)==True:
            for each in ship:
                row=each[0]
                col=each[1]
                grid[row][col]=SHIP_UNCLICKED
            num = num+1
    return grid

'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["Number of rows"]):
        for col in range(data["Number of cols"]):
            if grid[row][col] == SHIP_UNCLICKED: 
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="yellow")
            elif grid[row][col] == EMPTY_UNCLICKED:
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="blue")
            elif grid[row][col] == SHIP_CLICKED:
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="red")
            elif grid[row][col] == EMPTY_CLICKED:
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="white")
            if(grid[row][col]==SHIP_UNCLICKED) and (showShips==False):
                canvas.create_rectangle(data["Cell Size"]*col, data["Cell Size"]*row, data["Cell Size"]*(col+1), data["Cell Size"]*(row+1), fill="blue")
    return data

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    if ship[0][1]==ship[1][1]==ship[2][1]:
        ship.sort()
        if ship[0][0]+1==ship[1][0]==ship[2][0]-1:
            return True
    return False
    
'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    if ship[0][0]==ship[1][0]==ship[2][0]:
        ship.sort()
        if ship[0][1]+1==ship[1][1]==ship[2][1]-1:
            return True
    return False

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    ycoord=int(event.y/data["Cell Size"])
    xcoord=int(event.x/data["Cell Size"]) 
    return [ycoord,xcoord] 
    

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for row in range(len(ship)):
        canvas.create_rectangle(data["Cell Size"]*ship[row][1],data["Cell Size"]*ship[row][0],data["Cell Size"]*(ship[row][1]+1),data["Cell Size"]*(ship[row][0]+1),fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
       if isHorizontal(ship) or isVertical(ship):
           return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data): 
    if shipIsValid(data["user Board"],data["temporary Ship"]):
        for ship in data["temporary Ship"]:
            data["user Board"][ship[0]][ship[1]]=SHIP_UNCLICKED
        data["numOfShips"] +=1
    else:
        print("ship is not valid")
    data["temporary Ship"] =[]
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["numOfShips"]==5:
        print("Start the game:")
        return
    if[row,col] not in data["temporary Ship"]:
        data["temporary Ship"].append([row,col]) 
        if len(data["temporary Ship"])==3:
            placeShip(data) 
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board==data["computer Board"] or data["user Board"]: 
        if board[row][col]==SHIP_UNCLICKED: 
            board[row][col]=SHIP_CLICKED 
        elif board[row][col]==EMPTY_UNCLICKED: 
            board[row][col]=EMPTY_CLICKED
    if isGameOver(board):
        data["winner"]=player
    return

'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if(data["computer Board"][row][col]==SHIP_CLICKED) or (data["computer Board"][row][col]==EMPTY_CLICKED): 
        return 
    else: 
        updateBoard(data,data["computer Board"],row,col,"user")
    

'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''

def getComputerGuess(board):
    index=0 
    while(index<1): 
        row=random.randint(0,9) 
        col=random.randint(0,9) 
        if(board[row][col]==SHIP_UNCLICKED) or (board[row][col]==EMPTY_UNCLICKED): 
            index=index+1 
            return[row,col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]==SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if(data["winner"]=="user"):
        canvas.create_text(100, 50, text="Congrats! You won !!", fill="black", font=('Arial 11 bold'))
        canvas.create_text(150, 70, text="Press Enter to Play Again !!", fill="black", font=('Arial 13 bold'))
    if(data["winner"]=="comp"):
        canvas.create_text(100, 50, text="Try Again ! You lost!!", fill="black", font=('Arial 11 bold'))
        canvas.create_text(150, 70, text="Press Enter to Play Again !!", fill="black", font=('Arial 13 bold'))
    if(data["winner"]=="draw"): 
        canvas.create_text(100 ,50, text="Draw Match! Out of moves!!", fill="black", font=("Arial 11 bold"))
        canvas.create_text(150, 70, text="Press Enter to Play Again !!", fill="black", font=('Arial 13 bold'))
    return

### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    # test.week3Tests()
    runSimulation(500, 500)
    # test.testIsHorizontal()
    # test.testIsVertical()
    # test.testGetClickedCell() 
    # test.testShipIsValid()
    # test.testUpdateBoard() 
    # test.testGetComputerGuess()
    # test.testIsGameOver() 