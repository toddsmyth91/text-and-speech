# must for mac do 'brew install tesseract'
import pytesseract
import cv2 #opencv-python

# print images supported by pytesseract
#print(pytesseract.get_languages())

# read the image using OpenCV
image = cv2.imread("input.png")
image = cv2.imread("input-eng-jpn.png")
image = cv2.imread("input-jpn.png")
# or you can use Pillow
# image = Image.open("input.png")

# get the string
string = pytesseract.image_to_string(image, lang="eng+jpn")
#string = pytesseract.image_to_data(image, lang="eng+jpn")
# print it
print(string)
