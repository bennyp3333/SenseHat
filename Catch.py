from sense_hat import SenseHat
import random
import time
  
# max rgb values are [248,252,248]

class catch:

	def __init__(self, sense):
		self.sense = sense
		self.xMax = 7
		self.loX,self.loY = 3, 7
		self.lastX = self.loX
		self.roundNum = 1
		self.tempX = 0
		self.tempY = 0
		#recipe arrays
		self.recipeArray1 = [[206,154,64],[248,0,0],[206,154,64]]
		self.recipeArray2 = [[0,252,0],[248,164,0],[206,154,64],[206,154,64]]
		self.recipeArray3 = [[206,154,64],[248,0,0],[0,0,248],[188,0,100],[206,154,64]]
		#base is the base number of blocks to catch
		self.base = 3
		#define colors
		#green1,2, red1,2, blue1,2, purple1,2, (light)brown1,2, orange1,2
		self.colorArray = [[0,252,0], [248,0,0], [0,0,248], [188,0,100], [206,154,64], [248,164,0]]
		self.colorArray2 = [[0,126,0], [124,0,0], [0,0,124], [94,0,50], [103,77,32], [124,82,0]]
		
	def catcher(self):
		#setup catch order, create player
		self.setupRound()
		sense.set_pixel(self.loX, self.loY, [248,252,248])
		fall = True
		
		while(True):
			#run the program in here
			
			#player control
			for event in sense.stick.get_events():
				if event.action == 'pressed' and event.direction == 'right' and self.loX < self.xMax-1:
					self.loX = self.lastX+1
				elif event.action == 'pressed' and event.direction == 'left' and self.loX > 0:
					self.loX = self.lastX-1
			
			#move player to new pixel		
			sense.set_pixel(self.lastX,self.loY,[0,0,0])
			self.lastX = self.loX
			sense.set_pixel(self.loX, self.loY, [248,252,248])
			
			time.sleep(0.5)
			
			if fall == True:
				#do the ingredient falling and check for a catch
				self.falling()
				fall = False
			elif fall == False:
				fall = True
				self.summonIngredient()
			
	def setupRound(self):
		#check round number, print the desired recipe and create recipe array
		yPlace = 0
		if self.roundNum == 1:
		  sense.show_message("Catch ingredients in the top right! Round one, raspberry pie!")
		  for i in self.recipeArray1:
		    sense.set_pixel(7,yPlace,self.recipeArray1[yPlace])
		    yPlace += 1
		elif self.roundNum == 2:
		  sense.show_message("Round 2, taco!")
		  for i in self.recipeArray2:
		    sense.set_pixel(7,yPlace,self.recipeArray2[yPlace])
		    yPlace += 1
		elif self.roundNum == 3:
		  #sense.show_message("Final round, wildberry pie! ")
		  for i in self.recipeArray3:
		    sense.set_pixel(7,yPlace,self.recipeArray3[yPlace])
		    yPlace += 1
		else:
		  sense.show_message("You Win!")
		  
		
	def summonIngredient(self):
	  #creates a new ingredient every other cycle
	  ingColor = random.randint(0,5)
	  ingPlace = random.randint(0,6)
	  sense.set_pixel(ingPlace, 0, self.colorArray[ingColor])
	  
	def falling(self):
	  #if pixel in bottom row is not the player, set it to black
	  for x in range (0,7):
  	  if sense.get_pixel(x,7) != [248,252,248]:
	      sense.set_pixel(x,7,[0,0,0])
	  #if pixel is colored in not the bottom row, move it down one, also allows the player to "catch" an ingredient
	  for y in range (6,-1,-1):
	    for x in range (0,7):
	      if sense.get_pixel(x,y) != [0,0,0]: 
	        if  sense.get_pixel(x,y+1) != [248,252,248]:
	          sense.set_pixel(x, y+1, sense.get_pixel(x,y))
	          sense.set_pixel(x,y,[0,0,0])
	        else:
	          self.tempX = x
	          self.tempY = y
	          self.advanceStage()
	          
	def advanceStage(self):
	  #checks if coaught ingredient is the same as the next ingredient you were uspposed to catch, advances game if it is
	  if sense.get_pixel(self.tempX,self.tempY) == sense.get_pixel(7,0):
	    if sense.get_pixel(7,1) == [0,0,0]:
	      self.roundNum += 1
	      self.setupRound()
	    else:
	      sense.set_pixel(self.tempX, self.tempY,[0,0,0])
	      for y in range(0,7):
	        sense.set_pixel(7,y,sense.get_pixel(7,y+1))
	  else:
	    #faliure state
	    sense.show_message("Oh No! You failed!")
    
    
sense = SenseHat()
sense.clear()
catch = catch(sense)
catch.catcher()