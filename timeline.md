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


July 14, 2022 11:44:36 AM

<br/>

- Might need to look into computer vision for more accurate detection of a hand.
- A possible comparison needs to be made between a simple DNN and a CNN to see which one works better.
- Need to implement a video system for classification

<br/>


July 19, 2022 6:37:20 PM

<br/>

- LSTMs are barely performing at all. Seems like noise isn't predictable at all.
- Repeated Random sequences works well. The accuracy jumps as a result of repeated data points but fine tuning gives a 100% accuracy.
- Maybe need to look into how well distributed this randomized dats is in order to analyze the underperforming model.
