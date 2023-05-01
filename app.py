import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle 
app = Flask(__name__)

model = pickle.load(open("olympic.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    features=[float(x) for x in request.form.values()]
    f=[np.array(features)]
    prediction= model.predict(f)
    if prediction<0:
        prediction=0
    p=np.rint(prediction)
    

    return render_template("index.html",prediction_text="The country is expected to achieve {} medals".format(p))


if __name__ == "__main__":
        app.run(debug=True)
    