import cv2
import numpy as np
import mediapipe as mp
import math
import time

mp_face_mesh=mp.solutions.face_mesh
face_mesh=mp_face_mesh.FaceMesh(static_image_mode=False,max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5)
mp_drawing=mp.solutions.drawing_utils
path=0
cap=cv2.VideoCapture(path)
while(1):
    ret,frame=cap.read()
    if not ret:
        break
    rbg_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=face_mesh.process(rbg_frame)
    if results.multi_face_landmarks:
        for face_landmark in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(frame,face_landmark,mp_face_mesh.FACEMESH_IRISES,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing.DrawingSpec(thickness=1,circle_radius=1))
    cv2.imshow("results",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()