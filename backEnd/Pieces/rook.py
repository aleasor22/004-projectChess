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
		currColumn = self.locationID[0]
		currRow = self.locationID[1]
		self.canMoveHere = []


		##Forward & Backward Movement
		for index in range(8):
			self.canMoveHere.append(f"{currColumn}{index+1}")

		##Side to Side Movement
		for index in self._chessObject.columnTitle:
			self.canMoveHere.append(f"{index}{currRow}")
		



	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackRook.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteRook.png"
		else:
			print("Incorrect team selected @ROOK.set_team()")