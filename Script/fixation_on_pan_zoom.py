# ce script permet de d'isoler les points de fixation lors d'un zoom et d'un pan 

import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
import json




f = open('recordings/info.player.json',)
json_time = json.load(f)


start_time_system = float(json_time["start_time_system_s"]) # System Time at recording start
start_time_synced = float(json_time["start_time_synced_s"])     # Pupil Time at recording start
# Calculate the fixed offset between System and Pupil Time
offset = start_time_system - start_time_synced
# resultat_carte.cvs est produit par l'enquête
# Cette algo permet de connairte les fixations durant un pan et un zoom

path_to_export = "recordings"
path_to_pan= os.path.join(path_to_export, "pan.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
path_to_zoom= os.path.join(path_to_export, "zoom.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
path_to_fix= os.path.join(path_to_export, "coord_fixation_on_map.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte
path_to_fixation = os.path.join(path_to_export, "fixations_on_surface_Surface 1.csv")

assert os.path.exists(path_to_pan)
assert os.path.exists(path_to_fix)
assert os.path.exists(path_to_zoom)
assert os.path.exists(path_to_fixation)

fixation = pd.read_csv(path_to_fixation)
zoom = pd.read_csv(path_to_zoom)
fix_80 = pd.read_csv(path_to_fix)
pan = pd.read_csv(path_to_pan)



# recpipération des temps debut et fin des pan et zoom
time_zoom = []

for i in range(len(zoom)): 
    time_zoom.append([zoom["tps_ini"][i],zoom["tps_f"][i]])

time_pan = []
for i in range(len(pan)): 
    time_pan.append([pan["tps_ini"][i],pan["tps_f"][i]])
liste_index_zoom = []
liste_index_pan = []
for k in range(len(fixation)):
    timestamp = fixation["world_timestamp"][k]
    time = (timestamp+offset)*1000
    for zoom in time_zoom:
        if time > zoom[0] and time < zoom[1]:
            liste_index_zoom.append(fixation["fixation_id"][k])
    for pan in time_pan:
        if time > pan[0] and time < pan[1]:
            liste_index_pan.append(fixation["fixation_id"][k])
liste_pan =[]
liste_zoom = []
for j in range(len(fix_80)):
    if fix_80["id_fixation"][j] in liste_index_zoom:
        liste_zoom.append([fix_80["id_fixation"][j],fix_80["x"][j],fix_80["y"][j],fix_80["zoom"][j],fix_80["etape"][j]])
    if fix_80["id_fixation"][j] in liste_index_pan:
        liste_pan.append([fix_80["id_fixation"][j],fix_80["x"][j],fix_80["y"][j],fix_80["zoom"][j],fix_80["etape"][j]])



with open('resultat_enquete/pan_fixation_on_map.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_fixation","x","y","zoom","etape"]) # rajouter le zoom
    for i in range(len(liste_pan)):
        writer.writerow(liste_pan[i])



with open('resultat_enquete/zoom_fixation_on_map.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_fixation","x","y","zoom","etape"]) # rajouter le zoom
    for i in range(len(liste_zoom)):
        writer.writerow(liste_zoom[i])
