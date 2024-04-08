import os
import pandas as pd
import csv



import pandas as pd
import glob



path_zoom = glob.glob('zoom/*')
path_pan = glob.glob('pan/*')
path_fix = glob.glob('fixations_on_surface/*')

print(path_zoom)
liste_zoom= []
liste_pan = []
liste_fix = []

for i in range(len(path_zoom)):
    assert os.path.exists(path_zoom[i])
    
    liste_zoom.append(pd.read_csv(path_zoom[i]))


for i in range(len(path_pan)):
    assert os.path.exists(path_pan[i])
    
    liste_pan.append(pd.read_csv(path_pan[i]))


for i in range(len(path_fix)):
    assert os.path.exists(path_fix[i])
    
    liste_fix.append(pd.read_csv(path_fix[i]))


box_carte = [8/1920,(1080-(600+140))/1080,(1142+8)/1920,(1080-140)/1080] 

new_liste_pan = []
new_liste_zoom = []
for x in range(len(liste_fix)):
    liste_pan_x = liste_pan[x]
    liste_zoom_x = liste_zoom[x]
    new_pan = []
    new_zoom= []

    liste_fixation_x = liste_fix[x]
    for t in range(len(liste_pan_x)):
        
        
        id_pan = liste_pan_x["world_index"][t]
        index_fix_pan = liste_fixation_x[liste_fixation_x["world_index"] == id_pan ]
        if not index_fix_pan.empty:
        
            x_relatif = (float(index_fix_pan["norm_pos_x"].iloc[0])-box_carte[0])/(box_carte[2]-box_carte[0])
            y_relatif = (float(index_fix_pan["norm_pos_y"].iloc[0])-box_carte[1])/(box_carte[3]-box_carte[1])
            x_pixel = float(index_fix_pan["norm_pos_x"].iloc[0])*1920
            y_pixel =  float(index_fix_pan["norm_pos_y"].iloc[0])*1080
            new_pan.append([liste_pan_x["world_index"][t],
                liste_pan_x["id_fixation"][t],
                liste_pan_x['x'][t],
                liste_pan_x['y'][t],
                liste_pan_x["zoom"][t],
                liste_pan_x["etape"][t],
                liste_pan_x["id_pan"][t],
                x_relatif,y_relatif,x_pixel,y_pixel])

    for p in range(len(liste_zoom_x)):

        id_zoom = liste_zoom_x["world_index"][p]
        index_fix_zoom = liste_fixation_x[liste_fixation_x["world_index"] == id_zoom ]
        if not index_fix_zoom.empty:
            x_relatif = (float(index_fix_zoom["norm_pos_x"].iloc[0])-box_carte[0])/(box_carte[2]-box_carte[0])
            y_relatif = (float(index_fix_zoom["norm_pos_y"].iloc[0])-box_carte[1])/(box_carte[3]-box_carte[1])
            x_pixel = float(index_fix_zoom["norm_pos_x"].iloc[0])*1920
            y_pixel =  float(index_fix_zoom["norm_pos_y"].iloc[0])*1080
            new_zoom.append([liste_zoom_x["world_index"][p],
                liste_zoom_x["id_fixation"][p],
                liste_zoom_x['x'][p],
                liste_zoom_x['y'][p],
                liste_zoom_x["zoom"][p],
                liste_zoom_x["etape"][p],
                liste_zoom_x["id_zoom"][p],
                x_relatif,y_relatif,x_pixel,y_pixel])
    new_liste_zoom.append(new_zoom)
    new_liste_pan.append(new_pan)


for x in range(len(liste_fix)):
    with open('pan/pan_fixation_on_map_ecran_'+path_zoom[x].split(".")[0].split("\\")[1].split("_")[5] + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","id_fixation","x","y","zoom","etape",'id_pan',"x_rel","y_rel","x_pixel",'y_pixel']) # rajouter le zoom
        for i in range(len(new_liste_pan[x])):
            writer.writerow(new_liste_pan[x][i])



    with open('zoom/zoom_fixation_on_map_ecran_'+path_zoom[x].split(".")[0].split("\\")[1].split("_")[5] + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["world_index","id_fixation","x","y","zoom","etape",'id_zoom',"x_rel","y_rel","x_pixel",'y_pixel']) # rajouter le zoom
        for i in range(len(new_liste_zoom[x])):
            writer.writerow(new_liste_zoom[x][i])
