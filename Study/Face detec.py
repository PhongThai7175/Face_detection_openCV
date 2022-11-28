import cv2
import face_recognition

imgly = face_recognition.load_image_file("pic1/ly.jpg")
imgly = cv2.cvtColor(imgly,cv2.COLOR_BGR2RGB)

imgCheck = face_recognition.load_image_file("pic1/lyCheck.jpg")
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

#Xác định vị trí khuôn mặt
faceloc = face_recognition.face_locations(imgly)[0]
print(faceloc) #(y1 x2, y2 x1) tạo độ hình chữ nhật xđ khuôn mặt lấy tại

#mã hóa hình
encodely = face_recognition.face_encodings(imgly)[0]

cv2.rectangle(imgly, (faceloc[3],faceloc[0], faceloc[1], faceloc[1]), (255,0,255),2)

#ảnh Check
faceCheck = face_recognition.face_locations(imgCheck)[0]
encodeCheck = face_recognition.face_encodings(imgCheck)[0]
cv2.rectangle(imgCheck, (faceCheck[3],faceCheck[0], faceCheck[1], faceCheck[1]), (255,0,255),2)

results = face_recognition.compare_faces([encodely], encodeCheck)
#print(results)

#Sai số khi khác mặt
saiso = face_recognition.face_distance([encodely], encodeCheck)
print(results,saiso)
#Thêm sai số vào hình
cv2.putText(imgCheck,f"{results} {(1-(round(saiso [0],2))) *100}%", (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow("Ly",imgly)
cv2.imshow("Ly Check",imgCheck)
cv2.waitKey(0)

