import pygame


LOGO_FONT = None
BUTTON_FONT = None

def initFonts():
    global LOGO_FONT, BUTTON_FONT
    # LOGO_FONT = pygame.font.SysFont("gothicpixels", 50)
    # BUTTON_FONT = pygame.font.SysFont("deltarune", 20)

    # LOGO_FONT = pygame.font.SysFont("deltarune", 75)
    # BUTTON_FONT = pygame.font.SysFont("deltarune", 20)

    # https://www.dafont.com/monster-friend-fore.font
    # Gets the font from system
    # LOGO_FONT = pygame.font.SysFont("monsterfriendback", 50)
    # BUTTON_FONT = pygame.font.SysFont("monsterfriendback", 13)

    if LOGO_FONT is not None and BUTTON_FONT is not None:
        print("\033[93mWarning: Fonts already initialized.\033[0m")  # yellow text
        return  # already initialized
    if not pygame.get_init():
        raise RuntimeError("pygame must be initialized first")

    # Gets the font dynamically
    LOGO_FONT = pygame.font.Font("assets/fonts/MonsterFriendFore.otf", 50)
    BUTTON_FONT = pygame.font.Font("assets/fonts/MonsterFriendFore.otf", 13)