import pygame
from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *

'''
- Add a scoring system
- Implement multiple lives and respawning
- Make the ship have a triangular hit box instead of a circular one
- Make the asteroids lumpy instead of perfectly round
- Add an explosion effect for the asteroids
- Make the objects wrap around the screen instead of disappearing
- Create different weapon types
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped
- Add a background image
- Add a Main Menu
'''

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteriods, updatables, drawables)
    AsteroidField.containers = (updatables)

    Player.timer = 0
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatables.update(dt)

        for a in asteriods:
            if a.collision(player):
                print("Game Over!")
                return

        for a in asteriods:
            for b in shots:
                if a.collision(b):
                    a.split()
                    b.kill()

        screen.fill("black")

        for i in drawables:
            i.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
