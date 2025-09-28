##List of Imports
import os
import tkinter as tk
from PIL import ImageTk, Image


##Start of the Image Class
class imageWidget:
	def __init__(self, chess):
		"""Everything to do with creating/displaying images to screen"""
		self._chess = chess
		self._render = chess.get_canvas() #Only for this class

		## Image Data (Local)
		self._imgLocation = None
		self._imagePIL = None
		self._imgSize = None
		self._imageTK = None

		## Identifying Tags (Global)
		self.locationID = None	##Active tile location (Tile Square Ex. 'a1' or 'e6')
		self.canvasID = None	##Canvas tag (Tkinters canvas item id)
		self.pieceID = None		##Piece Name (Ex. ROOK or PAWN, used to identify piece class) - PLANS FOR REMOVAL
		self.myID = None		##Personal tag (Ex. ROOK-0 or ROOK-1 - used for the team dictionary)
		
		##Movement Logic
		self.canMoveHere = []
		self.moveSet = set()
		self.myGlobalMatrix = chess.MATRIX.get_matrix("Global")
		self.myPieceMatrix = chess.MATRIX.get_matrix("Piece")

	
	def createImage(self, imgLocation=None):
		if imgLocation != None:
			self._imagePIL = Image.open(imgLocation)
		else:
			self._imagePIL = Image.open(str(self._imgLocation))
		self._imgSize = self._imagePIL.size
		self._imageTK = ImageTk.PhotoImage(self._imagePIL)


	def placeImage(self, location):
		x, y = self._chess.get_nwCoord(location)
		self.locationID = location
		self.canvasID = self._render.create_image(
			x, y, tag=(self.locationID, self.myID, self.pieceID), image=self._imageTK, anchor="nw"
			)
		
	def removeImage(self):
		if self.canvasID != None:
			self._render.delete(self.canvasID)

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

	def get_imageTK_Dict(self, key=False):
		return self._imageTK
	
	def get_size(self):
		return self._imgSize