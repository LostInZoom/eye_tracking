import os

import av
import pandas as pd
from PIL import Image, ImageDraw, ImageChops
import cv2
import matplotlib.pyplot as plt

path_to_export = "recordings"
path_to_timestamps = os.path.join(path_to_export, "world_timestamps.csv")
path_to_video = os.path.join(path_to_export, "world.mp4")
path_to_fixation = os.path.join(path_to_export, "fixations_on_surface_Surface 1.csv")
path_to_marker = os.path.join(path_to_export, "marker_detections.csv")

assert os.path.exists(path_to_timestamps)
assert os.path.exists(path_to_video)
assert os.path.exists(path_to_fixation)
assert os.path.exists(path_to_marker)


timestamps = pd.read_csv(path_to_timestamps)
fixation = pd.read_csv(path_to_fixation)
marker = pd.read_csv(path_to_marker)

# timestamps.info()
timestamps_in_pupil_time = timestamps["# timestamps [seconds]"]
timestamp_start, timestamp_end = timestamps_in_pupil_time.iloc[[0, -1]]
video_length_in_seconds = timestamp_end - timestamp_start

video = av.open(path_to_video)
liste_index=[]

#on cherche les marker des coins
liste_marker = ['apriltag_v3:tag36h11:2','apriltag_v3:tag36h11:3','apriltag_v3:tag36h11:11','apriltag_v3:tag36h11:4']
for k in range(len(fixation)):
    liste_index.append(fixation["world_index"][k])


# for frame in video.decode(video=0):
#     if frame.index in liste_index:
#         frame.to_image().save('frame/test%04d.jpg' % frame.index)



for k in range(len(fixation)):
# Load video and seek to the 1200th frame

    frame_nb = int(fixation["world_index"][k])
    im = Image.open('frame/test'+str(frame_nb)+'.jpg')
    # draw = ImageDraw.Draw(im)
    # bleu = (0, 0, 255, 0)
    liste_xmin = []
    liste_ymin = []
    liste_xmax = []
    liste_ymax = []
    for i in range(len(marker)):
        if marker["world_index"][i] == frame_nb:
            if marker["marker_uid"][i]== liste_marker[3]:
                liste_xmin.append(marker['corner_3_x'][i])
                liste_ymax.append(marker['corner_3_y'][i])
            elif marker["marker_uid"][i]== liste_marker[0]:
                liste_xmax.append(marker['corner_0_x'][i])
                liste_ymax.append(marker['corner_0_y'][i])
            elif marker["marker_uid"][i]== liste_marker[1]:
                liste_xmax.append(marker['corner_1_x'][i])
                liste_ymin.append(marker['corner_1_y'][i])
            elif marker["marker_uid"][i] == liste_marker[2]:
                liste_xmin.append(marker['corner_2_x'][i])
                liste_ymin.append(marker['corner_2_y'][i])
            # liste_x.append(marker['corner_0_x'][i])
            # liste_x.append(marker['corner_1_x'][i])
            # liste_x.append(marker['corner_2_x'][i])
            # liste_x.append(marker['corner_3_x'][i])
            # liste_y.append(marker['corner_0_y'][i])
            # liste_y.append(marker['corner_1_y'][i])
            # liste_y.append(marker['corner_2_y'][i])
            # liste_y.append(marker['corner_3_y'][i])
            # coord = [float(marker['corner_0_x'][i]),float(marker['corner_0_y'][i]),
            #             float(marker['corner_1_x'][i]),float(marker['corner_1_y'][i]),
            #             float(marker['corner_2_x'][i]),float(marker['corner_2_y'][i]),
            #             float(marker['corner_3_x'][i]),float(marker['corner_3_y'][i]),
            #             float(marker['corner_0_x'][i]),float(marker['corner_0_y'][i])]
            # draw.polygon(coord,fill =bleu, outline ="blue")
    #récupération du xmin ymin, ymin et ymax
    # im.save('dessin/test'+str(frame_nb)+'.jpg')
    xmin = min(liste_xmin)
    ymin = min(liste_ymin)
    xmax = max(liste_xmax)
    ymax = max(liste_ymax)

    # on essaye de créer un masque 
    # masque = Image.new('RGB', im.size, color=(255,255,255))

    # polygone_coords = (xmin,ymin,xmin,ymax,xmax,ymax,xmax,ymin,xmin,ymin) 
    # masque_draw = ImageDraw.Draw(masque)
    # masque_draw.polygon(polygone_coords, fill=(0,0,0))
 
    # diff = ImageChops.lighter(im, masque)

    # masque.show()
    # diff.show()
    
    # masque.save('masque/test'+str(frame_nb)+'.jpg')
    im1 = im.crop((int(xmin),int(ymin), int(xmax), int(ymax)))
    im1.save('frame/surface_frame/test'+str(frame_nb)+'.jpg')


   








