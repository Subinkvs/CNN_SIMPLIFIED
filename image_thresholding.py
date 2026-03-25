import cv2

image_path = 'image_path/batter.webp'

img = cv2.imread(image_path)

new_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

ret, thresh = cv2.threshold(new_image, 80, 200, cv2.THRESH_BINARY)   # 0 -> Black color
                                                                     # 255 -> White color

cv2.imshow('image', img)
cv2.imshow('Grayscale', new_image)
cv2.imshow('image_threshold', thresh)


cv2.waitKey(0)