#Executável Jogo Festejando Firme.

import pygame
width = 1500
height = 750

killer_walk = []
killer_anim_frame = 1
killer_pos_x = 300
killer_pos_y = 225
killer_anim_time = 0

def load():
    global clock, hero_walk
    clock = pygame.time.Clock()
    for i in range(0, 5): #carrega as imagens da animação /  MUDAR PARA A QUANTIDADE DE IMAGENS range(1, x)
        killer_walk.append(pygame.image.load("iller_Walk_0" + str(i) + ".png"))


def update(dt):
    global hero_walk, hero_anim_frame, hero_pos_x,hero_pos_y, hero_anim_time, offset
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        offset=0
        hero_pos_x = hero_pos_x + (-0.1 * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
        offset=0

        

    if keys[pygame.K_RIGHT]:
        offset=5
        hero_pos_x = hero_pos_x + (0.1 * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
        offset=5

    if keys[pygame.K_UP]:
        offset=8
        hero_pos_y = hero_pos_y - (0.1 * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
        offset=8



    if keys[pygame.K_DOWN]:
        offset=12
        hero_pos_y = hero_pos_y + (0.1 * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_anim_frame = hero_anim_frame + 1 # avança para proximo frame
            if hero_anim_frame > 3: # loop da animação
                hero_anim_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
        offset=12


def draw_screen(screen):
    screen.fill((255,255,255))
    #desenha o personagem usando o índice da animação (Seleção do sprite)
    screen.blit(hero_walk[hero_anim_frame], (hero_pos_x, hero_pos_y))

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