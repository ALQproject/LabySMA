from policierVoleur import agent as ag
import pygame
from pygame.locals import *

##
 # * ********************************************************************************************************************
 # * *
 # * * * Voleur  : classe qui gère les attributs et méthodes du voleur et qui hérite de Agent
 # * *
 # *********************************************************************************************************************
 # **/
class Voleur(ag.Agent):
	#constructeur de voleur
	def __init__(self, plateau):
		ag.Agent.__init__(self, plateau)
		self.libre = True
	

	##
	# * ********************************************************************************************************************
	# * * * affihcer : fonction qui permet d'afficher un voleur
	# * * * Input   : surface de déplacement
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/		
	def afficher(self,surface):
		path = "icons/voleur.png"
		# importer l'image
		image = pygame.image.load(path).convert()
		# redimensionner l'image
		image = pygame.transform.smoothscale(image, (self.plateau.wc-2, self.plateau.hc-2)) 
		# affichage de l'image dans l'ecran
		surface.blit(image,(self.x*self.plateau.wc+2, self.y*self.plateau.hc+2))
