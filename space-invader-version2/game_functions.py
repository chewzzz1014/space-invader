# manage all the events here
import sys, pygame

def check_events():
    # monitor events using event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
