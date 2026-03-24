import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist
import pygame
import os

# INIT
pygame.mixer.init(frequency=22050, size=-16, channels=2)

alarm_path = os.path.join(os.getcwd(), "alarm.wav")

def calculate_EAR(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

EYE_THRESH = 0.30
EYE_FRAMES = 10
counter = 0

mp_face_mesh = mp.solutions.face_mesh

# 👇 THIS PART WAS MISSING
cap = cv2.VideoCapture(0)   # or "videos/demo.mp4"

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                left_eye = []
                right_eye = []

                for idx in LEFT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    left_eye.append((x, y))

                for idx in RIGHT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    right_eye.append((x, y))

                ear = (calculate_EAR(left_eye) + calculate_EAR(right_eye)) / 2.0

                cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                if ear < EYE_THRESH:
                    counter += 1

                    if counter >= EYE_FRAMES:
                        cv2.putText(frame, "DROWSINESS ALERT!", (50, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

                        try:
                            if not pygame.mixer.music.get_busy():
                                pygame.mixer.music.load(alarm_path)
                                pygame.mixer.music.play()
                        except Exception as e:
                            print("Sound Error:", e)

                else:
                    counter = 0
                    pygame.mixer.music.stop()

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()