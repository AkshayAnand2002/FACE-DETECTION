import cv2
face_cascade=cv2.CascadeClassifier(r'C:\Users\aksha\OneDrive\Desktop\some img_recog\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\aksha\OneDrive\Desktop\Akshay_Photo.jpg')
#HAAR CASCADE CLASSIFIER WORKS WITH GRAY SCALE IMAGES ONLY.
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect faces
faces=face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('img',img)
cv2.waitKey()
