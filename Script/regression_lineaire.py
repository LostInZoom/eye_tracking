from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

import pandas as pd
import glob

zoom = glob.glob('pan/*')

liste_zoom = []



for i in range(len(zoom)):
    assert os.path.exists(zoom[i])
    
    liste_zoom.append(pd.read_csv(zoom[i]))


# i = [float(test_pan_center["center"][0].split(", ")[0].split("(")[1]),float(test_pan_center["center"][0].split(", ")[1].split(")")[0])]


liste_coef_aff =[]
liste_coef =[]
# correlation_coefficient = np.corrcoef(x, y)[0, 1]
for t in range(len(liste_zoom)):
    list_zoom_t = liste_zoom[t]

    for x in range(max(list_zoom_t["id_pan"])+1):
        liste_x =[]
        liste_y =[]
        for i in range(len(list_zoom_t)):
            if list_zoom_t["id_pan"][i] == x: 
                liste_x.append(list_zoom_t["x"][i])
                liste_y.append(list_zoom_t["y"][i])   
        if(len(liste_x) != 0):
            correlation_coefficient = np.corrcoef(liste_x, liste_y)[0, 1]
            liste_coef.append([zoom[t].split(".")[0].split("_")[5],x,correlation_coefficient])
            liste_coef_aff.append(correlation_coefficient)
plt.hist(liste_coef_aff, bins=30, edgecolor='k')


with open('resultat_enquete/liste_coef_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_pan","coef_corrrelation"]) 
    for i in range(len(liste_coef)):
        writer.writerow(liste_coef[i])