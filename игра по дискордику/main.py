import pygame,control

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Castle Defence')
    bg_color = (0,0,0)
    sqr = pygame.Surface((50,70))
    sqr.fill('blue')

    while True:
            control.Controle(screen,sqr)
            screen.fill(bg_color)

if __name__ == '__main__':
    run()