"""  welcome to my pygame AIRCRAFT!

     * Next Step:
     *   1.main target is to display the game screen and background.
     *   2.key_pressed can make heroplane smoothly but shoot the bullets seem not good.
     *   3.enemyplane can design a method to shoot bullets and match the pace.
     *   4.import pygame.sprite to finish when enemy down could show animation.
     *   5.import music
     *   6.import more function

"""
import pygame
from pygame.locals import *
import time
import random

__all__ = ['AIRCRAFT']
__version__ = '3.0'

def main():

    """ setting game main screen and background, put all object in endless loop which make it alive!"""
    # set resolution ratio
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 852
    # game initiation
    pygame.init()
    # control the frame
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    background = pygame.image.load('./plane/background.png').convert()
    pygame.display.set_caption('AIRCRAFT')
    gameover = pygame.image.load('./plane/gameover.png')
    hero = Hero(screen)
    # set a array to store enemies
    enemies = []
    # set a number to refresh rate
    enemy_frequency = 0
    # record score
    score = 0

    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        hero.display()
        # set a loop to create more enemy
        if enemy_frequency % 100 == 0:
            enemy = Enemy(screen)
            enemies.append(enemy)
        enemy_frequency += 1
        if enemy_frequency >= 200:
            enemy_frequency = 0
        # make enemies move
        # delete enemy when enemy across the height
        for enemy in enemies:
            enemy.move()
            enemy.display()
            if enemy.judge():
                enemies.remove(enemy)
        # judge event when enemyRect meet bulletRect, use pop() to delete
        ememyIndex = 0 # set a flag
        for i in enemies:
            enemyRect = pygame.Rect(i.image.get_rect())
            enemyRect.left = i.x
            enemyRect.top = i.y
            bulletIndex = 0
            for j in hero.bullet_list:
                bulletRect = pygame.Rect(j.image.get_rect())
                bulletRect.left = j.x
                bulletRect.top = j.y
                if enemyRect.colliderect(bulletRect):
                    # according to enemy's width to judge type
                    # set a score to make it fun!
                    if enemyRect.width < 50:
                        score += 1000
                    elif enemyRect.width < 80:
                        score += 5000
                    elif enemyRect.width < 200:
                        score += 10000
                    # delete enemy, bullet
                    enemies.pop(ememyIndex)
                    hero.bullet_list.pop(bulletIndex)
                bulletIndex += 1
            ememyIndex += 1
        # game over when hero collide the enemies
        heroRect = pygame.Rect(hero.image.get_rect())
        heroRect.left = hero.x
        heroRect.top = hero.y
        for i in enemies:
            enemyRect = pygame.Rect(i.image.get_rect())
            enemyRect.left = i.x
            enemyRect.top = i.y
            if heroRect.colliderect(enemyRect):
                time.sleep(0.5)
                screen.blit(gameover, (0, 0))
                text_rect.centerx = screen.get_rect().centerx
                text_rect.centery = screen.get_rect().centery
                screen.blit(score_text, text_rect)
                pygame.display.update()
                # game over and exit
                time.sleep(5)
                exit()
        # set a score text to record your achievement!
        score_font = pygame.font.Font(None, 40)
        score_text = score_font.render('%s' % str(score), True, (128, 128, 128))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)
        # import keyboard and refresh the screen per frame
        key_control(hero)
        pygame.display.update()
        time.sleep(0.01)

class Hero(pygame.sprite.Sprite):

    """ define a plane that includes: default position, move function, shoot bullet"""

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = 230
        self.y = 700
        self.screen = screen
        self.image_path = './plane/hero.gif'
        self.image = pygame.image.load(self.image_path).convert()
        self.bullet_list = []
        self.is_hit = False
        self.rect = self.image.get_rect()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_delete_list = []
        # bullet out rage can delete
        for tmp in self.bullet_list:
            if tmp.judge():
                need_delete_list.append(tmp)
        for tmp in need_delete_list:
            self.bullet_list.remove(tmp)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        if self.x > 0:
            self.x -= 10

    def move_right(self):
        if self.x < 360:
            self.x += 10

    def move_up(self):
        if self.y > 100:
            self.y -= 10

    def move_down(self):
        if self.y < 700:
            self.y += 10

    def shoot_bullet(self):
        new_bullet = Bullet(self.x, self.y, self.screen)
        self.bullet_list.append(new_bullet)

class Bullet(pygame.sprite.Sprite):

    """ bullet need match the plane's pace, and judge the shoot range """

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image_path = './plane/bullet-1.gif'
        self.image = pygame.image.load(self.image_path)

    def move(self):
        self.y -= 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class Enemy(pygame.sprite.Sprite):

    """ enemy can move in loop, random shoot bullet """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        image_num = random.randint(0, 2)
        # create different enemies
        self.image_path = './plane/enemy' + str(image_num) + '.png'
        self.image = pygame.image.load(self.image_path)
        self.x = random.randint(20, 350)
        self.y = 0
        self.screen = screen
        self.direction = 'right'
        self.bullet_list = [

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

    def move(self):
        self.y += 1
            
    def shoot_bullet(self):
        # control enemy bullet
        num = random.randint(1, 50)
        if num == 1:
            new_bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullet_list.append(new_bullet)

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


class EnemyBullet(pygame.sprite.Sprite):

    """ enemy bullet need match the pace of enemy plane, also jude the shoot range"""

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x+30
        self.y = y+30
        self.screen = screen
        self.image_path = './plane/bullet1.png'
        self.image = pygame.image.load(self.image_path).convert()

    def move(self):
        self.y += 4

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(hero):

    """ setting key for player to control: movement, shoot, quit """

    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero.shoot_bullet()
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero.move_up()
            elif event.key == K_d or event.key == K_DOWN:
                print('down')
                hero.move_down()


if __name__ == '__main__':
    main()
