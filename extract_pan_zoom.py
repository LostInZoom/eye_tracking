import os

import av
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import csv
import datetime
import json

# resultat_carte.cvs est produit par l'enquête
# Cette algo permet de savoir quand la persone zoom et pan, on estime que le zoom ou la pan se finit lorsqu'il ne bouge plus pendant 1s

path_to_export = "recordings"
path_to_resultat= os.path.join(path_to_export, "resultat_carte.csv") # structure : time,zoom,xmin,ymin,xmax,ymax,etape,etat_carte

assert os.path.exists(path_to_resultat)
resultat = pd.read_csv(path_to_resultat)


zoom =[]
pan = []
def recursivite_zoom(i):
    rang = 0
    if (i < len(resultat)-10):
        zoom_i = resultat["zoom"][i+1]
        if(zoom_i == resultat["zoom"][i+2] and zoom_i == resultat["zoom"][i+3] and zoom_i == resultat["zoom"][i+4]  and zoom_i == resultat["zoom"][i+5] and zoom_i == resultat["zoom"][i+6]  and zoom_i == resultat["zoom"][i+7] and zoom_i == resultat["zoom"][i+8] and zoom_i == resultat["zoom"][i+9]and zoom_i == resultat["zoom"][i+10]):
            tps_fin = resultat["time"][i+1]
            zoom_fin = resultat["zoom"][i+1]
            rang = i+1
            etape = resultat["etape"][i+1]
        else:
            tps_fin,zoom_fin,rang,etape = recursivite_zoom(i+1)
    else : 
        tps_fin = resultat["time"][i+1]
        zoom_fin = resultat["zoom"][i+1]
        rang = rang_last_zoom+1
        etape = resultat["etape"][i+1]
    return tps_fin,zoom_fin,rang,etape

def recursivite_pan(i):
    rang = 0
    if (i < len(resultat)-10):
        x_min_in = resultat["xmin"][i+1]
        if(x_min_in == resultat["xmin"][i+2] and x_min_in == resultat["xmin"][i+3] and x_min_in == resultat["xmin"][i+4]  and x_min_in == resultat["xmin"][i+5] and x_min_in == resultat["xmin"][i+6]  and x_min_in == resultat["xmin"][i+7] and x_min_in == resultat["xmin"][i+8] and x_min_in == resultat["xmin"][i+9]and x_min_in == resultat["xmin"][i+10]):
            tps_fin = resultat["time"][i+1]
            x_min_f,y_min_f,x_max_f,y_max_f = resultat["xmin"][i+1],resultat["ymin"][i+1],resultat["xmax"][i+1],resultat["ymax"][i+1]
            rang = i+1
            etape = resultat["etape"][i+1]
        else:
            tps_fin,x_min_f,y_min_f,x_max_f,y_max_f,rang,etape = recursivite_pan(i+1)
    else : 
        tps_fin = resultat["zoom"][i+1]
        x_min_f,y_min_f,x_max_f,y_max_f = resultat["xmin"][i+1],resultat["ymin"][i+1],resultat["xmax"][i+1],resultat["ymax"][i+1]
        rang = rang_last_pan
    return tps_fin,x_min_f,y_min_f,x_max_f,y_max_f,rang,etape

rang_last_zoom = 0
rang_last_pan = 0
for i in range(len(resultat)-1):
    # on cherche les zooms
    if(rang_last_zoom < i):
        if (resultat["zoom"][i] != resultat["zoom"][i+1]):
            etape_ini =resultat["etape"][i] 
            zoom_ini = resultat["zoom"][i]
            temps_ini = resultat["time"][i]
            tps_fin,zoom_fin,rang_last_zoom,etape_f = recursivite_zoom(i)
            tps = tps_fin - temps_ini
            if(etape_f== etape_ini):
                zoom.append([temps_ini,tps_fin,zoom_ini,zoom_fin,tps,etape_ini])

    # on cherche les pans
    if(rang_last_pan < i):
        if (resultat["xmin"][i] != resultat["xmin"][i+1] and resultat["zoom"][i] == resultat["zoom"][i+1]):
            etape_ini =resultat["etape"][i] 

            x_min_in,y_min_in,x_max_in,y_max_in = resultat["xmin"][i],resultat["ymin"][i],resultat["xmax"][i],resultat["ymax"][i]
            temps_ini = resultat["time"][i]
            tps_fin,x_min_f,y_min_f,x_max_f,y_max_f,rang_last_pan,etape_f = recursivite_pan(i)
            tps = tps_fin - temps_ini
            if(etape_f== etape_ini):
                # pan.append([x_min_in,y_min_in,x_max_in,y_max_in,temps_ini,x_min_f,y_min_f,x_max_f,y_max_f,tps_fin,tps,etape_ini])
                pan.append([x_min_in,temps_ini,x_min_f,tps_fin,tps,etape_ini])






with open('resultat_enquete/zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["tps_ini","tps_f","zoom_ini","zoom_f","tps","etape"]) 
    for i in range(len(zoom)):
        writer.writerow(zoom[i])
with open('resultat_enquete/pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["x_min_ini","tps_ini","x_min_f","tps_f","tps","etape"])  
    for i in range(len(pan)):
        writer.writerow(pan[i])
