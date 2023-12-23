import os
from openai import OpenAI


def ai_request(request_mess):
    client = OpenAI(
        api_key="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") # Ключ api ChatGPT

    chat_completion = client.chat.completions.create(messages=[{ "role": "user", "content": request_mess}], model="gpt-3.5-turbo")

    return str(chat_completion.choices[0].message.content)