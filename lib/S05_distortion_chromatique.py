# coding: latin1

# Sauf mention explicite du contraire par la suite, ce travail a �t� fait par 
# Jean-Julien Fleck, professeur de physique/IPT en PCSI1 au lyc�e Kl�ber. 
# Vous �tes libres de le r�utiliser et de le modifier selon vos besoins.
# 
# Si l'encodage vous pose probl�me, vous pouvez r�encoder le fichier � l'aide 
# de la commande
# 
# recode l1..utf8 monfichier.py
# 
# Il faudra alors modifier la premi�re ligne en # coding: utf8
# pour que Python s'y retrouve.





'''
Programme con�u par Tom Morel (PCSI, lyc�e Jean Jaur�s) pour visualiser
l'influence de la couleur du rayon incident sur la distance focale d'une
lentille sph�rique
'''

from math import *      # Pour les fonctions math�matiques
from turtle import *    # Pour les dessins � l'�cran (appel� apr�s math pour radians())


def Cauchy(x):
    '''Fonction donnant l'indice du milieu en suivant la loi de Cauchy en
    fonction de la longueur d'onde x donn�e en m�tres.'''
    A=1.2
    B=171*1e-16
    n=A+(B/x**2)
    return n

N= 10                   # nombre de rayons � dessiner
xi= - 200               # coordonn�e xi de d�part
yi= -50                 # coordonn�e yi de d�part
longueur=[400,800]      # diff�rentes longueurs d'onde
pal=['blue','red']      # et les couleurs associ�es
R = 100                 # Le rayon de courbure de la lentille

up()                    # On soul�ve le crayon
goto(0,R)               # On va en haut � gauche de la lentille
right(90)               # On tourne pour commencer � descendre
down()                  # On pose le crayon
forward(2*R)            # On dessine le c�t� plat de la lentille
left(90)                # On se remet dans l'axe
circle(R,180)           # On trace le cercle sur 180 degr�s
up()                    # On soul�ve
goto(-200,0)            # Pour aller tracer l'axe optique
down()                  # On pose le stylo
right(180)              # Retour dans l'axe
forward(800)            # et trac� effectif

radians()               # On passe les angles en radians.

for j in range(len(longueur)): # On boucle sur les couleurs
    color(pal[j])              # S�lection de la couleur
    n=Cauchy(longueur[j]*1e-9) # On r�cup�re l'indice optique
    yi=-R/2                    # Ordonn�e initiale
    for i in range(N):         # On boucle sur les rayons � dessiner
        up()                   # On l�ve le crayon
        goto(-200,yi)          # On se place
        down()                 # et c'est parti !
        goto(sqrt(100**2-yi**2),yi) # On traverse jusqu'� la face sph�rique
        alpha=asin(yi/100)     # Angle d'incidence sur la face de sortie
        theta=asin(n*yi/100)   # Angle apr�s r�fraction dans l'air
        right(theta-alpha)     # On tourne de l'angle de d�viation
        forward(450)           # On compl�te le trac�
        left(theta-alpha)      # et on se remet dans l'axe
        yi=yi+(R/N)            # D�finition de la prochaine ordonn�e

# L'important est bien s�r de montrer le dessin se construire en direct, mais
# si on veut en conserver une trace, on peut utiliser ce hack:

base_name = 'PNG/S05_distortion_chromatique'

ts = getscreen()
ts.getcanvas().postscript(file=base_name + ".eps")

import os # Pour pouvoir appeler BBcut et convert
os.system('./BBcut {}.eps'.format(base_name))         # Pour tailler la bounding box
os.system('convert {0}.eps {0}.png'.format(base_name))# Pour convertir en png




