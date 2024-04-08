
import numpy as np
import os
import pandas as pd
import glob
import csv
import geopandas as gpd
from shapely.geometry import Point

shape = ["shape/p0.shp","shape/p1.shp","shape/p2.shp","shape/p3.shp","shape/p4.shp"]
fixation_on_map = glob.glob('fixation_on_map/*')

liste_fixation_on_map = []
liste_shape = []
for i in range(len(shape)):
    assert os.path.exists(shape[i])
    
    liste_shape.append(gpd.read_file(shape[i]))



for i in range(len(fixation_on_map)):

    assert os.path.exists(fixation_on_map[i])
    fix_csv = pd.read_csv(fixation_on_map[i])
    fix_csv['geometry'] = [Point(x, y) for x, y in zip(fix_csv['x'], fix_csv['y'])]


    
    liste_fixation_on_map.append(gpd.GeoDataFrame(fix_csv, geometry='geometry', crs='EPSG:3857'))

for t in range(len(liste_fixation_on_map)):
    liste_fixation_t = liste_fixation_on_map[t]
    for x in range(len(liste_shape)):
        if(x == 0):
     
            points_gdf_etape_x = liste_fixation_t[liste_fixation_t['etape'].isin([1, 2, 3, 4])]

        else : 
            points_gdf_etape_x = liste_fixation_t[liste_fixation_t['etape'] == x]
        points_gdf_etape_x = points_gdf_etape_x.to_crs(liste_shape[x].crs)
        intersection = gpd.sjoin(points_gdf_etape_x, liste_shape[x], predicate='within')

        name ="intersection_" + fixation_on_map[t].split(".")[0].split("_")[6] + "_" + str(x) 
        intersection.drop(['geometry', 'index_right'], axis=1, inplace=True)

        intersection.to_csv('intersection/'+name+".csv",index=False)
 
