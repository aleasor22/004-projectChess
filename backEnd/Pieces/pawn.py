##List of  Imports
import os
from .pieces import PIECES
from Images import *


##Start of Class PAWN
class PAWN(PIECES):
	def __init__(self, chess):
		PIECES.__init__(self, chess)
		self.piecePoints = 1
		

	def setup(self, tag):
		self.set_team()
		self.createImage()
		self.placeImage(tag)


	def availableMoves(self):
		##New Call Resets
		currRow = self.locationID[1]
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)

		if "White" in self._imgLocation:
			try: #Handles General Pawn Movement
				if self.myPieceMatrix[index_A][index_B+1] == "**":
					self.moveSet.add(self.myGlobalMatrix[index_A][index_B+1])
				if currRow == "2" and self.myPieceMatrix[index_A][index_B+2] == "**":
					self.moveSet.add(self.myGlobalMatrix[index_A][index_B+2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self.myPieceMatrix[index_A-1][index_B+1] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A-1][index_B+1])
				if self.myPieceMatrix[index_A+1][index_B+1] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A+1][index_B+1])
			except IndexError:
				pass
		if "Black" in self._imgLocation:
			try: #Handles General Pawn Movement
				if self.myPieceMatrix[index_A][index_B-1] == "**":
					self.moveSet.add(self.myGlobalMatrix[index_A][index_B-1])
					if currRow == "7" and self.myPieceMatrix[index_A][index_B-2] == "**":
						self.moveSet.add(self.myGlobalMatrix[index_A][index_B-2])
			except IndexError:
				pass
			try: ##Handles Pawn Attacks
				if self.myPieceMatrix[index_A-1][index_B-1] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A-1][index_B-1])
				if self.myPieceMatrix[index_A+1][index_B-1] != "**":
					self.moveSet.add(self.myGlobalMatrix[index_A+1][index_B-1])
			except IndexError:
				pass
		self.setToList()

	def set_team(self):
		if "-B" in self.myID:
			self._imgLocation = "Images/BlackPawn.png"
		elif "-W" in self.myID:
			self._imgLocation = "Images/WhitePawn.png"
		else:
			print("Incorrect team selected @PAWN.set_team()")