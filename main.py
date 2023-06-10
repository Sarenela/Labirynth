import pygame
import sys
from utils import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO
from Player import Player
from Wall import walls

# Inicjalizacja Pygameee
pygame.init()


# Utworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra w labirynt")

# Klasy





# Inicjalizacja gracza
player = Player()

# Grupa sprite'ów
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Główna pętla gry
running = True
while running:
    # Częstotliwość odświeżania ekranu
    pygame.time.Clock().tick(FPS)

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizacja
    all_sprites.update()

    # Rysowanie
    screen.fill(LIGHT_PISTACHIO)
    # Rysowanie ścian
    walls.draw(screen)
    all_sprites.draw(screen)

    # Wyświetlanie zmian
    pygame.display.flip()

# Zamknięcie programu
pygame.quit()
sys.exit()
