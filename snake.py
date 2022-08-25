import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Simple Snake')

blue=(0,0,255)
red=(255,0,0)
x=100
y=100

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            y-=1
            pygame.display.update()

    pygame.draw.rect(dis,blue,[x,y,10,10])
    pygame.display.update()
 
pygame.quit()
quit()