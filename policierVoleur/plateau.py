from policierVoleur import case as c
from  random import randint , choice
import random as rnd 
import pygame

# definition des couleurs
white  = (255,255,255)
black  = (0,0,0)
red = (255, 0, 0)

##
 # * ********************************************************************************************************************
 # * *
 # * * * PLateau  : classe qui gère le plateau où se déroule le jeu
 # * *
 # *********************************************************************************************************************
 # **/
class Plateau:
	# constructeur du plateau
	def __init__ (self,w,h,wc,hc, nb_cachettes):
		# nombre de cases verticales
		self.w = w
		# nombre de cases horizontales
		self.h = h
		# les cases qui constitue le plateau
		self.cases = []
		# la largeur d'une case
		self.wc = wc
		# la hauteur d'une case
		self.hc = hc
		# le nombre de cachettes
		self.nb_cachettes = nb_cachettes
		# initialisation du plateau
		for i in range(0,self.w):
			for j in range(0,self.h):
				case = c.Case()
				case.x = i
				case.y = j
				self.cases+=[case]

	##
	# * ********************************************************************************************************************
	# * * * set_cachettes : fonction qui permet de définir les cachettes où le voleur ets invisible
	# * * * Input   : instance courante
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/ 
	def set_cachettes(self):
		for i in range(self.nb_cachettes):
			rand_x = rnd.randrange(0,self.w)
			rand_y = rnd.randrange(0,self.h)
			self.cases[rand_y * self.w + rand_x].cachette = True
			

		
	##
	# * ********************************************************************************************************************
	# * * * creation_plateau : fonction qui permet de générer le labyrinthe où se déroule le jeu
	# * * * Input   : les coordonnées de départ
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
	def creation_plateau(self,x=-1,y=-1):
		if x==-1:
			x = rnd.randint(0,self.w-1)
			y = rnd.randint(0,self.h-1)
		cell_act = self.cases[x +  y * self.w]
		if not cell_act.state :
			cell_act.state = True
			tab = []
			if x+1<self.w and not self.cases[x+1 +  y * self.w].state : tab.append((x+1,y,"mur_droite"))
			if x-1>=0  and not self.cases[x-1 +  y * self.w].state    : tab.append((x-1,y,"mur_gauche"))
			if y-1>=0  and not self.cases[x +  (y-1) * self.w].state   : tab.append((x  ,y-1,"mur_haut"))
			if y+1<self.h and not self.cases[x +  (y+1) * self.w].state : tab.append((x  ,y+1,"mur_bas"))
			if tab:	
				while tab:
					C = choice (tab)
					if not self.cases[C[0] +  C[1] * self.w].state:
						cell = self.cases[C[0] +  C[1] * self.w]
						if C[2]=="mur_droite" :
							cell.mur_gauche=False
							cell_act.mur_droite=False
						if C[2]=="mur_gauche" :
							cell.mur_droite=False
							cell_act.mur_gauche=False
						if C[2]=="mur_haut" :
							cell.mur_bas=False
							cell_act.mur_haut=False
						if C[2]=="mur_bas" :
							cell.mur_haut=False
							cell_act.mur_bas=False
						self.creation_plateau(C[0] , C[1])

						# Maintenant on traite les axes en diagonale
						if C[0]+1 < self.w and self.cases[C[0]+1 + C[1] * self.w].state and not cell.mur_droite :
							if not self.cases[C[0]+1 + C[1] * self.w].mur_haut:
								cell.mur_hdroite = False
							if not self.cases[C[0]+1 + C[1]* self.w].mur_bas:
								cell.mur_bdroite = False
						if C[0]-1 >=0 and self.cases[C[0]-1 + C[1] * self.w].state and not cell.mur_gauche :
								if not self.cases[C[0]-1+C[1]*self.w].mur_haut:
									cell.mur_hgauche = False
								if not self.cases[C[0]-1+C[1]*self.w].mur_bas:
									cell.mur_bgauche = False
						if C[1]-1 >=0 and self.cases[C[0] + (C[1]-1)*self.w].state and not cell.mur_haut :
								if not self.cases[C[0]+(C[1]-1)*self.w].mur_droite and cell.mur_hdroite:
									cell.mur_hdroite = False
								if not self.cases[C[0]+(C[1]-1)*self.w].mur_gauche and cell.mur_hgauche:
									cell.mur_hgauche = False
						if C[1]+1 < self.h and self.cases[C[0] + (C[1]+1)*self.w].state and not cell.mur_bas :
								if not self.cases[C[0]+(C[1]+1)*self.w].mur_droite and cell.mur_bdroite:
									cell.mur_bdroite = False
								if not self.cases[C[0]+(C[1]+1)*self.w].mur_gauche and cell.mur_bgauche:
									cell.mur_bgauche = False
					tab.remove (C)
				return True
			else : 
				return False
		
		
	##
	# * ********************************************************************************************************************
	# * * * afficher : fonction qui permet d'afficher le labyrinthe généré
	# * * * Input   : string déterminant la direction de déplacement
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/
	def afficher(self,surface):
		# dessiner les limites du plateau
		pygame.draw.rect (surface , black , (0 , 0 , self.wc * self.w , self.hc * self.h),2)
		# dessiner les murs de chaque case
		for y in range(0,self.h):
			for x in range(0,self.w-1):
				case = self.cases[x + y * self.w]
				if case.mur_droite :
					pygame.draw.line (surface , black , ((x+1)*self.wc,y*self.hc) , ((x+1)*self.wc,(y+1)*self.hc))
				if case.mur_bas :
					pygame.draw.line (surface , black , (x*self.wc,(y+1)*self.hc) , ((x+1)*self.wc,(y+1)*self.hc))
				if case.mur_gauche :
					pygame.draw.line (surface , black , (x*self.wc,y*self.hc) , (x*self.wc,(y+1)*self.hc))
				if case.mur_haut :
					pygame.draw.line (surface , black , (x*self.wc,y*self.hc) , ((x+1)*self.wc,y*self.hc))	
				if case.cachette == True:
					#pygame.draw.rect(surface, red,(37 * self.wc , 19 * self.hc, self.wc, self.hc))
					pygame.draw.rect(surface, red,(case.x * self.wc , case.y * self.hc, self.wc, self.hc))

	##
	# * ********************************************************************************************************************
	# * * * get_mur : fonction qui permet de retourner le mur selon les coordonnées de la case et le numéro du mur
	# * * * Input   : coordonnées, numéro du mur
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/			
	def get_mur(self, x, y, num):
		if num == 0:
			return self.cases[x + y * self.w].mur_droite, "droite"
		if num == 1:
			return self.cases[x + y * self.w].mur_gauche, "gauche"
		if num == 2:
			return self.cases[x + y * self.w].mur_haut, "haut"
		if num == 3:
			return self.cases[x + y * self.w].mur_bas, "bas"
		if num == 4:
			return self.cases[x + y * self.w].mur_hdroite, "hdroite"
		if num == 5:
			return self.cases[x + y * self.w].mur_bdroite, "bdroite"
		if num == 6:
			return self.cases[x + y * self.w].mur_hgauche, "hgauche"
		if num == 7:
			return self.cases[x + y * self.w].mur_bgauche, "bgauche"