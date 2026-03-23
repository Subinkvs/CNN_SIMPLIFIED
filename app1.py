import cv2

imagepath = 'image_path/parrot_image.jpg'

img = cv2.imread(imagepath)

cv2.imshow('parrot_image', img)
cv2.waitKey()