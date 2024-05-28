from flask import Flask , render_template , request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model1.pkl','rb'))

cols = ['Gender','Age','openness','neuroticism','conscientiousness','agreeableness','extraversion']

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/index')
def index():
    return render_template("index.html")



@app.route('/predict',methods=["POST"])
def prediction():
    if request.method == "POST":
        gender = int(request.form['f1'])
        age = float(request.form['f2'])
        openness = float(request.form['f3'])
        neuroticism = float(request.form['f4'])
        conscientiousness = float(request.form['f5'])
        agreeableness = float(request.form['f6'])
        extraversion = float(request.form['f7'])
        # print(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion)

        x_sample = pd.DataFrame([[gender,age,openness,neuroticism,conscientiousness,agreeableness,extraversion]],columns=cols)
        print(x_sample)
        result = model.predict(x_sample)

        print(type(result[0]))
        print(result[0]== "0")
        print(result[0] == 0)

        return render_template("output.html",value=result)


if __name__=="__main__":
    app.run(debug=True)