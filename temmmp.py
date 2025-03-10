# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

data = pd.read_csv('survey_results_public.csv')
#print(data['FormalEducation'].value_counts())


#print(data['FormalEducation'].value_counts())

summary = data['FormalEducation'].value_counts()
values = []
for i in summary:
    values.append(i)
    
print(values)
#print(summary["Some college/university study without earning a degree"])

from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def barchart():
    labels = ["Associate degree", "Bachelor's degree", "I never completed any formal education", "Master's degree", "Other doctoral degree", "Primary/elementary school", "Professional degree (JD, MD, etc.)", "Secondary school", "Some college/university study without earning a degree"]
    #values = [3.1, 46.1, 0.7, 22.6, 2.3, 1.7, 1.5, 9.5,12.4]
    return render_template('chart.html', values=values, labels=labels)

if __name__ == '__main__':
	app.run()