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




"""

Petite animation turtle pour illustrer les lois de Descartes pour la 
r�fraction. L'id�e est de simuler la "classique" illustration par envoi d'un 
faisceau lumineux sur un h�micylindre de plexiglas et d'observer la direction 
prise par le rayon r�fract�.

On va colorer diff�remment les rayons tous les 10 degr�s pour suivre que le 
"tassement" s'observe principalement lorsque les angles incidents sont presque 
� la perpendiculaire de la normale.

"""


from math import *
from turtle import *

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
right(180)              # Retour dans l'axe
for i in range(20):     # On va tracer la normale en pointill�s
    down()              # On pose le stylo,
    forward(10)         # on avance en tra�ant,
    up()                # on rel�ve le stylo,
    forward(10)         # on avance sans tracer

n = 2.0                 # Indice du plexiglas
speed(10)               # On acc�l�re un peu
COLORS = ['red','blue'] # Les deux couleurs tous les 10� incidents
color('red')            # On commence sur le rouge
radians()               # On passe en radians (pour turtle) pour utiliser sin et cos
for i in range(1,91):   # Un rayon tous les degr�s
    if i > 80: speed(2) # Si on est proche de la fin, on ralentit un peu
    if i%10 == 9: color(COLORS[(i//10+1)%2]) # Changement de couleur
    i = pi*i/180        # Conversion en radians
    r = asin(sin(i)/n)  # Calcul de l'angle r�fract�
    up()                # On soul�ve le stylo pour se placer au bon endroit
    goto(-2*R*cos(i),-2*R*sin(i))
    left(i)             # On prend la bonne direction
    down()              # On pose le stylo
    forward(2*R)        # jusqu'� atteindre l'interface
    right(i-r)          # L�, on est r�fract�
    forward(2*R)        # et on continue notre route
    up()                # On se rel�ve
    right(r)            # et on se remet dans l'axe.


# � la fin, on attend 10s que l'orateur puisse expliquer aux �l�ves.
import time
time.sleep(10)



