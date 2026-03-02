from Enemigo import *
import random
class Ogro(Enemigo):
    def __init__(self,puntos_energia=20,ataque=3):
        super().__init__(tipo_enemigo='Ogro', punto_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplastar todo!!!")  

    def ataque_especial(sel):
        print("ogrp ataque especial")
        funciona_ataque_especial = random.random() < 0.20
