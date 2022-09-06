import pygame
import time
from random import *

pygame.init()

class SnakeGame:
  def __init__(self):
    self.ezmode = False
    self.game_over = False
    self.dis_width = 300
    self.dis_height = 300
    self.font = pygame.font.SysFont(None, 25)
    self.game = pygame.display.set_mode((self.dis_width, self.dis_height))
    self.clock = pygame.time.Clock()
    self.score = 0
    self.color_black = (0, 0, 0)
    self.color_blue = (0, 0, 255)
    self.color_green = (0, 255, 0)
    self.color_white = (255, 255, 255)
    self.snake_xy = [[100, 150]]
    self.snake_movement_x = 0
    self.snake_movement_y = 0
    self.food_x = 200
    self.food_y = 150
    self.array_stuff = []

  def message(self, msg, color, x, y):
    msg = self.font.render(msg, True, color)
    self.game.blit(msg, [x, y])

  def movement(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        if not self.snake_movement_y == 10:
          self.snake_movement_y = -10
          self.snake_movement_x = 0
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          if not self.snake_movement_y == -10:
            self.snake_movement_y = 10
            self.snake_movement_x = 0
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          if not self.snake_movement_x == 10:
            self.snake_movement_x = -10
            self.snake_movement_y = 0
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          if not self.snake_movement_x == -10:
            self.snake_movement_x = 10
            self.snake_movement_y = 0

  def check_bounds(self):
    for x in self.snake_xy:
      if x[0] > 295:
        if self.ezmode:
          x[0] = 0
          self.snake_movement_x = 10
          self.snake_movement_y = 0
        else:
          self.game_over = True
      if x[0] < 0:
        if self.ezmode:
          x[0] = 290
          self.snake_movement_x = -10
          self.snake_movement_y = 0
        else:
          self.game_over = True
      if x[1] > 295:
        if self.ezmode:
          x[1] = 0
          self.snake_movement_x = 0
          self.snake_movement_y = 10
        else:
          self.game_over = True
      if x[1] < 0:
        self.score += 1
        if self.ezmode:
          x[1] = 290
          self.snake_movement_x = 0
          self.snake_movement_y = -10
        else:
          self.game_over = True

  def check_body(self):
    for x in range(0, len(self.snake_xy) - 1):
      print(self.snake_xy[x])
      print(self.snake_xy[len(self.snake_xy) - 2])

  def spawn_food(self):
    if self.snake_xy[len(self.snake_xy) - 1][0] == self.food_x and self.snake_xy[len(self.snake_xy) - 1][1] == self.food_y:
      self.score += 1
      self.food_x = 10 * randint(1, 29)
      self.food_y = 10 * randint(1, 29)
      

  def add_body(self):
    pass

  def start_game(self):
    pygame.display.update()
    pygame.display.set_caption('Simple Snake')

    while(not self.game_over):
      self.game.fill(self.color_black)
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          self.game_over=True
        self.movement(event)
      
      self.snake_xy.insert(len(self.snake_xy) + 1, [self.snake_xy[len(self.snake_xy) - 1][0] + self.snake_movement_x, self.snake_xy[len(self.snake_xy) - 1][1] + self.snake_movement_y])
      if len(self.snake_xy) - 1 > self.score:
        self.snake_xy.pop(0)

      self.check_bounds()
      self.spawn_food()
      self.check_body()

      for x in self.snake_xy:
        pygame.draw.rect(self.game, self.color_white, [x[0] + 1, x[1] + 1, 8, 8])
      pygame.draw.rect(self.game, self.color_green, [self.food_x, self.food_y, 10, 10])
      self.message("Score: " + str(self.score), self.color_blue, 10, 10)
      pygame.display.update()
      time.sleep(.1)
    
    if self.game_over:
      self.game.fill(self.color_black)
      self.message("Game Over", self.color_blue, 100, 100)
      self.message("Score: " + str(self.score), self.color_blue, 100, 120)
      pygame.display.update()
      time.sleep(2)

p1 = SnakeGame()
p1.start_game()
print(p1.score)