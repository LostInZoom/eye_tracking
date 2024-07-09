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

liste_time = []
liste_fix = []
liste_pan = []
liste_zoom = []
liste_fix_4 = []
liste_pan_4 = []
liste_zoom_4 = []
for i in range(len(stat_fix)):
    for k in range(1,11):
        liste_fix.append([stat_fix['n'][i],stat_fix[str(k)][i],k])
        liste_pan.append([stat_pan['n'][i],stat_pan[str(k)][i],k])
        liste_zoom.append([stat_zoom['n'][i],stat_zoom[str(k)][i],k])
        liste_time.append([stat_time['n'][i],stat_time[str(k)][i],k])
    for k in range(9,11):
        liste_fix_4.append([stat_fix['n'][i],stat_fix[str(k)][i],k])
        liste_pan_4.append([stat_pan['n'][i],stat_pan[str(k)][i],k])
        liste_zoom_4.append([stat_zoom['n'][i],stat_zoom[str(k)][i],k])
    
with open('Stats/liste_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_time)):
        writer.writerow(liste_time[i])

with open('Stats/liste_fix.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_fix)):
        writer.writerow(liste_fix[i])


with open('Stats/liste_zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_zoom)):
        writer.writerow(liste_zoom[i])


with open('Stats/liste_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_pan)):
        writer.writerow(liste_pan[i])


with open('Stats/liste_fix_4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_fix_4)):
        writer.writerow(liste_fix_4[i])

with open('Stats/liste_zoom_4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_zoom_4)):
        writer.writerow(liste_zoom_4[i])


with open('Stats/liste_pan_4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","nbr","etape"]) 
    for i in range(len(liste_pan_4)):
        writer.writerow(liste_pan_4[i])
        

