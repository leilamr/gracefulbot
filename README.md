# Gracefulbot
Minibot com reconhecimento de saudações, agradecimentos e despedidas usando TensorFlow integrado ao Telegram (pt-br)(python)

# Requisitos
- Python 3.5
- Bibliotecas necessárias:
    - NLTK
    - Numpy
    - Tflearn
    - Random
    - Telebot
    
# Funcionamento
- O projeto é divido em três passos:
    - Transformar intenções conversação em um modelo TensorFlow
    - Criar uma estrutura de chatbot para processar respostas
    - Conectar o nosso modelo ao Telegram
    
# Intents.json
- O bot reconhece as seguintes expressões, que estão dividias em 4 (quatro) tags:
    - Tag: Saudação
        - "Oi","Tem alguém aí?", "Olá", "Bom dia", "Boa tarde", "Boa noite", "Seja bem-vindo", "Tudo bem?", "Tudo bom?", "Como você está?", "Como está?"
        - Possíveis respostas:     
            - "Oi, tudo bem?", "Bom te ver de novo", "Olá, como posso ajudar?", "Oi, como está?"
    - Tag: Agradecimentos
        - "Obrigada", "Muito obrigada", "Obrigada pela atenção", "Grata pela ajuda", "De nada", "Obrigado", "Muito obrigado",             "Obrigado pela atenção", "Grato pela ajuda", "Obrigada pela atencao", "Obrigado pela atencao","Ok", "Valeu",                   "Agradecido"
        - Possíveis respostas:
            - "Feliz por ajudar!", "Estou a disposição", "Foi um prazer.", "De nada!"
    - Tag: Despedidas
        - "Tchau", "Até logo", "Até amanha", "Foi um prazer", "Adeus", "Até mais", "Até breve"
        - Possíveis respostas:
            - "Até logo, obrigada por conversar comigo.", "Tenha um lindo dia.", "Tchau! Volte novamente em breve.", "Tchau", 
        "Até breve",

