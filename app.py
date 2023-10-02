import os

import gradio as gr
import openai
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Define message_history as a global variable
message_history = [{"role": "system", "content": "You are a helpful assistant."}]


def chat_with_assistant(user_prompt):
    global message_history  # Declare message_history

    user_prompt_dict = {"role": "user", "content": user_prompt}
    message_history.append(user_prompt_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_history, max_tokens=100
    )

    assistant_response_dict = dict(response["choices"][0]["message"])
    message_history.append(assistant_response_dict)

    return assistant_response_dict["content"]  # Return the assistant's response content


def chat_with_history(user_prompt):
    global message_history  # Declare message_history as global

    assistant_response = chat_with_assistant(user_prompt)
    return assistant_response


iface = gr.Interface(
    fn=chat_with_history,
    inputs=[
        "text",
    ],
    outputs="text",
    live=False,
)


if __name__ == "__main__":
    iface.launch()
