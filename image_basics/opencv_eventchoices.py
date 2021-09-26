import cv2
import numpy as np

DRAWING = False
IX,IY = -1,-1

# Draw circle with left mouse button
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)
        
def draw_rectangle(event, x, y, flags, param):
    global IX,IY,DRAWING
    
    if event == cv2.EVENT_LBUTTONDOWN:
        DRAWING = True
        IX,IY = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if DRAWING:
            cv2.rectangle(img, (IX,IY), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        DRAWING = False
        cv2.rectangle(img, (IX,IY), (x,y), (0,255,0), -1)
        
# Showing image with cv2
img = np.zeros((512,512,3)) # image looks gray if 8 bit image when dtype=np.int8

# Hooking up callbacks with functions
cv2.namedWindow(winname='my_drawing')
# cv2.setMouseCallback('my_drawing', draw_circle)
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()