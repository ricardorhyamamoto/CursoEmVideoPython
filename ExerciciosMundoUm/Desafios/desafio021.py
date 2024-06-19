# FAÇA UM PROGRAMA QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3

import pygame

pygame.init()

pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
