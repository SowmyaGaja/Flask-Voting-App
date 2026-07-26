from flask import Flask # Import Flask
#Create a Flask Application
app =Flask(__name__)

#Home endpoint
@app.route("/")
def home():
    return "Welcome to the Application"

#Health Endpoint
@app.route("/health")
def health():
    return "App is running"

#Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
    