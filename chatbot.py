# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Industrial Training | Batch 2026
# ============================================

responses = {
    "hello":       "Hi there! How can I help you?",
    "hi":          "Hey! Welcome to DecodeLabs Bot!",
    "how are you": "I'm just a bot, but I'm running perfectly!",
    "name":        "I am DecoBot, your rule-based assistant.",
    "help":        "I can answer: hello, hi, how are you, name, time, bye",
    "time":        "I don't have a clock, but your system does!",
    "bye":         "Goodbye! Have a great day!",
    "thanks":      "You're welcome! Happy to help.",
}

print("=" * 40)
print("   DecoBot — Rule-Based AI Chatbot")
print("   Type 'quit' to exit")
print("=" * 40)

while True:
    raw_input_text = input("\nYou: ")
    clean_input = raw_input_text.lower().strip()

    if clean_input in ["quit", "exit", "bye"]:
        print("DecoBot: Goodbye! See you next time!")
        break

    reply = responses.get(clean_input, "I don't understand that yet. Try: hello, help, bye")
    print(f"DecoBot: {reply}")

