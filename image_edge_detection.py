import cv2 


image_path = 'image_path/parrot_image.jpg'

img = cv2.imread(image_path)
img_edge = cv2.Canny(img, 100, 200)

cv2.imshow('image', img)
cv2.imshow('image_edge', img_edge)
cv2.waitKey(0)