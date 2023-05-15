import pygame
import sys
import random 



WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win_rect = WIN.get_rect()

clock = pygame.time.Clock()

def draw_block(x, y, color = (54, 92, 227)):
    pygame.draw.rect(WIN, color, ( x, y, 15, 15), 1, 1)

snake = [(300, 300), (320, 300), (340, 300)]

apple_possible_x = list(range(0, win_rect.right, 20))
random.shuffle(apple_possible_x)

apple_possible_y = list(range(0, win_rect.bottom, 20))
random.shuffle(apple_possible_y)

apple = (apple_possible_x[0], apple_possible_y[0])

velocity = [0, 0]

while True:

    #put player inputs/actions here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            if event.key == pygame.K_a and velocity[0] > -20:
                velocity[0] = -20
                velocity[1] = 0
            if event.key == pygame.K_d and velocity[0] < 20:
                velocity[0] = 20
                velocity[1] = 0
            if event.key == pygame.K_w and velocity[1] > -20:
                velocity[1] = -20
                velocity[0] = 0
            if event.key == pygame.K_s and velocity[1] < 20:
                velocity[1] = 20
                velocity[0] = 0

    


    ############### Logic below #################
    ate_apple = False
    for snake_block in snake:
        if snake_block == apple:
            snake.append((snake[-1]))
            apple = (10000, 10000)
            ate_apple = True
    if ate_apple != True:
        snake.pop(-1)

    snake.insert(0, (snake[0][0] + velocity[0], snake[0][1] + velocity[1]))
    
    



    ############### Logic ends ###################

    #put things that get drawn on screen here
    WIN.fill("black")
    for snake_block in snake:
        draw_block(snake_block[0], snake_block[1])

    draw_block(apple[0], apple[1], (235, 14, 14))

    pygame.display.update()
    clock.tick(10)
