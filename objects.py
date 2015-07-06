# This file contains objects used in the game

import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

squareSpawn = Window.width+50

class AttackCircle(Widget):
	def isTouched(self, touch): # return true if touch is within its boundaries
		isTouch = False
		if ((touch.x < self.center_x+(self.width/2)) & (touch.x > self.center_x-(self.width/2)) & (touch.y < self.center_y+(self.width/2)) & (touch.y > self.center_y-(self.width/2))):
			isTouch=True
		return isTouch

class AttackSquare(Widget):
	def __init__(self, **kwargs):
		super(AttackSquare, self).__init__(**kwargs)
		self.speedMultiplier = 1

	def setSpeedMultiplier(self, speedMultiplier):
		self.speedMultiplier = speedMultiplier

	def move(self):
		self.center_x-=2*self.speedMultiplier

	def respawn(self):
		# global squareSpawn
		self.center_x=(squareSpawn+random.randint(0,100))

class AttackBullet(Widget):
	def move(self): # adds to the position of the bullet, moving it left
		self.center_x+=5

	def reset(self, circle): # resets the bullet to its origin within the circle
		self.center_x=circle.center_x