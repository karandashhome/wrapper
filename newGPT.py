import openai
import requests
from log import logoutput

openai.api_key = "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"

model_engine = "text-davinci-003"
context = ""

while True:
    user_input = input("Введите ваш вопрос: ")
    prompt = f"Q: {context} {user_input}\nA:"
    logoutput(user_input)
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=0.8
    )

    answer = completion.choices[0].text.strip()


    def parse_string(string: str) -> str:
        new_string = ""
        count = 0

        for letter_index in range(len(string)):
            if string[letter_index] == "\n":
                count = 0
            if count % 130 == 0 and count != 0:
                new_string += "\n"
            new_string += string[letter_index]
            count += 1
        logoutput(new_string)
        return new_string


    print(parse_string(answer))

    # if user_input.lower() == "очистить":
    #     context = ""
    #     print(context)
    # else:
    #     print(context)
    #     context += answer

    continue_prompt = input("Нажмите н для выхода и любую клавишу, чтобы продолжить ")
    if continue_prompt.lower() == "н":
        break
    elif continue_prompt.lower() == "очистить":
        context = ""
        print(context)
    else:
        print(context)
        context += answer
