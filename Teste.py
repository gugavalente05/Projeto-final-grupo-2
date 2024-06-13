import pygame
import random
from random import randint as r

#---------------------------------------------------------------------

# Parte killer(PEDRO)
width = 1920
height = 1080
kiler_walk= []
Sprt_Killer_Walking = {0:(0, 0, 20, 56),1:(20, 0, 20, 56),2:(40, 0, 20, 56),3:(60, 0, 20, 56),4:(80, 0, 20, 56),
        5:((0, 60), (20, 120)),6:(20, 60, 20, 120),7:(40, 60, 20, 120),8:(60, 60, 20, 120),9:(80, 60, 20, 120)}
Sprt_Killer_Killing = {0:(0, 0, 20, 56),1:(20, 0, 20, 56),2:(40, 0, 20, 56),3:(60, 0, 20, 56),4:(80, 0, 20, 56),
        5:(86, 60, 21, 117),6:(60, 60, 21, 117),7:(40, 60, 21, 117),8:(20, 60, 21, 117),9:(0, 60, 21, 117)}
killer_anim_frame = 0
killer_pos_x = 860
killer_pos_y = 800
killer_anim_time = 1 # variavel para controle do tempo da animação
offset = 0

# Parte killer(PEDRO)

#--------------------------------------------------------------------


#--------------------------------------------------------------------

# Parte Npc(GUSTAVO)

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


# Parte Npc(GUSTAVO)

#------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------
    # carregando os spritessheets do KILLER(PEDRO)
def load():
    global clock, sheet,sheet_Killing, spt_wdt, spt_hgt, npc, sptD_wdtNpc, sptD_hgtNpc, sptA_wdtNpc, sptA_hgtNpc, sptM_wdtNpc, sptM_hgtNpc
    clock = pygame.time.Clock()
    sheet = pygame.image.load("Killer_A1.png")
    sheet_Killing = pygame.image.load("Killer_Kill_1.png")
    spt_wdt = sheet.get_width() / 5# Largura de um sprite
    spt_hgt = sheet.get_height() / 2# Altura de um sprite

    # carregando os spritessheets do KILLER(PEDRO)

#--------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

    # carregando os spritessheets do NPC(GUSTAVO)
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

    # carregando os spritessheets do NPC(GUSTAVO)
#--------------------------------------------------------------------------------------






altura = 0 #variáveis para altura e flag(Pedro)
flag = 0 #variáveis para altura e flag(Pedro)
def update(dt):
    global kiler_walk, killer_anim_frame, killer_pos_x, killer_anim_time, killer_pos_y, offset, flag, npc_anim_frame, npc_anim_time, flagD, ale
    keys = pygame.key.get_pressed()

#------------------------------------------------------------------------------------

    # Carregando as animações do NPC (GUSTAVO)
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
    # Carregando as animações do NPC (GUSTAVO)


#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

    # Controlando o Killer (Pedro)
    if keys[pygame.K_f]:
        flag = 1

    if flag==1:
        killer_anim_time = killer_anim_time + dt #incrementa o tempo usando dt
        if killer_anim_time > 100: #quando acumular mais de 100 ms
            killer_anim_frame = killer_anim_frame + 1# avança para proximo frame
            if killer_anim_frame > 4: # loop da animação
                flag = 0
                killer_anim_frame=0
            killer_anim_time = 0 #reinicializa a contagem do tempo
            


    if keys[pygame.K_LEFT] and flag==0: #(flag) -- variável para o personagem parar de andar e fazer a animação de parar
        offset = 0
        killer_pos_x = killer_pos_x + (-0.1 * dt) # movimenta o personagem
        killer_anim_time = killer_anim_time + dt #incrementa o tempo usando dt
        if killer_anim_time > 100: #quando acumular mais de 100 ms
            killer_anim_frame = killer_anim_frame + 1# avança para proximo frame
            if killer_anim_frame > 4: # loop da animação
                killer_anim_frame = 0
            killer_anim_time = 0 #reinicializa a contagem do tempo


    if keys[pygame.K_RIGHT]  and flag==0: #(flag) -- variável para o personagem parar de andar e fazer a animação de parar
        offset = 5
        killer_pos_x = killer_pos_x + (0.1 * dt) # movimenta o personagem
        killer_anim_time = killer_anim_time + dt #incrementa o tempo usando dt
        if killer_anim_time > 100: #quando acumular mais de 100 ms
            killer_anim_frame = killer_anim_frame + 1 # avança para proximo frame
            if killer_anim_frame > 4: # loop da animação
                killer_anim_frame = 0
            killer_anim_time = 0 #reinicializa a contagem do tempo

    if keys[pygame.K_UP] and flag == 0: #(flag) -- variável para o personagem parar de andar e fazer a animação de parar
        killer_pos_y = killer_pos_y - (0.1 * dt) # movimenta o personagem
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:#condicional para o personagem nao (bugar) andar para cima e para o lado ao mesmo tempo
            killer_anim_time = killer_anim_time + dt #incrementa o tempo usando dt
            if killer_anim_time > 100: #quando acumular mais de 100 ms
                killer_anim_frame = killer_anim_frame + 1# avança para proximo frame
                if killer_anim_frame > 4: # loop da animação
                    killer_anim_frame = 0
                killer_anim_time = 0 #reinicializa a contagem do tempo
            
    if keys[pygame.K_DOWN] and flag == 0 : #(flag) -- variável para o personagem parar de andar e fazer a animação de parar
        killer_pos_y = killer_pos_y + (0.1 * dt) # movimenta o personagem
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]: #condicional para o personagem nao (bugar) andar para cima e para o lado ao mesmo tempo
            killer_anim_time = killer_anim_time + dt #incrementa o tempo usando dt
            if killer_anim_time > 100: #quando acumular mais de 100 ms
                killer_anim_frame = killer_anim_frame + 1# avança para proximo frame
                if killer_anim_frame > 4: # loop da animação
                    killer_anim_frame = 0
                killer_anim_time = 0 #reinicializa a contagem do tempo


    # Controlando o Killer (Pedro)


#---------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def draw_screen(screen): 
    global flag
    """
    for i in range(0,2):
        screen.blit(npc[i], (killer_pos_x, killer_pos_y), tile[str(i)])

        
    """
    screen.fill((255, 255, 255))
# TODo E QUALQUER CÓDIGO DEVE PERTENCENTE A ESSA FUNÇAÕ DEVE SER ESCRITA DEPOIS DO SCREEN FILL
#----------------------------------------------------------------------------

#---------------------------------------------------------------------
    #Desenhando o NPC(GUSTAVO)
    for i in range(12):
        npc_index = i // 3  # determina qual sprite de NPC utilizar (D, A ou M)
        frame = npc_anim_frame[i]
        x = posx_random[i]
        y = posy_random[i]
        screen.blit(npc[npc_index], (x, y), (frame * sptD_wdtNpc, 0, sptD_wdtNpc, sptD_hgtNpc))
    #Desenhando o NPC(GUSTAVO)

#---------------------------------------------------------------------


#--------------------------------------------------------------------
    #Desenhando o Killer(PEDRO)
    if flag == 1:
        screen.blit(sheet_Killing,(killer_pos_x, killer_pos_y),Sprt_Killer_Killing[killer_anim_frame + offset])
    else:
        screen.blit(sheet,(killer_pos_x, killer_pos_y),Sprt_Killer_Walking[killer_anim_frame + offset])
    #desenhando o colider Killer(PEDRO)
    collider_killer = pygame.Rect(killer_pos_x ,killer_pos_y, 20, 56)
    collider_killer_toKill = pygame.Rect(killer_pos_x- 8,killer_pos_y+6, 36, 40)
    pygame.draw.rect(screen, (0, 255, 0), (collider_killer.x, collider_killer.y, collider_killer.width, collider_killer.height), 2)
    pygame.draw.rect(screen, (255, 0, 0), (collider_killer_toKill.x, collider_killer_toKill.y, collider_killer_toKill.width, collider_killer_toKill.height), 2)
#-----------------------------------------------------------------------
    
    

def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fechamento do prog
                running = False
                break
        
        screen.fill((0, 0, 0))
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