import cv2


image_path = 'image_path/parrot_image.jpg'

k_size = 7

img = cv2.imread(image_path)

img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 100)
img_median_blur = cv2.medianBlur(img, k_size)


cv2.imshow('image', img)
cv2.imshow('image_blur', img_blur)
cv2.imshow('image_gausian_blur', img_gaussian_blur)
cv2.imshow('image_median_blur', img_median_blur)
cv2.waitKey(0)