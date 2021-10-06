import cv2
import datetime
import os

face_cascade = cv2.CascadeClassifier(r'C:\Users\k019c1068\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
i=0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
      cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
      face = img[y: y + h, x: x + w]
      face_gray = gray[y: y + h, x: x + w]
      cv2.putText(img, "",(20,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,200), 2, cv2.LINE_AA)
    cv2.imshow('video image', img)
    key = cv2.waitKey(10)

    #i+=1
    #1秒ごとに撮影が100
    if(i % 10 == 0):
      date0=datetime.datetime.now()
      date_str_form=date0.strftime("%Y%m%d_%H%M%S_%f")
      path = "C:\\Users\\k019c1068\\Desktop\\hozon"
      cv2.imwrite(os.path.join(path , date_str_form+".jpg"), img)

    if key == 27:
      break

cap.release()
cv2.destroyAllWindows()