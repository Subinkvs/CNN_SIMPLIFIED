import cv2

imagepath = 'image_path/parrot_image.jpg'

img = cv2.imread(imagepath)

new_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

cv2.imshow('parrot_image', new_image)
cv2.waitKey(0)