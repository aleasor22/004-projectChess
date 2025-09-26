import tkinter ##Needed to import the tkinter Class
from PIL import ImageTk, Image ##NOTE may not need
from .boardMatrix import MATRIX


class mainCanvas:
	def __init__(self):
		self.__chessApp = tkinter.Tk()
		self.__chessApp.title("Chess.leasor  [v0.0.566]")
		self.__board = None ##Default to None
		self.boardSize = 1024

		##Board Variables
		self.MATRIX = MATRIX()
		self.bboxTileList = []


	def createCanvas(self, ):
		##Sets boundary based on parameter "boardSize"
		self.__chessApp.geometry(str(self.boardSize)+"x"+str(self.boardSize))

		##Generate the canvas object
		self.__board = tkinter.Canvas(self.__chessApp, width=self.boardSize, height=self.boardSize)
		self.__board.grid()
		# self.board.grid(row=0, column=0, rowspan=self.boardSize, columnspan=self.boardSize)
		self.__board.grid_propagate(False)
	
	def gridTagList(self):
		for col in range(8):
			for row in range(8):
				gridTag = self.MATRIX.get_tagAtIndex(col, row)
				pos = self.get_nwCoord(self.MATRIX.get_tagAtIndex(col, row))
				self.__board.create_text(pos[0]+64, pos[1]+64, font=("Arial", 16), text=gridTag, tag=gridTag)


	def createGrid(self):
		fillActive = False
		fillColor = 'gray'
		xPos = 0
		yPos = 0
		for row in range(8):
			for col in range(8):
				if fillActive == True:
					fillColor = 'white'
					fillActive = False
				else:
					fillColor = 'gray'
					fillActive = True
				gridTag = self.MATRIX.get_tagAtIndex(col, row, "Global")
				self.__board.create_rectangle(xPos, yPos, xPos+128, yPos+128, tag=gridTag, fill=fillColor)
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
		## NOTE: Even though find_withtag returns a tuple, using it to call .coords won't error out

	def get_nwCoord(self, tag):
		try:
			self.tileBoxCoords = self.__board.coords(self.__board.find_withtag(tag)[0])
			return (self.tileBoxCoords[0], self.tileBoxCoords[1])
		except tkinter.TclError:
			print(f"NW Coords: {self.tileBoxCoords}\n")
	
	def get_canvas(self):
		return self.__board
	
	def get_mainApp(self):
		return self.__chessApp
	
	def get_bbox(self, canvasID):
		return self.__board.coords(canvasID)
