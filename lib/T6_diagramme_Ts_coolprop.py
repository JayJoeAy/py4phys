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
Fabrication d'un diagramme (T,s) avec les iso-choses ad�quates.
"""

import numpy as np               # Les outils math�matiques
import CoolProp.CoolProp as CP   # Les outils thermodynamiques
import CoolProp.Plots as CPP     # Les outils thermographiques
import matplotlib.pyplot as plt  # Les outils graphiques

print(CP.FluidsList())           # Pour regarder les fluides disponibles
fluide= 'Water'                  # Le choix du fluide
iso_P = True                     # Veut-on des isobares ?
iso_x = True                     # et les isotitres ?
iso_h = True                     # et les isenthalpiques ?
iso_v = True                     # et les isochores ?

Ttriple = CP.PropsSI(fluide,'Ttriple')  # Valeur de la temp�rature au point triple
Tcrit = CP.PropsSI(fluide,'Tcrit')      # et au point critique

# Donn�es pour les isotitres
val_x = np.linspace(0.1,0.9,9)          # Les valeurs des isotitres

# Donn�es pour les isenthalpiques
dh = 100e3
htriple_x0 = CP.PropsSI('H','Q',0,'T',Ttriple,fluide) # Entropie triple � gauche
htriple_x1 = CP.PropsSI('H','Q',1,'T',Ttriple,fluide) # Entropie triple � droite
val_h = np.arange(3*dh,htriple_x1*1.4,dh)       # Valeurs � tracer
#s_to_show = list(range(2,len(val_s),2))               # et � afficher
h_to_show = None

# Donn�es pour les isochores (r�parties de mani�re logarithmique par d�faut)
vcrit = 1/CP.PropsSI(fluide,'rhocrit')                 # Volume massique critique
exp_min = int(np.floor(np.log10(vcrit)))+1             # Puissance de 10 proche
vtriple_x1 = 1/CP.PropsSI('D','Q',1,'T',Ttriple,fluide)# Point triple � droite
exp_max = int(np.ceil(np.log10(vtriple_x1)))-1         # Puissance de 10 proche
# Les valeurs � prendre
val_v = [a * 10**b for a in [1,2,5] for b in range(exp_min,exp_max+1)]
v_to_show = None                                       # On les affiche toutes.

# Donn�es pour les isobares (r�parties de mani�re logarithmique par d�faut)
Pcrit = CP.PropsSI(fluide,'pcrit')                 # Pression critique
exp_max = int(np.floor(np.log10(Pcrit)))+1         # Puissance de 10 proche
Ptriple= 1/CP.PropsSI(fluide,'ptriple')            # Point triple 
exp_min = int(np.ceil(np.log10(Ptriple)))+5          # Puissance de 10 
# Les valeurs � prendre
val_P = [a * 10**b for b in range(exp_min,exp_max+1) for a in [1,2,5]]
P_to_show = None                                   # On les affiche toutes.

# Quelques constantes
UNITS = {'T':'K','Q':'', 'S':'kJ/K/kg','V':'m$^3$/kg','P':'bar','H':'kJ/kg' }
LABEL = {'T':'T','Q':'x','S':'s',      'V':'v',       'P':'P',  'H':'h'}
COLOR_MAP = {'T': 'Darkred',
             'P': 'DarkCyan',
             'H': 'DarkGreen',
             'V': 'DarkBlue',
             'S': 'DarkOrange',   
             'Q': 'black'}

# On pr�pare un format pour impression sur A3 ou presque (dimensions en pouces)
plt.figure(figsize=(30,21))

def place_label(x,y,label,indice=None,cotan=False,color='k'):
    """ Routine qui se d�brouille pour mettre un label semi-transparent au 
    niveau de la courbe donn�es par ses coordonn�es x et y. Si on sait que le 
    label sera presque vertical avec possibilit� de d�passer 90�, on peut 
    utiliser cotan=True pour corriger (consid�ration purement esth�tique). 
    'indice' correspond � la position dans les tableaux x et y o� devra 
    s'afficher le label demand�. """
    print(x[0],y[0],label) # un peu de feedback pour savoir ce qu'on calcule
    N = len(x)//2          # Emplacement par d�faut
    if indice: N=indice    # sauf si l'utilisateur impose la valeur
    xi,xf = plt.xlim()     # Les limites en x du graphe
    yi,yf = plt.ylim()     # Pareil en y
    Xsize = xf - xi        # La largeur
    Ysize = yf - yi        # La hauteur puis la pente
    a = (y[N+1]-y[N-1])/(x[N+1]-x[N-1]) * Xsize/Ysize
    bbox = plt.gca().get_window_extent() # R�cup�ration de la taille de la figure
    a *= bbox.height / bbox.width        # Correction de la pente avec la taille 
    rot = np.degrees(np.arctan(a))       # Calcul de l'angle de rotation
    if cotan and rot < 0: rot = 180 + rot             # Si on d�passe la     verticale
    if cotan : rot = 90 - np.degrees(np.arctan(1/a))
    t = plt.text(x[N],y[N],label,        # On met le texte au bon endroit
    ha='center',va='center',color=color,rotation = rot) # Avec la bonne rotation
    # On se d�brouille pour que la "bo�te" d'�criture soit semi-transparente
    t.set_bbox(dict(facecolor='w',edgecolor='None',alpha=0.8))

def fait_isolignes(type,valeurs,position=None,nb_points=1000,to_show=None,round_nb = 0 ):
    """ S'occupe du calcul et du trac� des isolignes. """
    if not(to_show):                        # Valeurs par d�fauts:
        to_show = list(range(len(valeurs))) # toutes !
    Tmin,Tmax = plt.ylim()                  # On regarde les 
    smin,smax = plt.xlim()                  # limites du graphique
    # Par d�faut, l'�chantillonnage en T est lin�aire
    val_T = np.linspace(Tmin,Tmax,nb_points)
    # Pour chacune des valeurs demand�es, 
    nb_points_save = nb_points
    for val,i in zip(valeurs,range(len(valeurs))):
        nb_points = nb_points_save
        if type == 'V':  # Cas particulier des volumes massiques: D = 1/v
            val_s = CP.PropsSI('S','T',val_T,'D',1/val,fluide)  # et non en P
        elif type == 'H':
            val_s = np.linspace(smin,smax,nb_points)
            val_T = []
            for s in val_s:
                try:
                    val_T.append(CP.PropsSI('T','S',s,type,val,fluide))
                except: val_T.append(float("Nan"))
            val_T = np.array(val_T)
            val_s = val_s[val_T == val_T]
            val_T = val_T[val_T == val_T]
            nb_points = len(val_T)
            print(nb_points,"points valides sur l'isenthalpique")
            if nb_points < 10: continue
        else:            # Sinon, on utilise l'�ventail des temp�ratures
            val_s = CP.PropsSI('S','T',val_T,type,val,fluide)
        if type == 'H': val /= 1e3 # Pour mettre en kJ/kg
        if type == 'P': val /= 1e5 # Pour mettre en bar
        if round_nb >0 : val = str(round(val,round_nb)) # Pour faire joli
        else: val = str(int(round(val)))                # l� aussi...
        label = '${}={}$ {}'.format(LABEL[type],val,UNITS[type])
        if nb_points > 10:
            plt.plot(val_s,val_T,color=COLOR_MAP[type])     # Affichage courbe
            if i in to_show: # Ainsi que du label s'il fait partie de la liste
                place_label(val_s,val_T,label,int(position*nb_points))

# Le programme proprement dit commence ici.

Ts_plot = CPP.PropsPlot(fluide,'Ts')   # On demande gentiment le plot de base

if iso_x: # Les lignes isotitres sont un peu sp�ciales, donc ont leur code propre
    Ts_plot.draw_isolines('Q',val_x)   # Trac� des lignes isotitres
    # R�cup�ration de la liste des isotitres.
    isoQ = CPP.Plots.IsoLines(fluide,'Ts','Q').get_isolines(val_x)
    for line in isoQ:                  # Rajout des label
        label = line['label'] + line['unit']
        x,y = line['x'],line['y']
        place_label(x,y,label,indice=4*len(x)//5,cotan=True)
else: # On trace tout de m�me quelque chose (de d�j� pr�sent) pour s'assurer
    Ts_plot.draw_isolines('Q',[0,1],num=2)# une bonne s�lection des bornes
    

# Ici, on fait toutes les autres isolignes (le boulot a �t� fait plus haut)
if iso_P: fait_isolignes('P',val_P,position=0.8,to_show=P_to_show,round_nb=3)
if iso_h: fait_isolignes('H',val_h,position=0.8,to_show=h_to_show,round_nb=3)
if iso_v: fait_isolignes('V',val_v,position=0.25,to_show=v_to_show,round_nb=3)

plt.grid(which='both') # Rajout de la grille
Ts_plot._draw_graph()  # On oblige le dessin avant la sauvegarde
plt.savefig('PNG/T6_diagramme_Ts_coolprop_{}.png'.format(fluide))



