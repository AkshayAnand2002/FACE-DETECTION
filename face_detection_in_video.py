import cv2
face_cascade=cv2.CascadeClassifier(r'C:\Users\aksha\OneDrive\Desktop\some img_recog\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(r'C:\Users\aksha\OneDrive\Desktop\some img_recog\output.avi')
while cap.isOpened():
    _,img=cap.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect faces
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()

