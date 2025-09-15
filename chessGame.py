##Imports
from backEnd import *
from backEnd.Pieces import *
from pynput import keyboard


##-------GLOBAL VARIABLES-------##
debugActive = True ##NOTE: Set this to true to have generic Debugging items displayed
columnTitle = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ##Used to generate tags for each square
rowTitle = ["1", "2", "3", "4", "5", "6", "7", "8"]
	## EX: Grid Locations, (ADD MORE AS NEEDDED)


##-------INITIAL RUNTIME-------##
CHESS = mainCanvas(columnTitle, rowTitle)


##CREATE CANVAS AND CHESS BOARD
CHESS.createCanvas()
CHESS.createGrid()

##Create the "Board" that the game is played on
BOARD = CHESS.get_canvas()


##CLASS CALLING
PLACE = placements(CHESS)
MOVE = Move(CHESS, PLACE)
INPUTS = Inputs(CHESS, MOVE)



##CREATE & PLACE PIECES IN STARTING POSITION
##--WHITE PIECES--##
PLACE.createPieces("PAWN", 8, "white")
PLACE.createPieces("ROOK", 2, "white")
PLACE.createPieces("KNIGHT", 2, "white")
PLACE.createPieces("BISHOP", 2, "white")
PLACE.createPieces("QUEEN", 1, "white")
PLACE.createPieces("KING", 1, "white")
PLACE.placePieces("white")

##--BLACK PIECES--##
PLACE.createPieces("PAWN", 8, "black")
PLACE.createPieces("ROOK", 2, "black")
PLACE.createPieces("KNIGHT", 2, "black")
PLACE.createPieces("BISHOP", 2, "black")
PLACE.createPieces("QUEEN", 1, "black")
PLACE.createPieces("KING", 1, "black")
PLACE.placePieces("black")


##-------INITIAL RUNTIME DEBUGGING EVENTS-------##
CHESS.gridTagList(debugActive=False) ##Creates a list of all tile IDs, when debugActive=True it displays those tile IDs to screen
PLACE.findNextMove(debugActive) ##Used to generate an initial list of possible moves per piece, When debugActive=True it prints posible moves to terminal

##-------LOOPING RUNTIME-------##
# print(CHESS.get_mainApp().title())
def chessLoop():
	
	if INPUTS.get_activeWindowTitle() == CHESS.get_mainApp().title():
		INPUTS.applicationActive = True
	else:
		INPUTS.applicationActive = False
	##Bind All events
	INPUTS.bindEvents()
	
	
	CHESS.get_mainApp().after(1000, chessLoop)
	

##-------POST-LOGIC RUNTIME-------##
##NOTE: MUST BE RUN AT END OF PROGRAM, Tkinter won't run properly otherwise
chessLoop()
CHESS.get_mainApp().mainloop()