import pygame
import random
from os.path import join
#general setup
pygame.init()
WINDOW_WIDTH , WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
running = True
imagepath = 'data\images'
# MUSIC
pygame.mixer.init()
pygame.mixer.music.load("data/music/Izaya tiji - interlude.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.06)

# ICON
pygame.display.set_caption("TK's game")
pygame.display.set_icon(pygame.image.load(join(imagepath, 'doggie.jpg')))

# SURFACES
surf = pygame.Surface((75, 50))
surf.fill('green')
chalX = 1
chalY = 200

# CHALLENGER : importing image 
challenger_surf = pygame.image.load(join(imagepath, 'challenger.png')).convert_alpha()
challenger_rect = challenger_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

#TL 
TL_surf = pygame.image.load(join(imagepath, 'acuratl.png')).convert_alpha()
bee_surf = pygame.image.load(join(imagepath, 'bee.png')).convert_alpha()
tlX = 1
TL_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(50)]

#E46
bmw_surf = pygame.image.load(join(imagepath, 'e46game.png')).convert_alpha()
bmwX = 1
bmwY = 1


while running:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    #change rates
    chalX += 0.1
    bmwX += 0.09
    tlX += 0.13

    
    display_surface.fill('darkgray')
    for xy in TL_positions:
        display_surface.blit(TL_surf, xy)
    display_surface.blit(challenger_surf, (chalX,chalY))
    display_surface.blit(bmw_surf, (bmwX, bmwY))
    

    pygame.display.update()
    
    
pygame.quit()