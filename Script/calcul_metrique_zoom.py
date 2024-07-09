import os
import pandas as pd
import csv
import json

import geopandas as gpd
from shapely.geometry import Point

import matplotlib.pyplot as plt

import pandas as pd
import glob

def calcul_buffer(zoom):
    if(zoom >= 18):
        return 15
    elif (zoom >= 17):
        return 33
    elif (zoom >= 16):
        return 60
    elif (zoom >= 15):
        return 140
    elif (zoom >= 14):
        return 285
    elif (zoom >= 13):
        return 570
    elif (zoom >= 12):
        return 1200
    elif (zoom >= 11):
        return 2300
    else :
        return 4500


zoom = glob.glob('zoom/*')
zoom_center = glob.glob('zoom_center/*')

liste_zoom_fixation = []
liste_zoom_center = []

for i in range(len(zoom)):
    assert os.path.exists(zoom[i])
    
    liste_zoom_fixation.append(pd.read_csv(zoom[i]))




liste_valeur = []
def calcul_metrique(liste_zoom_fixation_x,n,id_participant):
    id_zoom_unique = liste_zoom_fixation_x['id_zoom'].unique()
    liste_valeur_x = []
    for id_zoom in id_zoom_unique:
        liste_fix_geom_id_zoom = liste_fix_x_geom[liste_fix_x_geom['id_zoom'] == id_zoom]
        type = "in"
        if(liste_fix_geom_id_zoom.iloc[-1]["zoom"] > liste_fix_geom_id_zoom.iloc[0]["zoom"]):
            if len(liste_fix_geom_id_zoom)> n:
                buffer = calcul_buffer(liste_fix_geom_id_zoom.iloc[n]["zoom"])
                buffer_point = liste_fix_geom_id_zoom.iloc[n].geometry.buffer(buffer)
                points_inside_buffer = liste_fix_geom_id_zoom[liste_fix_geom_id_zoom.geometry.within(buffer_point)]
        
        else:
            if len(liste_fix_geom_id_zoom)> n:
                buffer = calcul_buffer(liste_fix_geom_id_zoom.iloc[len(liste_fix_geom_id_zoom)-n-1]["zoom"])
                buffer_point = liste_fix_geom_id_zoom.iloc[len(liste_fix_geom_id_zoom)-n-1].geometry.buffer(buffer)
                points_inside_buffer = liste_fix_geom_id_zoom[liste_fix_geom_id_zoom.geometry.within(buffer_point)]
                type = "out"
        if len(liste_fix_geom_id_zoom)> n:
            liste_valeur_x.append([id_participant,id_zoom,len(points_inside_buffer)/len(liste_fix_geom_id_zoom),type,len(liste_fix_geom_id_zoom)])
    return liste_valeur_x


for x in range(len(liste_zoom_fixation)):
    id_participant = zoom[x].split("\\")[1].split("_")[5].split(".")[0]
    liste_zoom_fixation_x = liste_zoom_fixation[x]
    liste_fix_x_geom = gpd.GeoDataFrame(liste_zoom_fixation_x, geometry=gpd.points_from_xy(liste_zoom_fixation_x.x, liste_zoom_fixation_x.y))
    id_zoom_unique = liste_zoom_fixation_x['id_zoom'].unique()
    liste_valeur_x = calcul_metrique(liste_zoom_fixation_x,10,id_participant)
    
    liste_valeur+= liste_valeur_x



#comparaison in out 
valeur_in = []
valeur_out = []

for x in range(len(liste_valeur)):
    liste_valeur_x = liste_valeur[x]

    for valeur in liste_valeur_x:
        if valeur[2] =='in':
            valeur_in.append(valeur[1])
        else:
            valeur_out.append(valeur[1])

plt.hist(valeur_in, bins=10, edgecolor='k')
plt.show()


# for x in range(len(liste_valeur)):
#     with open('metrique_zoom/metrique_intersection_zoom_'+zoom[x].split("\\")[1].split("_")[5], 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["id_zoom","pourcentage","type","nbr_point_t"]) # rajouter le zoom
#         for i in range(len(liste_valeur[x])):
#             writer.writerow(liste_valeur[x][i])


with open('resultat_enquete/metrique_intersection_zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_zoom","pourcentage","type","nbr_point_t"]) # rajouter le zoom
    for i in range(len(liste_valeur)):
        writer.writerow(liste_valeur[i])
