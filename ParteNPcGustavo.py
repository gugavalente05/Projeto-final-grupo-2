import pygame
import random
from random import randint as r

width = 1920
height = 1080
npc = []
spriteNpc = 0
tileD = {}
npc_anim_frame = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
npc_anim_time = [random.randint(0, 300) for _ in range(12)]  # intervalo de tempo inicial aleatório para cada NPC
offset = 0
posy_random = []
posx_random = []
flagD = [0 for _ in range(12)]

for i in range(12):
    posx_random.append(random.randint(850, 1100))
    posy_random.append(random.randint(400,650))


def load():
    global clock, npc, sptD_wdtNpc, sptD_hgtNpc, sptA_wdtNpc, sptA_hgtNpc, sptM_wdtNpc, sptM_hgtNpc
    clock = pygame.time.Clock()
    for i in range(3):
        npc.append(pygame.image.load("npcD" + str(i + 1) + ".png"))
        sptD_wdtNpc = npc[i].get_width() / 5
        sptD_hgtNpc = npc[i].get_height() / 2
    for i in range(3):
        npc.append(pygame.image.load("npcA" + str(i + 1) + ".png"))
        sptA_wdtNpc = npc[i].get_width() / 5
        sptA_hgtNpc = npc[i].get_height() / 2
    for i in range(3):
        npc.append(pygame.image.load("npcM" + str(i + 1) + ".png"))
        sptM_wdtNpc = npc[i].get_width() / 2
        sptM_hgtNpc = npc[i].get_height() / 1


def update(dt):
    global npc_anim_frame, npc_anim_time, flagD, ale

    for i in range(12):
        ale = r(1,2)
        if ale == 1:
            flagD[i] == 1
        if flagD[i] != 1:
            npc_anim_time[i] += dt  # incrementa o tempo usando dt
            if npc_anim_time[i] > random.randint(200, 400):  # tempo de dança aleatório para cada NPC
                npc_anim_frame[i] += 1
                if npc_anim_frame[i] > 3:
                    npc_anim_frame[i] = 0
                npc_anim_time[i] = 0  # reinicializa a contagem do tempo
        else:
            npc_anim_frame[i] = 0


def draw_screen(screen):
    screen.fill((0, 0, 0))
    for i in range(12):
        npc_index = i // 3  # determina qual sprite de NPC utilizar (D, A ou M)
        frame = npc_anim_frame[i]
        x = posx_random[i]
        y = posy_random[i]
        screen.blit(npc[npc_index], (x, y), (frame * sptD_wdtNpc, 0, sptD_wdtNpc, sptD_hgtNpc))


def main_loop(screen):
    global clock
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # fechamento do prog
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
