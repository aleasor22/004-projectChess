##List of  Imports
import os
from backEnd.imageWidget import imageWidget
from Images import *


##Start of Class PAWN
class BISHOP(imageWidget):
	def __init__(self, canvas):
		imageWidget.__init__(self, canvas)
		self.pieceID = "BISHOP"
		
		##List of Moves
		self.canMoveHere = []
		self.moveSet = set()
		

	def setup(self, pos, color, tag):
			self.set_team(color)
			self.createImage()
			self.placeImage(pos[0], pos[1], tag)

	def availableMoves(self):
		# print(f"{self.myTeam}-{self.myID}'s Moves are being calculated")
		##Resets List
		self.canMoveHere = []
		self.moveSet = set()

		##Local Variables
		index_A, index_B = self._chessObject.MATRIX.findMatrixIndex(self.locationID)
		
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
		
		self.setToList()				
			

	def set_team(self, color):
		if color == "black":
			self._imgLocation = "Images/BlackBishop.png"
		elif color == "white":
			self._imgLocation = "Images/WhiteBishop.png"
		else:
			print("Incorrect team selected @Bishop.set_team()") 