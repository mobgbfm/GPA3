from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route('/chart')
def barchart1():

    data = pd.read_csv('survey_results_public.csv', usecols=['FormalEducation'],encoding='latin-1', low_memory=False)

    summary = data['FormalEducation'].value_counts()

    values = []
    for i in summary:
        values.append(i)

    values.sort()

         ##print(len(summary.index)) -- counted total row - in theory we should output this to the page less the NAs

    ## apostrophes are rendering wrong - this is not the right order-chart is orderd by size
    ## it doesn't seem to count NA?  - value counts must ignore it
    ## I put in the labels in the order of size of the results. 
    labels = ['I never completed any formal education','Professional degree','Primary/elementary school','Doctoral degree', 'Associate degree','Secondary school','Some college/university study without earning a degree','Master\'s degree', 'Bachelor\'s degree']


    return render_template('chart.html', values=values, labels=labels)


if __name__ == '__main__':
	app.run(debug=True)


