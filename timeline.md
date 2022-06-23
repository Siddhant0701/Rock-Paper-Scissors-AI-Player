# Timeline and events

</br>

June 7, 2022 9:03:29 PM

- Attempted creating a hand detection system using a Haar Cascade classifier.
- Haar Cascades do not have a defined way of detecting hands.
- Found an xml file [online](https://stackoverflow.com/questions/25542344/hand-detection-opencv)
- Doesn't work on anything other than a closed fist viewed from the side. 


</br>

June 15, 2022 11:13:01 PM

- [Google Open Source Module](https://google.github.io/mediapipe/). Can help in shortening the process of detection.
- Note: If this is that accurate, it might not even be necessary to build a CNN (Step 2) in order to classify an action.

<br/>


June 16, 2022 10:15:32 PM

<br/>

- Implemented Mediapipe hand detection.
- Can be used to produce a vector of coordinates for all the different parts of a hand.

<br/>


June 19, 2022 10:04:17 PM

<br/>

- Used tensorflow datasets to get the RPS images.
- Able to convert the images into vectors for easier training.

<br/>
