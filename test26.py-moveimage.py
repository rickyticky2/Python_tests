import pygame

MAX_X = 800
MAX_Y = 600
game_over = False

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My Ferst PyGame Game! :)")

myimage = pygame.image.load("pic.jpg").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 500
y = 100

# --------------MAIN GAME LOOP
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
               game_over = True
           if event.key == pygame.K_LEFT:
              x -= 20
           if event.key == pygame.K_RIGHT:
              x += 20
           if event.key == pygame.K_UP:
              y -= 20
           if event.key == pygame.K_DOWN:
              y += 20

    screen.blit(myimage, (x, y))
    pygame.display.flip()
