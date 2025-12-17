import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (168, 168, 168)
RED = (255, 0, 0)
YELLOW = (244, 252, 3)



# TODO refactor

LOGO_FONT = None
BUTTON_FONT =  None

def initFonts():
    global LOGO_FONT, BUTTON_FONT
    # LOGO_FONT = pygame.font.SysFont("gothicpixels", 50)
    # BUTTON_FONT = pygame.font.SysFont("deltarune", 20)

    # LOGO_FONT = pygame.font.SysFont("deltarune", 75)
    # BUTTON_FONT = pygame.font.SysFont("deltarune", 20)

    LOGO_FONT = pygame.font.SysFont("monsterfriendback", 50)
    BUTTON_FONT = pygame.font.SysFont("monsterfriendback", 13)
    # monsterfriendback
