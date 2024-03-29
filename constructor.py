# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:17:34 2023

@author: pepit
"""

import os
import pygame

ruta_principal = "C:\\Users\\pepit\\Desktop\\scidata\\Fun_Py_23-main\\juego_dbz"
os.chdir(ruta_principal)
from peleador import *


#%%

pygame.init()


'''crear ventana del juego'''

VENTANA_ANCHO = 1200
VENTANA_ALTO = 600

ventana = pygame.display.set_mode((VENTANA_ANCHO,VENTANA_ALTO))
pygame.display.set_caption("Dragon Ball Z de SciData")

'''Configurar frames por segundo'''
reloj = pygame.time.Clock()
FPS = 60

'''Cargar el escenario'''
escenario_imagen = pygame.image.load("C:\\Users\\pepit\Desktop\\scidata\\Fun_Py_23-main\\juego_dbz\\activos\\imagenes\\fondos\\torneo.png")

def dibujar_escenario():
    escenario_escalado = pygame.transform.scale(escenario_imagen,(VENTANA_ANCHO,VENTANA_ALTO))
    ventana.blit(escenario_escalado,(0,0))

'''Crear dos instancias de la clase Peleador'''
    
peleador1 = Peleador(200,330)
peleador2 = Peleador(900,330)   
    
run = True
while run:
    reloj.tick(FPS)   
    
    
    '''dibujar el escenario'''
    dibujar_escenario()
    
    '''dibujar peleadores'''
    peleador1.dibujar(ventana)
    peleador2.dibujar(ventana)

    '''mover jugadores'''
    peleador1.movimientos(VENTANA_ANCHO,VENTANA_ALTO)
#    peleador2.movimientos(VENTANA_ANCHO)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    '''actualizar pantalla'''
    pygame.display.update()
    
pygame.quit()
#"C:\\Users\\pepit\Desktop\\scidata\\Fun_Py_23-main\\juego_dbz\\activos\\imagenes\\fondos\\torneo.png"
#%%