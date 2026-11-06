# Import the Flask class to create our web application.
from flask import Flask

# Create the Flask application using this file's name.
app = Flask(__name__)

# Set the home page URL to the root address.
@app.get("/")
# Define the function that handles the home page.
def home():
    # Display a welcome message for the café.
    return "Welcome to Café Calle Ocho"

# Set the About page URL.
@app.get("/about")
# Define the function that handles the About page.
def about():
    # Display a short description of the café.
    return "Café Calle Ocho is a Cuban café in Little Havana."