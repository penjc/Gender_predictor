import joblib
import pandas as pd
import os
from plotly.offline import init_notebook_mode
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

init_notebook_mode(connected=True)

df = pd.read_csv('./gender.csv')

df.isnull().any()
del df['Unnamed: 9']
print(df[' Gender'].value_counts(ascending=True))
df[' Gender'].replace([' male', ' female'], ['male', 'female'], inplace=True)
print(df[' Gender'].value_counts(ascending=True))

y = df[' Gender']
x = df.drop(columns=' Gender', axis=1)
x = x.to_dict(orient="records")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=22)

transfer = DictVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)


def classify(model):
    model.fit(x_train, y_train)
    print('Accuracy:', model.score(x_train, y_train))


model = DecisionTreeClassifier(criterion="entropy")
classify(model)

y_pred = model.predict(x_test)

print(y_test == y_pred)

joblib.dump(model, './models/model.pkl')
joblib.dump(transfer, "./models/transfer.pkl")
