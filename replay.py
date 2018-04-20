import cv2
import numpy as np

cap = cv2.VideoCapture("HMD.mkv")
count = 0
j = 1
dup_frame = []
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    if ret == True:
        count += 1
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    dupli = frame

    if count >= 45:
        print(j)
        dupli = dup_frame[j-1]
        cv2.imshow('Color Frame', dupli)
        k = len(dup_frame)
        print("k ="+str(k))
        if j < k:
            j += 1
        else:
            j = 1



    else:
        cv2.imshow('Color Frame',dupli)
        dup_frame.append(frame)

    cv2.imshow('Frame',gray)
    if cv2.waitKey(51) & 0xFF ==ord('q'):
        break

cap.release()
print(count)
cv2.destroyAllWindows()

