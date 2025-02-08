from openai import OpenAI

def aiProcess(command):
    client = OpenAI(api_key = "Your_API_KEY")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Paras who speaks Hinglish. Paras is from India and is a coder. You analyze chat history and respond like Paras."},
        
        {"role": "user","content": command}
    ]
    )
    return completion.choices[0].message.content