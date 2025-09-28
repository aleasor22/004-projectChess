##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class PAWN(PIECES):
	def __init__(self, chess):
		PIECES.__init__(self, chess)
		
		##List of Moves
		self.canMoveHere = []

	def setup(self, tag):
		self.set_team()
		self.createImage()
		self.placeImage(tag)


	def availableMoves(self):
		# print(f"{self.myTeam}-{self.myID} Moves are being calculated")
		##New Call Resets
		currRow = self.locationID[1]
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)

		if "White" in self._imgLocation:
			for col in range(-1, 2):
				try:
					if index_A+col < 0:
						raise IndexError
					self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B+1])
					if col == 0 and currRow == "2":
						# print(self.myGlobalMatrix[index_A+col][index_B+2])
						self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B+2])
				except IndexError:
					continue
		if "Black" in self._imgLocation:
			for col in range(-1, 2):
				try:
					if index_A+col < 0:
						raise IndexError
					self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B-1])
					if col == 0 and currRow == "7":
						# print(self.myGlobalMatrix[index_A+col][index_B-2])
						self.moveSet.add(self.myGlobalMatrix[index_A+col][index_B-2])
				except IndexError:
					continue	
		self.setToList()
		# print("Moves Calculated:", self.canMoveHere)

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackPawn.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhitePawn.png"
		else:
			print("Incorrect team selected @PAWN.set_team()")