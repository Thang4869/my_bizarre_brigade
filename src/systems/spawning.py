import random
from src.entities.enemy import Enemy

def spawn_enemies(enemies_group, all_sprites, wave, enemies_per_wave, spawn_timer, screen_width):
    spawn_timer += 1
    if spawn_timer > 60 // wave:
        if len(enemies_group) < enemies_per_wave * wave:
            enemy = Enemy(screen_width)  # Truyền width nếu cần
            all_sprites.add(enemy)
            enemies_group.add(enemy)
            return 0  # Reset timer
    return spawn_timer