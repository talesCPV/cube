
import sys, math, pygame


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

angle = [90,90,0]
raio = 100
pivot = [300,300]
pointlist = [(0, 10), (10, 20),
             (10, 20), (20, 20),
             (20, 20), (20, 30),
             (20, 30), (10, 10)]

def setPoint():
    saida_x = raio * math.sin(math.radians(angle[0]))
    saida_y = raio * math.sin(math.radians(angle[1]))
    saida_z = raio * math.sin(math.radians(angle[2]))

    pointlist[0] = (pivot[0] - saida_x, pivot[1] - saida_y)
    pointlist[1] = (pivot[0] - saida_x, pivot[1] + saida_y)
    pointlist[2] = (pivot[0] + saida_x, pivot[1] - saida_y)
    pointlist[3] = (pivot[0] + saida_x, pivot[1] + saida_y)

    for a in range(8):
        print(pointlist[a])

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#            self.clock.tick(60)
    screen.fill((0, 0, 0)) #background

    pygame.draw.line(screen, (255, 255, 255), pointlist[0], pointlist[1])
    pygame.draw.line(screen, (255, 255, 255), pointlist[1], pointlist[3])
    pygame.draw.line(screen, (255, 255, 255), pointlist[2], pointlist[3])
    pygame.draw.line(screen, (255, 255, 255), pointlist[2], pointlist[0])
#    pygame.draw.polygon(screen, (255,200,150), pointlist)


    pygame.display.flip()

#    print(pointlist[0])
    setPoint()