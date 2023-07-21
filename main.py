import openai
import requests
from log import logoutput

openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

model_engine = "text-davinci-003"
context = ""

while True:
    user_input = input("Введите ваш вопросEnter your question here: ")
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


    continue_prompt = input("Enter  "clear" to remove the context of the conversation. Press "n" to exit the dialog, Press any other key to continue. ")
    if continue_prompt.lower() == "n":
        break
    elif continue_prompt.lower() == "clear":
        context = ""
        print(context)
    else:
        print(context)
        context += answer
