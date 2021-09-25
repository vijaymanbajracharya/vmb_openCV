import cv2

img = cv2.imread('../Resources/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    
    # If we have waited atleast 1ms and we have pressed the Esc key (27)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
        

