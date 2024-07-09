
import os

import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
import json


path_to_export = "Stats/script/recordings"
path_to_1= os.path.join(path_to_export, "stat_1_time.csv") 
path_to_3= os.path.join(path_to_export, "stat_3_time.csv") 
path_to_4= os.path.join(path_to_export, "stat_4_time.csv") 
path_to_5= os.path.join(path_to_export, "stat_5_time.csv") 
path_to_6= os.path.join(path_to_export, "stat_6_time.csv") 
path_to_7= os.path.join(path_to_export, "stat_7_time.csv") 
path_to_8= os.path.join(path_to_export, "stat_8_time.csv") 
path_to_9= os.path.join(path_to_export, "stat_9_time.csv") 
path_to_10= os.path.join(path_to_export, "stat_10_time.csv") 
path_to_11= os.path.join(path_to_export, "stat_11_time.csv") 
path_to_12= os.path.join(path_to_export, "stat_12_time.csv") 
path_to_13= os.path.join(path_to_export, "stat_13_time.csv") 
path_to_15= os.path.join(path_to_export, "stat_15_time.csv") 
path_to_16= os.path.join(path_to_export, "stat_16_time.csv") 
path_to_18= os.path.join(path_to_export, "stat_18_time.csv") 
path_to_19= os.path.join(path_to_export, "stat_19_time.csv") 
path_to_20= os.path.join(path_to_export, "stat_20_time.csv") 



assert os.path.exists(path_to_1)
assert os.path.exists(path_to_3)
assert os.path.exists(path_to_4)
assert os.path.exists(path_to_5)
assert os.path.exists(path_to_6)
assert os.path.exists(path_to_7)
assert os.path.exists(path_to_8)
assert os.path.exists(path_to_9)
assert os.path.exists(path_to_10)
assert os.path.exists(path_to_11)
assert os.path.exists(path_to_12)
assert os.path.exists(path_to_13)
assert os.path.exists(path_to_15)
assert os.path.exists(path_to_16)
assert os.path.exists(path_to_18)
assert os.path.exists(path_to_19)
assert os.path.exists(path_to_20)

# assert os.path.exists(path_to_fix_500)
stat_1 = pd.read_csv(path_to_1)
stat_3 = pd.read_csv(path_to_3)
stat_4 = pd.read_csv(path_to_4)
stat_5 = pd.read_csv(path_to_5)
stat_6 = pd.read_csv(path_to_6)
stat_7 = pd.read_csv(path_to_7)
stat_8 = pd.read_csv(path_to_8)
stat_9 = pd.read_csv(path_to_9)
stat_10 = pd.read_csv(path_to_10)
stat_11 = pd.read_csv(path_to_11)
stat_12 = pd.read_csv(path_to_12)
stat_13 = pd.read_csv(path_to_13)
stat_15 = pd.read_csv(path_to_15)
stat_16 = pd.read_csv(path_to_16)
stat_18 = pd.read_csv(path_to_18)
stat_19 = pd.read_csv(path_to_19)
stat_20 = pd.read_csv(path_to_20)

liste_stat = [stat_1,stat_3,stat_4,stat_5,stat_6,stat_7,stat_8,stat_9,stat_10,stat_11,stat_12,stat_13,stat_15,stat_16,stat_18,stat_19,stat_20]

liste_name = ["stat_1","stat_3","stat_4","stat_5","stat_6","stat_7","stat_8","stat_9","stat_10","stat_11","stat_12","stat_13","stat_15","stat_16","stat_18","stat_19","stat_20"]

liste_fix = []
liste_zoom = []
liste_pan = []
liste_time = []

for i in range(len(liste_stat)):
    stat = liste_stat[i]
    fix = [liste_name[i]]
    pan =[liste_name[i]]
    zoom = [liste_name[i]]
    time = [liste_name[i]]
    for k in range(1,11):
        pan.append(stat[str(k)][1])
        zoom.append(stat[str(k)][0])
        fix.append(stat[str(k)][2])
        time.append(stat[str(k)][3])


    liste_fix.append(fix)
    liste_zoom.append(zoom)
    liste_pan.append(pan)
    liste_time.append(time)

with open('Stats/stat_fix.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(liste_fix)):
        writer.writerow(liste_fix[i])


with open('Stats/stat_zoom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(liste_zoom)):
        writer.writerow(liste_zoom[i])


with open('Stats/stat_pan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(liste_pan)):
        writer.writerow(liste_pan[i])

        
with open('recordings/stat_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["n","1","2","3","4","5","6","7","8","9","10"]) 
    for i in range(len(liste_time)):
        writer.writerow(liste_time[i])


