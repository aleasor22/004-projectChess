##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class KING(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		
		##List of Moves
		self.canMoveHere = []

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self, ):
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
						self.moveSet.add(self.myGlobalMatrix[index_A+i][index_B+j])
						raise IndexError("Spot Used")
					self.moveSet.add(self.myGlobalMatrix[index_A+i][index_B+j])
				except IndexError as e:
					# print(e)
					continue
		self.setToList()


	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackKing.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhiteKing.png"
		else:
			print("Incorrect team selected @King.set_team()")