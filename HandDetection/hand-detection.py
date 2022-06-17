import cv2
import mediapipe as mp


dict ={
    0: "WRIST",
    1: "THUMB_CMC",
    2: "THUMB_MCP",
    3: "THUMB_IP",
    4: "THUMB_TIP",
    5: "INDEX_FINGER_MCP",
    6: "INDEX_FINGER_PIP",
    7: "INDEX_FINGER_DIP",
    8: "INDEX_FINGER_TIP",
    9:  "MIDDLE_FINGER_MCP",
    10: "MIDDLE_FINGER_PIP",
    11: "MIDDLE_FINGER_DIP",
    12: "MIDDLE_FINGER_TIP",
    13: "RING_FINGER_MCP",
    14: "RING_FINGER_PIP",
    15: "RING_FINGER_DIP",
    16: "RING_FINGER_TIP",
    17: "PINKY_MCP",
    18: "PINKY_PIP",
    19: "PINKY_DIP",
    20: "PINKY_TIP",
}

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# hands = mp_hands.Hands(
#     static_image_mode= True,
#     max_num_hands = 3,
#     min_detection_confidence=0.5)

# img = cv2.imread(r'hand-images/front.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# results = hands.process(img)
# img.flags.writeable= True

# for hand_landmark in results.multi_hand_world_landmarks:
#     for item in dict:
#         print(f'{dict[item]} : {hand_landmark.landmark[mp_hands.HandLandmark[dict[item]]]}')

# print(f'Hand Landmarks: {results.multi_hand_world_landmarks}\n')
# print(f'Handedness: {results.multi_handedness}\n')

# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# for landmarks in results.multi_hand_landmarks:
#     mp_drawing.draw_landmarks(img, landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style())

# cv2.imshow('Image',img)
# cv2.waitKey(0)




 ### WEBCAM
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(0) & 0xFF == 27:
      break
cap.release()
