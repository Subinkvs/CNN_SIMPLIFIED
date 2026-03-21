import cv2
import os

video_path = 'video.mp4'
video = cv2.VideoCapture(video_path)


ret = True

while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(16) # 60 FPS  1000/60 = 16.6

video.release()
cv2.destroyAllWindows()