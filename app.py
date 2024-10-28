from flask import Flask, request   # Importing flask to create a web app and request to handle parameters.
from flask_cors import CORS  # Cross origin Resource sharing    

app = Flask(__name__)   # Initializing ghe flask app
CORS(app) # Enabling CORS for all app routes so that it won't give any garbage response 

@app.route('/hello', methods=['GET']) # Definig routeto handle GET request to the /hello endpoint 
def hello_world():  #Define keyword ie. Function
    language = request.args.get('language', 'English') # It says to get the language parameter from the query,default to English if specific language not provided
    greet = {       # Dictionary containing messages in different languages as per JD
        'English': 'Hello world',
        'French': 'Bonjour le monde',
        'Hindi': 'Namastey sansar'
    }
    return greet.get(language, 'Hello world')   # Return the greet message,defualt set to English if no language is found

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)   # It says that the web app will run on port 5000,can be modified as well
