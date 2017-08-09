"""Game panel of 'Greedy Snake'

      * set FPS to make it smooth
      * set two rect element to represent snake and food
      * ste keyboard
      * judge collide and snake hit wall or itself
      * set a score to record
      * set a game over control and show some text

"""

from greedy_snake import *
from pygame.locals import *
import pygame


def snakeMain():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Greedy Snake')
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    direction_flag = 'R'
    score = 0
    while True:
        # set background
        clock.tick(60)
        screen.fill((255, 255, 255))
        # set score panel
        font = pygame.font.Font(None, 40)
        text_score = font.render('score: %s' % str(score), True, (255, 0, 0))
        text_rect = text_score.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(text_score, text_rect)
        # set snake auto move
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    direction_flag = 'R'
                elif event.key == K_LEFT:
                    direction_flag = 'L'
                elif event.key == K_UP:
                    direction_flag = 'U'
                elif event.key == K_DOWN:
                    direction_flag = 'D'
        # Draw food
        food_position = copy.deepcopy(food.foodList())
        foodRect = pygame.Rect(food.food_position[0], food.food_position[1], 20, 20)
        pygame.draw.rect(screen, (255, 0, 255), foodRect)
        # Draw Snake
        snake_position = snake.positionList()
        for pos in snake_position:
            temp_rect = pygame.Rect(pos[0], pos[1], 20, 20)
            pygame.draw.rect(screen, (255, 0, 0), temp_rect)
        # move the snake
        snake.changeDirection(direction_flag)
        snake.moveDirection()
        # judge collide rect
        snakeRect = pygame.Rect(pos[0], pos[1], 8, 8)
        if snakeRect.colliderect(foodRect):
            snake.eatFood(food_position)
            score += 1
            food.updateFood()
        # judge snake hit the wall or itself
        gameover_flag = False
        snake_position = snake.positionList()
        snake_head = snake_position[0]
        if direction_flag == 'R':
            if snake_head[0] > 546:
                gameover_flag = True
        elif direction_flag == 'L':
            if snake_head[0] < 0:
                gameover_flag = True
        elif direction_flag == 'U':
            if snake_head[1] < 0:
                gameover_flag = True
        elif direction_flag == 'D':
            if snake_head[1] > 546:
                gameover_flag = True
        for pos in range(1, len(snake_position) - 1):
            if snake_head == snake_position[pos]:
                gameover_flag = True
        # refresh per frame
        pygame.display.update()
        # game record
        if gameover_flag:
            pygame.font.init()
            screen.fill((100, 0, 0))
            font = pygame.font.SysFont('arial', 32)
            text = font.render('GAME OVER', True, (255, 255, 0))
            text_score = font.render('score: %s' % str(score), True, (255, 255, 0))
            screen.blit(text, (160, 200))
            screen.blit(text_score, (180, 230))
            pygame.display.update()
            while True:
                again_event = pygame.event.poll()
                if again_event.type == QUIT:
                    exit()

if __name__ == '__main__':
    snakeMain()


