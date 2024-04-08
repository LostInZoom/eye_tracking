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


pan = glob.glob('pan/*')


liste_pan_fixation = []


for i in range(len(pan)):
    assert os.path.exists(pan[i])
    
    liste_pan_fixation.append(pd.read_csv(pan[i]))




liste_valeur = []
def calcul_metrique(liste_pan_fixation_x,n,id_participant):
    id_pan_unique = liste_pan_fixation_x['id_pan'].unique()
    liste_valeur_x = []

    for id_pan in id_pan_unique:
        liste_fix_geom_id_pan = liste_fix_x_geom[liste_fix_x_geom['id_pan'] == id_pan]


        if len(liste_fix_geom_id_pan)> n:
            buffer = calcul_buffer(liste_fix_geom_id_pan.iloc[n]["zoom"])
            buffer_point = liste_fix_geom_id_pan.iloc[n].geometry.buffer(buffer)
            points_inside_buffer = liste_fix_geom_id_pan[liste_fix_geom_id_pan.geometry.within(buffer_point)]
        

        if len(liste_fix_geom_id_pan)> n:
            liste_valeur_x.append([id_participant,id_pan,len(points_inside_buffer)/len(liste_fix_geom_id_pan),len(liste_fix_geom_id_pan)])
    return liste_valeur_x


for x in range(len(liste_pan_fixation)):
    liste_pan_fixation_x = liste_pan_fixation[x]
    id_particpant = pan[x].split("\\")[1].split("_")[5].split(".")[0]
    liste_fix_x_geom = gpd.GeoDataFrame(liste_pan_fixation_x, geometry=gpd.points_from_xy(liste_pan_fixation_x.x, liste_pan_fixation_x.y))
    id_pan_unique = liste_pan_fixation_x['id_pan'].unique()
    liste_valeur_x = calcul_metrique(liste_pan_fixation_x,10,id_particpant)
    
    liste_valeur+= liste_valeur_x



# for x in range(len(liste_valeur)):
#     with open('metrique_pan/metrique_intersection_pan_'+pan[x].split("\\")[1].split("_")[5], 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["id_pan","pourcentage","nbr_point_t"]) # rajouter le zoom
#         for i in range(len(liste_valeur[x])):
#             writer.writerow(liste_valeur[x][i])

with open('resultat_enquete/metrique_intersection_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_participant","id_pan","pourcentage","nbr_point_t"]) # rajouter le zoom
    for i in range(len(liste_valeur)):
         writer.writerow(liste_valeur[i])
