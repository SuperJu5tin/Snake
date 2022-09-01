import pygame
pygame.init()
import time

class SnakeGame:
  def __init__(self):
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
    self.snake_x = 100
    self.snake_y = 150
    self.snake_movement_x = 0
    self.snake_movement_y = 0
    self.food_x = 200
    self.food_y = 150

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
    if self.snake_x > 295:
      self.snake_x = 0
      self.snake_movement_x = 10
      self.snake_movement_y = 0
    if self.snake_x < 0:
      self.snake_x = 290
      self.snake_movement_x = -10
      self.snake_movement_y = 0
    if self.snake_y > 295:
      self.snake_y = 0
      self.snake_movement_x = 0
      self.snake_movement_y = 10
    if self.snake_y < 0:
      self.score += 1
      self.snake_y = 290
      self.snake_movement_x = 0
      self.snake_movement_y = -10

  def spawn_food(self):
    pass

  def start_game(self):
    pygame.display.update()
    pygame.display.set_caption('Simple Snake')

    while(not self.game_over):
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          self.game_over=True
        self.movement(event)
      
      self.snake_y += self.snake_movement_y
      self.snake_x += self.snake_movement_x

      self.check_bounds()

      self.game.fill(self.color_black)
      pygame.draw.rect(self.game, self.color_blue, [self.snake_x, self.snake_y, 8, 8])
      pygame.draw.rect(self.game, self.color_green, [self.food_x, self.food_y, 10, 10])
      self.message("Score: " + str(self.score), self.color_blue, 10, 10)
      pygame.display.update()
      time.sleep(.075)


p1 = SnakeGame()
p1.start_game()
print(p1.score)