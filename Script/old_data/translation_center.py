import os
import pandas as pd
import csv
import json



import pandas as pd
import glob
pan = glob.glob('pan/*')
pan_center = glob.glob('pan_center/*')



liste_pan = []
liste_pan_center = []


for i in range(len(pan)):
    assert os.path.exists(pan[i])
    
    liste_pan.append(pd.read_csv(pan[i]))
for i in range(len(pan_center)):
    assert os.path.exists(pan_center[i])
    
    liste_pan_center.append(pd.read_csv(pan_center[i]))



liste_new_center = []
for x in range(len(liste_pan)):
    liste_pan_x = liste_pan[x]
    liste_first_fix =[[liste_pan_x["x"][0],liste_pan_x["y"][0]]]
    id_pan = 0
    for i in range(len(liste_pan_x)):
        if id_pan < liste_pan_x["id_pan"][i]:
            id_pan += 1
            liste_first_fix.append([liste_pan_x["x"][i],liste_pan_x["y"][i]])

    liste_pan_center_x = liste_pan_center[x]
    liste_first_center = [[float(liste_pan_center_x["center"][0].split(", ")[0].split("(")[1]),float(liste_pan_center_x["center"][0].split(", ")[1].split(")")[0])]]
    id_pan_center = 0
    for i in range(len(liste_pan_center_x)):
        if id_pan_center < liste_pan_center_x["id_pan"][i]:
            id_pan_center += 1
            liste_first_center.append([float(liste_pan_center_x["center"][i].split(", ")[0].split("(")[1]),float(liste_pan_center_x["center"][i].split(", ")[1].split(")")[0])])
    liste_tranlation_x = []
    for k in range(len(liste_first_fix)):
        liste_tranlation_x.append([liste_first_fix[k][0]-liste_first_center[k][0],liste_first_fix[k][1]-liste_first_center[k][1]])


    liste_new_center_x = []
    for t in range(len(liste_pan_center_x)):
        id_pan = liste_pan_center_x["id_pan"][t]
        x= float(liste_pan_center_x["center"][t].split(", ")[0].split("(")[1])
        y= float(liste_pan_center_x["center"][t].split(", ")[1].split(")")[0])
        liste_new_center_x.append([x+liste_tranlation_x[id_pan][0],y+liste_tranlation_x[id_pan][1],liste_pan_center_x["time"][t],id_pan])
    liste_new_center.append(liste_new_center_x)

for p in range(len(liste_new_center)):
    nom = 'pan_center_translation/pan_center_translation_'+pan_center[p].split(".")[0].split("_")[3] + ".csv"
    print(nom)
    with open(nom, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x",'y','time','id_pan']) # rajouter le zoom
        for i in range(len(liste_new_center[p])):
            writer.writerow(liste_new_center[p][i])