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

	def setup(self, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self, ):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Rests
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)
		self.canMoveHere = []
		self.moveSet = set()

		for i in range(-1, 2):
			for j in range(-1, 2):
				try:
					if (index_A+i) < 0 or (index_B+j) < 0:
						raise IndexError("Less than 0")
					if self.myPieceMatrix[index_A+i][index_B+j] != "**":
						raise IndexError("Spot Used")
					self.moveSet.add(self.myGlobalMatrix[index_A+i][index_B+j])
				except IndexError as e:
					# print(e)
					continue

		# print("Moves Calulated:", self.canMoveHere)
		self.setToList()


	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackKing.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteKing.png"
		else:
			print("Incorrect team selected @King.set_team()")