import numpy as np
import cv2
import datetime

print("Start capturing camera")
cap = cv2.VideoCapture(0)
# Default size: 780 x 1280
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
  
    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('s'):
        now = datetime.datetime.now()
        filename = now.strftime("%Y%m%d_%H%M%S")
        print(filename)
        cv2.imwrite(filename + '.png', frame)
        img = cv2.imread(filename + '.png')
        # height, width = img.shape[:2]
        # f = open(filename + '_pixels.txt', 'w')
        # f.write(','.join(str(v) for v in img.tolist()))
        # f.close()
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()