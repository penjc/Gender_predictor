## Gender machine learning API using Flask

 This project uses machine learning to predict the gender of a person based on their age, height, weight, occupation, education level, marital status, income, and favorite color.

### The application has two endpoints:

 '/' (home page) accepts POST and GET requests to render the form for user input and display the predicted gender.

 '/predict' accepts POST requests with JSON data containing the user's information and returns the predicted gender as a JSON response.

### Setup

1. Clone the repository:
 ```
 https://github.com/penjc/Gender_predictor.git
 ```
2. Navigate to the project directory:
 ```
 cd Gender_predictor
 ```
3. Install the required packages
 ```
 pip install -r requirements.txt
 ```

### Usage

 1. Start the server:
 ```
 python server.py
 ```

 2. Open a web browser and navigate to http://localhost:5000.

 3. Fill out the form with your input data and click on the "Submit" button.
 
 4. The predicted value will be displayed on the web page.


### API Usage

 1. Start the server:
  ```
  python server.py
  ```
 2. Send a POST request to http://localhost:5000/predict with the data in the script in JSON format. The response will contain the predicted value in JSON format.
  ```
  python request.py
  ```
 
   or Send a POST request to http://localhost:5000/predict with the data input in JSON format.
  
  ```
  python request_arg.py  <age> <height> <weight> <occupation> <education_level> <marital_status> <income> <favorite_color>
  ```




