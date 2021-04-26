# definition de la classe case
class Case:
	def __init__(self):
		self.state = False
		# les murs
		self.mur_droite = True
		self.mur_gauche = True 
		self.mur_haut = True 
		self.mur_bas = True
		self.mur_hdroite = True		# mur en haut à droite
		self.mur_bdroite = True		# mur en bas à droite
		self.mur_hgauche = True		# mur en haut à droite
		self.mur_bgauche = True		# mur en bas à droite
		# cachette
		self.cachette = False