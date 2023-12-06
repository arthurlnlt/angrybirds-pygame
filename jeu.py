from catapulte import catapulte
from classes import *


# la classe jeu rassemble les autres classes
class jeu:
    def __init__(self):
        self.catapulte = catapulte()
        self.loup = loup()
        self.loup2 = loup2()
        self.bloc_bois = bloc_bois()
        self.grosse_boule = grosse_boule()
        self.petite_boule = petite_boule()
        self.petit_bout_bois = petit_bout_bois()
        self.rectangle_bois = rectangle_bois()
        self.triangle_bois = triangle_bois()
        self.bloc_bois = bloc_bois()
        self.petit_bout_bois2 = petit_bout_bois2()
        self.petit_bout_bois3 = petit_bout_bois3()
        self.petit_bout_bois4 = petit_bout_bois4()
        self.petit_bout_bois5 = petit_bout_bois5()
        self.rectangle_bois2 = rectangle_bois2()
        self.rectangle_bois3 = rectangle_bois3()
        self.triangle_bois = triangle_bois()
        self.score = 0
