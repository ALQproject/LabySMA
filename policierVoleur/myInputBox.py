from policierVoleur import plateau as plat
from policierVoleur  import fonctions_BDD as bdd
from policierVoleur  import policier as pol
from policierVoleur  import voleurs as vol
import time 
import pygame
from random import randrange  
import random as rnd 
from math import sqrt

pygame.init()
inactive = (100, 80, 255)
active = (100, 200, 255)
list_inactive = (255, 100, 100)
list_active = (255, 150, 150)
FONT = pygame.font.Font(None, 32)

##
 # * ********************************************************************************************************************
 # * *
 # * * * MyInputText  : classe qui gère les inputs text de la page d'accueil
 # * *
 # *********************************************************************************************************************
 # **/
class MyInputText:
    #constructeur de input text
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    ##
	# * ********************************************************************************************************************
	# * * * handle_event : fonction qui permet de gérer les événements des utilisateurs qui modifient les inputs text
	# * * * Input   : les événements des utilisateurs
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = active if self.active else inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    ##
	# * ********************************************************************************************************************
	# * * * draw : fonction qui permet de dessiner les inputs text
	# * * * Input   : la surface d'affichage
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)