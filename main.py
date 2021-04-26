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



time_perso = 60 # temps en ms avant chaque test du clavier pour les touches qui concernent le perso



if __name__ == "__main__":
	#cnx = bdd.connectionBDD("localhost", "root", "","policierVoleur")
	jeu = j.Jeu(8, 1, 8, 50, 15, 0.8 , 8, 5)
	jeu.start()