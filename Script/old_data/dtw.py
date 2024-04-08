from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import os
from fastdtw import fastdtw
import pandas as pd
import glob
import csv
pan = glob.glob('pan/*')
zoom = glob.glob('zoom/*')
zoom_center = glob.glob('zoom_center/*')
pan_center = glob.glob('pan_center_translation/*')



liste_pan = []
liste_zoom = []
liste_zoom_center = []
liste_pan_center = []


for i in range(len(pan)):
    assert os.path.exists(pan[i])
    
    liste_pan.append(pd.read_csv(pan[i]))

for i in range(len(zoom)):
    assert os.path.exists(zoom[i])
    
    liste_zoom.append(pd.read_csv(zoom[i]))

for i in range(len(zoom_center)):
    assert os.path.exists(zoom_center[i])
    
    liste_zoom_center.append(pd.read_csv(zoom_center[i]))

for i in range(len(pan_center)):
    assert os.path.exists(pan_center[i])
    
    liste_pan_center.append(pd.read_csv(pan_center[i]))

# i = [float(test_pan_center["center"][0].split(", ")[0].split("(")[1]),float(test_pan_center["center"][0].split(", ")[1].split(")")[0])]

liste_dtw_pan = []
liste_dtw_zoom = []
for t in range (len(liste_zoom)):
    liste_zoom_t = liste_zoom[t]  
    liste_zoom_center_t = liste_zoom_center[t]  
    liste_pan_t = liste_pan[t]  
    liste_pan_center_t = liste_pan_center[t]   
    for x in range(max(liste_pan_t["id_pan"])):
        liste_pan_x = []
        liste_pan_center_x = []
        for i in range(len(liste_pan_t)):
            if liste_pan_t["id_pan"][i] == x: 
                liste_pan_x.append([liste_pan_t["x"][i],liste_pan_t["y"][i]])
        for i in range(len(liste_pan_center_t)):
            if liste_pan_center_t["id_pan"][i]  == x:         
                liste_pan_center_x.append([liste_pan_center_t["x"][i],liste_pan_center_t["y"][i]])
        if len(liste_pan_x) != 0 and len(liste_pan_center_x) != 0:

            distance, path = fastdtw(np.array(liste_pan_x, dtype=np.double), np.array(liste_pan_center_x, dtype=np.double))
            liste_dtw_pan.append([zoom_center[t].split(".")[0].split("_")[3],x,distance,path])
    for x in range(max(liste_zoom_t["id_zoom"])):
        liste_zoom_x = []
        liste_zoom_center_x = []
        for i in range(len(liste_zoom_t)):
            if liste_zoom_t["id_zoom"][i] == x: 
                liste_zoom_x.append([liste_zoom_t["x"][i],liste_zoom_t["y"][i]])
        for i in range(len(liste_zoom_center_t)):
            if liste_zoom_center_t["id_zoom"][i]  == x:         
                center = [float(liste_zoom_center_t["center"][i].split(", ")[0].split("(")[1]),float(liste_zoom_center_t["center"][i].split(", ")[1].split(")")[0])]
                liste_zoom_center_x.append([center[0],center[1]])
        if len(liste_zoom_x) != 0 and len(liste_zoom_center_x) != 0:
            distance, path = fastdtw(np.array(liste_zoom_x, dtype=np.double), np.array(liste_zoom_center_x, dtype=np.double))
            liste_dtw_zoom.append([zoom_center[t].split(".")[0].split("_")[3],x,distance,path])


with open('resultat_enquete/liste_dtw_zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_zoom","distance","path"]) 
    for i in range(len(liste_dtw_zoom)):
        writer.writerow(liste_dtw_zoom[i])
with open('resultat_enquete/liste_dtw_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_pan","distance","path"])  
    for i in range(len(liste_dtw_pan)):
        writer.writerow(liste_dtw_pan[i])

# liste_pan_x = []
# liste_pan_center_x = []
# for i in range(len(test_pan)):
#     if test_pan["id_pan"][i] == 1: 
#         # liste_pan_x.append(test_pan["x"][i])
#         liste_pan_x.append([test_pan["x"][i],test_pan["y"][i]])

# for i in range(len(test_pan_center)):
#     if test_pan_center["id_pan"][i]  == 1:         
#         center = [float(test_pan_center["center"][i].split(", ")[0].split("(")[1]),float(test_pan_center["center"][i].split(", ")[1].split(")")[0])]
#         liste_pan_center_x.append([center[0],center[1]])
#         # liste_pan_center_x.append(center[0])

# np_pan = np.array(liste_pan_x, dtype=np.double)
# np_center = np.array(liste_pan_center_x, dtype=np.double)

# distance, path = fastdtw(np_pan, np_center)
# print("Distance DTW entre les trajectoires : ", distance)
# print("Chemin optimal dans la matrice de correspondance DTW : ", path)

