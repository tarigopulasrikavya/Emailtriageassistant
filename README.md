Email Triage Assistant

An AI-powered Email Triage Assistant built using Streamlit that automatically classifies emails into Urgent, Important, Spam, and Normal, generates short summaries, and provides smart reply suggestions to improve productivity.
Project Overview

Managing large volumes of emails is time-consuming and error-prone.
This project uses Natural Language Processing (NLP) techniques to:

Automatically read emails

Classify them by priority

Summarize long email content

Suggest quick, context-aware replies

The system provides a clean dashboard UI for easy navigation and filtering.

🛠️ Technologies Used
Frontend

Streamlit – Interactive web UI

HTML & CSS – Custom styling and layouts

Backend

Python 3.8+

AI / NLP

Rule-based + NLP classification logic

Text summarization logic

Automated reply generation
Project Structure
EMAILTRIAGEASSISTANT/
│
├── app.py                 
├── requirements.txt       
│
├── core/
│   ├── email_reader.py    
│   ├── classifier.py      
│   ├── summarizer.py      
│   ├── reply_generator.py 
│
├── data/
│   └── sample_emails.json 
│
├── ui/
│   ├── styles.css         
│   └── layout.html        
│
└── README.md              
Features

📥 Automatic email loading

🚨 Urgent email detection

📌 Important email identification

🚫 Spam filtering

🟢 Normal email categorization

✂️ AI-powered summarization

✍️ Smart reply suggestions

📊 Dashboard with real-time metrics

🎨 Clean & modern UI
Application:
🚨 Urgent Emails

Highlighted in red

High priority alerts like bank issues, security warnings

Immediate action suggested 
<img width="934" height="416" alt="image" src="https://github.com/user-attachments/assets/71978f72-022e-462c-a266-0a27f9ba29fa" />
Important Emails

Highlighted in blue

Includes meetings, deadlines, interviews

Professional reply suggestions provided

<img width="953" height="462" alt="image" src="https://github.com/user-attachments/assets/10ce1c37-e85d-4a4b-b6d5-34dfc1308e94" />
 Spam Emails

Highlighted in orange

Promotional or marketing emails

Automatically marked as promotional

<img width="938" height="416" alt="image" src="https://github.com/user-attachments/assets/860ce9c6-5ec3-4b8b-9afd-128d4b4ea837" />
Normal Emails

Highlighted in green

Regular informational emails

Simple acknowledgment replies suggested 
 <img width="936" height="404" alt="image" src="https://github.com/user-attachments/assets/e449a2b3-3a92-4772-b98d-b74cd0470013" />


