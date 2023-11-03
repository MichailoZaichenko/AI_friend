import g4f

def ask_gpt(promt:str)->str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
    )
    return response

print(ask_gpt('How are you?'))