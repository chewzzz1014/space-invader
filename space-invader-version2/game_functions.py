# manage all the events here
import sys, pygame

def check_events(ship):
    # monitor events using event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # ship movement based on user input
        elif event.type == pygame.KEYDOWN:  # pressed key on keyboard
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # fill the screen with background color
    screen.fill(ai_settings.bg_color)

    # draw the ship to screen
    ship.blitme()

    # update the screen
    pygame.display.flip()