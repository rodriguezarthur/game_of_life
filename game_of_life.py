import game_of_life_func
import sys, pygame
from random import randint

grid = [[randint(0,1) for i in range(50)] for j in range(50)]

pygame.init()

size = width,height = 600,600
screen = pygame.display.set_mode(size)
black = 0,0,0

def draw_grid(grid):
    w = len(grid[0])
    h = len(grid)
    square_size = (width-5*(w-1))/w
    for i in range(h-1):
        pygame.draw.rect(screen,black,pygame.Rect(0,(i+1)*square_size+i*5,600,5))
    for i in range(w-1):
        pygame.draw.rect(screen,black,pygame.Rect((i+1)*square_size+i*5,0,5,600))
    for i in range(h):
        for j in range(w):
            if grid[i][j]:
                pygame.draw.rect(screen,black,pygame.Rect(i*(square_size+5),j*(square_size+5),square_size+5,square_size+5))
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    draw_grid(grid)
    pygame.display.flip()
    grid = game_of_life_func.evolution(grid)
    pygame.time.wait(100)