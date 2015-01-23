# TODO:
#	- make circles buttons
#		- when pressed moveBullet# = True
#		- when released moveBullet# = False
#	- repetative code = function
#	- move objects to separate file, game in another


import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty

squareSpawn = Window.width+50
squareSpeedMultiplier = 1

class AttackCircle(Widget):
	def isTouched(self, touch): # return true if touch is within its boundaries
		isTouch = False
		if ((touch.x < self.center_x+(self.width/2)) & (touch.x > self.center_x-(self.width/2)) & (touch.y < self.center_y+(self.width/2)) & (touch.y > self.center_y-(self.width/2))):
			isTouch=True
		return isTouch

class AttackSquare(Widget):
	def move(self):
		self.center_x-=2*squareSpeedMultiplier

	def respawn(self):
		global squareSpawn
		self.center_x=(squareSpawn+random.randint(0,100))

class AttackBullet(Widget):
	def move(self): # adds to the position of the bullet, moving it left
		self.center_x+=5

	def reset(self, circle): # resets the bullet to its origin within the circle
		self.center_x=circle.center_x

class AttackGame(Widget):
	score = NumericProperty(0)
	points = NumericProperty(0)

	bullet1 = AttackBullet()
	bullet2 = AttackBullet()
	bullet3 = AttackBullet()
	bullet4 = AttackBullet()
	circle1 = AttackCircle()
	circle2 = AttackCircle()
	circle3 = AttackCircle()
	circle4 = AttackCircle()
	square1 = AttackSquare()
	square2 = AttackSquare()
	square3 = AttackSquare()
	square4 = AttackSquare()

	def update(self, dt): # update the game
		global squareSpeedMultiplier


		# update score and square speed
		self.score+=1
		if (self.score==1000):
			squareSpeedMultiplier+=0.5
		elif (self.score%2000==0): # increase by 0.5 every 2000 points
			squareSpeedMultiplier+=0.5

		# if any bullet reaches the end of the screen, reset all bullets
		if ((self.bullet1.center_x>Window.width) | (self.bullet2.center_x>Window.width) | (self.bullet3.center_x>Window.width) | (self.bullet4.center_x>Window.width)):
			self.bullet1.reset(self.circle1)
			self.bullet2.reset(self.circle1)
			self.bullet3.reset(self.circle1)
			self.bullet4.reset(self.circle1)

		# if a bullet hits a square, respawn the square
		if (self.bullet1.collide_widget(self.square1)):
			self.square1.respawn()
			self.bullet1.reset(self.circle1)
			self.points+=1
		if (self.bullet2.collide_widget(self.square2)):
			self.square2.respawn()
			self.bullet2.reset(self.circle1)
			self.points+=1
		if (self.bullet3.collide_widget(self.square3)):
			self.square3.respawn()
			self.bullet3.reset(self.circle1)
			self.points+=1
		if (self.bullet4.collide_widget(self.square4)):
			self.square4.respawn()
			self.bullet4.reset(self.circle1)
			self.points+=1

		# constantly move squares
		self.square1.move()
		self.square2.move()
		self.square3.move()
		self.square4.move()

		#if any squares reach circle, end game
		if(self.circle1.collide_widget(self.square1)|self.circle2.collide_widget(self.square2)|self.circle3.collide_widget(self.square3)|self.circle4.collide_widget(self.square4)):
			pass # change to end game screen

	def on_touch_down(self):
		touch_down = True;

	#def on_touch_down(self, touch): # move bullet when circle is touched
	def touched(self, touch, touch_down):
		if (touch_down==True):
			if (self.circle1.isTouched(touch)==True): # move only bullet 1
				self.bullet1.move()
				self.bullet2.reset(self.circle1)
				self.bullet3.reset(self.circle1)
				self.bullet4.reset(self.circle1)
			elif (self.circle2.isTouched(touch)==True): # move only bullet 2
				self.bullet2.move()
				self.bullet1.reset(self.circle1)
				self.bullet3.reset(self.circle1)
				self.bullet4.reset(self.circle1) 
			elif (self.circle3.isTouched(touch)==True): # move only bullet 3
				self.bullet3.move()
				self.bullet1.reset(self.circle1)
				self.bullet2.reset(self.circle1)
				self.bullet4.reset(self.circle1)
			elif (self.circle4.isTouched(touch)==True): # move only bullet 4
				self.bullet4.move()
				self.bullet1.reset(self.circle1)
				self.bullet2.reset(self.circle1)
				self.bullet3.reset(self.circle1)
			else: # reset all bullets
				self.bullet1.reset(self.circle1)
				self.bullet2.reset(self.circle1)
				self.bullet3.reset(self.circle1)
				self.bullet4.reset(self.circle1)

	def on_touch_up(self, touch): # reset all bullets on touch release
		self.bullet1.reset(self.circle1)
		self.bullet2.reset(self.circle1)
		self.bullet3.reset(self.circle1)
		self.bullet4.reset(self.circle1)

class HomeScreen(Screen):
	pass

class GameScreen(Screen):
	pass

class ShopScreen(Screen):
	pass

class EndScreen(Screen):
	pass

class AttackApp(App):
	def build(self):
		# sm = ScreenManager()
		# sm.add_widget(HomeScreen(name='home'))
		# sm.add_widget(GameScreen(name='game'))

		game = AttackGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0) #update the game every 1/60 of a second
		return game

if __name__ == '__main__':
	AttackApp().run()