import gradio as gr
from difflib import get_close_matches

# Knowledge base with common daily dialog questions and answers
responses = {
    "hi": "Hello there! 😊",
    "hello": "Hey! How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what's your name": "I'm your friendly daily dialog assistant.",
    "good morning": "Good morning! Hope you have a fantastic day ahead!",
    "good night": "Sweet dreams! 🌙",
    "how's the weather": "I can’t check the weather, but I hope it’s nice where you are!",
    "what are you doing": "Just hanging out, ready to chat with you!",
    "can you help me": "Of course! Ask me anything.",
    "what time is it": "I don't have a clock, but I can chat anytime you like!",
    "what do you like to do": "I like chatting with people like you!",
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus! 😂",
    "thank you": "You're welcome!",
    "thanks": "No problem!",
    "how was your day": "Pretty awesome, thanks for asking!",
    "do you speak other languages": "I understand English best, but I'm learning!",
    "bye": "Goodbye! Have a great day! 👋",
    "see you later": "See you! Come back anytime.",
    "what should I eat today": "Something delicious and healthy sounds good!",
    "i'm bored": "Let’s play 20 questions or tell each other jokes!"
}

def chatbot(user_input):
    user_input = user_input.lower().strip()
    match = get_close_matches(user_input, responses.keys(), n=1, cutoff=0.5)
    if match:
        return responses[match[0]]
    return "Hmm, I’m not sure how to respond to that. Try asking something more casual or daily!"

# Gradio Interface
iface = gr.Interface(fn=chatbot,
                     inputs=gr.Textbox(lines=2, placeholder="Say something like 'Hi' or 'How are you?'..."),
                     outputs="text",
                     title="🗣️ Daily Dialog Chatbot",
                     description="Chat with me about everyday stuff — greetings, jokes, weather, and more!")

iface.launch()
