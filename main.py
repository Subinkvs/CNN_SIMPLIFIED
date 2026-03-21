import cv2

image = cv2.imread('image_path/parrot_image.jpg')

cv2.imshow('Image', image)


new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('new_image', new_image)



cv2.waitKey(0)