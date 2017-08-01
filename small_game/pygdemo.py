"""Steps for building the dome of game

     * 1.main target is to display the game screen and background.
     * 2.test keyboard event and setting key for player.
     * 3.create a plane and set keyboard to control it.
     * 4.positioning plane and move it
     * 5.create and display bullet
     * 6.create and display enemy
     * 7.make enemy auto move
     * 8.enemy can shoot bullet

"""
import pygame
from pygame.locals import *
import time
import random

__all__ = ['pygdome']
__version__ = '1.0'


class HeroPlane(object):

    """ define a plane that includes: default position, move function, shoot bullet"""

    def __init__(self, screen):
        self.x = 230
        self.y = 700
        self.screen = screen
        self.image_name = './player.png'
        self.image = pygame.image.load(self.image_name).convert()
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_delete_list = []
        for tmp in self.bullet_list:
            if tmp.judge():
                need_delete_list.append(tmp)
        for tmp in need_delete_list:
            self.bullet_list.remove(tmp)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shoot_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)

class Bullet(object):

    """ bullet need match the plane's pace, and judge the shoot range """

    def __init__(self, x, y, screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load('./bullet.png').convert()

    def move(self):
        self.y -= 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyPlane(object):

    """ enemy can move in loop, random shoot bullet """

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image_name = './enemy.png'
        self.image = pygame.image.load(self.image_name).convert()
        self.direction = 'right'
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x,self.y))
        need_delete_list = []
        for tmp in self.bullet_list:
            if tmp.judge():
                need_delete_list.append(tmp)
        for tmp in need_delete_list:
            self.bullet_list.remove(tmp)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):
        if self.direction == 'right':
            self.x += 4
        elif self.direction == 'left':
            self.x -= 4
        if self.x > 480-50:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def shoot_bullet(self):
        num = random.randint(1, 100)
        if num == 88:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)

class EnemyBullet(object):

    """ enemy bullet need match the pace of enemy plane, also jude the shoot range"""

    def __init__(self, x, y, screen):
        self.x = x+30
        self.y = y+30
        self.screen = screen
        self.image_name = './bullet1.png'
        self.image = pygame.image.load(self.image_name).convert()

    def move(self):
        self.y += 4

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(heroPlane):

    """ setting key for player to control: movement, shoot, quit """

    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                heroPlane.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                heroPlane.move_right()
            elif event.key == K_SPACE:
                print('space')
                heroPlane.shoot_bullet()

def main():

    """ setting game main screen and background, put all object in endless loop which make it alive!"""

    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load('./plane.png').convert()
    heroPlane = HeroPlane(screen)
    enemyPlane = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        heroPlane.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.shoot_bullet()
        key_control(heroPlane)
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()