#import necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

#constructing the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

#load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("image", image)

#wait for a escape, enter or space key to be pressed and then continue to other codes.
while True:
  ch = cv2.waitKey()
  if ((ch == 13) or (ch==32) or (ch==27)): #enter or space key   
    break

#converting the image to grayscale and creating a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
while True: ##wait for a escape, enter or space key to be pressed and then continue to other codes.
  ch = cv2.waitKey()
  if ((ch == 13) or (ch==32) or (ch==27)): #enter or space key   
    break

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixel in the bin")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()




'''
To run this above code file:
  $ workon cv
  $ navigate to directory where this code file is residing
  $ python filename.py -i path_to_image.jpg


Note: 
1. If your python virtual environment is newly created one, then you may need to install matplotlib 
for that virtualenv first. For that use pip to install only to that virtualenv. Use the command 
  
  $pip install matplotlib

2. And you need to install OpenCV to this virtualenv also. For that:
Via pip you can specify the package version to install using the following:

  $pip install opencv-python==2.4.9

However, that package does not seem to be available on pypi. A little trick for checking available versions:
  
  $pip install opencv-python==

Which returns: Could not find a version that satisfies the requirement
opencv-python== (from versions: 3.1.0.0, 3.1.0.1, 3.1.0.2, 3.1 .0.3, 3.1.0.5, 3.2.0.6, 3.2.0.7) No matching 
distribution found for opencv-python==

Then its good to choose most resent

!!--aspriya scripts-- www.aspriya.com !!
'''