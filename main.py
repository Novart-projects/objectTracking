import cv2
import numpy as np

def Tracking():
    min_color = np.array((30, 60, 60), np.uint8)
    max_color = np.array((90, 170, 170), np.uint8)
    cap = cv2.VideoCapture("IMG_0390.mov")
    tr = []
    while (cap.isOpened()):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv, min_color, max_color)
        for i in tr:
            cv2.circle(frame, i, 10, (0, 255, 255), -1)
        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 10:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            tr.append((x, y))
        frame = cv2.resize(frame, (900, 500), cv2.INTER_NEAREST)
        cv2.imshow("tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    Tracking()

