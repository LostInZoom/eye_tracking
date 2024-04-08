# post-processing of data obtained from the survey 

# list of script :

# list of folder of different data

## coord_fixation_on_map
- coord_fixation_on_map_1.csv
file containing geolocated fixation points
world_index,id_fixation,x,y,zoom,etape
## fixations_on_surface
- fixations_on_surface_Surface_1.csv

file produced by the pupil player tool containing the fixation points
world_timestamp,world_index,fixation_id,start_timestamp,duration,dispersion,norm_pos_x,norm_pos_y,x_scaled,y_scaled,on_surf
## infos_player
info.player_1
file produced by the pupil player tool



## intersection
- intersection_1_0.csv
intersection between the zones of interest and the fixing points for stage x
world_index,id_fixation,x,y,zoom,etape,id

## metrique_pan
- metrique_intersection_pan_1.csv
percentage of point in the first point buffer when paning
id_pan,pourcentage,type,nbr_point_t

## metrique_zoom
- metrique_intersection_zoom_1.csv
percentage of point in the first point buffer when zooming
id_zoom,pourcentage,type,nbr_point_t

## shape 
intersection zone shape file
## old_data
 - pan
 - zoom
 
## pan
world_index,id_fixation,x,y,zoom,etape,id_pan,x_rel,y_rel,x_pixel,y_pixel
Fixation on the sides with the relative and pixel positions of the fixing points
- pan_fixation_on_map_ecran_1.csv
## pan_center                     h
center of pans
center,time,id_pan

## pan_center_translation
center of the sides with a translation applied according to the distance between the centre and the first fixation point
x,y,time,id_pan

## pan_dist_pixel
- pan_dist_pixel_1.csv
distance in pixels between two consecutive points in a pan 

 dist,id_pan,world_index,world_index_suiv


## pan_time
time of pan 
x_min_ini,tps_ini,x_min_f,tps_f,tps,etape

## resultat_enquete

liste_coef_pan
liste_coef_zoom
liste_dtw_pan
liste_dtw_zoom
liste_hausdorff_pan (avec center translation)
liste_hausdorff_zoom
nbr_saccade_entrante
nbr_saccade_sortante
rapport_saccade_fixation

## saccade
world_index,etape,id_polygone


## zoom
world_index,id_fixation,x,y,zoom,etape,id_zoom,x_rel,y_rel,x_pixel,y_pixel
fixation during zooming with relative and pixel positions of fixation points
- zoom_fixation_on_map_ecran_1.csv
## zoom_center
center,time,id_zoom

## zoom_dist_pixel
- zoom_dist_pixel_1.csv
distance in pixels between two consecutive points when zoomed in 
 
  dist,id_zoom,world_index,world_index_suiv


## zoom_time
tps_ini,tps_f,zoom_ini,zoom_f,tps,etape
