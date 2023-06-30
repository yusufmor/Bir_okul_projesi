from typing import Any
import pygame
import sys
import os
sys.path.append(os.getcwd() )
print(sys.path)
from Main.Dosya_islemleri import Dosya_düzenleme
import random


class Ses_cal():
    def __init__(self , sarkı_adi ):
        self.Sarki_adi = sarkı_adi
        self.file = Dosya_düzenleme("Sesler" , "mp3" , "ses" , os.getcwd() +os.sep + "Ses_ve_Gorunti" + os.sep)
        self.file()
        pygame.init()
    @property
    def Sarki_adi(self):
        return self.__sarki_adi
    
    @Sarki_adi.setter
    def Sarki_adi(self , value):
        value = str(value)

        if value.isalnum() or value.isdigit():
            raise TypeError("Ne yapıyon be abi")

        self.__sarki_adi = value
    def duzenli_cal(self):
        pygame.mixer.music.load(self.Sarki_adi)
        pygame.mixer.music.play(-1)

    def Kackere_clasin(self , calma_sayisi):
        sarki = pygame.mixer.Sound(self.Sarki_adi)
        sarki.play(calma_sayisi)  

A = Ses_cal(os.getcwd() +os.sep + "Ses_ve_Gorunti" + os.sep + "Sesler" + os.sep + "ses4.mp3")