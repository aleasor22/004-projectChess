##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class BISHOP(PIECES):
	def __init__(self, canvas):
		PIECES.__init__(self, canvas)
		self.piecePoints = 3
		
		##List of Moves
		self.canMoveHere = []
		self.moveSet = set()
		

	def setup(self, tag):
			self.set_team()
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self):
		##Resets List
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)
		for northEast in range(8):
			try:
				if index_B-northEast < 0:
					raise IndexError(f"Index Less than 0 - {index_B-northEast}")
				if northEast == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
				elif self.myPieceMatrix[index_A+northEast][index_B-northEast] != "**":
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
					self.moveSet.add(self.myGlobalMatrix[index_A+northWest][index_B-northWest])
				elif self.myPieceMatrix[index_A-northWest][index_B-northWest] != "**":
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
					raise IndexError
				self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break		
		self.setToList()				
			

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackBishop.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhiteBishop.png"
		else:
			print("Incorrect team selected @Bishop.set_team()") 