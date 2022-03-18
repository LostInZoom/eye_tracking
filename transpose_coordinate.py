import os

import av
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import cv2
import matplotlib.pyplot as plt
import csv


path_to_export = "transpose"
path_to_fixation = os.path.join(path_to_export, "fixations_on_surface_Surface 1.csv")
assert os.path.exists(path_to_fixation)
fixation = pd.read_csv(path_to_fixation)

coord_fixation =[]
box_coordinate = [565051,6527555,565676,6527850]#(xmin,ymin,xmax,ymax)

box_carte = [0/1920,+(1080-981)/1080,1570/1920,(1080-195)/1080] # a calculer en pourcentage (xmin,ymin,xmax,ymax)
print(box_carte)
for k in range(len(fixation)):
    id = fixation["fixation_id"][k]
    if int(fixation["world_index"][k]) > 120 and int(fixation["world_index"][k])< 560:
    #on prend en compte les point qui sont positionnée sur la carte
        if float(fixation["norm_pos_x"][k]) > box_carte[0] and float(fixation["norm_pos_x"][k]) < box_carte[2]:   
            if float(fixation["norm_pos_y"][k]) > box_carte[1] and float(fixation["norm_pos_y"][k]) < box_carte[3]:

            # on calcul la position relative du point dans la carte
                x_relatif = (float(fixation["norm_pos_x"][k])-box_carte[0])/(box_carte[2]-box_carte[0])
                y_relatif = (float(fixation["norm_pos_y"][k])-box_carte[1])/(box_carte[3]-box_carte[1])
                x_coord = box_coordinate[0] + x_relatif*(box_coordinate[2]-box_coordinate[0] )
                y_coord = box_coordinate[1] + y_relatif*(box_coordinate[3]-box_coordinate[1] )
                coord_fixation.append([id,x_coord,y_coord])


with open('transpose/coord_fixation_on_map_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_fixation","x","y"])
    for i in range(len(coord_fixation)):
        writer.writerow(coord_fixation[i])
