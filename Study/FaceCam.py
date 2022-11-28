import cv2
import face_recognition
import os
import numpy as np
#Load ảnh
path= "pic2"
ima = []
classNames = []
myList = os.listdir(path)
print(myList)
for he in myList:
    print(he)
    anhhientai = cv2.imread(f"{path}/{he}")
    ima.append(anhhientai)
    classNames.append(os.path.splitext(he)[0])
print(len(ima))
print(classNames)

#Encoding
def mahoa (ima):
    encodelist = []
    for img in ima:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img) [0]
        encodelist.append(encode)
    return encodelist

encodelistknow = mahoa(ima)
print("Success")
print(len(encodelistknow))

#mo cam
cap =cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frameS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

#xác định vị trí khuôn mặt, encode ảnh trên cam
    facecurFram = face_recognition.face_locations(frameS) #lấy từng vị trí khuôn mặt hiện tại
    encodecurFram = face_recognition.face_encodings(frameS)

    for encodeFace, faceloc in zip(encodecurFram,facecurFram):
        matches = face_recognition.compare_faces(encodelistknow,encodeFace)
        faceDis = face_recognition.face_distance(encodelistknow,encodeFace) #xem khoảng cách giống nhau
        print(faceDis)
        matchIndex = np.argmin(faceDis) #Trả về index dis nhỏ nhất

        if faceDis[matchIndex] <0.50 :
            name = classNames[matchIndex].upper()
        else:
            name = "Ai vay?"
        #print tên
        y1, x2, y2, x1 = faceloc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2 )

        cv2.imshow("hehe", frame)
        if cv2.waitKey(1) == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()


