from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

bulletOrigin = Window.height/6; # bullet origin x value

class AttackCircle(Widget):
	def isTouched(self, touch): # return true if touch is within its boundaries
		isTouch = False
		if ((touch.x < self.center_x+(self.width/2)) & (touch.x > self.center_x-(self.width/2)) & (touch.y < self.center_y+(self.width/2)) & (touch.y > self.center_y-(self.width/2))):
			isTouch=True
		return isTouch

class AttackSquare(Widget):
	pass

class AttackBullet(Widget):
	def move(self): # adds to the position of the bullet, moving it left
		self.center_x+=5

	def reset(self, circle): # resets the bullet to its origin within the circle
		self.center_x=circle.center_x

class AttackGame(Widget):
	bullet1 = AttackBullet()
	bullet2 = AttackBullet()
	bullet3 = AttackBullet()
	bullet4 = AttackBullet()
	circle1 = AttackCircle()
	circle2 = AttackCircle()
	circle3 = AttackCircle()
	circle4 = AttackCircle()

	def update(self, dt): # update the game
		if ((self.bullet1.center_x>Window.width) | (self.bullet2.center_x>Window.width) | (self.bullet3.center_x>Window.width) | (self.bullet4.center_x>Window.width)):
			self.bullet1.reset(self.circle1)
			self.bullet2.reset(self.circle1)
			self.bullet3.reset(self.circle1)
			self.bullet4.reset(self.circle1)

	def on_touch_move(self, touch): # move bullet when circle is touched
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
		Clock.schedule_interval(game.update, 1.0 / 60.0) #update the game every 1/60 of a second
		return game

if __name__ == '__main__':
	AttackApp().run()