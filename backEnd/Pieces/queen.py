##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class QUEEN(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 9

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackQueen.png"
		elif "-W" in self.myID:
			self._imgLocation =  "Images/WhiteQueen.png"
		else:
			print("Incorrect team selected @QUEEN.set_team()")