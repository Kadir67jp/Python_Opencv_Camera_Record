#! python3 
# camera_360_record.py

import os
import time
import cv2

FPS_VALUE = 24.0                                    # frame_per_second- Set the speed of the video
WIDTH = 1920
HEIGHT = 1080
DIMENSIONS = (WIDTH,HEIGHT)
VIDEO_TYPE = cv2.VideoWriter_fourcc(*'XVID')

# Get Output Directory
def get_output_dir():
    if not os.path.exists('VIDEO_RECORDS'):         # if directory not exist
        os.makedirs('VIDEO_RECORDS')                # create directory
    
    time_str = time.strftime("%Y%m%d_%H%M%S")       # get current date and time as string
    filename = "video_" + time_str + ".avi"
    output_dir = os.path.join('VIDEO_RECORDS', filename)
    
    return output_dir

# Set resolution of video
def change_resolution(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

# Main Program
def main():
    capture = cv2.VideoCapture(1)                   # Video capturing
    change_resolution(capture,WIDTH,HEIGHT)         # Change resolution
    OUTPUT_DIR= get_output_dir()
    out = cv2.VideoWriter(OUTPUT_DIR, VIDEO_TYPE, FPS_VALUE, DIMENSIONS)

    while(True):
        ret, frame = capture.read()                 # Capture frame-by-frame
        out.write(frame)                            # Save Frame
        cv2.imshow('frame',frame)                   # Display frame
    
        # crop_frame = frame[50:-50, 420:-420]      # Crop the frame
        # cv2.imshow('frame',crop_frame)            # Display the crop frame

        if cv2.waitKey(20) & 0xFF == ord('q'):      # Terminate the camera by pressing "q" from keyboard
            break
        
    # Release the capture
    capture.release()
    out.release()
    cv2.destroyAllWindows()

main()