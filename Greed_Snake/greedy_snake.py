"""Introduction of 'Greedy Snake'

    * define a snake class
    * define a food class

"""

import copy
import random
import sys
# add file into path in order to import according to your path
sys.path.append('/home/python/Desktop/Greedy_snake')

class Snake(object):

    """snake can auto move, change direction, eat food and insert it into snake's body"""

    def __init__(self):
        self.position_list = [[100, 100]]
        self.direction = 'R'

    def positionList(self):
        return self.position_list

    def changeDirection(self, direction):
        self.direction = direction

    def moveDirection(self):
        body_length = len(self.position_list) - 1
        while body_length > 0:
            self.position_list[body_length] = copy.deepcopy(self.position_list[body_length - 1])
            body_length -= 1
        if self.direction == 'R':
            self.position_list[0][0] += 3
        elif self.direction == 'L':
            self.position_list[0][0] -= 3
        elif self.direction == 'U':
            self.position_list[0][1] -= 3
        elif self.direction == 'D':
            self.position_list[0][1] += 3

    def eatFood(self, foodPoint):
        self.position_list.insert(0, foodPoint)

class Food(object):

    """ random produce food position, food random update when snake eat food"""

    def __init__(self):
        x = random.randint(1, 45) * 10
        y = random.randint(1, 45) * 10
        self.food_position = [x, y]

    def foodList(self):
        return self.food_position

    def updateFood(self):
        self.food_position[0] = random.randint(0, 40) * 10
        self.food_position[1] = random.randint(0, 40) * 10



