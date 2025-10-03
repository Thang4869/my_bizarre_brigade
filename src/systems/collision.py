import pygame

def check_player_collision(player, enemies):
    return pygame.sprite.spritecollide(player, enemies, True)