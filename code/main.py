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

#TL 
TL_surf = pygame.image.load(join(imagepath, 'acuratl.png')).convert_alpha()
TL_rect = TL_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

TL_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(50)]

#E46
bmw_surf = pygame.image.load(join(imagepath, 'e46game.png')).convert_alpha()
bmw_rect = bmw_surf.get_frect(topleft = (10,WINDOW_HEIGHT / 2))
bmw_direction = 1
bmw_speed = 7
#BEE
bee_surf = pygame.image.load(join(imagepath, 'bee.png')).convert_alpha()
bee_rect = bee_surf.get_frect(bottomleft = (20 , WINDOW_HEIGHT - 20))
while running:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    #player movement
    bmw_rect.x += bmw_direction * bmw_speed
    
    if bmw_rect.left == 0:
        bmw_direction = 1
    if bmw_rect.right > WINDOW_WIDTH or bmw_rect.left < 0:
        bmw_direction *= -1
    
    display_surface.fill('black')
    
    #display_surface.blit(TL_surf, TL_rect)
    display_surface.blit(bmw_surf, bmw_rect)
    display_surface.blit(bee_surf, bee_rect)
    

    pygame.display.update()
    
    
pygame.quit()