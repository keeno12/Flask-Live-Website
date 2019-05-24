from flask import Flask, render_template, request, jsonify, Response
import pickle
import pandas as pd

#  Create an app object that will route our calls
app = Flask(__name__)

# Add a single endpoint for testing
@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')

# Add route for miles per gallon
@app.route('/mpg',methods = ['GET'])
def mpg():
    return render_template('mpg.html')

model = pickle.load(open('linreg.p','rb'))
@app.route('/inference',methods = ['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'],req['horsepower'],req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c':c,'h': h,'w':w,'prediction':prediction[0] })     

#When we run from command line
if __name__=='__main__':
    app.run(host='0.0.0.0',port = 3333,debug = True)
