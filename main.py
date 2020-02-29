
import sys, math, pygame


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Cubo")

clock = pygame.time.Clock()

vai = 0

angle = [0,0,0]
raio = 100
pivot = [300,300]
points_3D = [(0, 10), (10, 20),
             (10, 20), (20, 20),
             (20, 20), (20, 30),
             (20, 30), (10, 10)]

center_face = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

def setPoint():

    sen_x = math.sin(math.radians(angle[0]))
    sen_y = math.sin(math.radians(angle[1]))
    sen_z = math.sin(math.radians(angle[2]))
    cos_x = math.cos(math.radians(angle[0]))
    cos_y = math.cos(math.radians(angle[1]))
    cos_z = math.cos(math.radians(angle[2]))

    #Z1
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] - raio * sen_y * cos_x, pivot[1] - raio * sen_x * cos_y), pivot)
    #Z2
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] + raio * sen_y * cos_x, pivot[1] + raio * sen_x * cos_y), pivot)
    #Y1
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] - raio * sen_x * cos_z, pivot[1] - raio * sen_z * cos_x), pivot)
    #Y2
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] + raio * sen_x * cos_z, pivot[1] + raio * sen_z * cos_x), pivot)
    #X1
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] - raio * sen_z * cos_y, pivot[1] - raio * sen_y * cos_z), pivot)
    #X2
    pygame.draw.line(screen, (255, 255, 255), (pivot[0] + raio * sen_z * cos_y, pivot[1] + raio * sen_y * cos_z), pivot)

    print(angle)

#    points_3D[0] = (pivot[0] - (raio * cos_x), pivot[1] - (raio * sen_y))
#    points_3D[1] = (pivot[0] - (raio * cos_x), pivot[1] + (raio * sen_y))
#    points_3D[2] = (pivot[0] + (raio * cos_x), pivot[1] - (raio * sen_y))
#    points_3D[3] = (pivot[0] + (raio * cos_x), pivot[1] + (raio * sen_y))

#    points_3D[4] = (pivot[0] - (raio * cos_z), pivot[1] - (raio * sen_y))
#    points_3D[5] = (pivot[0] - saida_x_neg, pivot[1] + saida_y_neg)
#    points_3D[6] = (pivot[0] + saida_x_neg, pivot[1] - saida_y_neg)
#    points_3D[7] = (pivot[0] + saida_x_neg, pivot[1] + saida_y_neg)


#    print(points_3D)
#    print(sen_y,cos_y)

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


#    pygame.draw.line(screen, (255, 255, 255), points_3D[0], points_3D[1])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[1], points_3D[3])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[3], points_3D[2])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[2], points_3D[0])

#    pygame.draw.line(screen, (255, 0, 0), points_3D[4], points_3D[4])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[5], points_3D[7])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[6], points_3D[7])
#    pygame.draw.line(screen, (255, 255, 255), points_3D[6], points_3D[4])

#    pygame.draw.line(screen, (255, 255, 255), pointlist[0], pointlist[4])
#    pygame.draw.line(screen, (255, 255, 255), pointlist[1], pointlist[5])
#    pygame.draw.line(screen, (255, 255, 255), pointlist[2], pointlist[6])
#    pygame.draw.line(screen, (255, 255, 255), pointlist[3], pointlist[7])
#    pygame.draw.polygon(screen, (255,200,150), pointlist)


#    angle[0] += 1
#    angle[1] += 1
#    angle[2] += 1
    pygame.display.flip()

