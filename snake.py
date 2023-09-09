import pygame
import time
import random

# Inizializza Pygame
pygame.init()

# Impostazioni del gioco
larghezza, altezza = 640, 480
dimensione_cella = 20
velocita = 15

# Colori
nero = (0, 0, 0)
bianco = (255, 255, 255)
rosso = (255, 0, 0)

# Inizializza lo schermo
schermo = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("Snake Game")

# Inizializza il serpente
serpente = [(larghezza // 2, altezza // 2)]
direzione = (0, 0)

# Funzione per inizializzare il cibo
def inizializza_cibo():
    return (random.randrange(0, larghezza, dimensione_cella), random.randrange(0, altezza, dimensione_cella))

# Inizializza il cibo
cibo = inizializza_cibo()

# Punteggio
punteggio = 0

# Funzione per disegnare il serpente
def disegna_serpente(serpente):
    for segmento in serpente:
        pygame.draw.rect(schermo, nero, (segmento[0], segmento[1], dimensione_cella, dimensione_cella))

# Funzione principale
def gioca():
    global direzione, punteggio, cibo

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direzione != (0, 1):
                    direzione = (0, -1)
                elif evento.key == pygame.K_DOWN and direzione != (0, -1):
                    direzione = (0, 1)
                elif evento.key == pygame.K_LEFT and direzione != (1, 0):
                    direzione = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direzione != (-1, 0):
                    direzione = (1, 0)

        nuovo_serpente = [(serpente[0][0] + direzione[0] * dimensione_cella, serpente[0][1] + direzione[1] * dimensione_cella)]
        if nuovo_serpente[0] == cibo:
            punteggio += 1
            cibo = inizializza_cibo()
        else:
            serpente.pop()

        if (nuovo_serpente[0][0] < 0 or nuovo_serpente[0][0] >= larghezza or
            nuovo_serpente[0][1] < 0 or nuovo_serpente[0][1] >= altezza or
            nuovo_serpente[0] in serpente):
            pygame.quit()
            quit()

        serpente.insert(0, nuovo_serpente[0])

        # Pulisce lo schermo
        schermo.fill(bianco)

        # Disegna il cibo
        pygame.draw.rect(schermo, rosso, (cibo[0], cibo[1], dimensione_cella, dimensione_cella))

        # Disegna il serpente
        disegna_serpente(serpente)

        # Aggiorna lo schermo
        pygame.display.update()

        # Limita la velocità del gioco
        time.sleep(1 / velocita)

# Esegui il gioco
gioca()
