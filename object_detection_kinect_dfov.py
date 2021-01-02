from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import os
from matplotlib import pyplot as plt
import cv2
import freenect
import frame_convert2
import matplotlib.pyplot as plt
import math
import numpy as np
import pygame_gui


execution_path = os.getcwd()

color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange', 'spoon': 'gray', 'cup': 'yellow', 'chair': 'green', 'elephant': 'pink', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold', 'keyboard': 'violet', 'cow': 'magenta', 'mouse': 'crimson', 'sports ball': 'raspberry', 'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue', 'hot dog': 'navy', 'apple': 'cobalt', 'parking meter': 'aliceblue', 'sandwich': 'skyblue', 'skis': 'deepskyblue', 'microwave': 'peacock', 'knife': 'cadetblue', 'baseball bat': 'cyan', 'oven': 'lightcyan', 'carrot': 'coldgrey', 'scissors': 'seagreen', 'sheep': 'deepgreen', 'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen', 'remote': 'forestgreen', 'bicycle': 'olivedrab', 'toilet': 'ivory', 'tv': 'khaki', 'skateboard': 'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat', 'tie': 'burlywood', 'orange': 'melon', 'bird': 'bisque', 'dining table': 'chocolate', 'hair drier': 'sandybrown', 'cell phone': 'sienna', 'sink': 'coral', 'bench': 'salmon', 'bottle': 'brown', 'car': 'silver', 'bowl': 'maroon', 'tennis racket': 'palevilotered', 'airplane': 'lavenderblush', 'pizza': 'hotpink', 'umbrella': 'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop': 'indigo', 'vase': 'mediumpurple', 'baseball glove': 'slateblue', 'traffic light': 'mediumblue', 'bed': 'navy', 'broccoli': 'royalblue', 'backpack': 'slategray', 'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear': 'peacock', 'clock': 'lightcyan', 'wine glass': 'teal', 'frisbee': 'aquamarine', 'donut': 'mincream', 'suitcase': 'seagreen', 'dog': 'springgreen', 'banana': 'emeraldgreen', 'person': 'honeydew', 'surfboard': 'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen', 'potted plant': 'greenyellow', 'toaster': 'ivory', 'stop sign': 'beige', 'couch': 'khaki'}

FOCAL_LENGTH = 50
FOV = 0.81669197516247493684
V_FOV_X = 62
V_FOV_Y = 48.6
D_FOV_X = 58.6
D_FOV_Y = 46.6
WIDTH = 640
HEIGHT = 480
D_F = (0.5 * WIDTH) / math.tan(0.5 * D_FOV_X)
V_F = (0.5 * WIDTH) / math.tan(0.5 * V_FOV_X)
resized = False


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])


video_detector = ObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
objects = video_detector.CustomObjects(person=True)
video_detector.loadModel()

plt.show()
cv2.namedWindow('Depth')
cv2.namedWindow('Video')
#gui = pygame_gui.LocationsGUI()
#gui.start()
while 1:
    video = get_video()
    depth = freenect.sync_get_depth(format=freenect.DEPTH_REGISTERED)[0]
    returned_image, detections = video_detector.detectCustomObjectsFromImage(custom_objects=objects, input_image=video, input_type="array",
                                                      output_type="array")
    people = []
    for detection in detections:
        mid_x = (detection['box_points'][0] + detection['box_points'][2]) // 2
        mid_y = (detection['box_points'][1] + detection['box_points'][3]) // 2
        cv2.circle(returned_image, center=(mid_x, mid_y), radius=2, color=(0,0,255))
        cv2.circle(depth, center=(mid_x, mid_y), radius=2, color=(0, 0, 255))
        z = depth[mid_y][mid_x]*0.00328084
        center = (0, 0, D_F)
        pixel = (mid_x - WIDTH/2, mid_y - HEIGHT/2, D_F)
        dot = np.dot(center, pixel)
        alpha = math.acos(dot / (np.linalg.norm(center) * np.linalg.norm(pixel)))
        alpha = math.copysign(alpha, pixel[0])
        deg = math.degrees((alpha))
        #print(f'{z} ft, {deg} degrees, {alpha} alpha, {dot} dot, {pixel} pixel')
        people.append({'x':mid_x, 'y':mid_y, 'dist':z, 'angle':deg})
    # law of cosines a^2 = b^2 + c^2 - 2bccosA, solves SAS triangle
    dist_less_6 = []
    if len(people) >= 2:
        for i in range(len(people)):
            for j in range(i+1, len(people)):
                p1 = people[i]
                p2 = people[j]
                b = p1['dist']
                c = p2['dist']
                angle = abs(p1['angle'] - p2['angle'])
                a = math.sqrt(b*b + c*c - 2*b*c*math.cos(angle))
                print(f'distance between: {a} ft')
                if a < 6:
                    print("MOVE 6 FEET APART!")
                dist_less_6.append(a<=6)
    """if any(dist_less_6):
        gui.draw_bad()
    else:
        gui.draw_good()
    if len(people) > 0:
        gui.draw_people(people)"""
    cv2.imshow('Depth', depth)
    cv2.imshow('Video', returned_image)
    if cv2.waitKey(10) == 27:
        break