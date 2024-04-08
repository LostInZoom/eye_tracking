# fixations_on_surface
- fixations_on_surface_Surface_1.csv
fichier produit par l'outil pupil player
world_timestamp,world_index,fixation_id,start_timestamp,duration,dispersion,norm_pos_x,norm_pos_y,x_scaled,y_scaled,on_surf

# coord_fixation_on_map
- coord_fixation_on_map_1.csv
fichier qui contient les points de fixation géolocalisée
world_index,id_fixation,x,y,zoom,etape

# intersection
- intersection_1_0.csv
intersection entre les zones d'intérêts et les points de fixation de l'étape x
world_index,id_fixation,x,y,zoom,etape,id

# metrique_zoom
- metrique_intersection_zoom_1.csv
pourcentage de point dans le buffer du premier point lors s'un zoom
id_zoom,pourcentage,type,nbr_point_t

# old_data
 - pan
 - zoom
# pan
world_index,id_fixation,x,y,zoom,etape,id_pan,x_rel,y_rel,x_pixel,y_pixel
fixation durant les pans avec les positions relatifs et en pixel des points de fixation
- pan_fixation_on_map_ecran_1.csv
# pan_center                     h
centre des pans
center,time,id_pan

# pan_center_translation
centre des pans avec une translation appliqué suivant l'écart entre le centre et le premier point de fixation
x,y,time,id_pan

# pan_dist_pixel
- pan_dist_pixel_1.csv
distance en pixel entre deux points consécutifs lors d'un pan 
 dist,id_pan,world_index,world_index_suiv


# pan_time

x_min_ini,tps_ini,x_min_f,tps_f,tps,etape

# resultat_enquete
liste_coef_pan
liste_coef_zoom
liste_dtw_pan
liste_dtw_zoom
liste_hausdorff_pan (avec center translation)
liste_hausdorff_zoom
nbr_saccade_entrante
nbr_saccade_sortante
rapport_saccade_fixation
# saccade
world_index,etape,id_polygone

# shape

# zoom
world_index,id_fixation,x,y,zoom,etape,id_zoom,x_rel,y_rel,x_pixel,y_pixel
fixation durant les zooms avec les positions relatifs et en pixel des points de fixation
- zoom_fixation_on_map_ecran_1.csv
# zoom_center
center,time,id_zoom

# zoom_dist_pixel
- zoom_dist_pixel_1.csv
distance en pixel entre deux points consécutifs lors d'un zoom 
 dist,id_zoom,world_index,world_index_suiv


# zoom_time
tps_ini,tps_f,zoom_ini,zoom_f,tps,etape
