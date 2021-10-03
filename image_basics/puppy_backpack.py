import cv2
import numpy as np

img = cv2.imread('../Resources/Computer-Vision-with-Python/DATA/dog_backpack.jpg')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,0,255), 10)
        
# Hooking up callbacks with functions
cv2.namedWindow(winname='my_drawing')
# cv2.setMouseCallback('my_drawing', draw_circle)
cv2.setMouseCallback('my_drawing', draw_circle)

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()