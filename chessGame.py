##Imports
from backEnd import *
from backEnd.Pieces import *
from pynput import keyboard


##-------GLOBAL VARIABLES-------##
ActiveDebug = False ##NOTE: Set this to true to have generic Debugging items displayed
	## EX: Grid Locations, (ADD MORE AS NEEDDED)


##-------INITIAL RUNTIME-------##
CHESS = mainCanvas()


##CREATE CANVAS AND CHESS BOARD
CHESS.createCanvas()
CHESS.createGrid()

##Create the "Board" that the game is played on
BOARD = CHESS.get_canvas()

##BLANK PIECES
PIECE_LIST = [ROOK(BOARD), KNIGHT(BOARD), BISHOP(BOARD), KING(BOARD), QUEEN(BOARD), PAWN(BOARD)]

##CLASS CALLING
PLACE = placements(BOARD, CHESS, PIECE_LIST)
INPUTS = Inputs(BOARD, CHESS)


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
CHESS.displayGridTagList(ActiveDebug)


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