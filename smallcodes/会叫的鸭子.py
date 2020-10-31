import sys
import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(size=(431, 363))
pygame.display.set_caption("鸭子")
what_you_pressed = ["None","None","None"]
pic_duck = pygame.image.load("duck.jpg")

# 创建字典//暂时没用的操作

dict = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107,
               'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114,'s': 115,'t': 116,'u': 117,'v': 118,
               'w': 119,'x': 120,'y': 121,'z': 122}


def playSE(musicname, volume=1):
    sound = pygame.mixer.Sound(musicname+".wav")
    sound.set_volume(volume)
    sound.play()


def showText(screen, string, size, pos, color):
    textImage = None
    font = pygame.font.SysFont('arial',size)
    textImage = font.render(string, True, color)
    screen.blit(textImage, pos)


while True:
    screen.blit(pic_duck, (0, 0))
    showText(screen,"ASCII:"+str(what_you_pressed[-1]), 24, (10, 330), (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            what_you_pressed.append(event.key)
            if what_you_pressed[-4:] == [pygame.K_d, pygame.K_u, pygame.K_c, pygame.K_k]:
                playSE("duck")
    pygame.display.update()
