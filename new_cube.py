import sys, math, pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cubo 3D")

clock = pygame.time.Clock()

pivot = [300,300]

faces = [(0,1,3,2,0,4,5,7,6,4),(2,6),(1,5),(3,7)]
angle = [90, 0, 0]

def plot3DPoint(point):
    senX = math.sin(angle[0] * math.pi / 180 )
    cosX = math.cos(angle[0] * math.pi / 180 )
    senY = math.sin(angle[1] * math.pi / 180 )
    cosY = math.cos(angle[1] * math.pi / 180 )
    senZ = math.sin(angle[2] * math.pi / 180 )
    cosZ = math.cos(angle[2] * math.pi / 180 )

    X = (point[2] * senY + point[0] * cosY) * cosZ - point[1] * senZ
    Y = point[0] * senZ + (point[1] * cosX - point[2] * senX) * cosZ
    Z = (point[1] * senX + point[2] * cosX) * cosY - point[0] * senY

    factor = 400 / (4 + Z)
    x = X * factor + pivot[0]
    y = -Y * factor + pivot[1]
    return (x, y)


class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle[0] * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle[1] * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle[2] * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

'''
vertices = [
    Point3D(1, 1, 1),
    Point3D(1, 1, -1),
    Point3D(1, -1, 1),
    Point3D(1, -1, -1),
    Point3D(-1, 1, 1),
    Point3D(-1, 1, -1),
    Point3D(-1, -1, 1),
    Point3D(-1, -1, -1)
]
'''

pontos = ((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    screen.fill((0, 0, 0)) #background

    # It will hold transformed vertices.
#    t = []

#    for v in vertices:
#        r = v.rotateX(angle).rotateY(angle).rotateZ(angle)
#        p = r.project(screen.get_width(), screen.get_height(), 400, 4)
#        t.append(p)

    vertices = []
    for i in pontos:
        vertices.append(plot3DPoint(i))

    for f in faces:
        for p1 in range(len(f)-1):
            p2 = p1 + 1
            print(vertices)
            pygame.draw.line(screen, (255, 0, 0), (vertices[f[p1]][0], vertices[f[p1]][1]), (vertices[f[p2]][0], vertices[f[p2]][1]))
            print(p1,p2)


#    angle[0] += 1
#    angle[1] += 1
    angle[2] += 1

    pygame.display.flip()
