
import sys, math, pygame


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

vai = 0
#        X  Y  Z
angle = [90,40,10]
pontos3D = [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]
raio = 100
pivot = [300,300]


def plot3DPoint(ang,point):
    senX = math.sin(ang[0] * math.pi / 180 )
    cosX = math.cos(ang[0] * math.pi / 180 )
    senY = math.sin(ang[1] * math.pi / 180 )
    cosY = math.cos(ang[1] * math.pi / 180 )
    senZ = math.sin(ang[2] * math.pi / 180 )
    cosZ = math.cos(ang[2] * math.pi / 180 )

    X = (point[2] * senY + point[0] * cosY) * cosZ - point[1] * senZ
    Y = point[0] * senZ + (point[1] * cosX - point[2] * senX) * cosZ
    Z = (point[1] * senX + point[2] * cosX) * cosY - point[0] * senY

    return (X,Y,Z)


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(40)
    screen.fill((0, 0, 0)) #background

    for i in pontos3D:
        print(plot3DPoint(angle,i))

#center
    pygame.draw.line(screen, (255, 0, 0), pivot, pivot)

    pygame.display.flip()

