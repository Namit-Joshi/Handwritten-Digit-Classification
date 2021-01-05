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

## Deployment on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download Heroku CLI to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Follow the instructions given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) on how to deploy a web app.

## Directory Tree 
```
├── static 
│   ├── css
|   |   ├──style.css
|   ├── js
|   |   ├──canvas.js
├── templates
│   ├── index.html
│   ├── results.html
├── MNIST_final.ipynb
├── Procfile
├── README.md
├── app.py
├── finalmodel.h5
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" width=170>  ](https://flask.palletsprojects.com/en/1.1.x/) 
&nbsp;
[<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=250>  ](https://gunicorn.org) 
&nbsp;
[<img target="_blank" src="https://keras.io/img/logo.png" width=200>  ](https://keras.io/)
&nbsp;
[<img target="_blank" src="https://numpy.org/images/logos/numpy.svg" height=75 width=100>  ](https://numpy.org/)
&nbsp;
