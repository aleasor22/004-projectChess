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

##Call the Placement Class
PLACE = placements(BOARD, CHESS)
INPUTS = Inputs(BOARD, CHESS)

##Place Pieces in their starting spots
PLACE.placeTeamWhite()
PLACE.placeTeamBlack()




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