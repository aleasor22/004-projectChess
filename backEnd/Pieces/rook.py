##List of  Imports
import os
from backEnd.movement import Move
from Images import *


##Start of Class PAWN
class ROOK(Move):
	def __init__(self, canvas):
		Move.__init__(self, canvas)
		self.imgLocation = None
			

	def rookSetup(self, pos, color, tag):
		self.set_team(color)
		self.createImage(self.imgLocation, tag)
		self.placeImage(pos[0], pos[1], tag)
		

	def set_team(self, color):
		if color == "black":
			self.imgLocation = "Images/BlackRook.png"
		elif color == "white":
			self.imgLocation = "Images/WhiteRook.png"
		else:
			print("Incorrect team selected @ROOK.set_team()")