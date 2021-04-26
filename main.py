from  random import randint , choice
import pygame
from pygame.locals import *
from math import sqrt
from random import randrange  
import random as rnd 	
import time	
from datetime import datetime
# import mysql.connector
# from mysql.connector import Error
from policierVoleur import fonctions_BDD as bdd
from policierVoleur import jeu as j
from policierVoleur import myComboBox as combo
from policierVoleur import myInputBox as inputText
from policierVoleur import plateau as plat


# Définition  des couleurs
white  = (255,255,255)
black  = (0,0,0)
red = (255, 0, 0)
color_light = (170,170,170)
color_dark = (100,100,100)
inactive = (100, 80, 255)
active = (100, 200, 255)
list_inactive = (255, 100, 100)
list_active = (255, 150, 150)


# Fonction main
if __name__ == "__main__":

	# Établissement de la connexion avec la base de données
	#cnx = bdd.connectionBDD("localhost", "root", "","policierVoleur")

	# initialisation de pygame
	pygame.init ()
	clock = pygame.time.Clock()
	pygame.display.set_mode ( (1000 , 600 ))
	screen = pygame.display.get_surface ()

	# configuration élémentaires
	width = screen.get_width()
	height = screen.get_height()

	# Configuration du style des boutons et des inputs texts
	smallfont = pygame.font.SysFont('Corbel',35)
	smallerfont = pygame.font.SysFont('arial',14)

	label_start = smallfont.render('Start' , True , white)
	label_voleurs = smallfont.render('Nombre de voleurs' , True , black)
	label_policier = smallfont.render('Nombre de policiers' , True , black)
	label_cachettes = smallfont.render('Nombre de cachettes' , True , black)
	label_vision = smallfont.render('Rayon de vision' , True , black)
	label_longueur = smallfont.render('Longeur du labyrinthe' , True , black)
	label_largeur = smallfont.render('Largeur du labyrinthe' , True , black)
	label_info1 = smallerfont.render('Si une des valeurs ci-dessus n\'est pas saisie ou invalide, la valeur par defaut sera prise' , True , black)
	label_info2 = smallerfont.render('Policiers: 4, Voleurs = 4, Axes = 4, Vision = 30, Cachettes = 4, Vitesse = 0.8 Largeur = 20, Longeur = 10' , True , black)
	
	
	# creation du combobox de vitesse
	listVitesse = combo.MyComboBox(
		[inactive, active],
		[list_inactive, list_active],
		200,290, 140, 32, 
		pygame.font.SysFont(None, 30), 
		"Vitesse", ["0.1", "0.5", "0.9"])

	# creation du combobox d'axe
	listAxes = combo.MyComboBox(
		[inactive, active],
		[list_inactive, list_active],
		600, 290, 140, 32,
		pygame.font.SysFont(None, 30), 
		"Axe", ["4", "8"])

	# creation de input text de cachette
	input_cachette = inputText.MyInputText(850,210, 50, 30)
	# creation de input text de nombre de voleurs
	input_voleurs = inputText.MyInputText(850,50, 50, 30)
	# creation de input text de nombre de policiers
	input_policier = inputText.MyInputText(350, 50, 50, 30)
	# creation de input text du rayon de vision
	input_vision = inputText.MyInputText(350,210, 50, 30)
	# creation de input text de la longueur
	input_longueur = inputText.MyInputText(350,130, 50, 30)
	# creation de input text de la largeur
	input_largeur = inputText.MyInputText(850,130, 50, 30)
	input_boxes = [input_cachette, input_voleurs, input_policier, input_vision, input_longueur, input_largeur]
	
	#Entrées de l'utilisateurs
	users_input = [0,0,0,0,0,0,0,0]

	while (True):
		
		clock.tick(30)
		event_list = pygame.event.get()
		
		# Traitement du menu déroulan de vitesse 
		selected_option = listVitesse.update(event_list)
		if selected_option >= 0:
			listVitesse.main = listVitesse.options[selected_option]
			users_input[6] = float(listVitesse.options[selected_option])

		# Traitement du menu déroulan des axes 
		selected_option = listAxes.update(event_list)
		if selected_option >= 0:
			listAxes.main = listAxes.options[selected_option]
			users_input[7] = int(listAxes.options[selected_option])


		# Traitement du bouton Start
		for event in event_list:
			for box in input_boxes:
				box.handle_event(event)

			if event.type == pygame.QUIT:
				pygame.quit()
			
			# Surveiller la souris
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				# Si le bouton est cliqué, les valeurs des inputs sont lues et le jeu est lancé 
				if 430 <= mouse[0] <= 570 and 400 <= mouse[1] <= 440:
					for i in range(6):
						if input_boxes[i].text.isnumeric and input_boxes[i].text:
							users_input[i] = int(input_boxes[i].text)
					jeu = j.Jeu()
					if users_input[0]!= 0:
						jeu.nb_cachettes = users_input[0]
					if users_input[1]!= 0:
						jeu.nb_voleurs = users_input[1]
					if users_input[2]!= 0:
						jeu.nb_policiers = users_input[2]
					if users_input[3]!= 0:
						jeu.vision = users_input[3]
					if users_input[4]!= 0:
						jeu.h = users_input[4]
					if users_input[5]!= 0:
						jeu.w = users_input[5]
					if users_input[6]!=0:
						jeu.vitesse = users_input[6]
					if users_input[7]!=0:
						jeu.nb_axes = users_input[7]
					jeu.start()

	
		# Remplissage du plateau (Arrière plan)
		screen.fill (white)


		# Sauvegarde la position de la souris
		mouse = pygame.mouse.get_pos()
		
		# Si la souris pointe sur le bouton, sa couleur change
		if 430 <= mouse[0] <= 570 and 400 <= mouse[1] <= 440:
			pygame.draw.rect(screen,color_light,[430,400,140,40])
			
		else:
			pygame.draw.rect(screen,color_dark,[430,400,140,40])


	
		# Determination des dimensions des Labels
		screen.blit(label_start , (470,407))
		screen.blit(label_voleurs , (550,50))
		screen.blit(label_policier , (50,50))
		screen.blit(label_cachettes , (550,210))
		screen.blit(label_vision , (50,210))
		screen.blit(label_longueur , (50,130))
		screen.blit(label_largeur , (550,130))
		screen.blit(label_info1, (250, 500))
		screen.blit(label_info2,(200, 520))

		# Affichage des inputs text
		for box in input_boxes:
		 	box.draw(screen)
		
		# Affichage des menus déroulant
		listVitesse.draw(screen)
		listAxes.draw(screen)


		pygame.display.flip ()

		