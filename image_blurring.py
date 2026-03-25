import cv2 


image_path = cv2.imread('image_path/Freelance.jpg')

image_resize = cv2.resize(image_path, (681, 1024))

k_size = 7  # 7 * 7 matrix

blur_image = cv2.blur(image_resize, (k_size, k_size))
img_gaussianblur = cv2.GaussianBlur(image_resize, (k_size, k_size), 5) # where is the SD(Standard Deviation)
img_mediumblur = cv2.medianBlur(image_resize, k_size)


cv2.imshow('image', image_resize)
cv2.imshow('blur_image', blur_image)
cv2.imshow('Gaussian_blur_image', img_gaussianblur)
cv2.imshow('Medium_image', img_mediumblur)

cv2.waitKey(0)