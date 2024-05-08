import pygame

pygame.init()
tela = pygame.display.set_mode((720, 360))
pygame.display.set_caption('Shooter Obstacle')
clock = pygame.time.Clock()
ativo = True
coordenada_player = [15, 285]
gravidade = 0.5
aceleração = 0
força_do_pulo = -10
coordenada_inimigo = [720, 285]

def renderizar_textos(pontuação, recorde):
   font=pygame.font.SysFont('monospace',35)
   texto_pontos = font.render("Pontos: {}            Recorde: {}".format(str(pontuação), str(recorde)), 1,(0,0,0))
   tela.blit(texto_pontos, (20, 0))

recorde_player = [0, 0]
pontos = 0
velocidade_inimigo = 6
rotação_bola = 0

def dificuldade():
    global velocidade_inimigo
    global rotação_bola
    if velocidade_inimigo == 6 and pontos >= 10:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 7 and pontos >= 20:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 8 and pontos >= 30:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 9 and pontos >= 40:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 10 and pontos >= 50:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 11 and pontos >= 60:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 12 and pontos >= 70:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 13 and pontos >= 80:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 14 and pontos >= 90:
        velocidade_inimigo += 1
        rotação_bola += 0.1
    elif velocidade_inimigo == 15 and pontos >= 100:
        velocidade_inimigo += 1
        rotação_bola += 0.1

boladecanhao = pygame.image.load("boladecanhao.png").convert_alpha()
tamanho_boladecanhao = (50, 50)
boladecanhao = pygame.transform.scale(boladecanhao, tamanho_boladecanhao)

while ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ativo = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if coordenada_player[0] >= 660:
            pass
        else:
            coordenada_player[0] += 7
    if keys[pygame.K_LEFT]:
        if coordenada_player[0] <= 0:
            pass
        else:
            coordenada_player[0] -= 7
    if keys[pygame.K_UP]:
        if coordenada_player[1] != 285:
            pass
        else:
            aceleração += força_do_pulo

    aceleração += gravidade
    
    coordenada_player[1] += aceleração
    
    if coordenada_player[1] >= 285:
        coordenada_player[1] = 285
        aceleração = 0
    else:
        pass
    
    dificuldade()
    coordenada_inimigo[0] -= velocidade_inimigo
    if coordenada_inimigo[0] <= -55:
        coordenada_inimigo[0] = 720
        pontos += 1
    tela.fill('White')
    
    pygame.draw.rect(tela, (0,0,0), (0, 345, 720, 15))
    player = pygame.draw.rect(tela, (255, 0, 255), (coordenada_player[0], coordenada_player[1], 60, 60))
    enemy = pygame.draw.rect(tela, (255, 255, 255), (coordenada_inimigo[0], coordenada_inimigo[1], 55, 55))
    rotação_bola += 1
    boladecanhao_rotacionado = pygame.transform.rotate(boladecanhao, rotação_bola)
    tela.blit(boladecanhao_rotacionado, (coordenada_inimigo[0], coordenada_inimigo[1]))
    
    renderizar_textos(pontos, recorde_player[1])
    if player.colliderect(enemy):
        coordenada_player = [15, 285]
        coordenada_inimigo = [720, 285]
        recorde_player[1] = pontos if pontos > recorde_player[1] else recorde_player[1]
        pontos = 0
        velocidade_inimigo = 6
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
