##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class ROOK(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 5

	def setup(self, tag):
		self.set_team()
		self.createImage()
		self.placeImage(tag)

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackRook.png"
		elif "-W" in self.myID:
			self._imgLocation ="Images/WhiteRook.png"
		else:
			print("Incorrect team selected @ROOK.set_team()")