import pygame
import sys
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.systems.collision import check_player_collision
from src.systems.spawning import spawn_enemies

# Khởi tạo
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bizarre Brigade Prototype")
clock = pygame.time.Clock()

# Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game vars
wave = 1
enemies_per_wave = 5
spawn_timer = 0
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn enemies (sử dụng function)
    spawn_timer = spawn_enemies(enemies, all_sprites, wave, enemies_per_wave, spawn_timer, SCREEN_WIDTH)

    # Update
    all_sprites.update()

    # Collision
    if check_player_collision(player, enemies):
        print("Game Over! Wave:", wave)
        running = False

    # Check wave complete
    if len(enemies) == 0 and spawn_timer > 60:
        wave += 1
        print("Wave", wave, "started!")

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()