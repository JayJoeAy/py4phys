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
Programme con�u par Tom Morel (PCSI, lyc�e Jean Jaur�s) pour visualiser 
l'influence de la position du c�t� plat pour la qualit� d'une image. On se 
rend compte que lorsque le c�t� plat est du c�t� o� l'objet/image est au plus 
pr�s (r�gle des 4P), les aberrations g�om�triques sont moins prononc�es. 
Effets de bords int�ressants: 
 * la lentille �tant non-sym�trique, le centre optique n'est pas au milieu 
 (d'o� le d�calage observ� pour le foyer dans les deux positions).
 * dans le 2e cas, certains rayons ne peuvent pas ressortir de la lentille du 
 fait du ph�nom�ne de r�flexion totale.
"""

from math   import *   # Pour les calculs
from turtle import *   # Pour la tortue du LOGO

n = 1.4                # Indice choisi pour le verre
N = 20                 # Nombre de rayons � dessiner
xi= - 400              # Coordonn�e xi de d�part des rayons
yi= 80                 # Coordonn�e relative yi de d�part du premier rayon

R = 100                # Rayon de courbure de la lentille
decal = 1.5*R          # Moiti� du d�calage vertical entre les deux images
ylim = 60              # � partir de quand colorie-t-on les rayons en rouge

# Dessin de la premi�re lentille
up()                   # On l�ve le crayon
goto(xi+2*R,-R+decal)  # Position de d�part en bas � droite
left(90)               # On va vers le haut
down()                 # On pose le crayon
forward(2*R)           # Trac� de la partie plane
left(90)               # On se positionne vers la gauche
circle(R,180)          # et on fait le demi-cercle
up()                   # On l�ve le crayon
goto(xi,decal)         # Pr�paration de l'axe optique
down()                 # On pose le crayon
forward(800)           # et on le trace

# Dessin de la seconde lentille
up()                   # On l�ve le crayon
goto(xi+R,-R-decal)    # Position de d�part en bas � gauche
left(90)               # On va vers le haut
down()                 # On pose le crayon
forward(2*R)           # Trac� de la partie plane
right(90)              # On se positionne vers la droite
circle(-R,180)         # et on fait le demi-cercle
up()                   # On l�ve le crayon
goto(xi,-decal)        # Pr�paration de l'axe optique
right(180)             # Demi-tour droite !
down()                 # On pose le crayon
forward(800)           # et on le trace

radians()              # � partir d'ici, on passe en radians pour les angles

for i in range(N):     # Boucle sur les rayons � tracer
    up()               # On l�ve le crayon
    goto(xi,yi+decal)  # pour se mettre au point de d�part
    down()             # puis on le repose pour commencer le trac�
    alpha=asin(yi/R)   # Angle par rapport � la normale 1�re interface
    beta=asin(yi/(n*R))# Angle de r�fraction 1�re interface air/verre
    xa=-R*cos(alpha)-2*R # L� o� on va toucher la 1�re interface
    if abs(yi)>=ylim:  # On met les rayons extr�mes
        color('red')   # en rouge
    else:              # et les autres
        color('blue')  # en bleu
    goto(xa,yi+decal)  # Allons jusqu'au contact avec la lentille
    # Un petit calcul pour la position du contact avec la 2e interface
    yb=yi+(xa+2*R)*tan(alpha-beta) 
    goto(-2*R,yb+decal)# On y va !
    # Et on calcule l'angle de r�fraction en sortie de cette 2e interaface
    gamma=asin(n*sin(alpha-beta)) 
    right(gamma)       # La tortue �tant toujours horizontale, on tourne de cet angle
    forward(550)       # On avance tout droit
    left(gamma)        # et on se remet � l'horizontale pour le trac� suivant

    up()               # On passe � pr�sent au second sch�ma avec un lev� de crayon
    goto(xi,yi-decal)  # pour se mettre au point de d�part
    down()             # et on repose le crayon.
    alpha=asin(yi/R)   # Angle par rapport � la normale 2�re interface
    xa= R*cos(alpha)-3*R # Contact avec la 2�re interface (la partie plane est sans effet)
    if abs(yi)>=ylim:  # On met les rayons extr�mes
        color('red')   # en rouge
    else:              # et les autres
        color('blue')  # en bleu
    goto(xa,yi-decal)  # On va jusqu'au contact
    try:               # Attention, il est possible qu'il y ait r�flexion totale
        beta=asin(n*yi/R) # si ce calcul �choue...
        right(-alpha+beta)# Si tout va bien, on tourne
        forward(550)      # on avance
        left(-alpha+beta) # et on se remet dans l'axe
    except: pass       # Cas de la r�flexion totale: on ne fait rien de plus
    
    yi=yi-(160/(N-1))      # Passage au rayon suivant.

# L'important est bien s�r de montrer le dessin se construire en direct, mais
# si on veut en conserver une trace, on peut utiliser ce hack:

base_name = 'PNG/S05_gauss_4P'

ts = getscreen()
ts.getcanvas().postscript(file=base_name + ".eps")

import os # Pour pouvoir appeler BBcut et convert
os.system('./BBcut {}.eps'.format(base_name))         # Pour tailler la bounding box
os.system('convert {0}.eps {0}.png'.format(base_name))# Pour convertir en png
        



