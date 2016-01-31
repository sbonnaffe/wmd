#!/usr/bin/python
# WMD - The Webcam Motion Detector
# Detect movement on an image flow,
# and take pictures if the image variation
# reaches the detection triggers.
#
# Author: Séraphin Bonnaffé <seraphin.bonnaffe@gmail.com>

import cv2
from datetime import datetime
import time

# Place to save recorded pictures
pics_path = "pics/"

# Triggers
difference = 50
pixels = 10
mesh = 10

# Delay between two snapshots
delay_scanning = 0.2
delay_presence = 0.025

# Camera
camera_port = 0
ramp_frames = 40

# Init capture
camera = cv2.VideoCapture(camera_port)

# Image dimension
width = int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

print "WMD - The Webcam Motion Detector"
print "Camera port: " + str(camera_port) + " - Resolution: " + str(width) + "x" + str(height)

# Ramp the camera -  skip while frames while
# the camera adjusts to light levels
print("Adjusting image...")
for i in xrange(ramp_frames):
    ret, capture1 = camera.read()

delay = delay_scanning
print("WMD loaded! Start scanning...")
while(True):
    start = time.time()
    time.sleep(delay)
    ret, capture2 = camera.read()
    cv2.imshow('capture',capture2)

    # Convert to grayscale and Make diff
    capture1_grey = cv2.cvtColor(capture1, cv2.COLOR_BGR2GRAY)
    capture2_grey = cv2.cvtColor(capture2, cv2.COLOR_BGR2GRAY)
    capt_diff_grey = cv2.absdiff(capture1_grey, capture2_grey)

    # Parse image
    changedpixels = 0
    for i in xrange(0, height):
        if not i % mesh:
            for j in xrange(0, width):
                if not j % mesh:
                    if capt_diff_grey[i,j] > difference:
                        changedpixels += 1

    if changedpixels > pixels:
        # Save image
        file = pics_path + datetime.now().strftime("%Y-%m-%d_%H_%M_%S.%f")[:-3] + ".png"
        cv2.imwrite(file, capture2)
        print datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")[:-3] + ": Motion detected !"

        # change capture range
        delay = delay_presence
    else:
        delay = delay_scanning

    capture1 = capture2

    dt = int((time.time() - start) * 1000)
    print dt

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
del(camera)
