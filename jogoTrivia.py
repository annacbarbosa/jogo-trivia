import random

def jogar():
    """
    Função principal para jogar o jogo.
    """
    pontuacao_total = 0
    
    while True:  # Loop principal do jogo
        print("\nNovo jogo...")
        pontuacao = 0
        perguntas = selecionar_perguntas(trivia, 5)
        
        for pergunta in perguntas:
            resposta = mostrar_pergunta(pergunta)
            if resposta == pergunta["resposta"]:
                print("Resposta correta!\n")
                pontuacao += 1
            else:
                print(f"Resposta incorreta. A resposta correta era: {pergunta['resposta'].upper()}\n")
        
        print("Sua pontuação nesta rodada foi:", pontuacao)
        pontuacao_total += pontuacao
        
        if pontuacao == 5:
            print("Você acertou todas as perguntas desta rodada!")
        else:
            print("Você errou uma pergunta ou mais nesta rodada.")
            print("Sua pontuação total até agora é:", pontuacao_total)
            break  # O jogo termina se o jogador errar uma pergunta ou mais
    
    print("O jogo acabou. Sua pontuação final foi:", pontuacao_total)


trivia = [
    {
        "pergunta": "Quem foi a primeira pessoa a viajar no Espaço?",
        "alternativas": ["a) Yuri Gagarin", "b) A cadela Laika", "c) Neil Armstrong", "d) Buzz Aldrin"],
        "resposta": "a"
    },
    {
        "pergunta": "Quantos ossos temos no nosso corpo?",
        "alternativas": ["a) 206", "b) 126", "c) 300", "d) 18"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual a personagem mais famosa de Maurício de Sousa?",
        "alternativas": ["a) Mônica", "b) Mafalda", "c) Menino Maluquinho", "d) Smurfette"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual a nacionalidade de Napoleão Bonaparte?",
        "alternativas": ["a) Búlgara", "b) Espanhola", "c) Francesa", "d) Sul-Africana"],
        "resposta": "c"
    },
    {
        "pergunta": "Quem pintou a 'Mona Lisa'?",
        "alternativas": ["a) Michelangelo", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Vincent van Gogh"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual é o país mais populoso do mundo?",
        "alternativas": ["a) Índia", "b) Estados Unidos", "c) China", "d) Rússia"],
        "resposta": "c"
    },
    {
        "pergunta": "Quem escreveu 'Romeu e Julieta'?",
        "alternativas": ["a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Emily Brontë"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é a capital do Canadá?",
        "alternativas": ["a) Montreal", "b) Toronto", "c) Ottawa", "d) Vancouver"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual é o maior oceano do mundo?",
        "alternativas": ["a) Atlântico", "b) Índico", "c) Pacífico", "d) Ártico"],
        "resposta": "c"
    },
    {
        "pergunta": "Quem escreveu 'O Pequeno Príncipe'?",
        "alternativas": ["a) Antoine de Saint-Exupéry", "b) J.K. Rowling", "c) Roald Dahl", "d) Lewis Carroll"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é o maior deserto do mundo?",
        "alternativas": ["a) Deserto do Saara", "b) Deserto da Arábia", "c) Deserto de Gobi", "d) Deserto do Atacama"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é a capital da Austrália?",
        "alternativas": ["a) Sydney", "b) Perth", "c) Canberra", "d) Melbourne"],
        "resposta": "c"
    },
    {
        "pergunta": "Quem foi o primeiro presidente dos Estados Unidos?",
        "alternativas": ["a) Thomas Jefferson", "b) George Washington", "c) Abraham Lincoln", "d) John F. Kennedy"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual é o maior animal terrestre?",
        "alternativas": ["a) Elefante africano", "b) Baleia-azul", "c) Girafa", "d) Dinossauro"],
        "resposta": "a"
    },
    {
        "pergunta": "Quem pintou 'A Noite Estrelada'?",
        "alternativas": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Claude Monet", "d) Salvador Dalí"],
        "resposta": "a"
    }
]

def selecionar_perguntas(banco, quantidade):
    """
    Seleciona aleatoriamente uma quantidade específica de perguntas do banco.
    """
    return random.sample(banco, quantidade)

def mostrar_pergunta(pergunta):
    """
    Exibe uma pergunta e suas alternativas.
    """
    print(pergunta["pergunta"])
    [print(alternativa) for alternativa in pergunta["alternativas"]]
    resposta = input("Escolha a alternativa correta: ").lower()
    return resposta


jogar()
