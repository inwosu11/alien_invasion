import pygame

def run_game():
    #initializes the game and creates a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")


    while True: 

        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make thew most recently drawn screen visible 
        pygame.display.flip()
run_game()
