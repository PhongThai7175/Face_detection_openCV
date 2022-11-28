import cv2
img=cv2.imread("pic1/dua.jpg",1)

print(img.shape)
print(type (img))
print(img[153])

cv2.imshow("Hello",img)
cv2.waitKey()