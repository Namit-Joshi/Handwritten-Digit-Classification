from flask import Flask, request, render_template
from flask_cors import cross_origin
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model
import base64
import numpy as np
import cv2

#Initialize the useless part of the base64 encoded image.
init_Base64 = 21

#Initializing the Default Graph (prevent errors)
global graph
graph = tf.compat.v1.get_default_graph()

app = Flask(__name__, template_folder='templates')

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

#Second route : Use our model to make prediction - render the results page.
@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
        with graph.as_default():
            if request.method == 'POST':
                    model = load_model("finalmodel.h5")
                    final_pred = None
                    #Preprocess the image : set the image to 28x28 shape
                    #Access the image
                    draw = request.form['url']
                    #Removing the useless part of the url.
                    draw = draw[init_Base64:]

                    #print('Image URL: {}'.format(draw))
                    #Decoding
                    draw_decoded = base64.b64decode(draw)
                    image = np.asarray(bytearray(draw_decoded), dtype="uint8")
                    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

                    # print('Image received: {}'.format(image.shape))

                    #Resizing and reshaping to keep the ratio.
                    resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
                    vect = np.asarray(resized, dtype="uint8")

                    #print('Numpy Array: {}'.format(vect.shape))

                    vect = vect.reshape(1, 28, 28, 1).astype('float32')
                    vect = vect/255

                    #Launch prediction
                    my_prediction = np.argmax(model.predict(vect), axis = -1)

                    #print('My_Prediction: {}'.format(my_prediction))

                    #Getting the index of the maximum prediction
                    final_pred = my_prediction[0]

        return render_template('results.html', prediction = final_pred)

if __name__ == "__main__":
    app.run(debug=True)
