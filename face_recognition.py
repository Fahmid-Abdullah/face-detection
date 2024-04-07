import threading
import cv2 as cv
from deepface import DeepFace
import numpy as np
import ctypes

user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
notMatchCounter = 0

face_match = False
reference_img = cv.imread('E:/projects/face-recognition/reference_img.jpg') # Hardcode the path to run script.bat without errors

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except Exception as e:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0: # Every 30 frames
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv.putText(frame, "Match", (20, 450), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0), 3) # BGR
            notMatchCounter = 0
        else:
            notMatchCounter += 1
            if notMatchCounter >= 10:
                # Creating a red rectangle image
                red_screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
                red_screen[:, :] = (0, 0, 255)

                # Define text properties
                text = "Unauthenticated User Detected"
                font = cv.FONT_HERSHEY_DUPLEX
                font_scale = 3
                font_thickness = 5
                text_color = (255, 255, 255)  # White color

                # Get the size of the text to center it
                text_size = cv.getTextSize(text, font, font_scale, font_thickness)[0]
                text_x = (screen_width - text_size[0]) // 2
                text_y = (screen_height + text_size[1]) // 2

                # Put the text on the screen
                cv.putText(red_screen, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

                # Show the screen
                cv.namedWindow("No Match", cv.WINDOW_NORMAL)  # Enable resizing
                cv.setWindowProperty("No Match", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)  # Fullscreen mode
                cv.imshow("No Match", red_screen)


        #cv.namedWindow("Face Authentication", cv.WINDOW_NORMAL)  # Enable resizing
        #cv.setWindowProperty("Face Authentication", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)  # Fullscreen mode
        #cv.imshow("Face Authentication", frame) # Show camera input

        # Close the red screen window if a match is found
        if face_match:
            if cv.getWindowProperty("No Match", cv.WND_PROP_VISIBLE) > 0:
                cv.destroyWindow("No Match")


    key = cv.waitKey(1)
    if key == ord("q"):
        break

cv.destroyAllWindows()
