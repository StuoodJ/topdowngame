import pygame

dt = 0
clock = pygame.time.Clock()
player_pos = pygame.Vector2(1280 / 2, 720 / 2)
class player():
    def position():
        playerrect = pygame.Rect(player_pos.x, player_pos.y, 50, 50)
        keys = pygame.key.get_pressed()
        
        return keys, playerrect
    def clocktick():
        dt = clock.tick(60) / 1000
        return dt
        