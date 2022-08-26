import tensorflow_datasets as tfds
import numpy as np
import mediapipe as mp
from time import process_time
import os

## Env variables
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
os.environ["GLOG_minloglevel"] ="2"


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
mp_hands = mp.solutions.hands
hands = mp_hands.Hands( 
    static_image_mode= True,
    max_num_hands = 3,
    min_detection_confidence=0.5)

## Transform the image to a vector with 21 coordinates.
def image_to_vector(img):
    try:
        result_vector =[]
        result = hands.process(img)

        for hand_landmark in result.multi_hand_world_landmarks:
            for item in dict:
                landmarkObj = hand_landmark.landmark[mp_hands.HandLandmark[dict[item]]]
                result_vector.append([landmarkObj.x,landmarkObj.y, landmarkObj.z])
        
        return result_vector
    
    except:
        return ('NIL')


## Load dataset
(train_images,train_labels) = tfds.as_numpy(tfds.load('rock_paper_scissors', split='train[:70%]', batch_size=-1, as_supervised = True))
(validation_images,validation_labels) = tfds.as_numpy(tfds.load('rock_paper_scissors', split='train[70%:]', batch_size=-1, as_supervised = True))
(test_images,test_labels) = tfds.as_numpy(tfds.load('rock_paper_scissors', split='test', batch_size=-1, as_supervised = True))


start = process_time()

## Transforming data as necessary
train_data = [image_to_vector(img) for img in train_images]
test_data = map(image_to_vector, test_images)
validation_data = [image_to_vector(img) for img in validation_images]

mid = process_time()

## Filter out unprocessable images
train_data = list(filter(lambda x : x != 'NIL', train_data))
test_data = list(filter(lambda x : x != 'NIL', test_data))
validation_data = list(filter(lambda x : x != 'NIL', validation_data))


## Convert to numpy arrays
train_data = np.array(train_data)
test_data = np.array(test_data)
validation_data = np.array(validation_data)


end = process_time()
print(f'Time - {end -start}s\n Conversion Time - {mid-start}s \nTest Data - {test_data} \nTrain Data - {train_data} \nValidation Data - {validation_data}')


