
import os


try:
    from openai import OpenAI, OpenAIError
except ImportError:
    OpenAI = None
    OpenAIError = Exception


api_key = os.environ.get("OPENAI_API_KEY")
modo_mock = not api_key

client = None

if not modo_mock:
    if OpenAI is None:
        print("Biblioteca openai nao instalada. Usando modo mock.")
        modo_mock = True
    else:
        client = OpenAI(api_key=api_key)



historico = [
    {
        "role": "system",
        "content": (
            "Voce e um assistente de seguranca da informacao. "
            "Responda em portugues, com explicacoes simples e objetivas."
        )
    }
]


def responder_mock(mensagens):
    pergunta = mensagens[-1]["content"].lower()

   
    conversa = " ".join(
        mensagem["content"].lower()
        for mensagem in mensagens
        if mensagem["role"] == "user"
    )

    if "xss" in pergunta:
        return (
            "XSS (Cross-Site Scripting) e uma vulnerabilidade "
            "que permite inserir scripts maliciosos em paginas web."
        )

    if "prevenir" in pergunta and "xss" in conversa:
        return (
            "Para prevenir XSS, escape a saida HTML, "
            "valide as entradas e utilize templates "
            "com escape automatico, como Jinja2."
        )

    if "sql injection" in pergunta:
        return (
            "SQL Injection ocorre quando uma entrada maliciosa "
            "consegue alterar uma consulta SQL. "
            "A principal defesa e utilizar queries parametrizadas."
        )

    if "phishing" in pergunta:
        return (
            "Phishing e uma tentativa de enganar usuarios "
            "para obter dados, como senhas ou informacoes pessoais."
        )

    return (
        "No modo mock, consigo responder perguntas de exemplo "
        "sobre XSS, SQL Injection e phishing."
    )



def responder(mensagens):
    if modo_mock:
        return responder_mock(mensagens)

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens
    )

    return resposta.choices[0].message.content



print("=== CHATBOT DE SEGURANCA ===")

if modo_mock:
    print("Modo: MOCK (sem chamadas a API)")
else:
    print("Modo: API OpenAI")

print("Digite /sair para encerrar.\n")


while True:
    pergunta = input("Voce: ").strip()

    if pergunta.lower() == "/sair":
        print("Assistente: Ate logo!")
        break

    if not pergunta:
        print("Assistente: Digite uma pergunta.")
        continue

    mensagem_usuario = {
        "role": "user",
        "content": pergunta
    }

    try:
        
        mensagens = historico + [mensagem_usuario]

        resposta = responder(mensagens)

        if not resposta:
            print("Assistente: Nao foi possivel gerar uma resposta.")
            continue

      
        historico.append(mensagem_usuario)
        historico.append({
            "role": "assistant",
            "content": resposta
        })

        print("Assistente:", resposta)

    except OpenAIError:
        print("Assistente: Erro ao consultar a API. Tente novamente.")

    except (OSError, ValueError):
        print("Assistente: Erro de comunicacao ou configuracao.")
