Flask Voting Application

A simple Flask-based voting application developed as part of the Flask and Git versioning assignment.

The application allows users to:

Check application status
Vote for candidates
View voting results
Reset all votes
Technologies
Python 3
Flask
Git
GitHub
Project Structure
Flask-Voting-App/
├── app.py
├── requirements.txt
└── README.md
Installation & Setup
1. Clone the repository
git clone https://github.com/SowmyaGaja/Flask-Voting-App.git
cd Flask-Voting-App
2. Create a virtual environment
python -m venv venv
3. Activate the environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
python app.py

Application URL:

http://localhost:5000
API Endpoints
Endpoint	Method	Purpose	Example
/	GET	Displays welcome message	Welcome to the App
/health	GET	Checks application status	App is running
/vote/<name>	GET	Records one vote	/vote/sowmya
/results	GET	Displays vote counts as JSON	{"sowmya": 2}
/reset	GET	Clears all votes	Reset confirmation
Example Voting Flow
Vote for sowmya
http://localhost:5000/vote/sowmya
Vote for Ganesh
http://localhost:5000/vote/Ganesh
View results
http://localhost:5000/results

Example:

{
    "sowmya": 2,
    "Ganesh": 1
}
Reset votes
http://localhost:5000/reset

After reset:

http://localhost:5000/results

Expected result:

{}
Git Workflow

Development was performed using separate dev and main branches.

dev → Version 1 → merge → main
                  ↓
dev → Version 2 → merge → main
Workflow
Create/update features in dev
Test the application
Commit changes in dev
Push dev to GitHub
Merge dev into main
Push main to GitHub

main contains stable, tested code.

Version History
Version	Features
Version 1	Flask application, /, /health
Version 2	Voting system, /vote/<name>, /results, /reset
Testing

The application was tested using the browser.

Tested endpoints:

/
/health
/vote/sowmya
/vote/Ganesh
/vote/Sowmya
/vote/Senthil
/vote/sowmya
/results
/reset

The voting functionality was verified by adding votes, checking results, and resetting the votes.

Screenshots
1. Application Running

Add a screenshot showing the Flask application running in the browser.

![Application Running](screenshots/flask-running.png)

2. GitHub Branches

Add a screenshot showing both dev and main branches.

![GitHub Branches](screenshots/github-branches.png)
3. Git History

Add a screenshot showing the Version 1 and Version 2 commit/merge history.

![Git History](screenshots/git-history.png)
Learning Outcomes

This project demonstrates:

Flask application development
REST-style API endpoints
Dynamic URL parameters
JSON responses
Python dictionaries for in-memory data
Git branching
Feature-based development
Git merge workflow
GitHub version control