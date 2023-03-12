import pygame
import random
import time
pygame.init()

W = 600
H = 600
snake_block = 20
score = 0

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake by vbystrov")

foodx = round(random.randrange(0, W, 20) // 10.0) * 10.0
foody = round(random.randrange(0, H, 20) // 10.0) * 10.0

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169, 169, 169)





FPS = 10
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)

game_over = False

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    sc.blit(mesg, [250, 250])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(sc, (105, 105, 105), [x[0], x[1], snake_block, snake_block])


snake_List = []
Length_of_snake = 1

x = 0
y = 0
speed = 20

right = 0
left = 0
up = 0
down = 0

while not game_over:
    #повороты
    if right == 1:
        x += speed
    elif left == 1:
        x -= speed
    elif up == 1:
        y -= speed
    elif down == 1:
        y += speed
    #проверка на границы
    if x > W:
        x = 0
    elif x < 0:
        x = W
    elif y > H:
        y = 0
    elif y < 0:
        y = H

    #еда

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                right, left, up, down = 1, 0, 0, 0
            elif event.key == pygame.K_LEFT:
                right, left, up, down = 0, 1, 0, 0
            elif event.key == pygame.K_UP:
                right, left, up, down = 0, 0, 1, 0
            elif event.key == pygame.K_DOWN:
                right, left, up, down = 0, 0, 0, 1

    if x >= W or x < 0 or y >= H or y < 0:
        game_over = True

    snake_Head = []
    snake_Head.append(x)
    snake_Head.append(y)
    snake_List.append(snake_Head)
    print(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for z in snake_List[:-1]:
        if z == snake_Head:
            game_over = True

    sc.fill(GREY)
    pygame.draw.rect(sc, (47, 79, 79), [foodx, foody, snake_block, snake_block])
    our_snake(snake_block, snake_List)
    ms = str('Счет:' + str(score))

    mesg = font_style.render(ms, True, RED)
    sc.blit(mesg, [450, 580])
    pygame.display.update()
    clock.tick(FPS)





    if x == foodx and y == foody:
        foodx = round(random.randrange(0, W, 20) // 10.0) * 10.0
        foody = round(random.randrange(0, H, 20) // 10.0) * 10.0
        Length_of_snake += 1
        score += 1


message("You lost. Score:" + str(score), RED)
pygame.display.update()
time.sleep(2)