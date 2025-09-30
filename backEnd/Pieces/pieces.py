from ..imageWidget import IMAGE
from Images import *

class PIECES(IMAGE):
	def __init__(self, chess):
		IMAGE.__init__(self, chess)
		self.__chess = chess

		##Point System
		self.piecePoints = 0

		##Movement Logic
		self.canMoveHere = []
		self.moveSet = set()
		self.myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.myPieceMatrix = chess.MATRIX.get_matrix("Piece")
		
		##Visual aspect of Movement Logic
		self._shownMoves = [] ##Holds canvas IDs of a pieces possible moves
		self._showMovesImg = IMAGE(chess)
		self._showMovesImg.createImage("Images/possibleMove.png")

	
	def showMyMoves(self):
		self._shownMoves = [] ##Resets List
		if len(self.canMoveHere) > 0:
			for location in self.canMoveHere:
				self._showMovesImg.placeImage(location)
				self._shownMoves.append(self._showMovesImg.canvasID)
			# print(self._shownMoves)
	
	def delShownMoves(self):
		for id in self._shownMoves:
			self._render.delete(id)

	def isInList(self, ID, myList):
		if ID in myList:
			return True
		return False
	
	def setToList(self):
		self.canMoveHere=[]
		for length in range(len(self.moveSet)):
			popItem = self.moveSet.pop()
			if popItem != self.locationID:
				self.canMoveHere.append(popItem)
		# print(f"Posssible Moves for {self.myID}: {self.canMoveHere}")
		# print("\t@PIECES.setToList( )")