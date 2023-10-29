from fingerDetector import FingerDetector
import HandTracking3wo
import EyeTrackingVer2
import cv2
detector = FingerDetector()


def practising():
    running = True
    cap = cv2.VideoCapture(0)
    print('camara preparada')

    while running:
        success, image = cap.read()

        def funcHand():
            print("Hand tracking is active")
            # HandTracking3wo.py executed as script
            funcHand()

            HandTracking3wo.funcHand()

if not success:
            print("Eye tracking take over")
        def funceye():
            running1 = True
            while running1:
        # EyeTrackingVer2.py executed as script
funceye()
EyeTrackingVer2.funceye()
running1 = False

success, image = cap.read()
print("Hand tracking take over")
# HandTracking3wo.py executed as script
HandTracking3wo.funcHand()
running = False
