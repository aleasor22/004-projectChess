##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class QUEEN(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "QUEEN"
		
		##List of Moves
		self.canMoveHere = []

	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)

	def availableMoves(self, ):
		currColumn = self.locationID[0]
		currRow = self.locationID[1]

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackQueen.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteQueen.png"
		else:
			print("Incorrect team selected @QUEEN.set_team()")