import pygame
import sys

import asteroid
import asteroidfield
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player
import shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (shots, updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    my_asteroidfield = asteroidfield.AsteroidField()
    my_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # my_player.draw(screen)
        for thing in drawable:
           thing.draw(screen)
        # my_player.update(dt)
        updatable.update(dt)
        for ast in asteroids:
            if ast.collides_with(my_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for sht in shots:
                if ast.collides_with(sht):
                    log_event("asteroid_shot")
                    sht.kill()
                    ast.split()
        pygame.display.flip()
        dt = my_clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
