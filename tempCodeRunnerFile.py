comando = "clima"
match comando:
    case "oi" | "olá":
        print("Oi, como vai você?")
    case "clima" | "previsão do tempo":
        print("Está muito quente. Deve ter passado de 40 graus.")
    case _:
        print("Desculpe, não entendi o comando.")