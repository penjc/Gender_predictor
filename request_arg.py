import argparse
import requests

url = 'http://127.0.0.1:5000/predict'

parser = argparse.ArgumentParser(description='Send a POST request to the API endpoint')
parser.add_argument('age', type=int, help='The person\'s age')
parser.add_argument('height', type=int, help='The person\'s height in cm')
parser.add_argument('weight', type=int, help='The person\'s weight in kg')
parser.add_argument('occupation', type=str, help='The person\'s occupation')
parser.add_argument('education_level', type=str, help='The person\'s education level')
parser.add_argument('marital_status', type=str, help='The person\'s marital status')
parser.add_argument('income', type=int, help='The person\'s income in USD')
parser.add_argument('favorite_color', type=str, help='The person\'s favorite color')


args = parser.parse_args()

data = {
    ' Age': args.age,
    ' Height (cm)': args.height,
    ' Weight (kg)': args.weight,
    ' Occupation': args.occupation,
    ' Education_Level': args.education_level,
    ' Marital_Status': args.marital_status,
    ' Income (USD)': args.income,
    ' Favorite_Color': args.favorite_color
}

response = requests.post(url, json=data)

if response.ok:
    prediction = response.json()['prediction']
    print(f'Prediction: {prediction}')
else:
    print('Error:', response.status_code)
