import pygame
import threading
from pygame import mixer
from main import main as main_module

number_of_grey = "7"
WIDTH, HEIGHT = 1280, 720
GAMEDISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
MENU_IMG = pygame.transform.smoothscale(pygame.image.load(r"project_files/menu.png").convert(),
                                        (WIDTH, HEIGHT))
GAMEDISPLAY.fill((0, 0, 0))
white = (255, 255, 255)

mixer.init()
pygame.init()


def hover_sound():
    mixer.music.load('project_files/hover.wav')
    mixer.music.play()
    pygame.mixer.music.set_volume(0.5)


def click_sound():
    mixer.music.load('project_files/click.wav')
    mixer.music.play()
    pygame.mixer.music.set_volume(1)


def main():
    global number_of_grey
    clock = pygame.time.Clock()
    selected_option = 1

    def redraw_windows():
        GAMEDISPLAY.blit(MENU_IMG, (0, 0))
        pygame.display.update()

    while True:
        clock.tick(60)
        redraw_windows()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] in range(149, 607) and event.pos[1] in range(199, 515):
                    if selected_option != 0:
                        threading.Thread(target=hover_sound).start()
                    selected_option = 0
                elif event.pos[0] in range(665, 1139) and event.pos[1] in range(196, 728):
                    if selected_option != 2:
                        threading.Thread(target=hover_sound).start()
                    selected_option = 2
                else:
                    selected_option = 1000
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(149, 607) and event.pos[1] in range(199, 515):
                    threading.Thread(target=click_sound).start()
                    main_module()

                elif event.pos[0] in range(665, 1139) and event.pos[1] in range(196, 728):
                    pygame.quit()
                    quit()
                else:
                    pass


if __name__ == "__main__":
    main()
