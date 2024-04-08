
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import matplotlib.pyplot as plt
import csv
import numpy as np

path_to_export = "transpose"
path_to_fixation = os.path.join(path_to_export, "fixations_on_surface_Surface 1.csv")
assert os.path.exists(path_to_fixation)
point = pd.read_csv(path_to_fixation)

coordonnee_point_pixel = [[18,1080-140-10],[1132,1080-140-10],[8+571,1080-(300+140)],[18,(1080-(600+140-10))],[1132,(1080-(600+140-10))]]
# box_carte = [8/1920,(1080-(600+140))/1080,(1142+8)/1920,(1080-140)/1080] # a calculer en pourcentage (xmin,ymin,xmax,ymax)
taille_ecran_pixel =[1920,1080]

point_liste =[[],[],[],[],[]]
for k in range(len(point)):
    for l in range(len(coordonnee_point_pixel)):
        distance = np.sqrt((coordonnee_point_pixel[l][0]-float(point["norm_pos_x"][k])*taille_ecran_pixel[0])**2+(coordonnee_point_pixel[l][1]-float(point["norm_pos_y"][k])*taille_ecran_pixel[1])**2)
        if distance < 200:
            point_liste[l].append([distance,float(point["norm_pos_x"][k])*taille_ecran_pixel[0],float(point["norm_pos_y"][k])*taille_ecran_pixel[1]])
stat = []
for k in range(len(coordonnee_point_pixel)):
    somme_distance = 0
    somme_x = 0
    somme_y = 0
    for l in range(len(point_liste[k])):
        somme_distance += point_liste[k][l][0]
        somme_x += point_liste[k][l][1]
        somme_y += point_liste[k][l][2]
    stat.append([somme_distance/len(point_liste[k]),somme_x/len(point_liste[k]),somme_y/len(point_liste[k])])
moy = [0]
somme = 0
for k in range(len(stat)):
    somme += stat[k][0]
if(len(stat)!=0):
    moy[0] = somme /len(stat)
    
with open('transpose/coord_erreur_on_map.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["dist_p","x","y"])
    for i in range(len(stat)):
        writer.writerow(stat[i])
with open('transpose/moy_erreur_on_map.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([moy[0]])
