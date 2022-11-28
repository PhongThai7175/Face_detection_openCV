import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() #đẩy ảnh vào khung hình

#chia làm 4 khung hình
    '''width = int (cap.get(3))
    height = int(cap.get(4))
    small_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image = np.zeros(frame.shape,np.uint8)
    image[:height//2,:width//2]=small_frame
    image[:height//2,width//2:]=small_frame
    image[height//2:,:width//2]=small_frame
    image[height//2:,width//2:]=small_frame '''
    cv2.imshow("cam", frame)

    if cv2.waitKey(1)== ord("f"):
        break
cap.release()
cv2.destroyAllWindows()