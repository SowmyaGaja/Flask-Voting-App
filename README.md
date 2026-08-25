# Flask Voting Application

A simple Flask-based voting application developed as part of the Flask and Git versioning assignment.

The application allows users to:

* Check application status
* Vote for candidates
* View voting results
* Reset all votes

## Technologies

* Python 3
* Flask
* Git
* GitHub

## Project Structure

```text
Flask-Voting-App/
├── app.py
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SowmyaGaja/Flask-Voting-App.git
cd Flask-Voting-App
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Application URL:

```text
http://localhost:5000
```

---

# API Endpoints

| Endpoint       | Method | Purpose                      | Example              |
| -------------- | ------ | ---------------------------- | -------------------- |
| `/`            | GET    | Displays welcome message     | `Welcome to the App` |
| `/health`      | GET    | Checks application status    | `App is running`     |
| `/vote/<name>` | GET    | Records one vote             | `/vote/sowmya`        |
| `/results`     | GET    | Displays vote counts as JSON | `{"sowmya": 2}`       |
| `/reset`       | GET    | Clears all votes             | Reset confirmation   |

## Example Voting Flow

### Vote for sowmya

```text
http://localhost:5000/vote/sowmya
```

### Vote for Ganesh

```text
http://localhost:5000/vote/Ganesh
```

### View results

```text
http://localhost:5000/results
```

Example:

```json
{
    "sowmya": 1,
    "Ganesh": 1
}
```

### Reset votes

```text
http://localhost:5000/reset
```

After reset:

```text
http://localhost:5000/results
```

Expected result:

```json
{}
```

---

# Git Workflow

Development was performed using separate `dev` and `main` branches.

```text
dev → Version 1 → merge → main
                  ↓
dev → Version 2 → merge → main
```

### Workflow

1. Create/update features in `dev`
2. Test the application
3. Commit changes in `dev`
4. Push `dev` to GitHub
5. Merge `dev` into `main`
6. Push `main` to GitHub

`main` contains stable, tested code.

---

# Version History

| Version   | Features                                            |
| --------- | --------------------------------------------------- |
| Version 1 | Flask application, `/`, `/health`                   |
| Version 2 | Voting system, `/vote/<name>`, `/results`, `/reset` |

---

# Testing

The application was tested using the browser.

Tested endpoints:

* `/`
* `/health`
* `/vote/`sowmya
* `/vote/`Ganesh
* /vote/Sowmya
* /vote/Senthil
* /vote/sowmya
* `/results`
* `/reset`

The voting functionality was verified by adding votes, checking results, and resetting the votes.

---

# Screenshots

## 1. Application Running

Add a screenshot showing the Flask application running in the browser.

```text
![Application Running](screenshots/flask-running.png)
```

## 2. GitHub Branches

Add a screenshot showing both `dev` and `main` branches.

```text
![GitHub Branches](screenshots/github-branches.png)
```

## 3. Git History

Add a screenshot showing the Version 1 and Version 2 commit/merge history.

```text
![Git History](screenshots/git-history.png)
```

---

# Learning Outcomes

This project demonstrates:

* Flask application development
* REST-style API endpoints
* Dynamic URL parameters
* JSON responses
* Python dictionaries for in-memory data
* Git branching
* Feature-based development
* Git merge workflow
* GitHub version control
