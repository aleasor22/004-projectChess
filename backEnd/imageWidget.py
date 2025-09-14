##List of Imports
import os
import tkinter as tk
from PIL import ImageTk, Image


##Start of the Image Class
class imageWidget:
	def __init__(self, canvas):
		"""Everything to do with creating/displaying images to screen"""
		self.__render = canvas #Only for this class

		## Identifying Tags (Global)
		self.locationID = None
		self.canvasID = None
		self.pieceID = None
		self.myID = None
		
		## Image Data (Local)
		self._imgLocation = None
		self._imagePIL = None
		self._imgSize = None
		self._imageTK = None
	
	def createImage(self):
		self._imagePIL = Image.open(str(self._imgLocation))
		self._imgSize = self._imagePIL.size
		self._imageTK = ImageTk.PhotoImage(self._imagePIL)


	def placeImage(self, x, y, tag):
		self.locationID = tag
		self.canvasID = self.__render.create_image(
			x, y, tag=(self.locationID, self.myID, self.pieceID), image=self._imageTK, anchor="nw"
			)
		


	def changedMyTag(self, oldTag, newTag):
		#Save Value from original key
		old_imageTK = self._imageTK[oldTag]

		#Delete Key & Value from dictionary
		del self._imageTK[oldTag]
		##Delete original Piece
		if len(self.__render.find_withtag(oldTag)) != 0:
			self.__render.delete(self.__render.find_withtag(oldTag)[1])
		#add original Value back with new Key
		self._imageTK[newTag] = old_imageTK

	def get_imageTK_Dict(self, key=False):
		if key:
			return self._imageTK.keys()
		else:
			return self._imageTK
	
	def get_size(self):
		return self._imgSize
	

	# ##TODO: Determin if Needed/used. Then Remove later
	# def get_myTag(self): ## Returns entire List
	# 	return self._myTag