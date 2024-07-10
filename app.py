
import streamlit as st
import openai

openai.api_key = "YOUR_API_KEY"

predefined_responses = {
  "what is ai": "Artificial Intelligence (AI) is when computers or robots can do tasks that usually need human thinking, like recognizing pictures or playing games.",
    "what is programming": "Programming is telling a computer what to do by giving it instructions, like a recipe.",
    "what is a computer": "A computer is a machine that can follow instructions to do different tasks, like playing games or helping with homework.",
    "who made the first computer": "The first computer was created by Charles Babbage, and it was called the Analytical Engine.",
    "hi": "Hi, how can I help you?",
    "hello": "Hi, how can I help you?",
    "how are you": "I'm doing well, thank you. How about you?",
    "i'm fine": "That's good to hear.",
    "i'm doing well": "That's great. Do you have any questions?",
    "what is your name": "My name is LearnBot. I'm here to help you with your learning about AI and programming.",
    "i am not doing well": "I'm sorry to hear that. Take care!",
    "i am sad": "I'm sorry to hear that. Take care!",
    "i am tired": "I'm sorry to hear that. Take care!",
    "i am bored": "I'm sorry to hear that. Do something fun!",
    "can you help me": "Yes, I can. What do you want to learn about AI and programming?",
    "i want to learn about AI": "Artificial Intelligence (AI) is when computers or robots can do tasks that usually need human thinking, like recognizing pictures or playing games.",
    "i want to learn about programming": "Programming is telling a computer what to do by giving it instructions, like a recipe.",
    "can I make a chatbot": "Yes, you can. You need to learn about AI and programming to do that!",
}

def generate_response_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who provides clear and simple explanations suitable for kids under the age of 10."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response.choices[0].message['content'].strip()

def generate_kid_friendly_response(prompt):
    prompt_lower = prompt.lower()
    if prompt_lower in predefined_responses:
        return predefined_responses[prompt_lower]
    return generate_response_openai(prompt)

st.title("Kid-Friendly AI Chatbot")
st.write("Ask me anything about AI, programming, or computers!")

user_input = st.text_input("You: ")
if user_input:
    response = generate_kid_friendly_response(user_input)
    st.write("Bot:", response)
