# TODO:
#   - make circles buttons
#       - when pressed moveBullet# = True
#       - when released moveBullet# = False
#   - repetative code = function
#   - move objects to separate file, game in another

# THIS PUSH IS TO CREATE AND IMPLEMENT LIST OBJECTS
# square speed not twerking
# bullet collision not twerking
# bullet end of screen probs not working

# import random
import objects
from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty

squareSpeedMultiplier = 1  # TODO can I move this to AttackSquareList


class AttackGame(Widget):
    score = NumericProperty(0)
    points = NumericProperty(0)

    circles = objects.AttackCircleList()
    squares = objects.AttackSquareList()
    bullets = objects.AttackBulletList()

    def update(self, dt):  # update the game
        global squareSpeedMultiplier

        # update score by 1 on every update
        self.score += 1

        # update speed at score 1000, 2000, and every 2000 after that
        if (self.score == 400 | self.score % 2000 == 0):
            squareSpeedMultiplier += 2.0
            self.squares = self.squares.setAllSpeedMultiplier(squareSpeedMultiplier)

        # if any bullet reaches the end of the screen, reset all bullets
        self.bullets.checkPosition(Window.width, self.circles[0])

        # if a bullet hits a square, respawn the square and return points to add
        # self.points += self.bullets.checkForCollision(self.squares, self.circles[0], self.points)
        # for i in range(0, 4):
        #     if (self.bullets[i].collide_widget(self.squares[i])):
        #         self.squares[i].respawn()
        #         self.bullets[i].reset(self.circles[0])
        #         self.points += 1

        if (self.bullet1.collide_widget(self.square1)):
            self.square1.respawn()
            self.bullet1.reset(self.circle1)
            self.points += 1
        if (self.bullet2.collide_widget(self.square2)):
            self.square2.respawn()
            self.bullet2.reset(self.circle1)
            self.points += 1
        if (self.bullet3.collide_widget(self.square3)):
            self.square3.respawn()
            self.bullet3.reset(self.circle1)
            self.points += 1
        if (self.bullet4.collide_widget(self.square4)):
            self.square4.respawn()
            self.bullet4.reset(self.circle1)
            self.points += 1

        # constantly move squares
        # self.squares.moveAll()

        self.square1.move()
        self.square2.move()
        self.square3.move()
        self.square4.move()

        #if any squares reach circle, end game
        if(self.circle1.collide_widget(self.square1) | self.circle2.collide_widget(self.square2) |
                self.circle3.collide_widget(self.square3) | self.circle4.collide_widget(self.square4)):
            pass  # change to end game screen

    def on_touch_down(self, touch):
        touch_down = True

    #def on_touch_down(self, touch): # move bullet when circle is touched
    def touched(self, touch, touch_down):
        if (touch_down is True):
            if (self.circle1.isTouched(touch) is True):  # move only bullet 1
                self.bullet1.move()
                self.bullet2.reset(self.circle1)
                self.bullet3.reset(self.circle1)
                self.bullet4.reset(self.circle1)
            elif (self.circle2.isTouched(touch) is True):  # move only bullet 2
                self.bullet2.move()
                self.bullet1.reset(self.circle1)
                self.bullet3.reset(self.circle1)
                self.bullet4.reset(self.circle1)
            elif (self.circle3.isTouched(touch) is True):  # move only bullet 3
                self.bullet3.move()
                self.bullet1.reset(self.circle1)
                self.bullet2.reset(self.circle1)
                self.bullet4.reset(self.circle1)
            elif (self.circle4.isTouched(touch) is True):  # move only bullet 4
                self.bullet4.move()
                self.bullet1.reset(self.circle1)
                self.bullet2.reset(self.circle1)
                self.bullet3.reset(self.circle1)
            else:  # reset all bullets
                self.bullet1.reset(self.circle1)
                self.bullet2.reset(self.circle1)
                self.bullet3.reset(self.circle1)
                self.bullet4.reset(self.circle1)

    def on_touch_up(self, touch):  # reset all bullets on touch release
        self.bullet1.reset(self.circle1)
        self.bullet2.reset(self.circle1)
        self.bullet3.reset(self.circle1)
        self.bullet4.reset(self.circle1)


# class HomeScreen(Screen):
#     pass


# class GameScreen(Screen):
#     pass


# class ShopScreen(Screen):
#     pass


# class EndScreen(Screen):
#     pass


class AttackApp(App):
    def build(self):
        # sm = ScreenManager()
        # sm.add_widget(HomeScreen(name='home'))
        # sm.add_widget(GameScreen(name='game'))

        game = AttackGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)  # update every 1/60s
        return game


if __name__ == '__main__':
    AttackApp().run()
