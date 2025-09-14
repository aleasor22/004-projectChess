##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class BISHOP(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "BISHOP"
		

	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)


	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackBishop.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteBishop.png"
		else:
			print("Incorrect team selected @Bishop.set_team()")