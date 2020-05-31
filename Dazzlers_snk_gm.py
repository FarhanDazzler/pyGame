#By Farhan Dazzler
import pygame
import random
import  os

pygame.mixer.init()



pygame.init()

# Colors
white = (255, 255, 255)
red = 	(255,69,0)
black = (0, 0, 0)

# Creating window
screen_width = 700
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Dazzler's Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 35)

#background image
bgimg=pygame.image.load("bg2.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
gmimg=pygame.image.load("gameover.png")
gmimg=pygame.transform.scale(gmimg,(screen_width,screen_height)).convert_alpha()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play()

    while not exit_game:

        gameWindow.fill(black)
        text_screen("welcome to snake game ",white,150,200)
        text_screen("Press space to continue...",red,100,350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1


    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0

    init_velocity = 5
    snake_size = 15
    fps = 30
    if(not os.path.exists('highscore.txt')):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()


    while not exit_game:
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(gmimg,(0,0))


           # text_screen("Game Over! Press Enter To Continue", red, 5, 5)
          #  pygame.mixer.music.load('gameover.mp3')
           # pygame.mixer.music.play()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                pygame.mixer.music.load('eating.mp3')
                pygame.mixer.music.play()

                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

                if score>int(highscore):
                    highscore=score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))

            text_screen("Score: " + str(score) + "  High Score :"+ str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play(100)
                pygame.mixer.music.set_volume(.6)

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play(100)
                pygame.mixer.music.set_volume(.6)
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
