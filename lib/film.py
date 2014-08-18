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
Module pour g�n�rer simplement un petit film � partir d'une s�rie de fichiers 
png et �viter de recopier le m�me code de script en script pour ce faire...
"""

def make_film(base_name,out_file=None,resize="600x600",PNM='PNM'):
    """ 
    Fabrique un film automatiquement � partir des fichiers png commen�ant pas 
    'base_name' � l'aide de convert puis de ppmtoy4m et mpeg2enc (paquet 
    mjpegtools � installer sur la machine). Si 'out_file' n'est pas renseign�, 
    le film sera �crit dans le fichier base_name+'_film.mpeg'. Enfin, il peut 
    arriver que convert se plaigne d'histoires de taille: il faut alors 
    simplement jouer sur le 'resize' jusqu'� trouver une combinaison qui lui 
    plaise (a priori dans les m�mes proportions que la figure initiale).
    Pour le cas des figures monochromes, il faut visiblement sp�cifier 
    PNM='PPM' pour que cela fonctionne correctement.
    """
    if not(out_file): out_file = base_name + '_film.mpeg'
    
    import os
    
    cmd = '(for f in ' + base_name + '*png ; '
    cmd+= 'do convert -density 100x100 $f -depth 8 -resize {} {}:- ; done)'.format(resize,PNM)
    cmd+= ' | ppmtoy4m -S 420mpeg2'
    cmd+= ' |  mpeg2enc -f1 -b 12000 -q7 -G 30 -o {}'.format(out_file)
    
    print("Execution de la commande de conversion")
    print(cmd)
    os.system(cmd)
    print("Fin de la commande de conversion")



