##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class ROOK(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 5
		
		##List of Moves
		self.canMoveHere = []
			

	def setup(self, tag):
		self.set_team()
		self.createImage()
		self.placeImage(tag)
	
	def availableMoves(self):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Reset
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)
		# print("Index:", (index_A, index_B))
		
		## Horizontal Movement
		for west in range(index_A-1, -1, -1):
			if self.myPieceMatrix[west][index_B] != "**":
				break
			# print(self.myGlobalMatrix[west][index_B], end=" ")
			self.moveSet.add(self.myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			if self.myPieceMatrix[east][index_B] != "**":
				break
			# print(self.myGlobalMatrix[east][index_B], end=" ")
			self.moveSet.add(self.myGlobalMatrix[east][index_B])

		# print() ##Spacer
		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			if self.myPieceMatrix[index_A][north] != "**":
				# print(self.myPieceMatrix[index_A][north])
				break
			# print(self.myGlobalMatrix[index_A][north], end=" ")
			self.moveSet.add(self.myGlobalMatrix[index_A][north])
		
		for south in range(index_B+1, 8):
			if self.myPieceMatrix[index_A][south] != "**":
				# print(self.myPieceMatrix[index_A][south])
				break
			# print(self.myGlobalMatrix[index_A][south], end=" ")
			self.moveSet.add(self.myGlobalMatrix[index_A][south])

		# print("Moves Calculated: ", self.canMoveHere)
		self.setToList()

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackRook.png"
		elif "-W" in self.myID:
			self._imgLocation ="Images/WhiteRook.png"
		else:
			print("Incorrect team selected @ROOK.set_team()")