import random
from pygame import mixer
import pygame
import os
from game_over import main as game_over

pygame.init()
screen = pygame.display.set_mode((1280, 720))

cloud = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "cloud.png")).convert_alpha(), (300, 170))
cloud1 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "cloud1.png")).convert_alpha(),
                                      (300, 170))
cloud2 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "cloud3.png")).convert_alpha(),
                                      (300, 170))
mario1 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "mario1.png")).convert_alpha(),
                                      (70, 110))
mario2 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "mario2.png")).convert_alpha(),
                                      (70, 110))
mario3 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "mario3.png")).convert_alpha(),
                                      (70, 110))
pipe = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "pipe.png")).convert_alpha(), (160, 210))
pipe2 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "pip2.png")).convert_alpha(), (160, 210))
pipe3 = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "pip3.png")).convert_alpha(), (130, 130))
background = pygame.transform.smoothscale(pygame.image.load(os.path.join("images", "background.png")).convert_alpha(),
                                          (1280, 720))

mario_gif = [mario1, mario2, mario3]


def play_sound(sound):
    mixer.music.load(sound)
    mixer.music.play()
    pygame.mixer.music.set_volume(0.2)


class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current = 0
        self.y_vel = 0
        self.image = mario_gif[self.current // 6]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def display(self):
        self.y += self.y_vel
        self.current += 1
        if self.y < 250:
            self.y_vel *= -1
        if self.y == 450:
            self.y_vel = 0
        if self.current == 18:
            self.current = 0
        self.image = mario_gif[self.current // 6]
        self.rect.y = self.y
        screen.blit(self.image, (self.x, self.y))


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, x_vel):
        self.x = x
        self.y = y
        self.current = 0
        self.image = random.choice([pipe, pipe2])
        self.x_vel = x_vel
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.rect)

    def display(self):
        if self.image == pipe2:
            self.y = 380
        self.x += self.x_vel
        self.rect.x += self.x_vel
        screen.blit(self.image, (self.x, self.y))

    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)


def reset_screen():
    global screen, score
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (3, 177, 252), [0, 0, 1280, 550])

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (97, 71, 33), [0, 550, 1280, 170])
    font = pygame.font.Font(None, 50)
    text = font.render(f"SCORE:- {score}", True, (255, 255, 255))
    screen.blit(text, (1070, 30))


score = 0


def main():
    OBSTACLES_VEL = -10
    global score
    clock = pygame.time.Clock()
    done = False
    mario = Mario(600, 450)
    obstacles = [Pipe(720 + 800 + (800 * x), 450, OBSTACLES_VEL) for x in range(3)]

    while not done:
        reset_screen()
        for x in obstacles:
            last_x_pos = max([x.x for x in obstacles])
            if x.x < -800:
                obstacles.remove(x)
                obstacles.append(Pipe(last_x_pos + random.randint(780, 840), 450, OBSTACLES_VEL))
                score += 50
                play_sound('project_files/coin.wav')
                if score % 500 == 0:
                    OBSTACLES_VEL -= 0.05
            if x.collide(mario):
                done = True
                play_sound('project_files/smb_die.wav')
                game_over()

        for x in obstacles:
            x.display()
        clock.tick(60)
        mario.display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_sound('project_files/jump.wav')
                    if mario.y_vel == 0:
                        mario.y_vel = -6

        pygame.display.flip()


if __name__ == '__main__':
    main()
