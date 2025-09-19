##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class KING(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "KING"
		
		##List of Moves
		self.canMoveHere = []

	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)

	def availableMoves(self, ):
		##Rests
		index_A, index_B = self._chessObject.MATRIX.findMyIndex(self.locationID)
		self.moveSet = set()

		for i in range(-1, 1):
			print(i)

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackKing.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteKing.png"
		else:
			print("Incorrect team selected @King.set_team()")