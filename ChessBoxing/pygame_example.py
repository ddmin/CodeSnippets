import pygame
import os

pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Chess Boxing: Brains vs Brawn")

ASSETS_FOLDER = os.path.join(os.getcwd(), "ExampleAssets")

getImage = lambda image: pygame.image.load(os.path.join(ASSETS_FOLDER, image))
getMusic = lambda music: pygame.mixer.music.load(os.path.join(ASSETS_FOLDER, music))

music = getMusic('music.mp3')

# pygame.mixer.music.play(-1)

walkRight = [getImage('R1.png'), getImage('R2.png'), getImage('R3.png'), getImage('R4.png'), getImage('R5.png'), getImage('R6.png'), getImage('R7.png'), getImage('R8.png'), getImage('R9.png')]
walkLeft = [getImage('L1.png'), getImage('L2.png'), getImage('L3.png'), getImage('L4.png'), getImage('L5.png'), getImage('L6.png'), getImage('L7.png'), getImage('L8.png'), getImage('L9.png')]
bg = getImage('bg.jpg')
char = getImage('standing.png')

clock = pygame.time.Clock()

class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.vel = 5

        self.isJump = False
        self.left = False
        self.right = False

        self.walkCount = 0
        self.jumpCount = 10

        self.standing = True

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
                
    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render("-5", 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing

        self.vel = 8 * self.facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy:
    walkRight = [getImage('R1E.png'), getImage('R2E.png'), getImage('R3E.png'), getImage('R4E.png'), getImage('R5E.png'), getImage('R6E.png'), getImage('R7E.png'), getImage('R8E.png'), getImage('R8E.png'), getImage('R9E.png'), getImage('R10E.png'), getImage('R11E.png')]
    walkLeft = [getImage('L1E.png'), getImage('L2E.png'), getImage('L3E.png'), getImage('L4E.png'), getImage('L5E.png'), getImage('L6E.png'), getImage('L7E.png'), getImage('L8E.png'), getImage('L8E.png'), getImage('L9E.png'), getImage('L10E.png'), getImage('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = (self.x, self.end)
        self.walkCount = 0
        self.vel = 3
        self.health = 10
        self.visible = True

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - 5 * (10 - self.health), 10))
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("Hit")

font = pygame.font.SysFont('comicsans', 30, bold=True)

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render(f"Score: {score}", 1, (0, 0, 0))
    win.blit(text, (350, 10))
    man.draw(win)
    goblin.draw(win)
    
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


man = Player(200, 410, 64,64)
goblin = Enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []

score = 0

run = True
while run:
    clock.tick(27)
    
    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5
    
    if shootLoop > 0:
        shootLoop += 1

    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()