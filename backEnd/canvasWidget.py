import tkinter ##Needed to import the tkinter Class
from PIL import ImageTk, Image ##NOTE may not need
# from Images import * ##NOTE may not need


class mainCanvas:
	def __init__(self):
		self.__chessApp = tkinter.Tk()
		self.__chessApp.title("Chess.leasor  [v0.0.42]")
		self.__board = None ##Default to None
		self.boardSize = 1024
		self.rowTitle = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ##Used to generate tags for each square
		self.bboxTileList = []

	def createCanvas(self, ):
		##Sets boundary based on parameter "boardSize"
		self.__chessApp.geometry(str(self.boardSize)+"x"+str(self.boardSize))

		##Generate the canvas object
		self.__board = tkinter.Canvas(self.__chessApp, width=self.boardSize, height=self.boardSize)
		self.__board.grid()
		# self.board.grid(row=0, column=0, rowspan=self.boardSize, columnspan=self.boardSize)
		self.__board.grid_propagate(False)
	
	def displayGridTagList(self, debugActive):
		if debugActive:
			xPos = 0
			yPos = 0
			for column in range(8):
				for row in range(8):
					self.__board.create_text(xPos+64, yPos+64, font=("Arial", 16), text=(self.rowTitle[row], column+1), tag=(self.rowTitle[row], column+1))
					xPos += 128
				yPos += 128
				xPos = 0

	def createGrid(self, ): ## NOTE: Need to add a label system to the grid spots (A1, A2, A3, etc.)
		fillActive = False
		fillColor = 'white'
		xPos = 0
		yPos = 0
		for column in range(8):
			for row in range(8):
				if fillActive == True:
					fillColor = 'gray'
					fillActive = False
				else:
					fillColor = 'white'
					fillActive = True
				gridTag = str(self.rowTitle[row]) + str(column+1)
				self.__board.create_rectangle(xPos, yPos, xPos+128, yPos+128, tag=gridTag, fill=fillColor)
				xPos += 128
			if column % 2 == 0:
				fillActive = True
				# print("Only on even columns") #TODO REMOVE LATER
			else: 
				fillActive = False
			yPos += 128
			xPos = 0
		
		##Add bbox of each tile to self.bboxTileList
		for canvasID in self.__board.find_all():
			self.bboxTileList.append(self.__board.coords(canvasID))

		# print(self.__board.find_withtag("a1")) 
		## NOTE: Even though find_withtag returns a tuple, using it to call .coords won't error out
		# print(self.__board.coords(self.__board.find_withtag("a1")), "CANVAS WIDGET @60")

	def get_nwCoord(self, tag):
		return (self.__board.coords(self.__board.find_withtag(tag))[0], self.__board.coords(self.__board.find_withtag(tag))[1])
	
	def get_canvas(self):
		return self.__board
	
	def get_mainApp(self):
		return self.__chessApp
	
	def get_bbox(self, canvasID):
		return self.__board.coords(canvasID)
