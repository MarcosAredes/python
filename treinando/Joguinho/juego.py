import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição de variáveis
largura_tela = 800
altura_tela = 600
cor_fundo = (0, 0, 0)
FPS = 60

# Configuração da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong Game")


# Definição de objetos do jogo
class Paddle(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    def __init__(self, cor, tamanho):
        super().__init__()
        self.image = pygame.Surface((tamanho, tamanho))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.velocidade = [4, 4]


# Criando instâncias dos objetos do jogo
paddle1 = Paddle((255, 255, 255), 15, 100)
paddle1.rect.x = 50
paddle1.rect.y = altura_tela // 2 - 50

paddle2 = Paddle((255, 255, 255), 15, 100)
paddle2.rect.x = largura_tela - 50 - 15
paddle2.rect.y = altura_tela // 2 - 50

bola = Ball((255, 255, 255), 15)
bola.rect.x = largura_tela // 2 - 7
bola.rect.y = altura_tela // 2 - 7

# Grupos de sprites
todos_sprites = pygame.sprite.Group()
todos_sprites.add(paddle1, paddle2, bola)

# Loop principal do jogo
relogio = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação das paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.rect.y > 0:
        paddle1.rect.y -= 5
    if keys[pygame.K_s] and paddle1.rect.y < altura_tela - 100:
        paddle1.rect.y += 5

    if keys[pygame.K_UP] and paddle2.rect.y > 0:
        paddle2.rect.y -= 5
    if keys[pygame.K_DOWN] and paddle2.rect.y < altura_tela - 100:
        paddle2.rect.y += 5

    # Movimentação da bola
    bola.rect.x += bola.velocidade[0]
    bola.rect.y += bola.velocidade[1]

    # Colisões com as paredes
    if bola.rect.y > altura_tela - 15 or bola.rect.y < 0:
        bola.velocidade[1] = -bola.velocidade[1]

    # Colisões com as paletas
    if pygame.sprite.collide_rect(bola, paddle1) or pygame.sprite.collide_rect(
        bola, paddle2
    ):
        bola.velocidade[0] = -bola.velocidade[0]

    # Verifica se a bola saiu pela lateral e reinicia a posição
    if bola.rect.x > largura_tela or bola.rect.x < 0:
        bola.rect.x = largura_tela // 2 - 7
        bola.rect.y = altura_tela // 2 - 7

    # Limpa a tela
    tela.fill(cor_fundo)

    # Desenha os sprites
    todos_sprites.draw(tela)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de frames por segundo
    relogio.tick(FPS)
