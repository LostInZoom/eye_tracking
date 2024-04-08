import os
import pandas as pd
import csv
import json

import geopandas as gpd

import pandas as pd
import glob



path_to_zoom = glob.glob('zoom_time/*')
path_to_pan = glob.glob('pan_time/*')
path_to_fix = glob.glob('coord_fixation_on_map/*')
path_to_fixation = glob.glob('fixations_on_surface/*')
path_to_info = glob.glob('infos_player/*')



liste_zoom= []
liste_pan = []
liste_coord = []
liste_fixation = []
liste_json = []

for i in range(len(path_to_zoom)):
    assert os.path.exists(path_to_zoom[i])
    
    liste_zoom.append(pd.read_csv(path_to_zoom[i]))


for i in range(len(path_to_pan)):
    assert os.path.exists(path_to_pan[i])
    
    liste_pan.append(pd.read_csv(path_to_pan[i]))


for i in range(len(path_to_fix)):
    assert os.path.exists(path_to_fix[i])
    
    liste_coord.append(pd.read_csv(path_to_fix[i]))

for i in range(len(path_to_fixation)):
    assert os.path.exists(path_to_fixation[i])
    
    liste_fixation.append(pd.read_csv(path_to_fixation[i]))


for i in range(len(path_to_info)):
    assert os.path.exists(path_to_info[i])
    f = open(path_to_info[i],)
    
    liste_json.append(json.load(f))


liste_pan_on_map = []

liste_zoom_on_map = []
for x in range(len(liste_coord)):

    json_time = liste_json[x]
    fixation = liste_fixation[x]
    zoom = liste_zoom[x]
    fix_80 = liste_coord[x]
    pan = liste_pan[x]


    start_time_system = float(json_time["start_time_system_s"]) # System Time at recording start
    start_time_synced = float(json_time["start_time_synced_s"])     # Pupil Time at recording start
    offset = start_time_system - start_time_synced
    time_zoom_x = []
    liste_index_z_x =[]
    liste_index_p_x =[]

    for i in range(len(zoom)): 
        time_zoom_x.append([zoom["tps_ini"][i],zoom["tps_f"][i],i])

    time_pan_x = []
    for i in range(len(pan)): 
        time_pan_x.append([pan["tps_ini"][i],pan["tps_f"][i],i])
    liste_index_zoom_x = []
    liste_index_pan_x = []
    for k in range(len(fixation)):
        timestamp = fixation["world_timestamp"][k]
        time = (timestamp+offset)*1000
        for zoom in time_zoom_x:
            if time > zoom[0] and time < zoom[1]:
                liste_index_zoom_x.append(fixation["fixation_id"][k])
                liste_index_z_x.append(zoom[2])

        for pan in time_pan_x:
            if time > pan[0] and time < pan[1]:
                liste_index_pan_x.append(fixation["fixation_id"][k])
                liste_index_p_x.append(pan[2])

    liste_pan_x =[]
    liste_zoom_x = []


    for j in range(len(fix_80)):

        if fix_80["id_fixation"][j] in liste_index_zoom_x:
            liste_zoom_x.append([fix_80["world_index"][j],fix_80["id_fixation"][j],fix_80["x"][j],fix_80["y"][j],fix_80["zoom"][j],fix_80["etape"][j],liste_index_z_x[liste_index_zoom_x.index(fix_80["id_fixation"][j])]])
        if fix_80["id_fixation"][j] in liste_index_pan_x:
            liste_pan_x.append([fix_80["world_index"][j],fix_80["id_fixation"][j],fix_80["x"][j],fix_80["y"][j],fix_80["zoom"][j],fix_80["etape"][j],liste_index_p_x[liste_index_pan_x.index(fix_80["id_fixation"][j])]])
    liste_pan_on_map.append(liste_pan_x)
    liste_zoom_on_map.append(liste_zoom_x)



for x in range(len(liste_fixation)):
    liste_pan = liste_pan_on_map[x]
    liste_zoom = liste_zoom_on_map[x]

    with open('pan/pan_fixation_on_map_id_'+ path_to_zoom[x].split(".")[0].split("\\")[1].split("_")[1] + ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","id_fixation","x","y","zoom","etape",'id_pan']) # rajouter le zoom
        for i in range(len(liste_pan)):
            writer.writerow(liste_pan[i])



    with open('zoom/zoom_fixation_on_map_id_'+ path_to_zoom[x].split(".")[0].split("\\")[1].split("_")[1] + ".csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","id_fixation","x","y","zoom","etape",'id_zoom']) # rajouter le zoom
        for i in range(len(liste_zoom)):
            writer.writerow(liste_zoom[i])
