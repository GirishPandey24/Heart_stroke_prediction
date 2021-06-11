from flask import Flask,render_template,request
import pickle
import jsonify
import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)

tree=pickle.load(open('stroke_tree.pkl','rb'))





@app.route("/")
def home():
    return render_template('index.html')



scaler=StandardScaler()
@app.route('/predict',methods=['POST','GET'])
def predict():
    
    if request.method=='POST':    
        
        age=int(request.form['age'])
        hypertension=int(request.form['hypertension'])
        heart_disease=int(request.form['heart_disease'])
        avg_glucose_level=float(request.form['glucose'])
        bmi=float(request.form['bmi'])
        gender=request.form['gender']
        married=request.form['married']
        work_type=request.form['work_type']
        residence=request.form['residence']
        smoking=request.form['smoking']

        #gender
        if gender==0:
            gender_Male=1
            gender_Other=0
        elif gender==2:
            gender_Male=0
            gender_Other=1
        else:
            gender_Male=0
            gender_Other=0

        #married
        if married==0:
            ever_married_Yes=1
        else:
            ever_married_Yes=0

        #work_type
        if work_type==0:
            work_type_Never_worked=1
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=0
        elif work_type==1:
            work_type_Never_worked=0
            work_type_Private=1
            work_type_Self_employed=0
            work_type_children=0
        elif work_type==2:
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=1
            work_type_children=0
        elif work_type==4:
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=1
        else:
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=0

        #residence
        if residence==0:
            Residence_type_Urban=1
        else:
            Residence_type_Urban=0

        #smoking
        if smoking==0:
            smoking_status_formerly_smoked=1
            smoking_status_never_smoked=0
            smoking_status_smokes=0
        elif smoking==1:
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=1
            smoking_status_smokes=0
        elif smoking==2:
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=0
            smoking_status_smokes=1
        else:
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=0
            smoking_status_smokes=0
            #scaler.fit_transform
        feature=[[age, hypertension, heart_disease, avg_glucose_level, bmi,gender_Male, gender_Other, ever_married_Yes,work_type_Never_worked, work_type_Private,work_type_Self_employed, work_type_children, Residence_type_Urban,smoking_status_formerly_smoked, smoking_status_never_smoked,smoking_status_smokes]]
        
        print("#######################################################################")
        print(feature)
        result=tree.predict(feature)[0]
        #return "The age is {} and the Salary is {}".format(age,salary)
        if result==1:
             return render_template('index.html',label=1)
        else:
            return render_template('index.html',label=-1)
    else:
        return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
