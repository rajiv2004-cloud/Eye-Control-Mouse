#importing the requring module & libray
import cv2
import mediapipe as mp
import pyautogui

#for acessing camera
cam = cv2.VideoCapture(0)
#for face mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
screen_x = 200  
screen_y = 200
while True:

    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    #for printing the cordinates of eye
    #print(landmark_point)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        frame_h, frame_w, _ = frame.shape
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0, 255, 0))
            if id == 1:
                # Getting current mouse loc
                new_screen_x = screen_w / frame_w * x
                new_screen_y = screen_h / frame_h * y

                # Calculating difference from previous frame
                screen_x += (new_screen_x - screen_x) * 1.5
                screen_y += (new_screen_y - screen_y) * 1.5
                print(screen_x, screen_y)
                # Clipping if gone too far
                if screen_x < 50:
                    screen_x = 100
                elif screen_x > screen_w - 50:
                    screen_x = screen_w - 100

                if screen_y < 50:
                    screen_y = 100
                elif screen_y > screen_h - 50:
                    screen_y = screen_h - 100

                # moving the cursor
                pyautogui.moveTo(screen_x, screen_y)

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0, 255, 255))
        if (left[0].y - left[1].y)    < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow("Eye control mouse", frame)
    cv2.waitKey(1)