# STEP 1: Import the necessary modules.
import cv2
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='face_landmarker.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width, layer = frame_converted.shape
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_converted)
    
    result = detector.detect(mp_image) 
    face_landmarks = result.face_landmarks
    for idx, face in enumerate(face_landmarks):
            for lm in face:
                actualx = int(lm.x * width)
                actualy = int(lm.y * height)
                cv2.circle(frame, center=(actualx, actualy), radius=1, color=(0, 255, 0), thickness=-1)
    cv2.imshow("Face Landmarks", frame)
    cv2.waitKey(1)

