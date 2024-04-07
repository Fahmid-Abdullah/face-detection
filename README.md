# Face Recognition Script
This script uses OpenCV and the DeepFace library to perform real-time face recognition. It captures video from a webcam, compares the faces in the video frames to a reference image, and displays a message if a match is found or if an unauthenticated user is detected.

Requirements
- Python 3.x
- OpenCV (cv2)
- DeepFace
- NumPy

Install the required packages using pip:

```bash
pip install opencv-python deepface numpy
```

Additionally, you may get an error that asks you to install tf-keras. If so, install it similarly as the other packages:

```bash
pip install tf-keras
```

If you are using a python environment, you have to update script.bat:
```bash
@echo off
cd /d %~dp0
python face_recognition.py %*
pause
```
with the name of your environment. For example, if I am using a conda environment called base, I would add the following:

```bash
@echo off
call conda activate base
cd /d %~dp0
python face_recognition.py %*
pause
```

# Usage
1. Clone the repository or download the script.
2. Take a picture of yourself and save it somewhere on your computer.
3. In face_recognition.py, update 

```bash
reference_img = cv.imread('E:/projects/face-recognition/reference_img.jpg')
```

with the exact path of the image you took earlier.

4. Run the script using:

```bash
python face_recognition.py
```

or run script.bat

5. Press q to quit the application.

# Notes
- The script uses a separate thread to perform face recognition, which allows for smoother video processing.
- If the script detects an unauthenticated user (i.e., a face that does not match the reference image) for 10 consecutive frames, it displays a red screen with a warning message.
- Adjust the path to the reference image as needed in the reference_img variable.
- The script is currently configured to work on Windows. Modify the screen resolution detection (screen_width and screen_height) for other operating systems.
