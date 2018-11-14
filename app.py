from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route('/test')
def barchart1():

    data = pd.read_csv('survey_results_public.csv')

    summary = data['FormalEducation'].value_counts()
    values = []
    for i in summary:
        values.append(i)
   
    print(values)


    labels = ["Associate degree", "Bachelor's degree", "I never completed any formal education", "Master's degree",
          "Other doctoral degree", "Primary/elementary school", "Professional degree (JD, MD, etc.)",
          "Secondary school", "Some college/university study without earning a degree"]

    return render_template('chart.html', values=values, labels=labels)
	
	
if __name__ == '__main__':
	app.run(debug=True)
	


