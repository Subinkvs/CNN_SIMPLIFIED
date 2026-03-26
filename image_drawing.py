import cv2


image_path = 'image_path/white_board.jpg'

image = cv2.imread(image_path)
resize_image = cv2.resize(image, (600, 700))


"""
Draw a line on the image.

Parameters:
-----------
resize_image : ndarray
    The image on which the line is drawn.
(100, 150) : tuple
    Starting point (x, y).
(300, 450) : tuple
    Ending point (x, y).
(0, 255, 0) : tuple
    Color in BGR format (Green).
3 : int
    Thickness of the line.
"""
cv2.line(resize_image, (100, 150), (300, 450), (0, 255, 0), 3)


"""
Draw a rectangle on the image.

Parameters:
-----------
resize_image : ndarray
    The image on which the rectangle is drawn.
(200, 350) : tuple
    Top-left corner (x, y).
(450, 600) : tuple
    Bottom-right corner (x, y).
(0, 0, 255) : tuple
    Color in BGR format (Red).
5 : int
    Thickness of the rectangle border.
    Use -1 to fill the rectangle.
"""
cv2.rectangle(resize_image, (200, 350), (450, 600), (0, 0, 255), 5)


"""
Draw a circle on the image.

Parameters:
-----------
resize_image : ndarray
    The image on which the circle is drawn.
(300, 150) : tuple
    Center of the circle (x, y).
100 : int
    Radius of the circle.
(255, 0, 0) : tuple
    Color in BGR format (Blue).
10 : int
    Thickness of the circle boundary.
    Use -1 to draw a filled circle.
"""
cv2.circle(resize_image, (300, 150), 100, (255, 0, 0), 10)



cv2.imshow('white_board', resize_image)
cv2.waitKey(0)