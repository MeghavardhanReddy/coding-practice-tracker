# 🚀 Coding Practice Tracker

A full-stack web application built using **Flask**, **MySQL**, and **SQLAlchemy** to help users track coding practice, monitor progress, and analyze performance across platforms like LeetCode, Codeforces, HackerRank, and more.

---

## ✨ Features

- 🔐 User Authentication (Register/Login/Logout)
- 📚 Problem Management (Add, Edit, Delete, Search)
- 📝 Practice Session Tracking
- 📊 Dashboard Analytics
- 🔍 Search & Filter Problems
- 💾 MySQL Database
- 🔒 Password Hashing
- 📈 Progress Tracking

---

## 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python | Backend |
| Flask | Web Framework |
| MySQL | Database |
| SQLAlchemy | ORM |
| Flask-Login | Authentication |
| Bootstrap 5 | UI |
| HTML/CSS | Frontend |
| JavaScript | Client-side |

---

## 📂 Project Structure

```text
coding-practice-tracker/
│
├── app.py
├── config.py
├── database/
├── forms/
├── models/
├── routes/
├── static/
├── templates/
└── utils/
```

---

## 📸 Screenshots

### Login

![Login](docs/screenshots/login.png)

### Dashboard

![Dashboard](docs/screenshots/dashboard.png)

### Problem Management

![Problems](docs/screenshots/problems.png)

### Practice Tracker

![Practice](docs/screenshots/practice.png)

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/MeghavardhanReddy/coding-practice-tracker.git
cd coding-practice-tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Configure Environment

Copy

```
.env.example
```

to

```
.env
```

Update your MySQL credentials.

### Run

```bash
python app.py
```

---

## Database

Main Tables

- Users
- Problems
- Practice

Relationships

```
User
 ├── Problems
 └── Practice Sessions
```

---

## Security

- Password Hashing
- Flask Sessions
- SQLAlchemy ORM
- CSRF Protection

---

## Future Improvements

- Charts & Reports
- Daily Streak
- Goals
- PDF Export
- Email Reminders
- Automatic LeetCode & Codeforces Sync

---

## Author

**Meghavardhan Reddy**

GitHub

https://github.com/MeghavardhanReddy

---

## License

MIT License
