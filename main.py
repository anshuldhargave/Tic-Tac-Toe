
import random


def inititalizingBoard(board):
    # board = [' ', ' ',' ',' ', ' ',' ',' ',' ',' ']
    #board = []
    for x in range(0, 9):
        board.append(" ")
    return board


def inititalizingBoard1(board):
    #board = [' ', ' ',' ',' ', ' ',' ',' ',' ',' ']
    board = []


def printBoard(board, uData, nm):
    print("\n")
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + "     0 | 1 | 2")
    print("---------")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + "     3 | 4 | 5")
    print("---------")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + "     6 | 7 | 8")
    print("\n")
    print(f"{nm} is playing...")



def whoGoesFirst():  # generate a random number and then decide who goes first OR # toss a coin and decide who goes first
    randomNumber = random.randint(0, 4)
    if randomNumber == 2:
        print("You'll be playing first.")
    else:
        print("Computer will be playing first")
        makeComputerMove()


def choosePiece(nm):
    global HP  # ye global likhne ke baad hi player and computer ko barabr pieces mil rhe hai
    global CP  # and if ye global HP and CP hata diya toh incorrect pieces milrhe hai
    i = input(f"Please choose your piece {nm}: ")
    while(i not in ('X', 'x', 'o', 'O')):
        i = input("Invalid Input! Please choose 'X' or 'O' : ")
    if(i in ('X', 'x')):
        HP = 'X'
        CP = 'O'
    else:
        # (i in ('O','o')):
        HP = 'O'
        CP = 'X'


# def getUserInput(board, nm):
#     try:
#         pos = input(f"Please give a position to play {nm}: ")
#         while not pos.isnumeric(): 
#             pos = (input(f"Please give a valid position {nm}: "))
#         return pos
#             # if not validMove(pos, board):
#             #     pos = (input(f"Please give a valid position {nm}: "))
#             #     return pos
#     except ValueError:
#         print("hi") 

def getUserInput(board, nm):
    pos = int(input(f"Please give a position to play {nm}: "))
    if not validMove(pos, board):
        pos = int(input(f"Please give a valid position {nm}: "))
    return pos
           
    
    
    
    # if not int(pos):
        # askAGain = input(f"Please give a valid position to play {nm}: ")  

def makeHumanMove(board, nm):
    pos = getUserInput(board, nm)
    pos = int(pos)
    board[pos] = HP

def validMove(pos, board):
    #pos = int(pos)
    return (pos >= 0) and (pos < 9) and (board[pos] == " ")


def bestPossibleMove(board): 
    goodSequence = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for move in goodSequence:
        if validMove(move, board):
            return move


def makeComputerMove(board):
    goodSequence = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    achaMove = goodMove(CP, board)  # first preference
    if(achaMove == 999):
        achaMove = goodMove(HP, board)  # second preference
    if(achaMove == 999):
        achaMove = bestPossibleMove(board)  # third preference
    #print("best move decided: ", achaMove)
    board[achaMove] = CP


def allPositionsOf(player, board):
    allPositions = []
    for index in range(0, len(board)):
        if(board[index] == player):
            allPositions.append(index)
    return allPositions


def goodMove(player, board):
    winningPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    allPositions = allPositionsOf(player, board)
    for winningPosition in winningPositions:
        tempWinningPosition = winningPosition
        matches = 0
        for index in range(0, len(tempWinningPosition)):
            if(tempWinningPosition[index] in allPositions):
                tempWinningPosition[index] = 999
                matches += 1
            if(matches == 2):
                for num in tempWinningPosition:
                    if num != 999 and (board[num] == " "):
                        return num
    return 999


def checkWinner(player, board):
    # print("checking winner for: ", player)
    if (board[0] == board[1] == board[2] == player):
        # print("is Winner!")
        return True
    elif (board[3] == board[4] == board[5] == player):
        # print("is Winner!")
        return True
    elif (board[6] == board[7] == board[8] == player):
        # print("is Winner!")
        return True
    elif (board[0] == board[3] == board[6] == player):
        # print("is Winner!")
        return True
    elif (board[1] == board[4] == board[7] == player):
        # print("is Winner!")
        return True
    elif (board[2] == board[5] == board[8] == player):
        # print("is Winner!")
        return True
    elif (board[0] == board[4] == board[8] == player):
        # print("is Winner!")
        return True
    elif (board[2] == board[4] == board[6] == player):
        # print("is Winner!")
        return True
    else:
        return False


def kheloAurPlayerBadlo(currentPlayer, board, nm):
    if (currentPlayer == HP):
        makeHumanMove(board, nm)
        currentPlayer = CP
    else:
        makeComputerMove(board)
        currentPlayer = HP
    return currentPlayer


def doYouWantToPlayAgain(msg):
    play_Again = input(msg)
    if (play_Again in ('y', 'YES', 'yes', 'Yes')):
        return True
    else:
        return False


def login():  # If three invalid attempts, program ends.
    for attempts in range(2):
        name = input("Please enter your name: ")
        passwordEnternedByUsder = input("Please enter your password: ")
        if (name in uData) and (passwordEnternedByUsder in uData[name]):
            print("")
            print(f"WELCOME {name}!")
            return (True, name)
    else:
        # print("You're LOggED OUT!")
        return (False,)


def displayWelcomeMessage(msg):
    print(msg)


def getData():
    return uData


def getScore(a):
    return uData[a[1]][1]


def byeByeMsg(msg):  # Print thanks for playing and display the final score and also tell the user how many games you've played. (If yes, increase the count)
    print(msg)

    
# Creating Dictionary
uData = {'Anshul': ['123', 0, 0], 'Praful': ['456', 0, 0]}


# Functions_Calling:

def main():
    displayWelcomeMessage("WELCOME TO THE BEST GAME EVER\n ***TIC-TAC-TOE***")
    gameIsStillGoing = True
    activePlayer = ()
    activePlayer = login()
    if(activePlayer[0]):
        while(gameIsStillGoing):
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            uData = getData()
            currentPlayerName = activePlayer[1]
            uData[currentPlayerName][2] = uData[currentPlayerName][2] + 1
            printBoard(board, uData, activePlayer[1])
            choosePiece(activePlayer[1])
            print(f"{activePlayer[1]} : {HP}")
            print(f"Computer : {CP}")

            currentPlayer = HP
            continueGame = True
            while(continueGame):
                aglaPlayer = kheloAurPlayerBadlo(currentPlayer, board, activePlayer[1])
                printBoard(board, uData, activePlayer[1])
                if(checkWinner(currentPlayer, board) == True):
                    if currentPlayer == HP:
                        print(f"{activePlayer[1]} WON!!!")
                        uData[activePlayer[1]][1] += 10
                        s = uData[activePlayer[1]][1]
                        print(f"Your current score is {s}")
                    else:
                        print("Computer WON!!!")
                        s = uData[activePlayer[1]][1]
                        ss = s-10
                        uData[activePlayer[1]][1] = ss
                        print(
                            f"Your current score is {uData[activePlayer[1]][1]}\n")
                    continueGame = False
                    break

                elif " " not in board:
                    print("Draw.")
                    #print(f"Your current score is {s}")
                    continueGame = False
                currentPlayer = aglaPlayer
            gameIsStillGoing = doYouWantToPlayAgain("Do you want to continue playing, Y|N ?: ")
            # if gameIsStillGoing == True:
            #     uData[a[1]][2] = uData[a[1]][2] + 1
            if gameIsStillGoing == False:  # ,'YES','yes','Yes'):
                finalScore = getScore(activePlayer)
                byeByeMsg(f"Your Final Score is {finalScore} in total {uData[currentPlayerName][2]} games.\n")
            if(not gameIsStillGoing):
                break
        print(f"Thank you for playing {activePlayer[1]}!\n")
        newGameUser = input("Do you want to play again with different user?, Y|N: ")
        print("See you soon! \n")
        if newGameUser == 'y':
            activePlayer = login()
    else:
        print("Invalid Credentials! Please restart the game...")


main()
