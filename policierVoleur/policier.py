from policierVoleur import agent as ag
import pygame 

##
 # * ********************************************************************************************************************
 # * *
 # * * * Policier  : classe qui gère les attributs et méthodes du policier qui hérite de Agent
 # * *
 # *********************************************************************************************************************
 # **/
class Policier(ag.Agent):
	def __init__(self, plateau):
		ag.Agent.__init__(self, plateau)
	
	##
	# * ********************************************************************************************************************
	# * * * affihcer : fonction qui permet d'afficher un policier
	# * * * Input   : surface de déplacement, rayon de vision du policier, longueur et largeur du plateau
	# * * * Output  : vide
	# * 
	# *********************************************************************************************************************
	# **/	
	def afficher(self,surface,vision, w, h):
		path = "icons/policier.png"
		# importer l'image
		image = pygame.image.load(path).convert()
		# redimensionner l'image
		image = pygame.transform.smoothscale(image, (self.plateau.wc-2, self.plateau.hc-2)) 
		# affichage de l'image dans l'ecran
		surface.blit(image,(self.x*self.plateau.wc+2, self.y*self.plateau.hc+2))
		# affichage de la vision
		surface1 = pygame.Surface((w,h))
		surface1.set_colorkey((0,0,0))
		# pour la transparence
		surface1.set_alpha(50)
		pygame.draw.circle(surface1, (0,255,0), (self.x*self.plateau.wc+self.plateau.wc/2+2, self.y*self.plateau.hc+self.plateau.wc/2+2), vision)
		surface.blit(surface1, (0, 0))

