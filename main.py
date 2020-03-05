
import sys, math, pygame


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

vai = 0
#        X  Y  Z
angle = [0,0,0]
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

    pontos.append(project((X,Y,Z),400,4))


    return (project((X,Y,Z),400,4))


def project(points, fov, viewer_distance):
    """ Transforms this 3D point to 2D using a perspective projection. """
    factor = fov / (viewer_distance + points[2])
    x = points[0] * factor + pivot[0]
    y = -points[1] * factor + pivot[1]
    return (x, y)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(40)
    screen.fill((0, 0, 0)) #background

    pontos = []

    for i in pontos3D:
        plot3DPoint(angle,i)

    print(pontos)

    pygame.draw.line(screen, (255, 0, 0), pontos[0],pontos[1])
    pygame.draw.line(screen, (255, 0, 0), pontos[1],pontos[3])
    pygame.draw.line(screen, (255, 0, 0), pontos[3],pontos[2])
    pygame.draw.line(screen, (255, 0, 0), pontos[2],pontos[0])

    pygame.draw.line(screen, (255, 0, 0), pontos[4],pontos[5])
    pygame.draw.line(screen, (255, 0, 0), pontos[5],pontos[7])
    pygame.draw.line(screen, (255, 0, 0), pontos[7],pontos[6])
    pygame.draw.line(screen, (255, 0, 0), pontos[6],pontos[4])

    pygame.draw.line(screen, (255, 0, 0), pontos[0],pontos[4])
    pygame.draw.line(screen, (255, 0, 0), pontos[1],pontos[5])
    pygame.draw.line(screen, (255, 0, 0), pontos[2],pontos[6])
    pygame.draw.line(screen, (255, 0, 0), pontos[3],pontos[7])

#center
    pygame.draw.line(screen, (255, 0, 0), pivot, pivot)

    pygame.display.flip()

    angle[0] += 1
    angle[1] += 1
#    angle[2] += 1