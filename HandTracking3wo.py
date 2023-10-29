from fingerDetector import FingerDetector
from djitellopy import Tello
import cv2

detector = FingerDetector()

def setDirection(code):
    if code == 10:
        print('Connect')
        #command = action10()

    elif code == 1:
        print('TakeOFF')
        command = action11()


    elif code == 2:
        print('Rotate Left')
        command = action12()

    elif code == 3:
        print('Rotate Right')
        command = action13()

    elif code == 8:
        print('Landing')
        command = action14()

    elif code == 4:
        print('move_forward')
        command = action15()

    elif code == 5:
        print('move_back')
        command = action16()

    elif code == 6:
        print('rotate_clockwise')
        command = action17()

    elif code == 7:
        print('rotate_counter_clockwise')
        command = action18()
    else:
        print('stop')

def action10():
    global tello
    tello = Tello()
    tello.connect()

def action11():
    global tello
    global flying
    if not flying:
        tello.takeoff()
        flying = True


def action12():
    global tello
    tello.move_left(50)


def action13():
    global tello
    tello.move_right(50)

def action15():
    global tello
    tello.move_forward(50)


def action16():
    global tello
    tello.move_back(50)

def action17():
    global tello
    tello.rotate_clockwise(30)

def action18():
    global tello
    tello.rotate_counter_clockwise(30)

def action14():
    global tello
    global flying
    if flying:
        tello.land()
        flying = False

def practising():
    # when the user changes the pattern (new face, new pose or new fingers) the system
    # waits some time (ignore 8 video frames) for the user to stabilize the new pattern
    # we need the following variables to control this
    prevCode = -1
    cont = 0
    running = True
    cap = cv2.VideoCapture(0)
    print ('camara preparada')

    while running:
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        code, img = detector.detect(image)
        img = cv2.resize(img, (800, 600))
        img = cv2.flip(img, 1)

        # if user changed the pattern we will ignore the next 8 video frames
        if (code != prevCode):
            cont = 4
            prevCode = code
        else:
            cont = cont - 1
            if cont < 0:
                # the first 8 video frames of the new pattern (to be ignored) are done
                # we can start showing new results
                direction = setDirection(code)
                cv2.putText(img, direction, (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 10)
                if code == 7:
                    running = False

        cv2.imshow('video', img)
        cv2.waitKey(1)
    cv2.destroyWindow('video')
    cv2.waitKey(1)

print ('vamos a empezar')
action10()
flying = False
practising()