py4phys
-------

Projet pour rassembler l'ensemble des programmes Python qui peuvent �tre 
utiles pour illustrer le cours de physique de CPGE.

## Organisation

* Le fichier py4phys.pdf rassemble les codes et les graphiques qui en sont issus. 
* Le r�pertoire lib/ rassemble les fichiers .py pr�ts � �tre utilis�s.
* Vous trouverez aussi quelques animations sur la page 
http://pcsi.kleber.free.fr/IPT/py4phys.html

## Roadmap

Pour le moment, j'essaie de rassembler toutes les id�es concernant le cours de 
physique de PCSI, plus quelques illustrations annexes que j'ai toujours voulu 
mettre en oeuvre (comme l'exploration des zones chaotiques de la rotation 
d'Hyp�rion autour de Saturne).

## Description succincte des fichiers

### Bloc Induction
* I1_lignes_champ_magnetique.py: Code �crit par Sylvain Condamin (adapt� d'un 
code de Thierry Pr�) pour simuler les lignes de champ magn�tique autour de 
divers objets (fil infini, dip�le magn�tique ou spire)
* I2_champ_tournant_diphase.py (non encore �crit): Fabrique une petite 
animation pour illustrer la notion de champ tournant � partir de deux bobines 
en quadrature de phase.
* I2_champ_tournant_triphase.py (non encore �crit): Comme le pr�c�dent, mais 
en triphas�.
* I4_couplage_de_deux_circuits.py: r�solution num�rique d'un couplage de 
circuits oscillants pour illustrer notamment la notion de battements en cas de 
couplage faible.

### Bloc M�canique
* M2_trainee.py (non encore fait): illustration de l'influence de la tra�n�e 
sur un tir d'obus.
* M2_trainee_portrait_de_phase.py (non encore fait): pareil via un portrait de 
phase.
* M4_oscillateur_de_landau_effets_non_lineaires.py (non encore fait): Non 
isochronisme des oscillations dans le cas d'un oscillateur de Landau.
* M4_oscillateur_de_landau_portrait_de_phase.py (non encore fait): Portrait de 
phase pour un oscillateur de Landau
* M4_pendule_simple_non_isochronisme.py (non encore fait): Non isochronisme 
des oscillations pour un pendule simple.
* M4_pendule_simple_oscillations_amorties.py (non encore fait): Oscillations 
amorties dans le cadre du pendule simple.
* M4_pendule_simple_portrait_de_phase.py (non encore fait): fabrication du 
portrait de phase d'un pendule simple. 
* M5_mouvement_dans_champ_E_et_B.py (non encore fait): calcul de la 
trajectoire d'une particule charg�e soumise � la fois � un champ E et un champ 
B.
* M5_mouvement_helicoidal.py (non encore fait): Trajectoire d'une particule 
charg�e soumise uniquement � un champ magn�tique.
* M_hyperion.py: �tude d'une section de Poincar� pour la rotation propre 
d'Hyp�rion (satellite de Saturne) qui mette en avant le caract�re chaotique 
d'une telle rotation (cf Ian Stewart, "Dieu joue-t-il aux d�s" pour une 
introduction � cette probl�matique).
* M_papillon_de_lorentz.py (non encore fait): Illustration du concept 
d'attracteur �trange � l'aide du papillon de Lorentz
* M_pendule_double.py (non encore fait): Illustration de la d�pendance aux 
conditions initiales pour les mouvements chaotiques sur l'exemple du pendule 
double rigide.

### Bloc Signal
S01_oscillateur_harmonique_energie.py
S01_oscillateur_harmonique_periode.py
S02_onde_progressive.py
S02_onde_progressive_animation_superposition.py
S03_battements.py
S03_diffraction.py
S03_fresnel.py
S03_interferences.py
S03_ondes_stationnaires.py
S04_arc_en_ciel_turtle.py
S04_lois_de_descartes.py
S05_distortion_chromatique.py
S05_gauss_4P.py
S05_lentilles_construction_graphique.py
S06_paquet_d_ondes_MQ.py
S07_elec_resolution_pivot_de_gauss.py
S08_circuit_premier_ordre_complexe.py
S08_circuit_premier_ordre_simple.py
S09_oscillateur_amorti_libre.py
S10_oscillateur_amorti_force.py
S11_filtre_bizarre.py
S11_filtre_derivateur.py
S11_filtre_diagrammes_en_amplitudes.py
S11_filtre_integrateur.py
S11_filtres_second_ordre.py
T1_balles_rebondissantes_en_boite.py
T1_particules_en_boite_libre.py
T1_particules_en_boite_mouvement_brownien.py
T2_diagramme_PT_coolprop.py
T2_diagramme_Pv_coolprop.py
T2_reseau_d_isothermes_coolprop.py
T5_isentropique_GP_vs_gaz_reel_coolprop.py
T6_cycle_de_carnot_reel_et_GP.py
T6_diagramme_Ph_coolprop.py
T6_resolution_cycle_diesel.py
bode.py
portrait_de_phase.py
