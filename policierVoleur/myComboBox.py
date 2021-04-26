from policierVoleur import plateau as plat
from policierVoleur  import fonctions_BDD as bdd
from policierVoleur  import policier as pol
from policierVoleur  import voleurs as vol
import time 
import pygame
from random import randrange  
import random as rnd 
from math import sqrt

# Definir les couleurs du comboBox
inactive = (100, 80, 255)
active = (100, 200, 255)
list_inactive = (255, 100, 100)
list_active = (255, 150, 150)


##
 # * ********************************************************************************************************************
 # * *
 # * * * MyComboBox  : classe qui gère les menus déroulants de la page d'accueil
 # * *
 # *********************************************************************************************************************
 # **/
class MyComboBox():

    #constructeur de comboBox
    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    ##
	# * ********************************************************************************************************************
	# * * * deplacer : fonction qui permet de dessiner le bouton du menu
	# * * * Input   : surface d'affichage
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))

    ##
	# * ********************************************************************************************************************
	# * * * deplacer : fonction qui permet de mettre  jour le bouton du menu
	# * * * Input   : une liste d'événement réalisés par l'utilisateur
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1


