##Imports
from backEnd import *
from backEnd.Pieces import *
from pynput import keyboard


##-------GLOBAL VARIABLES-------##
debugActive = True ##NOTE: Set this to true to have generic Debugging items displayed


##-------INITIAL RUNTIME-------##
CHESS = CANVAS()


##CREATE CANVAS AND CHESS BOARD
CHESS.createCanvas()
CHESS.createGrid()

##Create the "Board" that the game is played on
BOARD = CHESS.get_canvas()


##CLASS CALLING
CALC = MOVECALC(CHESS)
PLACE = PLACEMENT(CHESS, CALC)
INPUTS = Inputs(CHESS, PLACE)



##CREATE & PLACE PIECES IN STARTING POSITION
##--WHITE PIECES--##
PLACE.createPieces("PAWN", 8, "white")
PLACE.createPieces("ROOK", 2, "white")
PLACE.createPieces("KNIGHT", 2, "white")
PLACE.createPieces("BISHOP", 2, "white")
PLACE.createPieces("QUEEN", 1, "white")
PLACE.createPieces("KING", 1, "white")

##--BLACK PIECES--##
PLACE.createPieces("PAWN", 8, "black")
PLACE.createPieces("ROOK", 2, "black")
PLACE.createPieces("KNIGHT", 2, "black")
PLACE.createPieces("BISHOP", 2, "black")
PLACE.createPieces("QUEEN", 1, "black")
PLACE.createPieces("KING", 1, "black")

PLACE.placePieces()

##-------INITIAL RUNTIME DEBUGGING EVENTS-------##
if debugActive:
	CHESS.gridTagList() ##Creates a list of all tile IDs, when debugActive=True it displays those tile IDs to screen

##-------LOOPING RUNTIME-------##
# print(CHESS.get_mainApp().title())
def chessLoop():
	
	if INPUTS.get_activeWindowTitle() == CHESS.get_mainApp().title():
		INPUTS.applicationActive = True
	else:
		INPUTS.applicationActive = False
	##Bind All events
	INPUTS.bindEvents()

	PLACE.underCheck() #Checks if the king is in check
	if PLACE.kingInCheck: ##Handles logic when a king is in check
		PLACE.changeLocationColor('red')
		CALC.check = True
		CALC.dangerZone(PLACE.kingInCheckTracking)
	else:
		PLACE.changeLocationColor()
		CALC.check = False

	CHESS.get_mainApp().after(1000, chessLoop)
	

##-------POST-LOGIC RUNTIME-------##
##NOTE: MUST BE RUN AT END OF PROGRAM, Tkinter won't run properly otherwise
chessLoop()
CHESS.get_mainApp().mainloop()