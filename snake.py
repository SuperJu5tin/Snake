import pygame
pygame.init()

dis_width = 300
dis_height = 300

game = pygame.display.set_mode((dis_width, dis_height))
font = pygame.font.SysFont(None, 25)
pygame.display.update()
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
blue=(0,0,255)

x=100
y=150

score = 0

constantChangesX=0
constantChangesY=0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
 
def message(msg, color, x, y):
  msg = font_style.render(msg, True, color)
  game.blit(msg, [x, y])

game_over=False
while not game_over:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      game_over=True

# Movement

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        if not constantChangesY == 10:
          constantChangesY = -10
          constantChangesX = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        if not constantChangesY == -10:
          constantChangesY = 10
          constantChangesX = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if not constantChangesX == 10:
          constantChangesX = -10
          constantChangesY = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        if not constantChangesX == -10:
          constantChangesX = 10
          constantChangesY = 0

  y+=constantChangesY
  x+=constantChangesX

  if x > 295:
    x = 0
    constantChangesX = 10
    constantChangesY = 0

  if x < 0:
    x = 290
    constantChangesX = -10
    constantChangesY = 0

  if y > 295:
    y = 0
    constantChangesX = 0
    constantChangesY = 10

  if y < 0:
    y = 290
    constantChangesX = 0
    constantChangesY = -10

  game.fill(black)
  pygame.draw.rect(game,blue,[x, y, 7, 7])
  message("Score: " + str(score), blue, 10, 10)
  pygame.display.update()
  clock.tick(20)

# Food
  # if x = foodx
 
pygame.quit()
quit()
