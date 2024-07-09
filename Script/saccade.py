import numpy as np
import os
import pandas as pd
import glob
import csv
import geopandas as gpd

import matplotlib.pyplot as plt


intersection = glob.glob('intersection/*')
fixation_on_map = ['coord_fixation_on_map\\coord_fixation_on_map_10.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_11.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_12.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_13.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_15.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_16.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_18.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_19.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_1.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_20.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_3.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_4.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_5.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_6.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_7.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_8.csv',
                    'coord_fixation_on_map\\coord_fixation_on_map_9.csv']
liste_fixation_on_map = []
liste_intersection = []

for i in range(len(fixation_on_map)):

    assert os.path.exists(fixation_on_map[i])
    fix_csv = pd.read_csv(fixation_on_map[i])
    liste_fixation_on_map.append(fix_csv)
for i in range(len(intersection)):

    assert os.path.exists(intersection[i])
    intersection_csv = pd.read_csv(intersection[i])
    liste_intersection.append(intersection_csv)

nbr_fixation_zone = [[0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,0,0],[0,0,0,0]]
nbr_saccade_zone = [[0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,0,0],[0,0,0,0]]

liste_saccade_entrante = []
liste_saccade_sortante = []
nbr_saccade_entrante = []
nbr_saccade_sortante = []
nbr_fix_zone = []

for t in range(len(liste_intersection)):
    intersection_t = liste_intersection[t] 
    liste_fixation = liste_fixation_on_map[t//5]
    etape = 1
    liste_saccade_entrante_t = []
    liste_saccade_sortante_t = []
    nbr_saccade_entrante_t =0
    nbr_saccade_sortante_t=0
    id_zone = 0
    for k in range(len(intersection_t)):
        index_k= intersection_t["world_index"][k]
        index_fix = liste_fixation["world_index"].tolist().index(index_k)

        fix_adj = [liste_fixation["world_index"][index_fix-1],liste_fixation["world_index"][index_fix+1]]


        nbr_fixation_zone[t%5][intersection_t["id"][k]-1] +=1
        if (fix_adj[0] not in intersection_t["world_index"].tolist()):
            liste_saccade_entrante_t.append([index_fix,intersection_t["etape"][k],intersection_t["id"][k]])
            nbr_saccade_zone[t%5][intersection_t["id"][k]-1] +=1
            nbr_saccade_entrante_t +=1
        if (fix_adj[1] not in intersection_t["world_index"].tolist()):
            liste_saccade_sortante_t.append([index_fix,intersection_t["etape"][k],intersection_t["id"][k]])
            nbr_saccade_sortante_t +=1
    liste_saccade_entrante.append(liste_saccade_entrante_t)
    liste_saccade_sortante.append(liste_saccade_sortante_t)

    nbr_saccade_entrante.append([intersection[t].split("\\")[1].split("_")[1],intersection[t].split("\\")[1].split("_")[2].split(".")[0],nbr_saccade_entrante_t])
    nbr_saccade_sortante.append([intersection[t].split("\\")[1].split("_")[1],intersection[t].split("\\")[1].split("_")[2].split(".")[0],nbr_saccade_sortante_t])

zoom_zone = [[[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[]]]

for t in range(len(liste_intersection)):
    intersection_t = liste_intersection[t] 
    etape = 1
    liste_ancre_zoom = []
    particpant = int(intersection[t].split("\\")[1].split("_")[1])
    zone = int(intersection[t].split("\\")[1].split("_")[2].split(".")[0])

    for k in range(len(intersection_t)):
        # liste_zoom.append([intersection_t["zoom"][k],intersection_t["id"][k]])

        zoom_zone[zone][int(intersection_t["id"][k])-1].append([intersection_t["zoom"][k],particpant])


rapport_saccade_fix = []
for i in range(len(nbr_saccade_zone)):
    zone = []
    for t in range(len(nbr_saccade_zone[i])):
        zone.append(nbr_saccade_zone[i][t]/nbr_fixation_zone[i][t])
    rapport_saccade_fix.append(zone)




for x in range(len(liste_saccade_entrante)):
    with open('saccade/saccade_entrante_'+intersection[x].split("\\")[1], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","etape","id_polygone"]) # rajouter le zoom
        for i in range(len(liste_saccade_entrante[x])):
            writer.writerow(liste_saccade_entrante[x][i])

    with open('saccade/saccade_sortante_'+intersection[x].split("\\")[1], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","etape","id_polygone"]) # rajouter le zoom
        for i in range(len(liste_saccade_sortante[x])):
            writer.writerow(liste_saccade_sortante[x][i])    
            
            
with open('resultat_enquete/nbr_saccade_entrante.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["participant","zone","nbr"]) # rajouter le zoom
    for i in range(len(nbr_saccade_entrante)):
        writer.writerow(nbr_saccade_entrante[i])

with open('resultat_enquete/nbr_saccade_sortante.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["participant","zone","nbr"]) # rajouter le zoom
    for i in range(len(nbr_saccade_sortante)):
        writer.writerow(nbr_saccade_sortante[i])

with open('resultat_enquete/rapport_saccade_fixation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(rapport_saccade_fix)):
        row = [i]
        row.extend(rapport_saccade_fix[i])
        writer.writerow(row)