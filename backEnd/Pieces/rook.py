##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class ROOK(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "ROOK"
		
		##List of Moves
		self.canMoveHere = []
			

	def setup(self, pos, color, tag):
		self.set_team(color)
		self.createImage()
		self.placeImage(pos[0], pos[1], tag)
	
	def availableMoves(self):
		##Reset
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index = self._chessObject.MATRIX.findMatrixIndex(self.locationID)
		
		for i in range(8):
			self.moveSet.add(self.myMatrix[index[0]][i])

		for j in range(8):
			self.moveSet.add(self.myMatrix[j][index[1]])

		self.setToList()

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackRook.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteRook.png"
		else:
			print("Incorrect team selected @ROOK.set_team()")