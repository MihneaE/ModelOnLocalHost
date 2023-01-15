# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from sklearn import linear_model
import pickle
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

pickle.dump('AlexnetModel/model.h5', open('model.pkl', 'wb'))
model = open('model.pkl', 'rb')
final_model = pickle.load(model)

@app.route('/')

def home():
    return render_template('index.html')



@app.route('/predict', methods = ['POST'])

def predict():
    list = ["HAPPY", "SAD", "FEAR", "ANGRY"]
    list_features = [string(x) for x in list]
    features = [np.array(list_features)]
    prediction = model.predict(features)

    output = round(prediction[0], 4)

    return render_template('index.html', prediction_text ='The emotion of the image is: '.format(output))

if __name__ == "__main__":
    app.run()
