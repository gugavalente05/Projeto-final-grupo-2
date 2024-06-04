#Executável Jogo Festejando Firme.

import pygame
width = 800
height = 600
hero_frame = 1
hero_pos_x = 6
hero_pos_y = 225
hero_time = 0

width = 1000  # Largura Janela
height = 800 # Altura Janela

def load():
    global clock, sheet, spt_wdt, spt_hgt
    clock = pygame.time.Clock()
    sheet = pygame.image.load('PC_Computer_-_Party_Hard_-_Darius_Party_Killer-removebg-preview.png')
    spt_wdt = sheet.get_width() 
    spt_hgt = sheet.get_height()


def update(dt):
    global hero_frame, hero_pos_x, hero_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero_pos_x = hero_pos_x + (0.1 * dt)
        hero_time = hero_time + dt
        if hero_time > 100:
            hero_frame = hero_frame + 1
            if hero_frame > 3:
                hero_frame = 0
            hero_time = 0


def draw_screen(screen):
    screen.fill((255,255,255))
    #desenha o personagem usando o índice da animação (Seleção do sprite)
    screen.blit(sheet,(hero_pos_x, hero_pos_y),(spt_wdt * hero_frame, 0 ,spt_wdt,spt_hgt))

def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fechamento do prog
                running = False
                break

        # Define FPS máximo
        clock.tick(60)
        # Tempo transcorrido desde a última atualização 
        dt = clock.get_time()
        # Atualiza posição dos objetos
        update(dt)
        # Desenha objetos
        draw_screen(screen)
        # Pygame atualiza a visualização da tela
        pygame.display.update()

# Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()