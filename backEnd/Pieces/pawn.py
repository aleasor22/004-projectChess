##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class PAWN(PIECES):
	def __init__(self, chess):
		PIECES.__init__(self, chess)
		self.piecePoints = 1
		

	def setup(self, tag):
		self.set_team()
		self.createImage()
		self.placeImage(tag)

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackPawn.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhitePawn.png"
		else:
			print("Incorrect team selected @PAWN.set_team()")