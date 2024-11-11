
import pygame
import player
#player.player.position()[keys, player_rect]; player.player.clocktick() dt; player.player_pos;
pygame.init()
screen = pygame.display.set_mode((1280, 720))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
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