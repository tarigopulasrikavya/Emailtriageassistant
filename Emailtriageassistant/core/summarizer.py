def summarize_email(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    if len(sentences) <= 1:
        return text
    return sentences[0] + "."
