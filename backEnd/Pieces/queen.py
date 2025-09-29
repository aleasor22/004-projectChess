##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class QUEEN(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 9

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self, ):
		##Reset
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)
		
		##Bishop Style Movement
		for northEast in range(8):
			try:
				if index_B-northEast < 0:
					raise IndexError(f"Index Less than 0 - {index_B-northEast}")
				if northEast == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
				elif self.myPieceMatrix[index_A+northEast][index_B-northEast] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
					raise IndexError
				else:
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break
		for northWest in range(8):
			try:
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				if northWest == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A-northWest][index_B-northWest])
				elif self.myPieceMatrix[index_A-northWest][index_B-northWest] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A-northWest][index_B-northWest])
					raise IndexError
				self.moveSet.add(self.myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
		for southEast in range(8):
			try:
				if southEast == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+southEast][index_B+southEast])
				elif self.myPieceMatrix[index_A+southEast][index_B+southEast] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A+southEast][index_B+southEast])
					raise IndexError
				self.moveSet.add(self.myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		for southWest in range(8):
			try:
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				if southWest == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
				elif self.myPieceMatrix[index_A-southWest][index_B+southWest] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
					raise IndexError
				self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break

		##Rook Style Movement
		## Horizontal Movement
		for west in range(index_A-1, -1, -1):
			if self.myPieceMatrix[west][index_B] != "**":
				self.moveSet.add(self.myGlobalMatrix[west][index_B])
				break
			self.moveSet.add(self.myGlobalMatrix[west][index_B])

		for east in range(index_A+1, 8):
			if self.myPieceMatrix[east][index_B] != "**":
				self.moveSet.add(self.myGlobalMatrix[east][index_B])
				break
			self.moveSet.add(self.myGlobalMatrix[east][index_B])

		## Vertical Movment
		for north in range(index_B-1, -1, -1):
			if self.myPieceMatrix[index_A][north] != "**":
				self.moveSet.add(self.myGlobalMatrix[index_A][north])
				break
			self.moveSet.add(self.myGlobalMatrix[index_A][north])
		
		for south in range(index_B+1, 8):
			if self.myPieceMatrix[index_A][south] != "**":
				self.moveSet.add(self.myGlobalMatrix[index_A][south])
				break
			self.moveSet.add(self.myGlobalMatrix[index_A][south])
			
		self.setToList()	

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackQueen.png"
		elif "-W" in self.myID:
			self._imgLocation =  "Images/WhiteQueen.png"
		else:
			print("Incorrect team selected @QUEEN.set_team()")