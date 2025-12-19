def generate_summary(chat):
    summary = "Conversation Summary:\n\n"
    for msg in chat:
        summary += f"{msg['speaker'].upper()}: {msg['text']}\n\n"
    return summary
