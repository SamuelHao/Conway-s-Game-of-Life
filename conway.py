import pygame
import time
import random
pygame.init()

displayWidth = 1280
displayHeight = 720

gridWidth = 5
gridHeight = 5
gridMargin = 1

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)


gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Conways Game of Life')

clock = pygame.time.Clock()


grid = []
gridPos = []
gridPos = [0,0]
startLife = 0

for row in range(1920):
    grid.append([])
    for column in range(1080):
        grid[row].append(0)

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " +str(count),True,black)
    gameDisplay.blit(text,(0,0))
        

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def printOut(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = (((displayWidth/2),(displayHeight/2)))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.5)
    gameLoop()

def button(text,x,y,width,height,colour,highlight,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay,highlight,(x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,colour,(x,y,width,height))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(text,smallText)
    textRect.center = ( (x+(width/2)),(y + (height/2)) )
    gameDisplay.blit(textSurf, textRect)
        
def titleScreen():
    x = 0
    y = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("Conway's Game of Life",largeText)
            TextRect.center = (((displayWidth/2),(displayHeight/2)))
            gameDisplay.blit(TextSurf, TextRect)
            
            
            button("GO!",300,550,100,50,green,brightGreen,gameLoop)
            button("Quit!",800,550,100,50,red,brightRed,quit)

            
            
            
            pygame.display.update()
            clock.tick(120)

def lifeLoop():
    global startLife
    if startLife == 1:
        startLife = 0
    else:
        startLife = 1
        
def gameLoop():
    population = 0
    colour = white
    gameDisplay.fill(white)
    gameExit = False
    liveNeighbours = 0
    while not gameExit:
        x = 0
        y = 0
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                row = mouse[0] - mouse[0]%5
                column = mouse[1] - mouse[1]%5
                #print(row,column)
                if grid[row][column] == 1:
                    grid[row][column] = 0
                else:
                    grid[row][column] = 1

            
        for row in range(displayWidth//gridWidth):
            y = 0
            for column in range(displayHeight//gridWidth):
                if startLife == 1:
                    liveNeighbours = 0
                    if grid[x+5][y+5] == 1 or grid[x+5][y+5] == -1:
                        liveNeighbours += 1
                    if grid[x+5][y] == 1 or grid[x+5][y] == -1:
                        liveNeighbours += 1
                    if grid[x+5][y-5] == 1 or grid[x+5][y-5] == -1:
                        liveNeighbours += 1
                    if grid[x][y-5] == 1 or grid[x][y-5] == -1:
                        liveNeighbours += 1
                    if grid[x-5][y-5] == 1 or grid[x-5][y-5] == -1:
                        liveNeighbours += 1
                    if grid[x-5][y] == 1 or grid[x-5][y] == -1:
                        liveNeighbours += 1
                    if grid[x-5][y+5] == 1 or grid[x-5][y+5] == -1:
                        liveNeighbours += 1
                    if grid[x][y+5] == 1 or grid[x][y+5] == -1:
                        liveNeighbours += 1

                    if grid[x][y] == 1 and liveNeighbours < 2:
                        grid[x][y] = -1
                    if grid[x][y] == 1 and liveNeighbours > 3:
                        grid[x][y] = -1
                    if grid[x][y] == 0 and liveNeighbours == 3:
                        grid[x][y] = 2
                y += gridWidth
            x += gridWidth

        x = 0
        for row in range(displayWidth//gridWidth):
            y = 0
            pygame.draw.rect(gameDisplay,colour,[x,y,gridWidth,gridHeight])
            for column in range(displayHeight//gridWidth):
                if grid[x][y] == -1:
                    grid[x][y] = 0
                if grid[x][y] == 2:
                    grid[x][y] = 1
                if grid[x][y] == 1:
                    colour = black
                pygame.draw.rect(gameDisplay,colour,[x,y,gridWidth,gridHeight])
                colour = white
                y += gridWidth
            x += gridWidth
            

        #score(population)
        button("LIFE!",1150,650,100,50,green,brightGreen,lifeLoop)    
        pygame.display.update()
        clock.tick(120)

titleScreen()
pygame.quit()
quit()
