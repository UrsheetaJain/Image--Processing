import cv2
image = cv2.imread("person.jpeg")
cv2.imshow("person",image)
cv2.waitKey(0)
cv2.destoryAllWindows()
