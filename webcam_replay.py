import numpy as np
import cv2


cap = cv2.VideoCapture(0)
record = []
k = 0
attack = False
rec = False
while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("Frame", frame)
    if attack is False:
        dup_frame = frame
    else:
        if k < len(record):
            dup_frame = record[k]
            k += 1
        else:
            k = 0
            dup_frame = record[k]


    cv2.imshow("Duplicate Frame", dup_frame)

    if rec is True:
        record.append(frame)


    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('c'):
        rec = True
    elif ch & 0xFF == ord('s'):
        rec = False
        attack = True




cap.release()
cv2.destroyAllWindows()
