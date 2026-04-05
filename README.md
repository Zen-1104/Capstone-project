# Capstone-project

## Overview

This project is a simple web-based event registration system developed as part of the Google Cloud Digital Leader capstone project.

The application allows users to register for events such as hackathons and workshops through a web interface. The main goal of this project is to demonstrate how a basic application can later be extended and deployed using cloud technologies.

---

## Features

- Event selection (Hackathon / Workshop)
- Registration form (Name and UNI ID)
- Data stored in a database
- Admin panel to view registered users
- Delete functionality for admin
- Success message after registration

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: SQLite (local)

---

## Project Structure

```bash
.
├── app.py
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/

```

## How to Run the Project Locally

1. Clone the repository:

```bash
git clone https://github.com/Zen-1104/Capstone-project
cd Capstone-project
```

2. Install dependencies:

```bash
pip install flask  
```

3. Run the application:

```bash
python3 app.py  
```

4. Open in browser:

```bash
http://127.0.0.1:5001  
```

---

## How It Works

- User selects an event and fills the form
- Data is sent to the Flask backend
- Data is stored in SQLite database
- Admin page displays all registered users

---

## Future Scope (Cloud Implementation)

This application is designed to be extended into a cloud-native system.

Proposed improvements using Google Cloud:

- Hosting using Cloud Run
- Database migration to Cloud SQL or Firestore
- Static files via Cloud Storage
- Use of API Gateway for scalability
- Serverless architecture for better performance and cost efficiency

---

## Learning Outcomes

- Basic full-stack web development
- Handling forms and backend routing
- Database integration
- Understanding how local apps can be migrated to cloud systems

---

## Notes

- This is a local prototype version
- No authentication system implemented (admin access is basic)
- Database file is excluded from version control

---

## Author

Zen-1104