import pygame, sys

def Controle(screen, sqr):
    pygame.draw.circle(screen, 'red', (5,7), 5)
    screen.blit(sqr,(0,0))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP: #                 Ниже описывается нажатие от отжатие на клавишу
            if event.key == pygame.K_w: #W вверх
                pass
            elif event.key == pygame.K_a: #A вправо
                pass
            elif event.key == pygame.K_s: #S вниз
                pass
            elif event.key == pygame.K_d: #D влево
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #W вверх
                pass
            elif event.key == pygame.K_a: #A вправо
                pass
            elif event.key == pygame.K_s: #S вниз
                pass
            elif event.key == pygame.K_d: #D влево
                pass
