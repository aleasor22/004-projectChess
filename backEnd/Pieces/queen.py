##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class QUEEN(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "QUEEN"

	def setup(self, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(tag)

	def availableMoves(self, ):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Reset
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chess.MATRIX.findMatrixIndex(self.locationID)
		
		##Bishop Style Movement
		# print("North East:", end=" ")
		for northEast in range(8):
			try:
				if index_B-northEast < 0:
					raise IndexError(f"Index Less than 0 - {index_B-northEast}")
				if northEast == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
				elif self.myPieceMatrix[index_A+northEast][index_B-northEast] != "**":
					raise IndexError
				else:
					# print(self.myGlobalMatrix[index_A+northEast][index_B-northEast], end=" ")
					self.moveSet.add(self.myGlobalMatrix[index_A+northEast][index_B-northEast])
			except IndexError as e:
				# print(e)
				break

		# print("\nNorth West:", end=" ")
		for northWest in range(8):
			try:
				if index_A-northWest < 0 or index_B-northWest < 0:
					raise IndexError("Index Less than 0")
				if northWest == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+northWest][index_B-northWest])
				elif self.myPieceMatrix[index_A-northWest][index_B-northWest] != "**":
					raise IndexError
				# print(self.myGlobalMatrix[index_A-northWest][index_B-northWest], end=" ")
				self.moveSet.add(self.myGlobalMatrix[index_A-northWest][index_B-northWest])
			except IndexError as e:
				# print(e)
				break
			
		# print("\nSouth East:", end=" ")
		for southEast in range(8):
			try:
				if southEast == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A+southEast][index_B+southEast])
				elif self.myPieceMatrix[index_A+southEast][index_B+southEast] != "**":
					raise IndexError
				# print(self.myGlobalMatrix[index_A+southEast][index_B+southEast], end=" ")
				self.moveSet.add(self.myGlobalMatrix[index_A+southEast][index_B+southEast])
			except IndexError as e:
				# print(e)
				break
		# print("\nSouth West:", end=" ")
		for southWest in range(8):
			try:
				if index_A-southWest < 0:
					raise IndexError("Index Less than 0")
				if southWest == 0:
					self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
				elif self.myPieceMatrix[index_A-southWest][index_B+southWest] != "**":
					raise IndexError
				# print(self.myGlobalMatrix[index_A-southWest][index_B+southWest], end=" ")
				self.moveSet.add(self.myGlobalMatrix[index_A-southWest][index_B+southWest])
			except IndexError as e:
				# print(e)
				break

		##Rook Style Movement
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
		
		# print("Moves Calculated:", self.canMoveHere)
		self.setToList()	

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackQueen.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteQueen.png"
		else:
			print("Incorrect team selected @QUEEN.set_team()")