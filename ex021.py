#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Tinyfolk.mp3')
pygame.mixer.music.play()
input('Agora você escuta?')
