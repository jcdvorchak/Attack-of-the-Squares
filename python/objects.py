# This file contains objects used in the game

import random
from kivy.uix.widget import Widget
from kivy.core.window import Window

squareSpawn = Window.width+50


class AttackCircle(Widget):
    # return true if touch is within its boundaries
    def isTouched(self, touch):
        isTouch = False
        if ((touch.x < self.center_x + (self.width/2)) & (touch.x > self.center_x - (self.width/2)) &
                (touch.y < self.center_y + (self.width/2)) & (touch.y > self.center_y - (self.width/2))):
            isTouch = True
        return isTouch


class AttackCircleList(list):
    def __init__(self, **kwargs):
        super(AttackCircleList, self).__init__(**kwargs)
        for i in range(0, 4):
            self.append(AttackCircle())


class AttackSquare(Widget):
    # speedMultiplier = 1

    def __init__(self, **kwargs):
        super(AttackSquare, self).__init__(**kwargs)
        self.speedMultiplier = 1

    def setSpeedMultiplier(self, speedMultiplier):
        self.speedMultiplier = speedMultiplier
        return self  

    def move(self):
        self.center_x -= 2*self.speedMultiplier

    def respawn(self):
        # global squareSpawn
        self.center_x = (squareSpawn+random.randint(0, 100))


class AttackSquareList(list):
    def __init__(self, **kwargs):
        super(AttackSquareList, self).__init__(**kwargs)
        for i in range(0, 4):
            self.append(AttackSquare())

    def setAllSpeedMultiplier(self, speedMultiplier):
        for i in range(0, 4):
            self[i] = self[i].setSpeedMultiplier(speedMultiplier)
            return self  

    def moveAll(self):
        for i in range(0, 4):
            self[i].move()


class AttackBullet(Widget):
    def move(self):  # adds to the position of the bullet, moving it left
        self.center_x += 5

    # resets the bullet to its origin within the circle
    def reset(self, circle):
        self.center_x = circle.center_x


class AttackBulletList(list):
    def __init__(self, **kwargs):
        super(AttackBulletList, self).__init__(**kwargs)
        for i in range(0, 4):
            self.append(AttackBullet())

    # if any bullet reaches the end of the screen, reset it
    def checkPosition(self, max, resetPos):
        for i in range(0, 4):
            currBullet = self[i]
            if (currBullet.center_x > max):
                currBullet.reset(resetPos)

    # if a bullet hits a square, respawn the square and add a point
    # def checkForCollision(self, squares, resetPos, points):
    #     newPoints = 0
    #     for i in range(0, 4):
    #         if (self[i].collide_widget(squares[i])):
    #             squares[i].respawn()
    #             self[i].reset(resetPos)
    #             newPoints += 1
    #     return newPoints


        # if (self.bullet1.collide_widget(self.square1)):
        #     self.square1.respawn()
        #     self.bullet1.reset(self.circle1)
        #     self.points += 1
        # if (self.bullet2.collide_widget(self.square2)):
        #     self.square2.respawn()
        #     self.bullet2.reset(self.circle1)
        #     self.points += 1
        # if (self.bullet3.collide_widget(self.square3)):
        #     self.square3.respawn()
        #     self.bullet3.reset(self.circle1)
        #     self.points += 1
        # if (self.bullet4.collide_widget(self.square4)):
        #     self.square4.respawn()
        #     self.bullet4.reset(self.circle1)
        #     self.points += 1
