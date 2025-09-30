##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class BISHOP(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 3		

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)
			
	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackBishop.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhiteBishop.png"
		else:
			print("Incorrect team selected @Bishop.set_team()") 