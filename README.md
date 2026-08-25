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
* `/results`
* `/reset`

The voting functionality was verified by adding votes, checking results, and resetting the votes.

---

# Screenshots

## 1. Application Running

Home Endpoint </br>
<img width="396" height="195" alt="AdobeExpressPhotos_32fbb552ab544eb8a0543f1c46516672_CopyEdited" src="https://github.com/user-attachments/assets/7e4adb36-53fa-41ae-bcf6-fc70f7254e84" />

Health Endpoint</br>
<img width="521" height="231" alt="AdobeExpressPhotos_8631c925e9084d09b1018847bab27461_CopyEdited" src="https://github.com/user-attachments/assets/4182cf42-55fe-4699-bc4b-b7be3791b66e" />

Voting Endpoint</br>
<img width="551" height="339" alt="image" src="https://github.com/user-attachments/assets/6e545f4d-786b-4491-be4f-36127b4be1c1" />

Voting Result Endpoint</br>
<img width="950" height="378" alt="Screenshot 2026-08-25 123024" src="https://github.com/user-attachments/assets/6cd688ce-57de-49a7-b25b-b67f46722d15" />

## 2. GitHub Branches

screenshot showing both `dev` and `main` branches.

<img width="1268" height="868" alt="Screenshot 2026-08-25 123510" src="https://github.com/user-attachments/assets/5528f961-56f6-4d01-ae83-e92f3f03d147" />

## 3. Git History

screenshot showing the Version 1 and Version 2 commit/merge history.

<img width="850" height="133" alt="AdobeExpressPhotos_7c8e036636e343dcb32fb7a2114802f9_CopyEdited" src="https://github.com/user-attachments/assets/4921f046-766e-4895-9892-c8030aa762d9" />

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
