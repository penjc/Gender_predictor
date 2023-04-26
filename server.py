from flask import Flask, render_template, request, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired
import joblib
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pjc'
model = joblib.load('./models/model.pkl')
transfer = joblib.load('./models/transfer.pkl')

def pred(features):
    features = features.to_dict(orient="records")
    features = transfer.transform(features)
    prediction = model.predict(features)
    return prediction


class PredForm(FlaskForm):
    Age = IntegerField('Age: ', validators=[DataRequired()])
    Height = IntegerField('Height (cm): ', validators=[DataRequired()])
    Weight = IntegerField('Weight (kg): ', validators=[DataRequired()])
    Occupation = StringField('Occupation: ', validators=[DataRequired()])
    Education_Level = StringField('Education Level: ', validators=[DataRequired()])
    Marital_Status = StringField('Marital Status: ', validators=[DataRequired()])
    Income = IntegerField('Income (USD): ', validators=[DataRequired()])
    Favorite_Color = StringField('Favorite Color: ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def pred():
    form = PredForm()
    if request.method == 'POST':
        Age = request.form.get('Age')
        Height = request.form.get('Height')
        Weight = request.form.get('Weight')
        Occupation = request.form.get('Occupation')
        Education_Level = request.form.get('Education_Level')
        Marital_Status = request.form.get('Marital_Status')
        Income = request.form.get('Income')
        Favorite_Color = request.form.get('Favorite_Color')

        features = [[Age, Height, Weight, Occupation, Education_Level, Marital_Status, Income, Favorite_Color]]

        features = pd.DataFrame(features,
                                columns=[' Age', ' Height (cm)', ' Weight (kg)', ' Occupation', ' Education_Level',
                                         ' Marital_Status', ' Income(USD)',
                                         ' Favorite_Color'])
        print(features)
        features[[' Age', ' Height (cm)', ' Weight (kg)', ' Income(USD)']] = features[
            [' Age', ' Height (cm)', ' Weight (kg)', ' Income(USD)']].astype('int64')

        features = features.to_dict(orient="records")
        features = transfer.transform(features)
        prediction = model.predict(features)

        print(prediction)
        if form.validate_on_submit():
            return f'Prediction: {prediction}'
        else:
            flash('wrong argument')

    return render_template('index.html', form=form)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data = pd.DataFrame([data])

    data = data.to_dict(orient="records")
    data = transfer.transform(data)
    prediction = model.predict(data)

    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
