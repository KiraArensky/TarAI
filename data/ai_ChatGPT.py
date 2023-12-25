import openai


def ai_request(request_mess):
    try:
        openai.api_key = "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"  # Ключ api ChatGPT

        completion = openai.ChatCompletion.create(  # Запрос
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": request_mess} # Сообщение для GPT
            ]
        )
        print("\n\nЗапрос отправлен\n\n")
        return completion.choices[0].message.content
    except:
        ai_request(request_mess)