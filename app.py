from flask import Flask, jsonify # Import Flask
#Create a Flask Application
app =Flask(__name__)
votes = {}

#Home endpoint
@app.route("/")
def home():
    return "Welcome to the App"

#Health Endpoint
@app.route("/health")
def health():
    return "App is running"

#Voting Endpoint
@app.route("/vote/<name>")
def vote(name):
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    return jsonify({
        "message":f"Vote recorded for {name}",
        "votes": votes[name]
    })

#Vote Results End Point
@app.route("/results")
def results():
    return jsonify(votes)

#Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
    