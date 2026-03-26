import cv2


image_path = 'image_path/white_board.jpg'

image = cv2.imread(image_path)
resize_image = cv2.resize(image, (600, 700))


# line
cv2.line(resize_image, (100, 150), (300, 450), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(resize_image, (200, 350), (450, 600), (0, 0, 255), 5)

# Circle
cv2.circle(resize_image, (300, 150), 100, (255, 0, 0), 10)



cv2.imshow('white_board', resize_image)
cv2.waitKey(0)