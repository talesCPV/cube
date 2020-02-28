import sys, math, pygame
from operator import itemgetter

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

angle = [0,0,0]

center = [300,300]

pointlist = [(10, 10), (10, 20),
             (10, 20), (20, 20),
             (20, 20), (20, 30),
             (20, 30), (10, 10)]

def setPoint():
    for i in range(8):
        print(i)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            self.clock.tick(60)
            self.screen.fill((0, 0, 0)) #background

    pygame.draw.line(screen, (255, 255, 255), center, pointlist[0] )
#    pygame.draw.polygon(screen, (255,200,150), pointlist)


    pygame.display.flip()
