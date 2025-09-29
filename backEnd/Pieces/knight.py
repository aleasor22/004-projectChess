##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class KNIGHT(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 3
		
		##List of Moves
		self.canMoveHere = []


	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self, ):
		##Resets
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)

		for i in range(-2, 3):
			for j in range(-2, 3):
				try:
					if index_A+j < 0 or index_B+i < 0:
						raise IndexError
					if j % 2 == 0 and (i == -2 or i == 2):
						raise IndexError
					elif (i==-1 or i==1) and (j>=-1 and j<=1):
						raise IndexError
					elif (i==0 and j!=0):
						raise IndexError
					else:
						self.moveSet.add(self.myGlobalMatrix[index_A+j][index_B+i])
				except IndexError:
					continue
		self.setToList()
				


	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackKnight.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhiteKnight.png"
		else:
			print("Incorrect team selected @Knight.set_team()")