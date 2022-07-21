# Rock Paper Scissors AI - Predictive Player

Note: This project is still a Work in Progress.

## Introduction

The purpose of this project is to build an AI application that can play rock-paper scissors and win ~60%-65% of the time. A randomized program can win around ~33% of the time, so the goal is to almost double that rate using `Machine Learning techniques` and algorithms.

Another goal is to build the game such that there is no need to use a keyboard/mouse for the human to input their actions. This can be achieved by using their webcam and anaylzing their gestures using `Computer Vision`.
<br/>
<br/>


## Plan
There are 4 possible applications that can be derived from the project:

1. Hand Detection System - A program that is able to detect a hand properly from images or a live stream.
   
2. Gesture Classifier - A classifier that is able to differentiate between rock, paper and scissors based on the image alone.
   
3. AI Predictive Player - An AI player that learns from the patterns of someone playing with them and tries to win majority of the time.

4. Full Stack App - An application using databases and frontend that captures all this together.
<br/>
<br/>

## Hand Detection System

<br/>

The motivation for this system was to accurately capture a hand gesture along with a bounding box that can be fed into a network for gesture classification. This is important because, it can help trim out the unnecessary details in the captured image and also helps to make sure that any images being fed into the classifier are images that actually contain a hand gesture.

<br/>

Initially, `Haar Cascades` was considered along with `Open-CV`'s cascade classifier in order the properly detect a hand, but there are a couple problems with that:

- It is very vulnerable to random features in the images and could lead to many false positives.
- There aren't a lot of statistical parameters to control which can cause problems in the detection of at most, one hand.
- The already available `.xml` cascade files detect closed fists well, but are unable to detect any other gesture. 
  
<br/>

[<img src=images/cascade.jpg height=300>](images/cascade.jpg)
[<img src=images/open-hand-cascade.jpg height=300>](images/open-hand-cascade.jpg)

<br/>

A way to deal with would be to use Google's `Mediapipe` APIs in order to detect hands properly. It has the `Solutions` API that detects a hand and returns the coordinates of 21 different points on the hand. For utility, there is also a `Drawings` API that allows one to visualize these coordinates.

<br/>

[<img src=images/mediapipe.jpg height=300>](images/mediapipe.jpg)

<br/>

This can also help in improving the model that classifies the gestures.


<br/>
<br/>

## Gesture Classifier

<br/>

The goal for this application is build and fine-tune a model that can classify a gesture into either of rock, paper or scissors using `Tensorflow`'s `Keras` API to build a `Neural Network`. `Tensorflow Datasets` has a set of CGI-generated images of hands that can be used as the data to train and test the model. There are two ways to build this model:

- Using a `Convolutional Neural Network` by creating a bounding box on the hand from `Mediapipe` coordinates.
- Using a `Dense Neural Network` by using numerical coordinates from the `Mediapipe MULTI_HAND_WORLD_LANDMARKS` output.

Note: It is better to use `MULTI_HAND_WORLD_LANDMARKS` as the output as compared to others as it uses the approximate geometric center of the hand as the origin. This makes the data easier to manipulate and augment.

<br/>

### Performance Analysis

1. *Dense Network* - This network achieves an accuracy of about ~99%. Training and loss per epoch is also very optimal for both training and validation sets. It also achieves ~100% accuracy on a test dataset.

<br/>

[<img src=images/dnn_accuracy.jpg alt=CNN accuracy per epoch height=250>](images/dnn_accuracy.jpg)
[<img src=images/dnn_loss.jpg alt=CNN accuracy per epoch height=250>](images/dnn_loss.jpg)

<br/>

   
2. *Convvolutional Network* - This network achieves an accuracy of ~98% with the training data and ~94% with the test data. After about 8 epochs, the validation loss starts to increase, showing signs of overfitting. 

<br/>

[<img src=images/cnn_accuracy.jpg alt=CNN accuracy per epoch height=250>](images/cnn_accuracy.jpg)
[<img src=images/cnn_loss.jpg alt=CNN accuracy per epoch height=250>](images/cnn_loss.jpg)

<br/>

Based on this data, it is better to use the `DNN classifier` as it is much faster and shows much more promising results. The accuracy and loss per epoch changes at a steady and comparitively smooth rate. The charts for `CNN` are more instable in comparison. Also, because the `DNN` converts the image into coordinates, it is easier to predict on the images as it wouldn't consider/confuse features with background noise.


