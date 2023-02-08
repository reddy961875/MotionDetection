import cv2
import time
from skimage.metrics import structural_similarity
from datetime import datetime


def spot_diff(frame1, frame2):
    frame1 = frame1[1]
    frame2 = frame2[1]

    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    g1 = cv2.GaussianBlur(g1, (5, 5), 0)
    g2 = cv2.GaussianBlur(g2, (5, 5), 0)

    (score, diff) = structural_similarity(g2, g1, full=True)

    print("Image similarity:", score)

    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = [c for c in contours if cv2.contourArea(c) > 100]

    if len(contours):
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    else:
        print("No differences detected.")
        return 0

    cv2.imshow("Difference", thresh)
    cv2.imshow("Result", frame1)
    cv2.imwrite("stolen/" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".jpg", frame1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 1
