# resultat_carte.cvs est produit par l'enquête
# Cette algo compter les zoom et pan, on estime que le zoom ou la pan se finit lorsqu'il ne bouge plus pendant 1s



import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
import json


path_to_export = "recordings"
path_to_pan= os.path.join(path_to_export, "pan.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
path_to_zoom= os.path.join(path_to_export, "zoom.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
path_to_fix_80= os.path.join(path_to_export, "coord_fixation_on_map.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
# path_to_fix_500= os.path.join(path_to_export, "coord_fixation_on_map_500.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte

assert os.path.exists(path_to_pan)
assert os.path.exists(path_to_fix_80)
assert os.path.exists(path_to_zoom)
# assert os.path.exists(path_to_fix_500)
zoom = pd.read_csv(path_to_zoom)
fix_80 = pd.read_csv(path_to_fix_80)
pan = pd.read_csv(path_to_pan)
# fix_500 = pd.read_csv(path_to_fix_500)


tab_zoom = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(zoom)):
    etape = int(zoom["etape"][i])
    tab_zoom[etape-1] = tab_zoom[etape-1] +1
tab_pan = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(pan)):
    etape = int(pan["etape"][i])
    tab_pan[etape-1] = tab_pan[etape-1] +1


tab_80 = [0,0,0,0,0,0,0,0,0,0]
i_max = 0
liste_id_fix = []
for i in range(len(fix_80)):

    etape = int(fix_80["etape"][i])
    if(fix_80["zoom"][i] !=0):  
        if(liste_id_fix.count(fix_80["id_fixation"][i])==0):
            tab_80[etape-1] = tab_80[etape-1] +1
            liste_id_fix.append(fix_80["id_fixation"][i])


tab = [tab_zoom,tab_pan,tab_80]

with open('resultat_enquete/stat.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(tab)):
        writer.writerow(tab[i])
