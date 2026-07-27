import cv2
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width, layer = frame_converted.shape
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_converted)
    
    result = detector.detect(mp_image)  

    hand_landmarks = result.hand_landmarks
    for idx, hand in enumerate(hand_landmarks):
        biggestX = 0
        smallestX = 0
        biggestY = 0
        smallestY = 0
        for lm in hand:
            actualx = int(lm.x * width)
            actualy = int(lm.y * height)
            cv2.circle(frame, center=(actualx, actualy), radius=7, color=(0, 255, 0), thickness=2)
            if actualx >= biggestX:
                biggestX = actualx
            if actualy >= biggestY:
                biggestY = actualy
            if actualx <= smallestX or smallestX == 0:
                smallestX = actualx
            if actualy <= smallestY or smallestY == 0:
                smallestY = actualy

        if "Left" in str(result.handedness[idx]):
            colour = (0, 0, 0)
            cv2.rectangle(frame, (smallestX - 15, smallestY - 45), (smallestX + 37, smallestY - 15), (colour), 2)
            cv2.putText(frame, "Left", (smallestX - 10, smallestY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.67, (0, 0, 0), 2)
        if "Right" in str(result.handedness[idx]):
            colour = (255, 255, 255)
            cv2.rectangle(frame, (smallestX - 15, smallestY - 45), (smallestX + 50, smallestY - 15), (colour), 2)
            cv2.putText(frame, "Right", (smallestX - 10, smallestY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.67, (255, 255, 255), 2)
        cv2.rectangle(frame, (smallestX - 15, smallestY - 15), (biggestX + 15, biggestY + 15), (colour), 2)

        for hand in hand_landmarks:
                x4 = int(hand[4].x * width)
                y4 = int(hand[4].y * height)
                x8 = int(hand[8].x * width)
                y8 = int(hand[8].y * height)
                disX = (x8 - x4)
                disY = (y4 - y8)
                dis = math.sqrt((disX*disX) + (disY*disY))
                print(round(dis * 0.4))
                cv2.line(frame, (x4, y4), (x8, y8), (255, 255, 0), 3)  
    
        
   
            
    

    cv2.imshow("Hand Landmarks", frame)
    cv2.waitKey(1)