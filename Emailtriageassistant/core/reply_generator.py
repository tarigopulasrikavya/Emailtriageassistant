def generate_reply(category):
    if category == "Urgent":
        return "We are addressing this issue immediately."

    if category == "Important":
        return "Thank you for the information. We will take action."

    if category == "Spam":
        return "This email has been identified as promotional."

    return "Thank you for reaching out."
