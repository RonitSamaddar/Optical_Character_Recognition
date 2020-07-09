# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = ap.parse_args()

# load the example image and convert it to grayscale
image = cv2.imread(args.image)
cv2.imshow("Original Image",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Trying thresholding on the image
#if args["preprocess"] == "thresh":
#gray = cv2.threshold(gray, 0, 255,
#	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

"""
# Trying blur 
elif args["preprocess"] == "blur":
"""
#gray = cv2.medianBlur(gray, 3)



filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print("Text in Image = "+text)
# show the output images

cv2.waitKey(0)
cv2.destroyAllWindows()
