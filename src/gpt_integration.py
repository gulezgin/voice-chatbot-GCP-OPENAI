import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def gpt_ile_cevapla(metin):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=metin,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
