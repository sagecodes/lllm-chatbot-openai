import os

import gradio as gr
import openai
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_assistant(user_prompt, message_history):
    history_openai_format = []

    for human, assistant in message_history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": user_prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=history_openai_format, max_tokens=100
    )

    assistant_message = response["choices"][0]["message"]["content"]
    return assistant_message


iface = gr.ChatInterface(fn=chat_with_assistant)

if __name__ == "__main__":
    iface.launch()
