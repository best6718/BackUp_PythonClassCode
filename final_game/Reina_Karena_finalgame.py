# Author: Karena and Reina
# Final Frogo: A Frog Game
import pygame
import random
import math

pygame.init()

#used to be 800, 600
size = [1000, 1000]

#things we want to change: get rid of whaite squares, if frogs get closer have creatures speed up, insert more creatures into the game
gameWindow = pygame.display.set_mode(size)
pygame.display.set_caption('My Frog is Hungry for Mosquitos!!!')

# RGB Colors
BLACK  = (0,0,0)  # black is lack of all colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (187, 255, 153)
BLUE = (240,248,255)

clock = pygame.time.Clock()

# Load the frog, 3 mosquitos, a snake, a racoon and a fox AND the background image
myFrog = pygame.image.load('Frog1.png')
m1 = pygame.image.load('Mosquito.png')
m2 = pygame.image.load('Mosquito.png')
m3 = pygame.image.load('Mosquito.png')
snake = pygame.image.load('snake.png')
rac = pygame.image.load('raccoon.png')
fox = pygame.image.load('fox.png')
snake2 = pygame.image.load('snake.png')
rac2 = pygame.image.load('raccoon.png')
fox2 = pygame.image.load('fox.png')
background = pygame.image.load('leaf-pond-background.jpg')
bird = pygame.image.load('bird.png')
bird2 = pygame.image.load('bird.png')

# Change the size of the' Frog, the raccoon, the snake and the fox AND the background image
OtherSize = [50, 30]
myFrog = pygame.transform.scale(myFrog, OtherSize)
snake = pygame.transform.scale(snake, OtherSize)
rac = pygame.transform.scale(rac, OtherSize)
fox = pygame.transform.scale(fox, OtherSize)
snake2 = pygame.transform.scale(snake, OtherSize)
rac2 = pygame.transform.scale(rac, OtherSize)
fox2 = pygame.transform.scale(fox, OtherSize)
bird = pygame.transform.scale(bird, OtherSize)
bird2 = pygame.transform.scale(bird, OtherSize)                          
background = pygame.transform.scale(background, (size[0], size[1]))

# change the size of the mosquitos
MosquitoSize = [20, 20]
m1 = pygame.transform.scale(m1, MosquitoSize)
m2 = pygame.transform.scale(m2, MosquitoSize)
m3 = pygame.transform.scale(m3, MosquitoSize)


# function to display the Sprites in the game
# (x,y) Frog position
# (x_m1, y_m1) mosquito 1 position
def display_img(x,y,x_m1,y_m1, x_m2, y_m2, x_m3, y_m3, m1_alive, m2_alive, m3_alive, xr, yr, xs, ys, xf, yf, xr2, yr2, xs2, ys2, xf2, yf2, xb, yb,xb2, yb2, frog_alive):
    # Display background
    gameWindow.blit(background,(0,0))
    
    if frog_alive:
        gameWindow.blit(myFrog, (x,y))  # (0,0) is upper left

    gameWindow.blit(rac, (xr,yr))
    gameWindow.blit(snake, (xs, ys))
    gameWindow.blit(fox, (xf,yf))

    gameWindow.blit(rac2, (xr2, yr2))
    gameWindow.blit(snake2, (xs2, ys2))
    gameWindow.blit(fox2, (xf2, yf2))
    gameWindow.blit(bird, (xb, yb))
    gameWindow.blit(bird2,(xb2, yb2))

    if m1_alive:
        gameWindow.blit(m1, (x_m1, y_m1))
    if m2_alive:
        gameWindow.blit(m1, (x_m2, y_m2))
    if m3_alive:
        gameWindow.blit(m1, (x_m3, y_m3))

    #(x,y) = hit_walls(x, y, 0, WIDTH, 0, HEIGHT)
def hit_walls(x, y, xmin, xmax, ymin, ymax):
    # If img hits the boundaries, wrap around
    if x > xmax:
        x = xmin
    elif x < xmin:
        x = xmax
    if y > ymax:
        y = ymin
    elif y < ymin:
        y = ymax
    return(x,y)

def m_hit_walls(x, y, xmin, xmax, ymin, ymax):
    # keep mosquitos inside boundaries
    q = 20
    if x > xmax:
        x = xmax - q
    elif x < xmin:
        x = xmin + q
    if y > ymax:
        y = ymax - q
    elif y < ymin:
        y = ymin + q
    return(x,y)

def follow(x, y, xc, yc, alive):
    # d is the distance between the frog and the creature
    d = math.sqrt((x -xc) **2 ) + (( y - yc) ** 2)
    #We still want it to be that the frog has entered the same proximity of the creature to be eatened
    if (d < 50):
        alive = False   # frog has been eaten
    if ((random.randint(1, 100)) < 80) and (d < 200):
        p1 = x - xc
        p2 = y - yc
        xc +=  (p1 / 5)
        yc +=  (p2 / 5)
        return(xc, yc, alive)
    else:
        return(xc, yc, alive)

def set_obj_position(x, y, xnew, ynew):
    # x and y are the positions of the object
    return x, y, xnew, ynew

def set_position(x, y):
    # x and y are the positions of the object
    return x, y

def game():
    # x and y are the positions of the frog
    x, y, new_x, new_y = set_obj_position(20, 20, 0, 0)
    # position of  mosquito 1
    x_m1, y_m1, new_x_m1, new_y_m1 = set_obj_position(200, 200, 0, 0)
    # position of mosquito 2
    x_m2, y_m2, new_x_m2, new_y_m2 = set_obj_position(300, 500, 0, 0)
    # position of mosquito 2
    x_m3, y_m3, new_x_m3, new_y_m3 = set_obj_position(575, 650, 0, 0)
    # position of the rac, snake and fox
    xr, yr = set_position(120, 260)
    xs, ys = set_position(620, 40)
    xf, yf = set_position(220, 480)

    # position of second rac, snake, and fox
    xr2, yr2 = set_position(340, 560)
    xs2, ys2 = set_position(700, 700)
    xf2, yf2 = set_position(500, 600)
    xb, yb = set_position(430,200)
    xb2, yb2 = set_position(300,100)


    end = False
    m1_alive = True
    m2_alive = True
    m3_alive = True

    frog_alive = True

    while not end:

        # event handler loop
        for event in pygame.event.get(): # gets user events
            if event.type == pygame.QUIT:  # click x
                     end = True
                     print(event) # prints to console
            if event.type == pygame.KEYDOWN:  # pressing key down
                if event.key == pygame.K_LEFT:   #left arrow key
                    #changed from -5 to -10
                    new_x = -10 # move our image to the left
                elif event.key == pygame.K_RIGHT:
                    #changed from 5 to 10
                    new_x = 10
                elif event.key == pygame.K_UP:
                    #changed from -5 to -10
                    new_y = -10
                elif event.key == pygame.K_DOWN:
                    #changed from 5 to 10
                    new_y = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    new_x = 0  #  stop image from moving in the x direction
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    new_y = 0  #  stop image from moving in the y direction

        # the mosquitos move randomly inside the rectangle
        z = 10
        x_m1 += random.randint(-z, z)
        y_m1 += random.randint(-z, z)
        x_m2 += random.randint(-z, z)
        y_m2 += random.randint(-z, z)
        x_m3 += random.randint(-z, z)
        y_m3 += random.randint(-z, z)

        # If mosquitos hits the boundaries, stop them from leaving area
        (x_m1,y_m1) = m_hit_walls(x_m1, y_m1, 100, 300, 100, 300)
        (x_m2,y_m2) = m_hit_walls(x_m2, y_m2, 200, 400, 400, 600)
        (x_m3,y_m3) = m_hit_walls(x_m3, y_m3, 500, 700, 0, 200)

        # Display background before the new location of the image
        gameWindow.fill(WHITE)

        if frog_alive:  # Calculate the new location
            x += new_x
            y += new_y

        # Dangerous areas get red when frog is inside
        #if (x >= 100) and (x <= 300) and (y>= 100) and (y <= 300):
        #     pygame.draw.rect(gameWindow, RED, (100, 100, 200, 200))
        #else:
        #    pygame.draw.rect(gameWindow, BLUE, (100, 100, 200, 200))
        #if (x >= 500) and (x <= 700) and (y>= 0) and (y <= 200):
        #    pygame.draw.rect(gameWindow, RED, (500, 0, 200, 200))
        #else:
        #    pygame.draw.rect(gameWindow, BLUE, (500, 0, 200, 200))
        #if (x >= 200) and (x <= 400) and (y>= 400) and (y <= 600):
        #    pygame.draw.rect(gameWindow, RED, (200, 400, 200, 200))
        #else:
        #    pygame.draw.rect(gameWindow, BLUE, (200, 400, 200, 200))

            
        if frog_alive:
            # Calculate distance between frog and mosquitos
            d1 = math.sqrt( (x - x_m1)**2 + (y - y_m1)**2 )
            d2 = math.sqrt( (x - x_m2)**2 + (y - y_m2)**2 )
            d3 = math.sqrt( (x - x_m3)**2 + (y - y_m3)**2 )

            # Simulate frog eating mosquitos
            d = 15
            if (d1 < d):
                m1_alive = False
            if (d2 < d):
                m2_alive = False
            if (d3 < d):
                m3_alive = False

            # Simulate rac, snake and fox following the frog and maybe eating the frog
            frog_alive = True
            xr, yr, frog_alive = follow(x, y, xr, yr, frog_alive)
            xs, ys, frog_alive = follow(x, y, xs, ys, frog_alive)
            xf, yf, frog_alive = follow(x, y, xf, yf, frog_alive)

            xr2, yr2, frog_alive = follow(x, y, xr2, yr2, frog_alive)
            xs2, ys2, frog_alive = follow(x, y, xs2, ys2, frog_alive)
            xf2, yf2, frog_alive = follow(x, y, xf2, yf2, frog_alive)
            xb, yb, frog_alive = follow(x, y, xb, yb, frog_alive)
            xb2, yb2, frog_alive = follow(x, y, xb2, yb2, frog_alive)
             

            # If Frog hits the boundaries, wrap around
            (x,y) = hit_walls(x, y, 0, size[0], 0, size[1])


        # Display all the creatures
        display_img(x, y, x_m1, y_m1, x_m2, y_m2, x_m3, y_m3, m1_alive, m2_alive, m3_alive, xr, yr, xs, ys, xf, yf, xr2, yr2, xs2, ys2, xf2, yf2, xb, yb, xb2, yb2, frog_alive)

        
        # Game instructions 
        fontObj = pygame.font.Font('freesansbold.ttf', 15)
        textSurfaceObj = fontObj.render('Move the arrows to move the Frog', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 30)
        gameWindow.blit(textSurfaceObj, textRectObj)

        fontObj = pygame.font.Font('freesansbold.ttf', 15)
        textSurfaceObj = fontObj.render('Eat mosquitos and avoid other creatures', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 45)
        gameWindow.blit(textSurfaceObj, textRectObj)

        if (not frog_alive):
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('YOU LOST!', True, RED, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (400, 150)
            gameWindow.blit(textSurfaceObj, textRectObj)

        elif (not m1_alive) and (not m2_alive) and (not m3_alive):
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('YOU WON!', True, RED, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (400, 150)
            gameWindow.blit(textSurfaceObj, textRectObj)

        # Now we are ready to display all the work done
        pygame.display.update()

        # FPS Frames Per Second, how fast things move
        clock.tick(60)

# Here we start the game by calling the main function game()
game()
pygame.quit()

