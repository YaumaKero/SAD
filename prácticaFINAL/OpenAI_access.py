import openai

# Defino comandos para generar texto a partir de una pregunta
def responseAI(pregunta:str):
    openai.api_key = "YOUR_API_KEY"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pregunta,
        max_tokens=10,
        stop=None,
        temperature=0.1,
        n=1
    )
    respuesta_generada = response.choices[0].text.strip()
    return respuesta_generada