import cv2


image_path = "image_path/image.jpg"
img = cv2.imread(image_path)

print(img.shape)


resized_image = cv2.resize(img, (800, 500))

print(resized_image.shape)

cv2.imshow('image', resized_image)

cropped_image = resized_image[200:400, 150:300]

cv2.imshow('cropped_image', cropped_image)

cv2.waitKey(0)

