import pygame

pygame.init()

#set up the screen
screen = pygame.display.set_mode((500,500))

#keep running until user closes window

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#otherwise fill the screen with a colour

    screen.fill((255,255,255))

#draw a blue circle
    pygame.draw.circle(screen, (0,0,255), (250,250), 75) #surface, colour, where on the screen, radius
    pygame.display.flip()

pygame.quit()

