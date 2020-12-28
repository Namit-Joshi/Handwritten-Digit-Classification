# Handwritten-Digit-Classification

## Overview
This is a Flask web app in which the user draws any digit ranging from 0-9 and the app tries to recognize which digit the user has drawn.

## Demo
Link: [https://digit-recognition-nj.herokuapp.com/](https://digit-recognition-nj.herokuapp.com/)

[![](https://i.imgur.com/SroZ7hg.png)](https://digit-recognition-nj.herokuapp.com/)

[![](https://imgur.com/jgoAMDp.png)](https://digit-recognition-nj.herokuapp.com/)

## About the Dataset
MNIST dataset contains images of handwritten digits. It has 60,000 grayscale images under the training set and 10,000 grayscale images under the test set taken from American Census Bureau employees and American high school students 

The state of the art result for MNIST dataset has an accuracy of 99.79%. I have achieved an accuracy of 99.32% .I have used the Keras library with Tensorflow backend to classify the images.

# Different Layers in CNNs
## Convolutional Layers
Convolutional layer is the very first layer where we extract features from the images in our datasets. Due to the fact that pixels are only related with the adjacent and close pixels, convolution allows us to preserve the relationship between different parts of an image. Convolution is basically filtering the image with a smaller pixel filter to decrease the size of the image without loosing the relationship between pixels.

## Pooling Layer
When constructing CNNs, it is common to insert pooling layers after each convolution layer to reduce the spatial size of the representation to reduce the parameter counts which reduces the computational complexity. In addition, pooling layers also helps with the overfitting problem. Basically we select a pooling size to reduce the amount of the parameters by selecting the maximum, average, or sum values inside these pixels.I have used max pooling in my classification model.

## Fully Connected Layers
A fully connected network is our RegularNet where each parameter is linked to one another to determine the true relation and effect of each parameter on the labels. Since our time-space complexity is vastly reduced thanks to convolution and pooling layers, we can construct a fully connected network in the end to classify our images.

<br></br>

<img src="https://user-images.githubusercontent.com/42213693/90432513-44d3ff00-e0e8-11ea-8f01-b35a67030df0.jpeg">


## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>  ](https://flask.palletsprojects.com/en/1.1.x/) 
&nbsp;
[<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=250>  ](https://gunicorn.org) 
&nbsp;
[<img target="_blank" src="https://keras.io/img/logo.png" width=200>  ](https://keras.io/)
&nbsp;
[<img target="_blank" src="https://numpy.org/images/logos/numpy.svg" height=75 width=100>  ](https://numpy.org/)
&nbsp;
