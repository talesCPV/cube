
import sys, math, pygame


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

vai = 0
#         X  Y  Z
angle = [0,45,0]
raio = 100
pivot = [300,300]


def getAxis(x,y,z):
    points = []







def setPoint():

#    GIRO
#    angle[0] += 1 # X
#    angle[1] += 1 # Y
#    angle[2] += 1 # Z

    sen_x = math.sin(math.radians(angle[0]))
    cos_x = math.cos(math.radians(angle[0]))

    sen_y = math.sin(math.radians(angle[1]))
    cos_y = math.cos(math.radians(angle[1]))

    sen_z = math.sin(math.radians(angle[2]))
    cos_z = math.cos(math.radians(angle[2]))



#                 X             Y             Z
    axis = [((0,0),(0,0)),((0,0),(0,0)),((0,0),(0,0))]

    # DRAW
    pygame.draw.line(screen, (255, 255, 255), axis[0]
    pygame.draw.line(screen, (255, 255, 255), axis[1]
    pygame.draw.line(screen, (255, 255, 255), axis[2]

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(40)
    screen.fill((0, 0, 0)) #background


    setPoint()
#center
    pygame.draw.line(screen, (255, 0, 0), pivot, pivot)

    pygame.display.flip()

