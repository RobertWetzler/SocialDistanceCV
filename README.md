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
1. Our program detects all people in the Kinect's camera. To do this, we used a YOLO object detection model to find all people in frame (yolo.h5 file not included in repo). 
2. For each detected person, our program reads their distance from the camera using the Kinect's IR image frame.
3. Using an equation based on the Kinect's FOV and the detected distances, the screenspace coordinate + distance of each person is converted to a worldspace coordinate.
4. The distance between each person is calculated. If the distance is less than 6 feet, the message "MOVE 6 FEET APART!" is printed.

![DistanceDetection](/images/distance_detection.png)

*Credit to Devon Brandt (right), Robert's roomate, for helping test and present our project.*
