
import pygame
import player
#player.player.position()[keys, player_rect]; player.player.clocktick() dt; player.player_pos;
pygame.init()
sw = 1280
sh = 720
screen = pygame.display.set_mode((sw, sh))
blockpos = 0, 0
blocksize = 100
f = pygame.draw.rect(screen, "green", (blockpos[0], blockpos[1], 10, 10))
fx = 0
fy = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    for y in range((sh*4)//blocksize):
        for x in range((sw*4)//blocksize):
            if not fx > sw or fx < sw:
                pygame.draw.rect(screen, "green", (fx - player.player_pos.x, fy - player.player_pos.y, blocksize, blocksize))
                fx+=blocksize
        if not fy > sh or fy < sh:
            fx = 0
            fy+=blocksize
    fy = 0
    pygame.draw.rect(screen, "red", player.player.position()[1])
    
    if player.player.position()[0][pygame.K_w]:
        player.player_pos.y -= 300 * player.player.clocktick()
    if player.player.position()[0][pygame.K_s]:
        player.player_pos.y += 300 * player.player.clocktick()
    if player.player.position()[0][pygame.K_a]:
        player.player_pos.x -= 300 * player.player.clocktick()
    if player.player.position()[0][pygame.K_d]:
        player.player_pos.x += 300 * player.player.clocktick()
    
    # dt
    pygame.display.flip()
    player.player.clocktick()

    

pygame.quit()