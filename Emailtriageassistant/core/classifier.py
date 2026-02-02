def classify_email(email):
    text = (email["subject"] + " " + email["body"]).lower()

    if "urgent" in text or "immediately" in text or "alert" in text:
        return "Urgent"

    if "offer" in text or "discount" in text or "sale" in text:
        return "Spam"

    if "deadline" in text or "meeting" in text or "interview" in text:
        return "Important"

    return "Normal"
