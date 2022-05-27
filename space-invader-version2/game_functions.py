# manage all the events here
import sys, pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    # monitor events using event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # ship movement based on user input
        elif event.type == pygame.KEYDOWN:  # pressed key on keyboard
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    # fill the screen with background color
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # draw the ship to screen
    ship.blitme()

    # update the screen
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # remove bullets that have gone out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # create a new bullet and add to bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)