import os

import pandas as pd
import matplotlib.pyplot as plt
import csv
import json
import numpy



path_to_export = "Stats"
path_to_pan= os.path.join(path_to_export, "stat_pan.csv") 
path_to_fix= os.path.join(path_to_export, "stat_fix.csv") 
path_to_zoom= os.path.join(path_to_export, "stat_zoom.csv") 
path_to_time= os.path.join(path_to_export, "stat_time.csv") 

stat_time = pd.read_csv(path_to_time)
stat_fix = pd.read_csv(path_to_fix)
stat_pan= pd.read_csv(path_to_pan)
stat_zoom = pd.read_csv(path_to_zoom)


stat_time = pd.read_csv(path_to_time)
stat_fix = pd.read_csv(path_to_fix)
stat_pan= pd.read_csv(path_to_pan)
stat_zoom = pd.read_csv(path_to_zoom)

liste_fix_freq = []
liste_pan_freq = []
liste_zoom_freq= []



for i in range(len(stat_fix)):
    for k in range(1,11):
        liste_fix_freq.append([stat_fix['n'][i],stat_fix[str(k)][i]/stat_time[str(k)][i],k])
        liste_pan_freq.append([stat_pan['n'][i],stat_pan[str(k)][i]/stat_time[str(k)][i],k])
        liste_zoom_freq.append([stat_zoom['n'][i],stat_zoom[str(k)][i]/stat_time[str(k)][i],k])

    
with open('Stats/liste_fix_freq.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","freq","etape"]) 
    for i in range(len(liste_fix_freq)):
        writer.writerow(liste_fix_freq[i])


with open('Stats/liste_pan_freq.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","freq","etape"]) 
    for i in range(len(liste_pan_freq)):
        writer.writerow(liste_pan_freq[i])


with open('Stats/liste_zoom_freq.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","freq","etape"]) 
    for i in range(len(liste_zoom_freq)):
        writer.writerow(liste_zoom_freq[i])
