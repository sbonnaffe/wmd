# wmd
Webcam Motion Detector with Python

Motion detection based on webcam frame comparision.

The original algorithm was inpired from the article below:
  http://www.linuxuser.co.uk/tutorials/raspberry-pi-motion-detection
This example provides a motion detector for raspberry pi with camera module.

Then, it was adapted with OpenCV in order to use a simple USB webcam instead of the pi camera module.
It also allows to test and use this software on a standard comptuer.
Basic code sample to take picture from a webcam with OpenCV-Python can be found here:
  http://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/

Finally, the algorithm was optimized with the following features:
 - save pictures with milisecond-accurate timestamp
 - optionaly display live stream of the webcam input
 - apply frame comparision on a reduced number of pixels to reduce CPU load
 - measure time for frame comparision, and introduce apropriate sleep time to improve CPU load


wmd/
  - webcam_motion_detector.py : actual motion detector. Can be executed by itself, without any parameter.
  - samples/ : this directory contains example scripts. Just here as a reference
	 - pi_motion_detector.py :	original algorithm for raspberry pi with camera module
	 - takepicture.py        :	example to take a picture from USB webcam with OpenCV
	 - timetest.py           :	example to measure time between two instructions
	 - video_capture.py	     :	display video stream from USB webcam in a new window
