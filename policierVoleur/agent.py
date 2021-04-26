from  random import  choice

# definition de la classe Agent
class Agent:
	# constructeur de l'agent
	def __init__ (self,plateau):
		# la position de la case ou se trouve l'agent
		self.x = random.randint(0,plateau.w-1)
		self.y = random.randint(0,plateau.h-1)
		self.plateau = plateau

		
	#  deplacement de l'agent
	def deplacer(self,dir) :	
		if dir == "droite"  :
			if self.x+1 < self.plateau.w and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_droite:
				self.x += 1
			else :
				self.x = 0
		if dir == "gauche" :
			if self.x-1 >=0 and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_gauche:
				self.x -= 1
			else :
				self.x = self.plateau.w - 1
		if dir == "haut" :
			if self.y-1 >=0 and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_haut:
				self.y -= 1
			else :
				self.y = self.plateau.h - 1
		if dir == "bas":	
			if self.y+1 < self.plateau.h  and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_bas:
				self.y += 1
			else :
				self.y = 0
		if dir == "hdroite" :
			if self.x+1 < self.plateau.w and self.y-1 >= 0 and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_hdroite:
				self.x += 1
				self.y -= 1
			elif self.y == 0:
				self.x = 0
				self.y = self.plateau.h - 1
			else :
				self.x = 0
				self.y = self.y - 1
		if dir == "bdroite" :
			if self.x+1 < self.plateau.w and self.y+1 < self.plateau.h and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_bdroite:
				self.x += 1
				self.y += 1
			elif self.y == self.plateau.h - 1:
				self.x = 0
				self.y = 0
			else :
				self.x = 0
				self.y = self.y + 1
		if dir == "hgauche"  :
			if self.x-1 >= 0 and self.y-1 >= 0 and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_hgauche:
				self.x -= 1
				self.y -= 1
			elif self.y == 0:
				self.x = self.plateau.w - 1
				self.y = self.plateau.h - 1
			else :
				self.x = self.plateau.w - 1
				self.y = self.y - 1
			
		if dir == "bgauche" :
			if self.x-1 >= 0 and self.y+1 < self.plateau.h and not self.plateau.cases[self.x +  self.y * self.plateau.w].mur_bgauche:
				self.x -= 1
				self.y += 1
			elif self.y == self.plateau.h - 1:
				self.x = self.plateau.w - 1
				self.y = self.plateau.h - 1
			else :
				self.x = self.plateau.w - 1
				self.y = self.y + 1