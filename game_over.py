import random
import pygame
import os


pygame.init()
screen = pygame.display.set_mode((1280, 720))


def main():
    gifs = [
        pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "game_over_gif", x)).convert_alpha(),
                                     (1280, 720)) for x in os.listdir("images/game_over_gif")]
    clock = pygame.time.Clock()
    done = False
    counter = 0
    while not done:
        if counter >= len(gifs)-1:
            done = True
        clock.tick(15)
        screen.fill((255, 255, 255))
        screen.blit(gifs[counter], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.update()
        counter += 1


if __name__ == '__main__':
    main()

