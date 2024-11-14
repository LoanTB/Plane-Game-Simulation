import pygame,random,math

pygame.init()
timer = pygame.time.Clock()

resolution = [1280,720]
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Plane Game")

class Player():
    def __init__(self):
        self.position = [resolution[0]/2,resolution[1]/2]
        self.orientation = 90
        self.forces = [0,0]
        taille = 0.1
        self.length = 1169*taille
        self.images = []
        self.died = False
        for i in ["right","left"]:
            self.images.append(pygame.image.load("plane/"+i+".png"))
            ImageRect = self.images[-1].get_rect()
            ImageRect[2] *= taille
            ImageRect[3] *= taille
            self.images[-1] = pygame.transform.scale(self.images[-1],(ImageRect[2],ImageRect[3]))
        self.frame = 0
        self.speed = abs(self.forces[0])+abs(self.forces[1])
        self.aspeed = self.speed
        self.airproof = 0.9
        self.airfriction = 0.999
    def refresh(self):
        img_copy = pygame.transform.rotate(self.images[self.frame],self.orientation-90)
        screen.blit(img_copy,(self.position[0]-int(img_copy.get_width()/2),self.position[1]-int(img_copy.get_height()/2)))
        #screen.blit(rotate(,rotation),[self.position[0],self.position[1],0,0])
    def update(self):
        if map.ground-self.position[1] < 25:
            self.forces[0] *= 0.99
            self.forces[1] *= 0.99
        if map.ground-self.position[1] < 35:
            self.forces[1] -= ((35-(map.ground-self.position[1]))/35)*0.5
        if map.ground-self.position[1]-(self.length*0.8)*abs(math.cos(self.orientation/360*2*math.pi)) < 0:
            self.forces[0] *= 0.99
            rnd = random.randint(200,225)
            map.objects["circle"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*(70*math.cos(self.orientation/360*2*math.pi)+random.randint(-10,10)),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*(70*math.cos(self.orientation/360*2*math.pi)+random.randint(-10,10))+math.sin(self.orientation/360*2*math.pi)*10],[math.sin(self.orientation/360*2*math.pi)*(player.speed/4),math.cos(self.orientation/360*2*math.pi)*(player.speed/4)],[rnd,rnd,0],random.randint(1,3),random.randint(30,60)])
        if map.ground-self.position[1]-self.length*abs(math.cos(self.orientation/360*2*math.pi)) < -self.length/4:
            self.died = True
            for i in range(100):
                rnd = random.randint(0,100)
                map.objects["circle"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*random.randint(-80,80),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*random.randint(-80,80)],[math.sin(random.random()*2*math.pi)*20,math.cos(random.random()*2*math.pi)*20],[rnd,rnd,0],random.randint(2,10),-1])
        """elif map.ground-self.position[1] < 0:
            for i in range(5):
                rnd = random.randint(200,250)
                map.objects["circle"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*random.randint(-80,80),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*random.randint(-80,80)],[math.sin(random.random()*2*math.pi)*20,math.cos(random.random()*2*math.pi)*20],[rnd,rnd,0],random.randint(2,7),random.randint(30,60)])"""
        for i in range(int(self.speed-(map.ground-self.position[1]))):
            rnd = random.randint(200,250)
            map.objects["circle"].append([[self.position[0]-map.position[0]+random.randint(-125,125),map.ground-2-map.position[1]],[math.sin(random.random()*2*math.pi)*1,math.cos(random.random()*2*math.pi)*1],[rnd,rnd,rnd],random.randint(1,3+int((self.speed-(map.ground-self.position[1]))/4)),random.randint(30,60)])
        """if self.orientation > 315 or self.orientation < 45:
            self.frame = 0
        elif self.orientation > 45 and self.orientation < 135:
            self.frame = 0
        elif self.orientation > 135 and self.orientation < 225:
            self.frame = 0
        elif self.orientation > 225 and self.orientation < 315:
            self.frame = 1"""
        if self.orientation > 0 and self.orientation < 180:
            self.frame = 0
        elif self.orientation > 180 and self.orientation < 360:
            self.frame = 1
        self.speed = abs(self.forces[0])+abs(self.forces[1])
        if self.speed*60*(20/player.length/1000)*(60**2) > 1024 and self.speed*60*(20/player.length/1000)*(60**2) < 1224:
            grand = int((self.speed*60*(20/player.length/1000)*(60**2))-1024)
            for i in range(int(grand*0.25)):
                rnd = random.randint(200,250)
                map.objects["circle"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*random.randint(-10,80),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*random.randint(-10,80)],[math.sin((self.orientation+random.randint(int(-(grand*0.9)),int(grand*0.9)))/360*2*math.pi)*(player.speed/4),math.cos((self.orientation+random.randint(int(-(grand*0.9)),int(grand*0.9)))/360*2*math.pi)*(player.speed/4)],[rnd,rnd,rnd],random.randint(1,6),random.randint(30,60)])
        elif self.aspeed*60*(20/player.length/1000)*(60**2) < 1224 and self.speed*60*(20/player.length/1000)*(60**2) >= 1224:
            for i in range(int(360/2)):
                rnd = random.randint(200,250)
                map.objects["circle"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*random.randint(70,80),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*random.randint(70,80)],[math.sin(((i*2)+random.randint(-20,20))/360*2*math.pi)*(player.speed/2),math.cos(((i*2)+random.randint(-20,20))/360*2*math.pi)*(player.speed/2)],[rnd,rnd,rnd],random.randint(4,8),random.randint(60,120)])
        self.aspeed = self.speed
        map.position[0] -= self.forces[0]*1#((abs(self.position[0]-100-((resolution[0]-200)/2))/((resolution[0]-200)/2)))
        map.position[1] -= self.forces[1]*1#((abs(self.position[1]-100-((resolution[1]-200)/2))/((resolution[1]-200)/2)))
        self.position[0] += self.forces[0]*0#(1-(abs(self.position[0]-100-((resolution[0]-200)/2))/((resolution[0]-200)/2)))
        self.position[1] += self.forces[1]*0#(1-(abs(self.position[1]-100-((resolution[1]-200)/2))/((resolution[1]-200)/2)))
        #  127094.184hm/h**2 to pix/tic = (127094.184*(player.length/20/1000))/(60**3)
        self.forces[1] += 0.07
        self.forces[0] += 0.07*self.airproof*math.cos(self.orientation/360*2*math.pi)
        #self.orientation -= 0.5*math.cos(self.orientation/360*2*math.pi)
        self.forces[0] *= abs(math.sin(self.orientation/360*2*math.pi))*0.05+0.95
        self.forces[1] *= abs(math.cos(self.orientation/360*2*math.pi))*0.05+0.95
        self.forces[0] += self.airproof*math.sin(self.orientation/360*2*math.pi)*abs(self.forces[1]-(self.forces[1]*(abs(math.cos(self.orientation/360*2*math.pi))*0.05+0.95)))
        self.forces[1] += self.airproof*math.cos(self.orientation/360*2*math.pi)*abs(self.forces[0]-(self.forces[0]*(abs(math.sin(self.orientation/360*2*math.pi))*0.05+0.95)))
        #self.forces[0] += self.forces[1]-self.forces[1]*(-math.sin(self.orientation/360*2*math.pi)*0.1+0.9)
        #self.forces[1] += self.forces[0]-self.forces[0]*(-math.cos(self.orientation/360*2*math.pi)*0.1+0.9)

        self.forces[0] *= self.airfriction
        self.forces[1] *= self.airfriction
    def accelerate(self):
        self.forces[0] += (math.sin(self.orientation/360*2*math.pi)*0.25)*((2410-(self.speed*60*(20/player.length/1000)*(60**2)))/2410)
        self.forces[1] += (math.cos(self.orientation/360*2*math.pi)*0.25)*((2410-(self.speed*60*(20/player.length/1000)*(60**2)))/2410)
            #print(((math.sin(self.orientation/360*2*math.pi)*0.25)*((2410-(self.speed*60*(20/player.length/1000)*(60**2)))/2410))*60*(20/player.length/1000)*(60**2))

        """for i in range(int(abs(self.forces[0])+abs(self.forces[1]))):
            map.objects["circle"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(30-i,50+i),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(30-i,50+i)],[-math.sin((self.orientation+random.randint(-10,10))/360*2*math.pi)**10*10,-math.cos((self.orientation+random.randint(-10,10))/360*2*math.pi)**10*10],[random.randint(50,100),0,random.randint(200,255)],random.randint(1,2),random.randint(1,2)])
        if int(abs(self.forces[0])+abs(self.forces[1])) > 20:
            rnd = random.randint(200,255)
            for i in range(int((abs(self.forces[0])+abs(self.forces[1]))/10)):
                map.objects["circle"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(30-i*10,60+i*10),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(30-i*10,60+i*10)],[-math.sin((self.orientation+random.randint(-30,30))/360*2*math.pi)*5,-math.cos((self.orientation+random.randint(-30,30))/360*2*math.pi)*5],[rnd,rnd,rnd],random.randint(2,5),random.randint(30,300)])
        for i in range(1):
            map.objects["circle"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(30,60),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(30,60)],[-math.sin((self.orientation+random.randint(-20,20))/360*2*math.pi)*5,-math.cos((self.orientation+random.randint(-20,20))/360*2*math.pi)*5],[random.randint(200,255),random.randint(0,50),0],random.randint(1,3),random.randint(30,300)])
        for i in range(2):
            map.objects["circle"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(30,60),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(30,60)],[-math.sin((self.orientation+random.randint(-30,30))/360*2*math.pi)*5,-math.cos((self.orientation+random.randint(-30,30))/360*2*math.pi)*5],[random.randint(200,255),random.randint(150,200),0],random.randint(1,4),random.randint(30,300)])
        for i in range(2):
            rnd = random.randint(50,150)
            map.objects["circle"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(30,60),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(30,60)],[-math.sin((self.orientation+random.randint(-30,30))/360*2*math.pi)*5,-math.cos((self.orientation+random.randint(-30,30))/360*2*math.pi)*5],[rnd,rnd,rnd],random.randint(2,5),random.randint(30,300)])"""
    def decelerate(self):
        self.forces[0] *= 0.99
        self.forces[1] *= 0.99
    def turnleft(self):
        if map.ground-self.position[1]-self.length*abs(math.cos((self.orientation+(abs(self.forces[0])+abs(self.forces[1]))*0.15)/360*2*math.pi)) > -10:
            if (abs(self.forces[0])+abs(self.forces[1]))*0.15 < 2:
                self.orientation += (abs(self.forces[0])+abs(self.forces[1]))*0.15
            else:
                self.orientation += 2
            if self.orientation > 360:
                self.orientation = 360-self.orientation
    def turnright(self):
        if map.ground-self.position[1]-self.length*abs(math.cos((self.orientation-(abs(self.forces[0])+abs(self.forces[1]))*0.15)/360*2*math.pi)) > -10:
            if (abs(self.forces[0])+abs(self.forces[1]))*0.15 < 2:
                self.orientation -= (abs(self.forces[0])+abs(self.forces[1]))*0.15
            else:
                self.orientation -= 2
            if self.orientation < 0:
                self.orientation = 360+self.orientation
    def M61VulcanFire(self):
        for i in range(2):
            map.objects["bullets"].append([[self.position[0]-map.position[0]+math.sin(self.orientation/360*2*math.pi)*random.randint(45,50),self.position[1]-map.position[1]+math.cos(self.orientation/360*2*math.pi)*random.randint(45,50)],[self.forces[0]+math.sin((self.orientation+random.randint(-1,1))/360*2*math.pi)*50,self.forces[1]+math.cos((self.orientation+random.randint(-1,1))/360*2*math.pi)*50],[255,255,0],2,100])
        self.forces[0] -= math.sin((self.orientation+random.randint(-5,5))/360*2*math.pi)*0.05
        self.forces[1] -= math.cos((self.orientation+random.randint(-5,5))/360*2*math.pi)*0.05
    def Flares(self):
        for i in range(5):#"flares"
            map.objects["flares"].append([[self.position[0]-map.position[0]-math.sin(self.orientation/360*2*math.pi)*random.randint(40,50),self.position[1]-map.position[1]-math.cos(self.orientation/360*2*math.pi)*random.randint(40,50)],[random.randint(-5,5),random.randint(-5,5)],[255,200,0],random.randint(1,4),random.randint(30,300)])
class Map():
    def __init__(self):
        self.position = [400,-230]
        self.objects = {}
        self.ground = resolution[1]-100+self.position[1]
        self.objects["bullets"] = []
        self.objects["flares"] = []
        self.objects["circle"] = []
        self.objects["rect"] = []
        self.objects["rect"].append([[0,resolution[1]-100,(500*(player.length/20)),50],[0,0],[25,25,25],-1])
        for i in range(5):
            self.objects["rect"].append([[(2*i)*(50*(player.length/20)),resolution[1]-100,(50*(player.length/20)),25],[0,0],[255,255,255],-1])
        for i in range(1000):
            rnd = random.randint(150,255)
            self.objects["circle"].append([[random.randint(-resolution[0]*2,resolution[0]*4),random.randint(-resolution[1]*20,self.ground-100)],[0,0],[rnd,rnd,rnd],random.randint(5,20),-1])
    def refresh(self):
        self.ground = resolution[1]-100+self.position[1]
        pygame.draw.rect(screen,[0,200,0],[0,self.ground,resolution[0],resolution[1]])

        remove = []
        rep = 0
        for i in range(len(self.objects["rect"])):
            self.objects["rect"][i][0][0] += self.objects["rect"][i][1][0]
            self.objects["rect"][i][0][1] += self.objects["rect"][i][1][1]
            pygame.draw.rect(screen,self.objects["rect"][i][2],[self.objects["rect"][i][0][0]+self.position[0],self.objects["rect"][i][0][1]+self.position[1],self.objects["rect"][i][0][2],self.objects["rect"][i][0][3]])
            self.objects["rect"][i][3] -= 1
            if self.objects["rect"][i][3] == 0:
                remove.append(i-rep)
                rep += 1
        for i in remove:
            self.objects["rect"].remove(self.objects["rect"][i])

        remove = []
        rep = 0
        for i in range(len(self.objects["circle"])):
            self.objects["circle"][i][0][0] += self.objects["circle"][i][1][0]
            self.objects["circle"][i][0][1] += self.objects["circle"][i][1][1]
            pygame.draw.circle(screen,self.objects["circle"][i][2],[self.objects["circle"][i][0][0]+self.position[0],self.objects["circle"][i][0][1]+self.position[1]],self.objects["circle"][i][3])
            if self.objects["circle"][i][0][1]+self.position[1] > self.ground:
                self.objects["circle"][i][0][0] -= self.objects["circle"][i][1][0]
                self.objects["circle"][i][0][1] -= self.objects["circle"][i][1][1]
                self.objects["circle"][i][1][0] *= -0.5
                self.objects["circle"][i][1][0] *= -0.5
            self.objects["circle"][i][4] -= 1
            if self.objects["circle"][i][4] == 0:
                remove.append(i-rep)
                rep += 1
        for i in remove:
            self.objects["circle"].remove(self.objects["circle"][i])
        remove = []
        rep = 0
        for i in range(len(self.objects["bullets"])):
            self.objects["bullets"][i][1][0] *= 0.99
            self.objects["bullets"][i][1][1] *= 0.99
            self.objects["bullets"][i][0][0] += self.objects["bullets"][i][1][0]
            self.objects["bullets"][i][0][1] += self.objects["bullets"][i][1][1]
            pygame.draw.circle(screen,self.objects["bullets"][i][2],[self.objects["bullets"][i][0][0]+self.position[0],self.objects["bullets"][i][0][1]+self.position[1]],self.objects["bullets"][i][3])
            self.objects["bullets"][i][4] -= 1
            if self.objects["bullets"][i][4] == 0 or self.objects["bullets"][i][0][1]+self.position[1] > self.ground:
                remove.append(i-rep)
                rep += 1
        for i in remove:
            self.objects["bullets"].remove(self.objects["bullets"][i])
        remove = []
        rep = 0
        for i in range(len(self.objects["flares"])):
            self.objects["flares"][i][0][0] += self.objects["flares"][i][1][0]
            self.objects["flares"][i][0][1] += self.objects["flares"][i][1][1]
            pygame.draw.circle(screen,self.objects["flares"][i][2],[self.objects["flares"][i][0][0]+self.position[0],self.objects["flares"][i][0][1]+self.position[1]],self.objects["flares"][i][3])
            if self.objects["flares"][i][0][1]+self.position[1] > self.ground:
                self.objects["flares"][i][0][0] -= self.objects["flares"][i][1][0]
                self.objects["flares"][i][0][1] -= self.objects["flares"][i][1][1]
                self.objects["flares"][i][1][0] *= -0.5
                self.objects["flares"][i][1][0] *= -0.5
            self.objects["flares"][i][4] -= 1
            if self.objects["flares"][i][4] == 0:# or self.objects["flares"][i][0][1]+self.position[1] > self.ground:
                remove.append(i-rep)
                rep += 1
        for i in remove:
            self.objects["flares"].remove(self.objects["flares"][i])
class Game():
    def __init__(self):
        self.pressed = {}

speedometer = pygame.Surface((150,150))
pygame.draw.circle(speedometer,[10,10,10],[75,75],70)
pygame.draw.circle(speedometer,[100,100,100],[75,75],65)

#pygame.draw.line(speedometer,[150,150,150],[75,75],(i,1))

while True:
    player = Player()
    game = Game()
    map = Map()
    while not game.pressed.get(pygame.K_o):
        timer.tick(60)
        screen.fill([150,200,250])
        map.refresh()
        screen.blit(pygame.font.SysFont(None, 50).render("Speed :", 1, (25,25,25)), (10, 10))
        add = "".join(["0" for i in range(4-len(str(int(round(player.speed*60*(20/player.length/1000)*(60**2),0)))))])
        screen.blit(pygame.font.SysFont(None, 50).render(add+str(int(round(player.speed*60*(20/player.length/1000)*(60**2),0)))+"km/h", 1, (25,25,25)), (10, 50))
        screen.blit(pygame.font.SysFont(None, 50).render("Mach "+str(int((player.speed*60*(20/player.length/1000)*(60**2))/1224)), 1, (25,25,25)), (200, 50))
        add = "".join(["0" for i in range(2-len(str(int(round(((map.ground-player.position[1])*(20/player.length))/1000,2)))))])
        screen.blit(pygame.font.SysFont(None, 50).render(add+str(round(((map.ground-player.position[1])*(20/player.length))/1000,2))+"km", 1, (25,25,25)), (10, 100))
        screen.blit(pygame.font.SysFont(None, 50).render(str(round(((map.position[0])*(20/player.length))/1000,2))+"km", 1, (25,25,25)), (10, 150))

        #screen.blit(speedometer,[5,5,150,150])

        if not player.died:
            player.refresh()
            if game.pressed.get(pygame.K_UP) or game.pressed.get(pygame.K_z):
                player.accelerate()
            if game.pressed.get(pygame.K_DOWN) or game.pressed.get(pygame.K_s):
                player.decelerate()
            if game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q):
                player.turnleft()
            if game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d):
                player.turnright()
            if game.pressed.get(pygame.K_1) or game.pressed.get(pygame.K_f):
                player.M61VulcanFire()
            if game.pressed.get(pygame.K_0) or game.pressed.get(pygame.K_g):
                player.Flares()
            player.update()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
