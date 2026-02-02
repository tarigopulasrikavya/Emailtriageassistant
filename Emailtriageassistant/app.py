import streamlit as st
from core.email_reader import load_emails
from core.classifier import classify_email
from core.summarizer import summarize_email
from core.reply_generator import generate_reply

st.set_page_config(page_title="Email Triage Assistant", layout="wide")

# Load CSS
with open("ui/styles.css", encoding="utf-8") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">📧 Email Triage Assistant</div>
<div class="subheader">AI-powered email management & categorization</div>
<hr/>
""", unsafe_allow_html=True)

emails = load_emails()
for e in emails:
    e["category"] = classify_email(e)

# Metrics
total = len(emails)
urgent = sum(e["category"] == "Urgent" for e in emails)
important = sum(e["category"] == "Important" for e in emails)
spam = sum(e["category"] == "Spam" for e in emails)

c1, c2, c3, c4, c5 ,c6= st.columns(6)
c1.metric("📨 Total", total)
c2.metric("✅ Processed", total)
c3.metric("🚨 Urgent", urgent)
c4.metric("📌 Important", important)
c5.metric("🚫 Spam", spam)
c6.metric("📝 Normal", total - urgent - important - spam)

st.divider()

# Sidebar filter
st.sidebar.title("Filters")
filter_choice = st.sidebar.radio(
    "By Category",
    ["All Emails", "Urgent", "Important", "Spam", "Normal"]
)

filtered = emails if filter_choice == "All Emails" else [
    e for e in emails if e["category"] == filter_choice
]

# Layout
left, right = st.columns([2, 3])

# Inbox (LEFT)
with left:
    st.subheader("📨 Inbox")
    for i, email in enumerate(filtered):
        if st.button(email["subject"], key=f"mail_{i}"):
            st.session_state.selected_email = email

# Details (RIGHT)
with right:
    st.subheader("📄 Email Details")
    if "selected_email" not in st.session_state:
        st.info("Select an email from inbox")
    else:
        e = st.session_state.selected_email
        summary = summarize_email(e["body"])
        reply = generate_reply(e["category"])
        css = e["category"].lower()

        st.markdown(f"""
        <div class="email-card {css}">
            <b>From:</b> {e['sender']}<br/>
            <b>Subject:</b> {e['subject']}<br/><br/>
            <span class="label {css}">{e['category']}</span>
            <p><b>Summary:</b><br/>{summary}</p>
            <div class="reply-box">
                <b>Suggested Reply:</b><br/>{reply}
            </div>
        </div>
        """, unsafe_allow_html=True)