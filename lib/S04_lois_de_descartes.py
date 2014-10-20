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
for i in range(20):
    down()                  # On pose le stylo
    forward(10)            # et trac� effectif
    up()
    forward(10)

n = 2.0
speed(10)
COLORS = ['red','blue']
color('red')
radians()
for i in range(1,91):
    if i > 80: speed(2)
    if i%10 == 9: color(COLORS[(i//10+1)%2])
    i = pi*i/180
    r = asin(sin(i)/n)
    up()
    goto(-2*R*cos(i),-2*R*sin(i))
    left(i)
    down()
    forward(2*R)
    right(i-r)
    forward(2*R)
    up()
    right(r)

import time

time.sleep(10)



