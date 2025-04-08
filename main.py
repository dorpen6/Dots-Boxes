import pygame

# Creating Window & Dots

SCREEN = WIDTH, HEIGHT = 300, 300
CELL_SIZE_BETWEEN_DOTS = 20
PADDING_BETWEEN_DOTS = 20 # SPACE BETWEEN DOTS
ROWS = COLUMNS = (WIDTH - 4*PADDING_BETWEEN_DOTS) // CELL_SIZE_BETWEEN_DOTS # ROWS & COLUMNS = (300(WIDTH) - 80 (PADDING * 4)) / 20 = (300 - 80) / 20 = 220 / 20 = 11 -> 11 ROWS & COLUMNS
print(ROWS, COLUMNS)

# CREATING A WINDOW
pygame.init()
screen = pygame.display.set_mode(SCREEN)

# COLOR DEFINING FOR THE GAME
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# KEEP the WINDOW RUNNING
running = True
while running:
    for event in pygame.event.get(): # EVENT HANDLING
        if event.type == pygame.QUIT: # IF EVENT IS QUIT, which means they pressed the exit button on the top right
            running = False # STOP THE LOOP

pygame.quit() # CLOSE THE WINDOW
            