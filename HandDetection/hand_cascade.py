import cv2 as cv

vid = cv.VideoCapture(0)

while(True):
    ret, img = vid.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('hand.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)


    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    cv.imshow('Webcam', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv.destroyAllWindows()
