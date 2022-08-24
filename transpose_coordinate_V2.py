import os

import av
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import csv
import datetime
import json

# resultat_carte.cvs est produit par l'enquête
# fixations_on_surface_Surface est produit par l'acquisition avec l'ET, il est dans export/surface
# info.player.json est dans le dossier produit par l'acquisition (il permet de calculer le temps réel)



f = open('recordings/info.player.json',)
json_time = json.load(f)


start_time_system = float(json_time["start_time_system_s"]) # System Time at recording start
start_time_synced = float(json_time["start_time_synced_s"])     # Pupil Time at recording start
# Calculate the fixed offset between System and Pupil Time
offset = start_time_system - start_time_synced

# Choose a Pupil timestamp that you want to convert to System Time
# (this can be any or all timestamps of interest)

# pupil_timestamp = 674439.4695  # This is a random example of a Pupil timestamp

# Add the fixed offset to the timestamp(s) we wish to convert
# pupiltime_in_systemtime = pupil_timestamp + offset

# # Using the datetime python module, we can convert timestamps 
# # stored as seconds represented by floating point values to a 
# # more readable datetime format.
# pupil_datetime = datetime.datetime.fromtimestamp(pupiltime_in_systemtime)
# print(pupil_datetime,pupiltime_in_systemtime*1000)


path_to_export = "recordings"
path_to_enquete = "resultat_enquete"
path_to_fixation = os.path.join(path_to_export, "fixations_on_surface_Surface 1.csv")
path_to_resultat= os.path.join(path_to_export, "resultat_carte.csv")

assert os.path.exists(path_to_fixation)
fixation = pd.read_csv(path_to_fixation)

assert os.path.exists(path_to_resultat)
resultat = pd.read_csv(path_to_resultat)

coord_fixation =[]
# box_coordinate = [565051,6527555,565676,6527850]#(xmin,ymin,xmax,ymax)

box_carte = [8/1920,(1080-(600+140))/1080,(1142+8)/1920,(1080-140)/1080] # a calculer en pourcentage (xmin,ymin,xmax,ymax)

def box_coord(timestamp):
    box = [0,0,0,0]
    zoom = 0
    etape = 1
    etat_carte =0 

    for t in range(len(resultat)):
        if (timestamp+offset)*1000 >= resultat["time"][t]:
            zoom = resultat["zoom"][t]
            etape = resultat["etape"][t]
            box = [float(resultat["xmin"][t]),float(resultat["ymin"][t]),float(resultat["xmax"][t]),float(resultat["ymax"][t])]
            etat_carte = int(resultat["etat_carte"][t])
            continue
        else:
            break
    
    return box,zoom,etape,etat_carte
for k in range(len(fixation)):
    id = fixation["fixation_id"][k]
    if int(fixation["world_index"][k]) > 10: # on enleve les points de debut lors du lancement de l'acquisition 
    #on prend en compte les points qui sont positionnée sur la carte
        if float(fixation["norm_pos_x"][k]) > box_carte[0] and float(fixation["norm_pos_x"][k]) < box_carte[2]:   
            if float(fixation["norm_pos_y"][k]) > box_carte[1] and float(fixation["norm_pos_y"][k]) < box_carte[3]:

                box_coordinate,zoom,etape,etat_carte = box_coord(fixation["world_timestamp"][k])
            # on calcul la position relative du point dans la carte
                if(etat_carte == 0 ):
                    x_relatif = (float(fixation["norm_pos_x"][k])-box_carte[0])/(box_carte[2]-box_carte[0])
                    y_relatif = (float(fixation["norm_pos_y"][k])-box_carte[1])/(box_carte[3]-box_carte[1])
                    x_coord = box_coordinate[0] + x_relatif*(box_coordinate[2]-box_coordinate[0] )
                    y_coord = box_coordinate[1] + y_relatif*(box_coordinate[3]-box_coordinate[1] )
                    coord_fixation.append([id,x_coord,y_coord,zoom,etape])
                


with open('resultat_enquete/coord_fixation_on_map_V2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id_fixation","x","y","zoom","etape"]) # rajouter le zoom
    for i in range(len(coord_fixation)):
        writer.writerow(coord_fixation[i])
