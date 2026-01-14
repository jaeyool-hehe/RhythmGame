import pygame

def load_boss_images():
    # generalFrogState
    general_frog_state_list = [pygame.transform.scale(pygame.image.load(f"assets/images/GeneralFrog/GeneralFrogState{counter}.png"), (240, 240)) for counter in range(1, 6)]

    boss_images.update({1 : general_frog_state_list})
    # shrimp
    for counter in range(1, 6):
        # boss_image = pygame.image.load(f"assets/images/CommanderShrimp/CommanderShrimpState{counter}.png")
        # boss_image = pygame.transform.scale(boss_image, (240, 240))
        # boss_images.update({f"{counter}": boss_image})

        commander_shrimp_state_list = [pygame.transform.scale(pygame.image.load(f"assets/images/CommanderShrimp/CommanderShrimpState{counter}.png"),(240, 240)) for counter in range(1, 6)]

        boss_images.update({2: commander_shrimp_state_list})
    # bull
    for counter in range(1, 6):
        horn_bull_state_list = [pygame.transform.scale(pygame.image.load(f"assets/images/HornBull/HornBullState{counter}.png"), (240, 240)) for counter in range(1, 6)]
        boss_images.update({3: horn_bull_state_list})
    # turtle
    for counter in range(1, 6):
        magma_turtle_state_list = [pygame.transform.scale(pygame.image.load(f"assets/images/MagmaTurtle/MagmaTurtleState{counter}.png"), (240, 240)) for counter in range(1, 6)]
        boss_images.update({4: magma_turtle_state_list})

    # crow
    for counter in range(1, 6):
        crow_state_list = [pygame.transform.scale(pygame.image.load(f"assets/images/Crow/CrowState{counter}.png"),(240, 240)) for counter in range(1, 6)]
        boss_images.update({5: crow_state_list})


# mission
# fix the sizing of the player image
# put the boss images to the display


def load_player_images():
    for counter in range(1, 6):
        playerImage = pygame.image.load(f"assets/images/Player/PlayerState{counter}.png")
        playerImage = pygame.transform.scale(playerImage, (240, 240))
        player_images.append(playerImage)




boss_images = {}


player_images = []