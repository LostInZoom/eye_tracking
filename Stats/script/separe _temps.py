
import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
import json




path_to_export = "recordings"
path_to_stat = os.path.join(path_to_export, "stat_20.csv")
path_to_resultat= os.path.join(path_to_export, "resultat_carte.csv")

assert os.path.exists(path_to_stat)
stat = pd.read_csv(path_to_stat)

assert os.path.exists(path_to_resultat)
resultat = pd.read_csv(path_to_resultat)

coord_fixation =[]

heure = [resultat["time"][1]]
n_etape = 1
#on récupérer le temps de changement d'étape 
for k in range(len(resultat)):
    if  resultat["etape"][k] != n_etape:
        heure.append(resultat["time"][k])
        n_etape +=1
# on calcul le temps 
last = len(resultat)-1
heure.append(resultat["time"][last])
liste_stat = []
for k in range(len(stat)):
    liste = []
    for i in range(1,11):
        liste.append(stat[str(i)][k])
    liste_stat.append(liste)

liste_time = []
for i in range(0,10):
        liste_time.append((heure[i+1]-heure[i])/1000)

liste_stat.append(liste_time)

with open('recordings/stat_20_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(liste_stat)):
        writer.writerow(liste_stat[i])

