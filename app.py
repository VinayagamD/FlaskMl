from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api', methods= ['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)  # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])  # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run()
