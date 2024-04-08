import os
import pandas as pd
import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_score
import archetypes as arch
from sklearn.datasets import load_iris
import geopandas as gpd
from sklearn.cluster import KMeans
import pandas as pd
import glob
liste_participant = [1,3,4,5,6,7,8,9,10,11,12,13,15,16,18,19,20]

liste_coef_pan= pd.read_csv('resultat_enquete/liste_coef_pan.csv') 
liste_coef_zoom= pd.read_csv('resultat_enquete/liste_coef_zoom.csv') 

liste_dist_pan= pd.read_csv('resultat_enquete/liste_dist_pan.csv') 
liste_dist_zoom= pd.read_csv('resultat_enquete/liste_dist_zoom.csv') 


liste_hausdorff_pan= pd.read_csv('resultat_enquete/liste_hausdorff_pan.csv') 
liste_hausdorff_zoom= pd.read_csv('resultat_enquete/liste_hausdorff_zoom.csv') 
liste_hausdorff_norm_pan= pd.read_csv('resultat_enquete/liste_hausdorff_norm_pan.csv') 

liste_metrique_pan= pd.read_csv('resultat_enquete/metrique_intersection_pan.csv') 
liste_metrique_zoom= pd.read_csv('resultat_enquete/metrique_intersection_zoom.csv') 



count = 0
count_2 = 0
liste_x = []
for x in liste_participant:
    liste_coef_pan_x = liste_coef_pan[liste_coef_pan['id_participant'] == x]
    liste_dist_pan_x = liste_dist_pan[liste_dist_pan['id_participant'] == x]
    liste_hausdorff_norm_pan_x = liste_hausdorff_norm_pan[liste_hausdorff_norm_pan['id_participant'] == x]
    liste_metrique_pan_x = liste_metrique_pan[liste_metrique_pan['id_participant'] == x]

    max_value = max(max(liste_dist_pan_x["id_pan"]),max(liste_dist_pan_x["id_pan"]),max(liste_hausdorff_norm_pan_x["id_pan"]),max(liste_metrique_pan_x["id_pan"]))
    for i in range (max_value+1):
        test = True
        liste_x_i = [0,0,0,0]
        index_coef = liste_coef_pan_x[liste_coef_pan_x['id_pan'] == i].index
        if not index_coef.empty:
            val = abs(liste_coef_pan_x['coef_corrrelation'][index_coef].tolist()[0])
            if  not np.isnan(val):
                liste_x_i[0] = val
        else:
            test =False
        index_dist = liste_dist_pan_x[liste_dist_pan_x['id_pan'] == i].index
        if not index_dist.empty:
            liste_x_i[1]  = liste_dist_pan_x['somme_norm'][index_dist].tolist()[0]
        else:
            test =False
        index_m = liste_metrique_pan_x[liste_metrique_pan_x['id_pan'] == i].index
        if not index_m.empty:
            liste_x_i[2]  = liste_metrique_pan_x['pourcentage'][index_m].tolist()[0]
        else:
            test =False
        index_h = liste_hausdorff_norm_pan_x[liste_hausdorff_norm_pan_x['id_pan'] == i].index
        if not index_h.empty:
            liste_x_i[3]  = liste_hausdorff_norm_pan_x['norm'][index_h].tolist()[0]
            count_2+=1
        else:
            test =False
            count +=1
        if(test):
            liste_x.append(liste_x_i)





# liste_zoom_in = []
# liste_zoom_out = []
# for x in liste_participant:
#     liste_coef_zoom_x = liste_coef_zoom[liste_coef_zoom['id_participant'] == x]
#     liste_dist_zoom_x = liste_dist_zoom[liste_dist_zoom['id_participant'] == x]
#     liste_hausdorff_zoom_x = liste_hausdorff_zoom[liste_hausdorff_zoom['id_participant'] == x]
#     liste_metrique_zoom_x = liste_metrique_zoom[liste_metrique_zoom['id_participant'] == x]

#     max_value = max(max(liste_dist_zoom_x["id_zoom"]),max(liste_dist_zoom_x["id_zoom"]),max(liste_hausdorff_zoom_x["id_zoom"]),max(liste_metrique_zoom_x["id_zoom"]))
#     for i in range (max_value+1):
#         in_out = True
#         test = True
#         liste_x_i = [0,0,0]
#         index_coef = liste_coef_zoom_x[liste_coef_zoom_x['id_zoom'] == i].index
#         if not index_coef.empty:
#             val = abs(liste_coef_zoom_x['coef_corrrelation'][index_coef].tolist()[0])
#             if  not np.isnan(val):
#                 liste_x_i[0] = val
#         else:
#             test =False
#         index_dist = liste_dist_zoom_x[liste_dist_zoom_x['id_zoom'] == i].index
#         if not index_dist.empty:
#             liste_x_i[1]  = liste_dist_zoom_x['somme_norm'][index_dist].tolist()[0]
#         else:
#             test =False
#         index_m = liste_metrique_zoom_x[liste_metrique_zoom_x['id_zoom'] == i].index
#         if not index_m.empty:
#             liste_x_i[2]  = liste_metrique_zoom_x['pourcentage'][index_m].tolist()[0]
#             if (liste_metrique_zoom_x['type'][index_m].tolist()[0] == 'out'):
#                 in_out = False
#         else:
#             test =False
#         # index_h = liste_hausdorff_zoom_x[liste_hausdorff_zoom_x['id_zoom'] == i].index
#         # if not index_h.empty:
#         #     liste_x_i[3]  = liste_hausdorff_zoom_x['distance'][index_h].tolist()[0]
#         #     count_2+=1
#         # else:
#         #     test =False
#         if(test):
#             if (in_out):
#                 liste_zoom_in.append(liste_x_i)
#             else : 
#                 liste_zoom_out.append(liste_x_i)





# data = pd.DataFrame(liste_zoom_out, columns=['corr', 'somme_norm', 'pourcentage','haus'])
# X = data.iloc[:,0:4].values

# wcss = []
# for i in range(1,11):
#     k_means = KMeans(n_clusters=i,init='k-means++', random_state=42)
#     k_means.fit(liste_zoom_out)
#     wcss.append(k_means.inertia_)
# plt.plot(np.arange(1,11),wcss)
# plt.xlabel('Clusters')
# plt.ylabel('SSE')
# plt.show()

# k_means_optimum = KMeans(n_clusters = 2, init = 'k-means++',  random_state=42)
# y = k_means_optimum.fit_predict(X)
# data['cluster'] = y 

# data1 = data[data.cluster==0]
# data2 = data[data.cluster==1] 



# kplot = plt.axes(projection='3d')
# xline = np.linspace(0, 1, 1000)
# yline = np.linspace(0, 1, 1000)
# zline = np.linspace(0, 1, 1000)
# kplot.plot3D(xline, yline, zline, 'black')
# # Data for three-dimensional scattered points
# kplot.scatter3D(data1['corr'],data1['somme_norm'],data1['haus'], c='red', label = 'Cluster 1')
# kplot.scatter3D(data2['corr'],data2['somme_norm'],data2['haus'],c ='green', label = 'Cluster 2')
# plt.scatter(k_means_optimum.cluster_centers_[:,0], k_means_optimum.cluster_centers_[:,1], color = 'indigo', s = 200)
# plt.legend()
# plt.title("Kmeans")
# plt.show()


#liste_x, liste_zoom_in, liste_zoom_out

array_data = np.array(liste_x)



model = arch.AA(n_archetypes=3)

model.fit(array_data)

model.archetypes_
print(model.archetypes_)
plt.figure(figsize=(10, 10))
arch.simplex(model.alphas_, alpha=0.5, show_circle=False, show_direction=True)

plt.show()