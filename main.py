import pygame
import sys
import random 

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def shrink_image(image, colorkey = None):
    new_image = pygame.transform.scale(image, (image.get_width() * .1, image.get_height() * .1))
    if colorkey is not None:
        if colorkey == -1:
            colorkey = new_image.get_at((0,0))
            new_image.set_colorkey(colorkey, pygame.RLEACCEL)
    return new_image

player_image = pygame.image.load("art/goodgoku.png")
player_image = shrink_image(player_image)
player_image.set_colorkey(player_image.get_at((0, 0)))
player_rect = player_image.get_rect()

while True:

    #put player inputs/actions here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            if event.key == pygame.K_a:
                player_rect.x -= 50
            if event.key == pygame.K_d:
                player_rect.x += 50
            if event.key == pygame.K_w:
                player_rect.y -= 50
            if event.key == pygame.K_s:
                player_rect.y += 50 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('left stop')
            if event.key == pygame.K_RIGHT:
                print('right stop')

    ############### Logic below #################
    border_rect = border_rect
    if player_rect.colliderect(border_rect): 
        pass


    




    ############### Logic ends ###################

    #put things that get drawn on screen here
    WIN.fill("black")
    WIN.blit(player_image, player_rect)

    pygame.display.update()

