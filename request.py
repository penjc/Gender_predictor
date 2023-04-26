import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    ' Age': 30,
    ' Height (cm)': 170,
    ' Weight (kg)': 70,
    ' Occupation': 'Software Engineer',
    ' Education_Level': "Master's Degree",
    ' Marital_Status': 'Single',
    ' Income (USD)': 60000,
    ' Favorite_Color': 'Blue'
}

response = requests.post(url, json=data)

if response.ok:
    prediction = response.json()['prediction']
    print(f'Prediction: {prediction}')
else:
    print('Error:', response.status_code)
