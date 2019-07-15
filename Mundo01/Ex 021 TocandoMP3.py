'''
    Faca um programa que abra e reproduza um arquivo MP3;
'''
import pygame;

pygame.mixer.init();
pygame.mixer.music.load('./_mp3/Wolf_of_winter.mp3');
pygame.mixer.music.play();
input("Espere terminar a musica,e aperte enter!");