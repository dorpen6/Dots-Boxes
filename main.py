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

# KEEP the WINDOW RUNNING
running = True
while running:
    for event in pygame.event.get(): # EVENT HANDLING
        if event.type == pygame.QUIT: # IF THE USER CLOSES THE WINDOW (IN THIS CASE THEY DID an EVENT)
            running = False # STOP THE LOOP

pygame.quit() # CLOSE THE WINDOW
            