##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class KING(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.dangerZone = set()
		self.attacters = []
		self.threats = set()
		self.inCheck = False

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackKing.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhiteKing.png"
		else:
			print("Incorrect team selected @King.set_team()")