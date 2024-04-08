from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

import pandas as pd
import glob

zoom = glob.glob('zoom/*')
pan = glob.glob('pan/*')
zoom_time = glob.glob('zoom_time/*')
pan_time = glob.glob('pan_time/*')
liste_zoom = []
liste_pan = []
liste_zoom_time = []
liste_pan_time = []

for i in range(len(zoom)):
    assert os.path.exists(zoom[i])
    
    liste_zoom.append(pd.read_csv(zoom[i]))


for i in range(len(pan)):
    assert os.path.exists(pan[i])
    
    liste_pan.append(pd.read_csv(pan[i]))


for i in range(len(zoom_time)):
    assert os.path.exists(zoom_time[i])
    
    liste_zoom_time.append(pd.read_csv(zoom_time[i]))


for i in range(len(pan_time)):
    assert os.path.exists(pan_time[i])
    
    liste_pan_time.append(pd.read_csv(pan_time[i]))


list_dist_zoom =[]
list_dist_pan =[]
list_somme_dist_zoom =[]
list_somme_dist_pan =[]
for x in range(len(liste_zoom)):
    liste_pan_x = liste_pan[x]
    liste_zoom_x = liste_zoom[x]
    liste_pan_time_x = liste_pan_time[x]
    liste_zoom_time_x = liste_zoom_time[x]
    id_participant = zoom[x].split("\\")[1].split("_")[5].split('.')[0]
    list_somme_dist_zoom_x =[]
    list_somme_dist_pan_x =[]
    list_dist_x_pan = []
    list_dist_x_zoom = []
    for t in range(max(liste_pan_x["id_pan"]+1)):
        liste_x =[]
        liste_y =[]
        somme_pan = 0
        
        for i in range(len(liste_pan_x)):
            if liste_pan_x["id_pan"][i] == t: 
                liste_x.append([liste_pan_x["x_pixel"][i],liste_pan_x["world_index"][i]])
                liste_y.append([liste_pan_x["y_pixel"][i],liste_pan_x["world_index"][i]])   
        if (len(liste_x)!= 0):
            for p in range(len(liste_x)-1):
                calcul_distance = np.sqrt((liste_x[p][0]-liste_x[p+1][0])**2+(liste_y[p][0]-liste_y[p+1][0])**2)
                somme_pan =+ somme_pan +calcul_distance
                list_dist_x_pan.append([calcul_distance,t,liste_x[p][1],liste_x[p+1][1]])

        
        tps_k = liste_pan_time_x['tps'][t]
        dist_norm = somme_pan/tps_k
        list_somme_dist_pan_x.append([id_participant,t,somme_pan,dist_norm])

    for t in range(max(liste_zoom_x["id_zoom"])+1):
        liste_x =[]
        liste_y =[]
        somme_zoom = 0
        for i in range(len(liste_zoom_x)):
            if liste_zoom_x["id_zoom"][i] == t: 
                liste_x.append([liste_zoom_x["x_pixel"][i],liste_zoom_x["world_index"][i]])
                liste_y.append([liste_zoom_x["y_pixel"][i],liste_zoom_x["world_index"][i]])   
        if (len(liste_x)!= 0):
            for p in range(len(liste_x)-1):
                calcul_distance = np.sqrt((liste_x[p][0]-liste_x[p+1][0])**2+(liste_y[p][0]-liste_y[p+1][0])**2)
                somme_zoom =+ somme_zoom +calcul_distance
                list_dist_x_zoom.append([calcul_distance,t,liste_x[p][1],liste_x[p+1][1]])

        tps_k = liste_zoom_time_x['tps'][t]
        dist_norm = somme_zoom/tps_k
        list_somme_dist_zoom_x.append([id_participant,t,somme_zoom,dist_norm])





    list_somme_dist_pan+= list_somme_dist_pan_x
    list_somme_dist_zoom+= list_somme_dist_zoom_x
    list_dist_zoom.append(list_dist_x_zoom)
    list_dist_pan.append(list_dist_x_pan)







with open('resultat_enquete/liste_dist_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_pan","somme_pixel","somme_norm"]) 
    for i in range(len(list_somme_dist_pan)):
        writer.writerow(list_somme_dist_pan[i])
        
with open('resultat_enquete/liste_dist_zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_zoom","somme_pixel","somme_norm"]) 
    for i in range(len(list_somme_dist_zoom)):
        writer.writerow(list_somme_dist_zoom[i])

# for x in range(len(liste_zoom)):
#     liste_pan_d = list_dist_pan[x]
#     liste_zoom_d = list_dist_zoom[x]

#     with open('pan_dist_pixel/pan_dist_pixel_'+ zoom[x].split("\\")[1].split("_")[5], 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["dist","id_pan","world_index","world_index_suiv"]) # rajouter le zoom
#         for i in range(len(liste_pan_d)):
#             writer.writerow(liste_pan_d[i])



#     with open('zoom_dist_pixel/zoom_dist_pixel_'+ zoom[x].split("\\")[1].split("_")[5], 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["dist","id_zoom","world_index","world_index_suiv"]) # rajouter le zoom
#         for i in range(len(liste_zoom_d)):
#             writer.writerow(liste_zoom_d[i])
