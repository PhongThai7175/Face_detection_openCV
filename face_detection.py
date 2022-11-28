import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

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
#print(len(encodelistknow))

#lưu danh sách đối tượng xuất hiện
def ketqua(name):
    with open("ketqua.csv", "r+") as f: #r+ là chế độ vừa đọc vừa ghi
        myDatalist = f.readline() #đọc tất cả các line
        nameList = []

        for line in myDatalist:
            entry = line.split(",") #Tách theo dấu ,
            nameList.append(entry[0]) #Tách 2 phần tử tên và thời gian (0,1) nên lấy tên = 0
        if name not in nameList:
            now = datetime.now()
            dinhdanggio = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dinhdanggio}")

#mo cam
cap =cv2.VideoCapture(0)
#cap =cv2.VideoCapture("Comp 2.mp4")
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
            ketqua(name)
        else:
            name = "Ai vay?"
        #print tên
        y1, x2, y2, x1 = faceloc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),2)
        cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2 )

        cv2.imshow("Result", frame)
        if cv2.waitKey(1) == ord("p"):
            break
cap.release()
cv2.destroyAllWindows()


