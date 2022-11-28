import cv2
#đọc ảnh
img=cv2.imread("pic1/dua.jpg",1)

#xuất ảnh
cv2.imshow("Hello",img)

#resize ảnh
#img=cv2.resize(img,(1900,1280))
#img=cv2.resize(img,(0,0), fx=0.5, fy=0.5)

k=cv2.waitKey()
#Trả về mã ASCII
print(k)
#Lưu ảnh
if k==ord('f'):
    cv2.imwrite("anhmoi.jpg",img)