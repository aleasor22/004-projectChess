import tkinter ##Needed to import the tkinter Class
from PIL import ImageTk, Image ##NOTE may not need
# from Images import * ##NOTE may not need


class mainCanvas:
	def __init__(self, columnTitle, rowTitle):
		self.__chessApp = tkinter.Tk()
		self.__chessApp.title("Chess.leasor  [v0.0.53]")
		self.__board = None ##Default to None
		self.boardSize = 1024

		##Board Variables
		self.columnTitle = columnTitle ##Used to generate tags for each square
		self.rowTitle = rowTitle ##Used for tracking of rows
		self.bboxTileList = []
		self.tileTitleList = []

		##Piece Tracking
		self.activePositions = []

	def createCanvas(self, ):
		##Sets boundary based on parameter "boardSize"
		self.__chessApp.geometry(str(self.boardSize)+"x"+str(self.boardSize))

		##Generate the canvas object
		self.__board = tkinter.Canvas(self.__chessApp, width=self.boardSize, height=self.boardSize)
		self.__board.grid()
		# self.board.grid(row=0, column=0, rowspan=self.boardSize, columnspan=self.boardSize)
		self.__board.grid_propagate(False)
	
	def gridTagList(self, debugActive):
		xPos = 0
		yPos = 0
		for row in self.rowTitle:
			for column in self.columnTitle:
				gridTag = f"{column}{row}"
				if debugActive:
					self.__board.create_text(xPos+64, yPos+64, font=("Arial", 16), text=gridTag, tag=gridTag)
				self.tileTitleList.append(gridTag)
				xPos += 128
			yPos += 128
			xPos = 0
		# print(self.tileTitleList, f"length of list: {len(self.tileTitleList)}")

	def createGrid(self, ): ## NOTE: Need to add a label system to the grid spots (A1, A2, A3, etc.)
		fillActive = False
		fillColor = 'gray'
		xPos = 0
		yPos = 0
		for row in range(8):
			for column in range(8):
				if fillActive == True:
					fillColor = 'white'
					fillActive = False
				else:
					fillColor = 'gray'
					fillActive = True
				gridTag = f"{self.columnTitle[column]}{row+1}"
				self.__board.create_rectangle(xPos, yPos, xPos+128, yPos+128, tag=gridTag, fill=fillColor)
				# self.__board.create_text(xPos+64, yPos+64, font=("Arial", 16), text=gridTag, tag=gridTag)
				xPos += 128
			if row % 2 == 0:
				fillActive = True
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

	def updateTracking(self, object):
		# print("Old List:", self.activePositions)
		for index in range(len(self.activePositions)):
			if self.__origin == self.activePositions[index]:
				self.activePositions[index] = self.__board.gettags(object.canvasID)[0]
		# print("New List:", self.activePositions)
		

	def get_nwCoord(self, tag):
		try:
			# print(f"find_withtag: {self.__board.find_withtag(tag)[0]}")
			# print(f"coords: {self.__board.coords(self.__board.find_withtag(tag)[0])}")
			self.tileBoxCoords = self.__board.coords(self.__board.find_withtag(tag)[0])
			# print(self.tileBoxCoords, f"Coords of Tag: {tag}")
			return (self.tileBoxCoords[0], self.tileBoxCoords[1])
		except tkinter.TclError:
			print(f"NW Coords: {self.tileBoxCoords}\n")
	
	def get_canvas(self):
		return self.__board
	
	def get_mainApp(self):
		return self.__chessApp
	
	def get_bbox(self, canvasID):
		return self.__board.coords(canvasID)

	def set_origin(self, origin):
		self.__origin = origin	
