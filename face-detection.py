import cv2 
import cv2.data  
import os

#print(os.listdir(cv2.data.haarcascades))
filename= "haarcascade_frontalface_alt2.xml"
path = cv2.data.haarcascades + filename
image = cv2.imread("person.jpeg")

modal =cv2.CascadeClassifier(path)
faces = modal.detectMultiScale(image,1.3,5)

for face in faces:
    x1 = face[0]
    y1 = face[1]
    x2 = x1 + face[2]
    y2 = y1 + face[3]

    cv2.rectangle(image,(x1,y1),(x2,y2),[255,0,0],2) 
#print(faces)
cv2.imshow("Person Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()