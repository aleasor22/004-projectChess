from ..imageWidget import IMAGE

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