# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('beni.mp3')
pygame.mixer.music.play()
pygame.event.wait()
