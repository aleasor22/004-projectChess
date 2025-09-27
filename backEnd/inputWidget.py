from .imageWidget import imageWidget
from pynput import keyboard
from Images import * #imports Image file locations
import pygetwindow

import tkinter ##Used for Debugging

class Inputs():
	def __init__(self, chessObject, movement):
		self.__listeningStarted =  False ##Is this needed
		self.__chessGame = chessObject
		self.__render = chessObject.get_canvas()
		self.__place = movement
		
		self.applicationActive = False
		self.currMouseLocation = None
		self.oldMouseLocation = None
		
		self.__listenForKeyboard = keyboard.Listener(on_press=self.onPress, on_release=self.onRelease)
		
		##Starts listening for keyboard & mouse events
		self.__listenForKeyboard.start()

		self.clickCounter = 0
		self.selectedPiece = None
		self.aPieceIsSelected = False
		self.canPlace = False
		self.originalLocaiton = None
		self.lastIMG = None


	##Logic for Mouse Inputs##
	def bindEvents(self, ):
		if self.applicationActive:
			self.__render.bind("<Motion>", self.findMyMouse)
			self.__render.bind("<Button-1>", self.onMousePress)
		else:
			self.__render.unbind("<Motion>")
			self.__render.unbind("<Button-1>")

	def onMousePress(self, event):
		# print(f"Mouse clicked at: {self.currMouseLocation}")
		if self.clickCounter == 0: ##Piece gets selected
			self.selectedPiece = self.__place.selectPiece(self.currMouseLocation)
			# print("first Click") ## Debuggin
			if self.selectedPiece != None:
				# print(f"Canvas ID: {self.selectedPiece.canvasID}")
				self.originalLocaiton = self.currMouseLocation
				self.aPieceIsSelected = True
				self.clickCounter += 1
		elif self.clickCounter == 1: ##Attemps to place Piece
			# print("Second Click") ## Debuggin
			print(f"Place here? {self.currMouseLocation}")
			try:				
				print(f"Selected Piece: {self.selectedPiece.myID} \nRemove {self.__place.get_piece(self.currMouseLocation).myID}")
				isPieceCaptured = self.__place.get_piece(self.currMouseLocation).myID
				self.__place.isLocationTaken(isPieceCaptured)
				pass
			except AttributeError:
				print("Free Space")
			
			
			self.aPieceIsSelected = False
			if self.canPlace:
				self.__place.movePiece(self.currMouseLocation)
			else:
				self.__place.movePiece(self.originalLocaiton)
			self.__render.delete(self.lastIMG)
			self.clickCounter = 0
		else:
			print("ERROR @onMousePress")

		

	def findMyMouse(self, event):
		try: 
			matchingCanvasIDs = None
			for bbox in self.__chessGame.bboxTileList:
				if event.x > bbox[0] and event.x < bbox[2]:
					if event.y > bbox[1] and event.y < bbox[3]:
						matchingCanvasIDs = self.__render.find_overlapping(bbox[0]+1, bbox[1]+1, bbox[2]-1, bbox[3]-1)[0]
						break

			self.currMouseLocation = self.__render.gettags(matchingCanvasIDs)[0] ##Saves current mouse location
			if self.currMouseLocation != self.oldMouseLocation:
				self.oldMouseLocation = self.currMouseLocation ##Saves original Mouse location
				
			if self.aPieceIsSelected:
				if self.currMouseLocation in self.selectedPiece.canMoveHere:
					self.canPlace = True
				else:
					self.canPlace = False
				## Visually shows the piece to follow the mouse
				pos = self.__chessGame.get_nwCoord(matchingCanvasIDs)
				self.__render.coords(self.selectedPiece.canvasID, pos[0], pos[1])
				self.lastIMG = self.selectedPiece.canvasID

		except tkinter.TclError as error:
			##currently triggers when perfectly inbetween tiles
			# print(f"Caught Error: {error} \n\t Error@ inputs.findMyMouse")
			pass

	##Logic for Keyboard inputs##
	def onPress(self, key):
		# try:
		# 	print('alphanumeric key {0} pressed'.format(key.char))
		# except AttributeError:
		# 	print('special key {0} pressed'.format(key))
		pass

	##Logic to Track Keyboard Inputs
	def onRelease(self, key):
		try:
			print(f'alphanumeric key {key.char} released')
		except AttributeError:
			##Kills program when the "escape" key is pressed
			if key == keyboard.Key.esc:
				self.stopListening()
				# self.unBindAllEvents() ##NOTE: May be needed later
				self.__render.quit()
			# print('special key {0} released'.format(key))
	
	def stopListening(self):
		self.__listeningStarted = False ##Sets listeningStarted to False
		##Stops the threads
		self.__listenForKeyboard.stop()


	
	##-------GETTERS/SETTERS-------##
	def get_activeWindowTitle(self):
		try:
			# print(pygetwindow.getActiveWindow().title)
			return pygetwindow.getActiveWindow().title
		except AttributeError as error:
			print(f"Caught Error: {error} \n\t @get_activeWindowTitle()")