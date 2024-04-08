import os

import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
import json


path_to_export = "recordings"
path_to_resultat= os.path.join(path_to_export, "resultat_carte.csv") 

assert os.path.exists(path_to_resultat)
resultat = pd.read_csv(path_to_resultat)
path_to_pan= os.path.join(path_to_export, "pan.csv")
path_to_zoom= os.path.join(path_to_export, "zoom.csv") 



assert os.path.exists(path_to_pan)
assert os.path.exists(path_to_zoom)


zoom = pd.read_csv(path_to_zoom)
pan = pd.read_csv(path_to_pan)


liste_centre_zoom =[]
liste_centre_pan = []

for i in range(len(resultat)):
    for k in range(len(zoom)):
        if resultat["time"][i]> zoom["tps_ini"][k] and resultat["time"][i]< zoom["tps_f"][k]:
            center =[(resultat["xmin"][i]+resultat["xmax"][i])/2,(resultat["ymin"][i]+resultat["ymax"][i])/2]
            liste_centre_zoom.append([center,resultat["time"][i],k])
    for p in range(len(pan)):
        if resultat["time"][i]> pan["tps_ini"][p] and resultat["time"][i]< pan["tps_f"][p]:
            center =[(resultat["xmin"][i]+resultat["xmax"][i])/2,(resultat["ymin"][i]+resultat["ymax"][i])/2]
            liste_centre_pan.append([center,resultat["time"][i],p])



with open('resultat_enquete/pan_center.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["center","time","id_pan"]) # rajouter le zoom
    for i in range(len(liste_centre_pan)):
        writer.writerow(liste_centre_pan[i])



with open('resultat_enquete/zoom_center.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["center","time","id_zoom"]) # rajouter le zoom
    for i in range(len(liste_centre_zoom)):
        writer.writerow(liste_centre_zoom[i])
