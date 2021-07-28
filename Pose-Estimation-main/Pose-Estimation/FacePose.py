import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_face = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face:
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img.flags.writeable = False
        result = face.process(img)
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if result.multi_face_landmarks:
            for face_landmark in result.multi_face_landmarks:
                mp_draw.draw_landmarks(img, face_landmark, mp_face.FACE_CONNECTIONS)
        cv2.imshow("Image",img)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()