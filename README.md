# SocialDistanceCV
*Detecting mask usage and social distancing using an Xbox Kinect.*
![ProjectImage](/images/mask_and_distance.png)


This project was the Microsoft Grand Prize Winner for Ohio State University's 2020 Hack OHI/O. Note that the code is unchanged from the hackathon, so things may seem all over the place.

## The Team
Our team "Hugs not Bugs" consisted of:
- Aiko Zhao
- Alex Vandenbusche
- Robert Wetzler

## The project
We delagated the project into two parts:
1. Detecting mask usage
   * Aiko
   * Alex
2. Detecting Social Distancing
   * Robert
  
### Detecting Mask Usage
To detect when someone is wearing a mask, we trained a model using a dataset of images of people with/without masks. Then, in real time, the model detects if a face in frame is wearing a mask, drawing a green or red box around them accordingly.
![MaskDetection](/images/mask_detection.png)


### Detecting Social Distancing
For every frame:
1. Our program detects all people in the Kinect's camera. To do this, we used YOLO object detection model to find all people in frame (yolo.h5 file not included in repo). 
2. For each detected person, our program reads the distance of their center from the Kinect's IR camera.
3. Using an equation based on the Kinect's FOV and the detected distances, the screenspace coordinate of each person is converted to a worldspace coordinate.
4. The distance between each person is calculated. If the distance is less than 6 feet, the message "Stay 6 feet apart" is printed.

![DistanceDetection](/images/distance_detection.png)

