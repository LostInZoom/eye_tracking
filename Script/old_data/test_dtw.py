from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import os
from fastdtw import fastdtw
import pandas as pd

from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

import pandas as pd
import glob




# liste_coef_aff =[]
# liste_coef =[]
# # correlation_coefficient = np.corrcoef(x, y)[0, 1]
# for t in range(len(liste_zoom)):
#     list_zoom_t = liste_zoom[t]

#     for x in range(max(list_zoom_t["id_zoom"])):
#         liste_x =[]
#         liste_y =[]
#         for i in range(len(list_zoom_t)):
#             if list_zoom_t["id_zoom"][i] == x: 
#                 liste_x.append(list_zoom_t["x"][i])
#                 liste_y.append(list_zoom_t["y"][i])   
#         if(len(liste_x) != 0):
#             correlation_coefficient = np.corrcoef(liste_x, liste_y)[0, 1]
#             liste_coef.append([zoom[t].split(".")[0].split("_")[5],x,correlation_coefficient])
#             liste_coef_aff.append(correlation_coefficient)
# plt.hist(liste_coef_aff, bins=30, edgecolor='k')

# plt.show()



liste_center = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11]]
liste_0 = [[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11]] # parallèle

liste_1 = [[1,1],[1,1.5],[1,1.6],[1,1.7],[1,2],[1,2.2],[1,2.6],[1,2.7],[1,3]] # plus lente

liste_2 = [[1,11],[1,10],[1,9],[1,8],[1,7],[1,6],[1,5],[1,4],[1,3],[1,2],[1,1]] #sens opposé

liste_3 = [[0,1],[2,2],[0,3],[2,4],[0,5],[2,6],[0,7],[2,8],[0,9],[2,10],[0,11]] #zigzag

liste_4 = [[1,101],[1,102],[1,103],[1,104],[1,105],[1,106],[1,107],[1,108],[1,109],[1,110],[1,111]]# parallèle loin
liste_5 = [[3,4],[6,7],[3,3],[6,1],[7,5],[1,7],[3,3],[4,9],[7,3],[3,7],[3,1]] #aléatoire

liste_6 = [[1,1],[1,5],[1,11]]

liste_6 =[[1,5],[1,2],[1,7],[1,3],[1,4],[1,6],[1,1],[1,8],[1,9],[1,10],[1,11]]
liste_traj = [liste_center,liste_0,liste_1,liste_2,liste_3,liste_4,liste_5,liste_6]
liste_dtw =[]
# for t in range (len(liste_traj)):

#     liste_traj_t = liste_traj[t]   

#     distance, path = fastdtw(np.array(liste_traj_t, dtype=np.double), np.array(liste_center, dtype=np.double))
#     liste_dtw.append([distance])
liste_x =  [1,1,1,1,1,1,1,1,1,1]
liste_y1 = [1,2,3,4,5,6,7,8,9,10]
liste_y2 = [5,3,7,4,9,10,2,8,6,1]

d =  np.corrcoef(liste_y1, liste_y1)[0, 1]
d2 = np.corrcoef(liste_y2, liste_y2)[0, 1]
print(d,d2)
