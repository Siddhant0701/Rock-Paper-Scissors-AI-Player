from tensorflow import keras
import mediapipe as mp
import numpy as np
import cv2 as cv
from time import sleep
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL


vid = cv.VideoCapture(0)
hands = mp.solutions.hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

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


class Model:
    def __init__(self, model_path):
        self.labels = {0: "Rock", 1: "Paper", 2: "Scissors"}
        self.model = keras.models.load_model(model_path)

    def predict(self, img):

        processed_coordinates = self.__process_img(img)
    
        if(np.max(processed_coordinates) == 0 or len(processed_coordinates) > 1):
            return "Nil"
    
        classes = self.model.predict(processed_coordinates, verbose=0)
        return self.labels[np.argmax(classes)]
            


    def __process_img(self,img):
        try:
            result_vector =[]
            result = hands.process(img)

            for hand_landmark in result.multi_hand_world_landmarks:
                for item in dict:
                    landmarkObj = hand_landmark.landmark[mp.solutions.hands.HandLandmark[dict[item]]]
                    result_vector.append([landmarkObj.x,landmarkObj.y, landmarkObj.z])
            
            data = np.reshape(np.array(result_vector, dtype=np.float64), (-1,63))
            data = (data - np.min(data)) / (np.max(data) - np.min(data))
            return data

        except:
            return np.zeros(63, dtype=np.float64)



model = Model('../models/model.h5')

## Get main coordinates of the hand
def image_to_vector(img):
    try:
        result_vector =[]
        result = hands.process(img)
        height = img.shape[0]
        width = img.shape[1]

        for hand_landmark in result.multi_hand_landmarks:
            for item in dict:
                landmarkObj = hand_landmark.landmark[mp.solutions.hands.HandLandmark[dict[item]]]
                result_vector.append([landmarkObj.x * width,landmarkObj.y * height])
        
        return np.array(result_vector, dtype=np.float64)
    
    except:
        return np.reshape(np.zeros(63, dtype=np.float64), (21,3))


def get_bounding_box(img):
    result = image_to_vector(img)
    max_x, min_x = np.max(result[:,0]), np.min(result[:,0])
    max_y, min_y = np.max(result[:,1]), np.min(result[:,1])

    max_x, max_y, min_x, min_y = int(max_x), int(max_y), int(min_x), int(min_y)
    return [(min_x, min_y), (max_x, max_y)]




while True:
    ret, img = vid.read()

    bbox = get_bounding_box(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    img = cv.rectangle(img, bbox[0], bbox[1], (0,255,0), 2)
    result = model.predict(img)
    img = cv.putText(img, result, (bbox[0][0], bbox[0][1]), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv.imshow('Webcam', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv.destroyAllWindows()
