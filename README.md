# 🐍 Automated Bulk Email Sender with Templates

## 🎯 Objective
This project is a Python-based CLI application that allows users to send bulk emails using customizable templates. It simulates real-world email marketing and notification systems with personalization, history tracking, and secure authentication.

---

## 🚀 Features

### 📧 Email Sending
- Send emails using SMTP (`smtplib`)
- Secure login using Gmail App Password
- Hidden password input using `getpass`

### 📂 Bulk Emailing
- Load contacts from CSV or JSON
- Automatically send emails to multiple recipients

### 🧾 Templates
- Reusable email templates
- Supports placeholders:
  - {name}
  - {company}
  - {message}

### ✏️ Personalization
- Each email is dynamically customized per user
- CLI input message is injected into template

### 🗂 Email History
- Stores sent email records in JSON
- Tracks:
  - Email
  - Subject
  - Status (Sent/Failed)
  - Timestamp

### 🔁 Retry Mechanism
- Automatically retries failed emails up to 3 times

### 🔐 Security
- Password is hidden during input
- Uses Gmail App Password (not real password)

---

## 🛠 Project Structure

email_sender/
│── main.py
│── email_service.py
│── contact_loader.py
│── template_manager.py
│── history_manager.py
│── utils.py
│── templates/
│     └── welcome.txt
│── data/
│     ├── contacts.csv
│     └── history.json

---

## ⚙️ Setup

1. Clone the repository
2. Navigate to project folder
3. Run:

python main.py

---

## 🔐 Gmail Setup

1. Enable 2-Step Verification
2. Go to Google Account → Security → App Passwords
3. Generate App Password for Mail
4. Use this password in the program

---

## 📄 Sample Template

Hello {name},

{message}

Welcome to {company}!

Best regards,
Team

---

## 📄 Sample Contacts CSV

name,email,company
Ali,ali@gmail.com,HK Academy
Ahmed,ahmed@gmail.com,TechSoft

---

## 🖥 Usage

1. Load Contacts
2. Choose Template
3. Send Email
4. View History
5. Exit

---

## 💡 Features Implemented

- Error handling
- Modular structure
- Retry mechanism
- Email validation
- Attachments support
- HTML emails

---

## ⚠️ Notes

- Use App Password, not Gmail password
- Avoid sending too many emails quickly

---

## 👨‍💻 Author

Software Engineering Project
