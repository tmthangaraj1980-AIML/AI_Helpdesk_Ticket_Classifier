# 🤖 AI Helpdesk Ticket Classifier

An End-to-End Machine Learning web application that automatically classifies IT Helpdesk support tickets into the appropriate department using Natural Language Processing (NLP).

The application predicts the ticket category, confidence score, top 3 possible categories, assigned support team, priority level, estimated resolution time, and suggested troubleshooting steps.

---

## 🚀 Features

- Machine Learning based ticket classification
- TF-IDF text vectorization
- Logistic Regression classifier
- Predicts Helpdesk category
- Confidence score
- Top 3 predictions
- Assigned IT Team
- Priority level
- Estimated Resolution Time
- Suggested Resolution Steps
- Sample Tickets for Demo
- Copy Solution button
- Responsive Bootstrap UI

---

## 🖥️ Technologies Used

### Backend

- Python
- Flask
- Scikit-learn
- Joblib

### Machine Learning

- TF-IDF Vectorizer
- Logistic Regression
- NLP Text Classification

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Fetch API

---

## 📂 Project Structure

```
AI_Helpdesk_Ticket_Classifier/
│
├── app.py
├── requirements.txt
├── README.md
├── models/
│   ├── lr_model.pkl
│   └── tfidf.pkl
│
├── dataset/
│
├── notebooks/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── 404.html
│   └── 500.html
│
└── utils/
    ├── __init__.py
    └── helpdesk_data.py
```

---

## 📊 Machine Learning Pipeline

```
Helpdesk Ticket
        │
        ▼
Text Cleaning
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Logistic Regression Model
        │
        ▼
Prediction
        │
        ├── Category
        ├── Confidence
        ├── Top 3 Predictions
        ├── Assigned Team
        ├── Priority
        ├── ETA
        └── Suggested Resolution
```

---

## 📌 Categories

- Password Reset
- VPN Issue
- Email Issue
- Hardware Issue
- Printer Issue
- Network Issue
- Software Installation
- Account Access
- Security / Phishing
- Access Request

---

## 💻 Sample Tickets

- Forgot my password.
- My laptop is not connecting to VPN.
- Outlook is not sending emails.
- Printer is offline.
- Need access to Power BI.
- Install Microsoft Office.
- Unable to login to SAP.
- No internet connection.
- Laptop is running slow.
- Received a phishing email.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/tmthangaraj1980-AIML/AI_Helpdesk_Ticket_Classifier.git
```

Go to project folder

```bash
cd AI_Helpdesk_Ticket_Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
py app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📈 Model Used

- TF-IDF Vectorizer
- Logistic Regression

---

## 🎯 Future Improvements

- Deep Learning (BERT)
- Ticket Auto Assignment
- Email Integration
- Database Support
- User Authentication
- Admin Dashboard
- Ticket History
- Multi-language Support

---
# Intelligent Helpdesk Ticket Classification 🤖🎫

An end-to-end Machine Learning web application designed to automatically classify incoming IT support tickets, assign them to the correct internal team, determine priority levels, and suggest instant resolutions.

## 🚀 Live Demo
Check out the live application hosted on Render: 
👉 [Live App Link](https://ai-helpdesk-ticket-classifier.onrender.com)


## 👨‍💻 Author

**Thangaraj T**

AI & Machine Learning Engineer

GitHub:
https://github.com/tmthangaraj

LinkedIn:
https://linkedin.com/in/thangaraj-t-340169158

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.