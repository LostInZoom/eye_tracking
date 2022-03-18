import os

import av
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import cv2
import matplotlib.pyplot as plt
import csv
import numpy as np

path_to_export = "transpose"
path_to_fixation = os.path.join(path_to_export, "coord_fixation_on_map_2.csv")
assert os.path.exists(path_to_fixation)
point = pd.read_csv(path_to_fixation)

coordonnee_point = [[565196,6527750],[565346,6527707],[565411,6527634],[565475,6527724]]

pix_m = 126/50

distance_min = 60

point_liste =[[],[],[],[]]
for k in range(len(point)):
    for l in range(len(coordonnee_point)):
        distance = np.sqrt((coordonnee_point[l][0]-int(point["x"][k]))**2+(coordonnee_point[l][1]-int(point["y"][k]))**2)
        if distance < 60:
            point_liste[l].append([distance,point["x"][k],point["y"][k]])
stat = []
for k in range(len(coordonnee_point)):
    somme_distance = 0
    somme_x = 0
    somme_y = 0
    for l in range(len(point_liste[k])):
        somme_distance += point_liste[k][l][0]
        somme_x += point_liste[k][l][1]
        somme_y += point_liste[k][l][2]
    stat.append([somme_distance/len(point_liste[k]),somme_distance/len(point_liste[k])*pix_m,somme_x/len(point_liste[k]),somme_y/len(point_liste[k])])
print(stat)
    
