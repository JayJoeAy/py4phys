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
l'influence de la couleur du rayon incident lors de sa r�fraction � 
l'int�rieur d'une goutte d'eau. Pour all�ger les calculs, on approxime un peu 
les expressions des cordes dans la goutte, mais cela reste parfaitement 
correct au trac�.
'''


from turtle import *   # Pour le dessin � l'�cran
from math import *     # Pour les fonctions math�matiques

def Cauchy(x):
    '''Fonction donnant l'indice du milieu en suivant la loi de Cauchy en 
    fonction de la longueur d'onde x donn�e en m�tres.'''
    A=1.58
    B=171*1e-16
    n=A+(B/x**2)
    return n

# On commence par les d�clarations
R =100          # Rayon du cercle
yi=R/2          # Coordonn�e y du premier rayon
xi=-2*R         # Coordonn�e x du premier rayon
longueur=[400,500,600,700,800]                    # Diff�rentes longueurs d'onde
pal=['purple','blue','dark green','orange','red'] # et les couleurs associ�es
i= asin(yi/R)   # angle d'incidence du premier rayon (en radian)

# On d�marre le dessin
up()            # On l�ve le crayon
goto(0,-R)      # On va au point de coordonn�e (0,-R)
down()          # On pose le crayon
circle(R,360)   # On dessine le cercle
up()            # On rel�ve le crayon
goto(xi,yi)     # On va au point de d�part du rayon lumineux
down()          # On repose le crayon
goto(-sqrt(R*R-yi*yi),yi) # Et on va jusqu'� toucher la goutte d'eau

def imprime_ecran(n):
    """ R�cup�re ce qui est affich� � l'�cran. """
    base_name = 'PNG/S04_arc_en_ciel_turtle'
    getscreen().getcanvas().postscript(file=base_name + "{:02d}.eps".format(n))
    

delay(40)       # On ralentit un peu Speedy Gonzales...
# � pr�sent, on va boucler sur les couleurs que l'on veut repr�senter
for j in range(len(longueur)):
    color(pal[j])               # On change la couleur du trait
    n= Cauchy(longueur[j]*1e-9) # Valeur de l'indice optique en fonction de lambda
    r=asin(sin(i)/n)            # Angle de r�fraction (en radian)
    right((i-r)*180/pi)         # Tourner � droite d'un angle (i-r) en degr�
    forward(190)                # On avance (� peu pr�s) de la distance ad�quate
    right(180-(2*r*180/pi))     # On tourne de pi-2*r � droite
    forward(190)                # On r�avance (� peu pr�s) de la distance ad�quate
    right((i-r)*180/pi)         # M�me configuration qu'� l'aller
    forward(200)                # On sort de la goutte
    up()                        # On rel�ve le crayon
    goto(-sqrt(R*R-yi*yi),yi)   # Et on retourne au point de d�part
    # Ne reste qu'� tourner � l'envers pour se remettre dans l'axe
    left(2*(i-r)*180/pi+180-(2*r*180/pi)) 
    down()                      # et on repose le crayon
    imprime_ecran(j)            # On prends une petite photo pour la route


import time

time.sleep(30)

# L'important est bien s�r de montrer le dessin se construire en direct, mais 
# si on veut en conserver une trace, on peut utiliser ce hack:

base_name = 'PNG/S04_arc_en_ciel_turtle'

ts = getscreen()
ts.getcanvas().postscript(file=base_name + ".eps")

import os # Pour pouvoir appeler BBcut et convert
os.system('./BBcut {}.eps'.format(base_name))         # Pour tailler la bounding box
os.system('convert {0}.eps {0}.png'.format(base_name))# Pour convertir en png



