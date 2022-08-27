import pygame
pygame.init()
dis=pygame.display.set_mode((800,300))
pygame.display.update()
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
blue=(0,0,255)

x=100
y=100

constantChangesX=0
constantChangesY=0

clock = pygame.time.Clock()

game_over=False
while not game_over:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      game_over=True

# Movement

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        constantChangesY = -5
        constantChangesX = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        constantChangesY = 5
        constantChangesX = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        constantChangesX = -5
        constantChangesY = 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        constantChangesX = 5
        constantChangesY = 0

  y+=constantChangesY
  x+=constantChangesX

  dis.fill(black)
  pygame.draw.rect(dis,blue,[x,y,10,10])
  pygame.display.update()
  clock.tick(10)

# Food
  # if x = foodx
 
pygame.quit()
quit()