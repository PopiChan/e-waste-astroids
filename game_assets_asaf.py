#collecting e-waste space invaders game

#imports
import pygame
from os.path import abspath, dirname
import math
import random
import ctypes
import time
#imports

#Start screen Loop
done = False
start_time = pygame.time.get_ticks()

#Paths
BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/assets/e_waste_images/'
Sound_Path = BASE_PATH + '/assets/sounds/'
#Paths

pygame.init()

user32 = ctypes.windll.user32
SIZE_W = user32.GetSystemMetrics(78)
SIZE_H = user32.GetSystemMetrics(79)
SIZE = width, height = SIZE_W, SIZE_H
astroid_location = 0,0

#settings
#SCREEN HEIGHT AND SCREEN WIDTH
s_width = SIZE_W
s_height = SIZE_H
window = pygame.display.set_mode((SIZE), pygame.FULLSCREEN)
# window = pygame.display.set_mode(SIZE)

# IMG_NAMES = ['spaceship','astroid','background']
IMG_NAMES = ['spaceship', 'astroid1','astroid2','astroid3','astroid4','astroid5',
            'astroid6','astroid7','astroid8','astroid9','astroid10','background']

IMAGES = {name: pygame.image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
        for name in IMG_NAMES}

BACKGROUND = IMAGES['background']
SPACESHIP = IMAGES['spaceship']
# ASTEROID = IMAGES['asteroid']
ASTROID1 = IMAGES['astroid1']
ASTROID2 = IMAGES['astroid2']
ASTROID3 = IMAGES['astroid3']
ASTROID4 = IMAGES['astroid4']
ASTROID5 = IMAGES['astroid5']
ASTROID6 = IMAGES['astroid6']
ASTROID7 = IMAGES['astroid7']
ASTROID8 = IMAGES['astroid8']
ASTROID9 = IMAGES['astroid9']
ASTROID10 = IMAGES['astroid10']

SHOOT = pygame.mixer.Sound('assets/sounds/shoot.wav')
BANG = pygame.mixer.Sound('assets/sounds/bang.wav')


def create_font(t,s=45,c=(0,0,0), b=True,i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text


pygame.display.set_caption('space waste')

clock = pygame.time.Clock()



class Bullet(object):
    """
    A class to represent Bullets

    ...

    Attributes
    ----------
    point: int
        the head of the spaceship from where the bullets fires
    x,y : int
        the position in the x and y axis in the game window
    width : int
        width of the bullet
    height: int
        height of the bullet
    cos: int
        cosine for the movement
    sin: int
        sine for the movement
    xvel: int
        velocity on the x axis
    yvel: int
        velocity on the y axis

    Methods
    -------
    move():
        moves the bullet
    draw(window object):
        draws the bullet onto the game screen
    detect_bullet_offscr:
        detects if the bullet go offscreen so that we can remove them from the list to reduce space usage
    
    """
    def __init__(self):
        self.point = user.head
        self.x, self.y = self.point
        self.width = 4
        self.height = 4
        self.cos = user.cos
        self.sin = user.sin
        self.xvel = self.cos * 10
        self.yvel = self.sin * 10

    def move(self):
        self.x += self.xvel
        self.y -= self.yvel

    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), [self.x, self.y, self.width, self.height])

    def detect_bullet_offscr(self):
        if self.x < -50 or self.x > s_width or self.y > s_height or self.y < -50:
            return True








class User(object):
    """
    A class to represent the User i.e the Ship

    ...

    Attributes
    ----------
    image :
        image of the spaceship
    width : int
        width of the spaceship
    height : int
        age of the person
    x: float
        position of the spaceship on the xaxis
    y: float
        position of the spaceship on the y axis
    angle: int
        angle of the spaceship
    rotatedSurface:
        rotates the spaceship
    rotatedRect: 
        rotates the rectangle encompassing spaceship
    head: float:
        Head of the spaceship from where bullets travel
    
    Methods
    -------
    draw(window):
        Draws the spaceship onto the screen
    turn_left():
        turns the spaceship to left
    turn_right():
        turns the spaceship to right
    move_forward():
        moves the spaceship forward
    update_offscreen():
        updates the spaceship to come out of the opposite side of window if spaceship travels off the main screen
    """
    def __init__(self):
        self.image = SPACESHIP
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = s_width // 10
        self.y = s_height // 10
        self.angle = 0
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width//2, self.y - self.sin * self.height//2)

    def draw(self,window):
        # window.blit(self.image,[self.x, self.y, self.width, self.height])
        window.blit(self.rotatedSurface, self.rotatedRect)

    def turn_left(self):
        self.angle += 5
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * (self.width//2), self.y - self.sin//2 * self.height//2)


    def turn_right(self):
        self.angle = self.angle - 5
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width//2, self.y - self.sin * self.height//2)

    def move_forward(self):
        self.x += self.cos * 6
        self.y -= self.sin * 6
        self.rotatedSurface = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width//2, self.y - self.sin * self.height//2)
    
    def update_offscreen(self):
        if self.x > s_width + 10:
            self.x = 0
        elif self.x < 0 - self.width:
            self.x = s_width
        elif self.y < -10:
            self.y = s_height
        elif self.y > s_height + 10:
            self.y = self.y = 0


class Enemy(object):
    """
    A class to represent the enemy(Asteroids)

    ...

    Attributes
    ----------
    image :
        image of the enemy
    width : int
        width of the enemy
    height : int
        height of the enemy
    x: int
        initial random position of the enemy on x axis
    y: int
        initial random position of the enemy on y axis
    xdirect: int
        direction of the enemy moving in on x axis
    ydirect: int
        direction of the enemy moving in on y axis
    xvel: int 
        velocity of the enemy on the x axis
    yvel: int:
        Velocity of the enemy on the y axis
    
    Methods
    -------
    draw(window):
        Draws the enemy onto the main screen
    """
    def __init__(self):
        astroid_number = random.randint(1,10)
        # self.image = IMAGES['asteroid{}'].format(astroid_number)
        # self.image = IMAGES['asteroid']
        Astroid_Path = IMAGE_PATH + 'asteroid{}.png'.format(astroid_number)
        self.image = pygame.image.load("assets/e_waste_images/astroid{}.png".format(astroid_number))

        self.width = 50
        self.height = 50
        self.random_point = random.choice([(random.randrange(0, s_width-self.width), random.choice([-1*self.height - 5, s_height + 5])), (random.choice([-1*self.width - 5, s_width + 5]), random.randrange(0, s_height - self.height))])
        self.x, self.y = self.random_point
        if self.x < s_width//2:
            self.xdirect = 1
        else:
            self.xdirect = -1
        if self.y < s_height//2:
            self.ydirect = 1
        else:
            self.ydirect = -1
        self.xvel = self.xdirect * random.randrange(1,3)
        self.yvel = self.ydirect * random.randrange(1,3)
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))    

def gameOverScreen():
    seconds_survived = (pygame.time.get_ticks() - start_time) // 1000
    # seconds_survived = (end_time - start_time) // 1000
    return round(seconds_survived)

def resetGameWindow():
    '''Resets the game window with enemies and spaceship reset to the start of the gameloop if the game ends, returns nothing'''
    window.blit(BACKGROUND, (0,0))
    font = pygame.font.SysFont('arial', 30)
    no_of_lives = font.render('Lives : '+ str(lives), 1, (255,255,255))
    s = pygame.Surface((s_width,s_height))  # the size of your rect
    s.set_alpha(128)                # alpha level
    s.fill((255,0,0))           # this fills the entire surface
    # play_again = font.render('Do you want to play again?? Press Space to play again',10,(0,0,0))
    play_again = create_font('Do you want to play again?? Press Space to play again')
    end_score = create_font('Your Score : ' + str(score))
    time_alive = create_font('Time Alive : ' + str(gameOverScreen()) + ' seconds')
    total_score = font.render('Score: ' + str(score),1,(255,255,255))
    user.draw(window)
    for asteroid in asteroids:
        asteroid.draw(window)

    for bullets in userBullets:
        bullets.draw(window)
    window.blit(no_of_lives,(25,25))
    window.blit(total_score, (25,75))
    if gameover:
        end = time.time()
        window.blit(s, (0,0))
        window.blit(play_again, (s_width//2-play_again.get_width()//2, s_height//2 - s_height//10*2 - play_again.get_height()//2))
        window.blit(end_score, (s_width//2-end_score.get_width()//2, s_height//2 - s_height//10*1 - end_score.get_height()//2))
        window.blit(time_alive, (s_width//2-time_alive.get_width()//2, s_height//2 - s_height//10*3 - time_alive.get_height()//2))
    pygame.display.update()


def main():
    '''Main driver for the game, initializes everything. Checks for collision and decreases lives and scores likewise. Checks for lives and if they are 0, calls on the resetGameWindow at the end, Returns nothing'''
    global user
    user = User()
    global userBullets
    userBullets = []
    global asteroids
    asteroids = []
    global parts
    parts = []
    global count
    count = 0
    global run
    run = True
    global gameover
    gameover = False
    global score
    global lives
    lives = 5
    score = 0
    #Game loop
    while run:

        clock.tick(60)
        count += 1
        if not gameover:
            if count % 50 == 0:
                ran = random.choice([1,2,3])
                asteroids.append(Enemy())
            user.update_offscreen()

        for bullets in userBullets:
            bullets.move()
            if bullets.detect_bullet_offscr():
                userBullets.pop(userBullets.index(bullets))
        #Checking if the spaceship collides with the asteroids
        for asteroid in asteroids:
            asteroid.x += asteroid.xvel
            asteroid.y += asteroid.yvel

            if (user.x >= asteroid.x and user.x <= asteroid.x + asteroid.width) or (user.x + user.width >= asteroid.x and user.x + user.width <= asteroid.x + asteroid.width):
                if(user.y >= asteroid.y and user.y <= asteroid.y + asteroid.height) or (user.y + user.height >= asteroid.y and user.y + user.height <= asteroid.y + asteroid.height):
                    lives -= 1
                    asteroids.pop(asteroids.index(asteroid))
                    break
            
            #Checking if asteroid gets hit by a bullet
            for bullet in userBullets:
                if (bullet.x >= asteroid.x and bullet.x <= asteroid.x + asteroid.width) or (bullet.x + bullet.width >= asteroid.x and bullet.x + bullet.width <= asteroid.x + asteroid.width):
                    if (bullet.y >= asteroid.y and bullet.y <= asteroid.y + asteroid.height) or (bullet.y + bullet.height >= asteroid.y and bullet.y + bullet.height <= asteroid.y + asteroid.height):
                        new_asteroid1 = Enemy()
                        score += 1
                        asteroids.pop(asteroids.index(asteroid))
                        userBullets.pop(userBullets.index(bullet))
                        BANG.play()

            if lives <= 0:
                end_time = pygame.time.get_ticks()
                gameover = True





        if not gameover:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_LEFT]:
                user.turn_left()
            if pressed_keys[pygame.K_RIGHT]:
                user.turn_right()
            if pressed_keys[pygame.K_UP]:
                user.move_forward()
            




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        userBullets.append(Bullet())
                        SHOOT.play()
                    else:
                        gameover = False
                        lives = 5
                        score = 0
                        asteroids.clear()

        resetGameWindow()
    pygame.quit()

