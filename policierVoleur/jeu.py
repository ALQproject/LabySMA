from policierVoleur import plateau as plat
from policierVoleur  import fonctions_BDD as bdd
from policierVoleur  import policier as pol
from policierVoleur  import voleurs as vol
import time 
import pygame
from random import randrange  
import random as rnd 
from math import sqrt

# definition des couleurs
white  = (255,255,255)
black  = (0,0,0)
red = (255, 0, 0)

def dist_euc(c1, c2):
	return sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)



class Jeu:

	def __init__(self, nb_policiers, nb_voleurs, nb_axes, vision, nb_cachettes, vitesse, w, h):
		self.nb_policiers = nb_policiers
		self.nb_voleurs = nb_voleurs
		self.nb_axes = nb_axes
		self.vision = vision
		self.nb_cachettes = nb_cachettes
		self.vitesse = vitesse
		self.policiers = []
		self.voleurs = []
		self.w = w
		self.h = h
		

	
	def start(self):
		begin= time.time()
		play = True
		plateau = plat.Plateau(self.w,self.h,20,20,self.nb_cachettes)
		pygame.init ()
		pygame.display.set_mode ( (self.w * 20 + 100, self.h * 20 ))
		screen = pygame.display.get_surface ()
		# creation du plateau 
		plateau.creation_plateau()
		# determination des cachettes
		plateau.set_cachettes()
		# initialisation des policiers
		for i in range(self.nb_policiers):
			self.policiers.append(pol.Policier(plateau))
		for i in range(self.nb_voleurs):
			self.voleurs.append(vol.Voleur(plateau))
		
		while (play == True):
			play = False
			screen.fill (white)
			events = pygame.event.get ()
			plateau.afficher(screen)
			for i in range(self.nb_voleurs):
				if (self.voleurs[i].libre == True):
					play = True
					while True:
						rand = randrange(self.nb_axes)
						isClosed, direction = plateau.get_mur(self.voleurs[i].x, self.voleurs[i].y,rand)
						if not isClosed:
							break
					self.voleurs[i].deplacer(direction)
					self.voleurs[i].afficher(screen)
					
			for i in range(self.nb_policiers):
				for j in range(self.nb_voleurs):
					while True:
						rand = randrange(self.nb_axes)
						isClosed, direction = plateau.get_mur(self.policiers[i].x, self.policiers[i].y,rand)
						if not isClosed:
							break
					if dist_euc(self.policiers[i], self.voleurs[j]) < self.vision:
						if self.policiers[i].x == self.voleurs[j].x:
							if self.policiers[i].y > self.voleurs[j].y:
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_bas == False :
									direction = "bas"
							else :
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_haut == False :
									direction = "haut"
						elif self.voleurs[j].y == self.policiers[i].y:
							if self.policiers[i].x > self.voleurs[j].x:
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_gauche == False :
									direction = "gauche"
							else :
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_droite == False :
									direction = "droite"

						else :
							if self.policiers[i].x > self.voleurs[j].x:
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_gauche == False :
									direction = "gauche"
							else :
								if plateau.cases[self.policiers[i].y * self.w + self.policiers[i].x].mur_droite == False :
									direction = "droite"
				
				self.policiers[i].deplacer(direction)
				self.policiers[i].afficher(screen, self.vision,self.w * 20 + 100, self.h * 20 )
			for i in range(self.nb_voleurs):
				for j in range(self.nb_policiers):
					if (self.voleurs[i].x == self.policiers[j].x and self.voleurs[i].y == self.policiers[j].y and plateau.cases[self.voleurs[i].y * self.w + self.voleurs[i].x].cachette == False):
						self.voleurs[i].libre = False
			time.sleep(self.vitesse)
			pygame.display.flip ()
		duree=time.time()-begin
		#requete="INSERT INTO statistic(nbre_voleurs, nbre_policiers, nbre_axes, vision_policier,vitesse,largeur_plateau,hauteur_plateau,duree) VALUES("+str(self.nb_voleurs)+","+ str(self.nb_policiers)+","+ str(self.nb_axes)+","+ str(self.vision)+","+str(self.vitesse)+","+str(self.w)+","+str(self.h)+","+str(duree)+");"
		#execution_requete(cnx, requete)
			