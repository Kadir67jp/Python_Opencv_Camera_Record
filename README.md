# CAMERA DISPLAY&RECORDING USING PYTHON OPENCV
- Program: camera_360_record.py
- Environment: Windows, Python3
- Camera: 1080p, 360 degree camera
- Different camera can be used

# Getting Started
- This program let you to display and record the video using the camera that already connected to your computer. 

## Prerequisites
    Python, Opencv

## Installing
### Install Opencv for Python
    For Windows
    -> pip install opencv-python

# Running the tests
 - Run the program from the command line

        ->python camera_360_record.py

## Record
- Recorded video file is saved into "VIDEO_RECORDS" folder.

# Notes
- If you want to use your laptop webcam change the capture index to O as below 
  
        capture = cv2.VideoCapture(1) =====>  capture = cv2.VideoCapture(0)
  
- Camera Resolution can be set by changing the value of WIDTH and HEIGHT as below

        WIDTH = 1920 HEIGHT = 1080    =====>  WIDTH = 640   HEIGHT = 480