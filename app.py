from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model=pickle.load(open('LogR.pkl','rb'))
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=='POST':
        age=float(request.form.get('age'))
        Sex=float(request.form.get('Sex'))
        Chestpaintype=float(request.form.get('Chestpaintype'))
        BP=float(request.form.get('BP'))
        Cholesterol=float(request.form.get('Cholesterol'))
        FBSover120=float(request.form.get('FBSover120'))
        EKGresults=float(request.form.get('EKGresults'))
        MaxHR=float(request.form.get('MaxHR'))
        Exerciseangina=float(request.form.get('Exerciseangina'))
        STdepression=float(request.form.get('STdepression'))
        SlopeofST=float(request.form.get('SlopeofST'))
        Numberofvesselsfluro=float(request.form.get('Numberofvesselsfluro'))
        Thallium=float(request.form.get('Thallium'))
        result=model.predict([[ age, Sex,Chestpaintype,BP,Cholesterol, FBSover120,EKGresults,MaxHR,Exerciseangina
        ,STdepression,SlopeofST,Numberofvesselsfluro,Thallium]])
        p=''
        if(result[0] == 0):

            p = 'NO'
        else:


            p = 'YES'
        return render_template('index.html',results=p)

    else:
      return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)