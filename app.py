# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:14:29 2020

@author: Hp   
"""  
  
from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)
model= load('multi.save')  
trans=load('onehot1')   
        
@app.route('/')  
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict(): 
    
    x_test = [[x for x in request.form.values()]]
    print(x_test) 
    test=trans.transform(x_test)
    test=test[:,0:]
    print(test)
    prediction = model.predict(test)
    print(prediction)
    output=prediction[0]
    
    if output==0:
        
        return render_template('negative.html', prediction_text='You does not have diabetes')

            
    else:
        
        return render_template('positive.html', prediction_text='You has  diabetes')
        

if __name__ == "__main__":
    app.run(debug=True)
