import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    #if comando in ('olá', 'boa tarde', 'bom dia'):
        #return 'Olá tudo bem!'
    #if comando == 'como estás':
        #return 'Estou bem, obrigado!'
    #if comando == 'como te chamas?':
        #return 'O meu nome é: Bot :)'
    #if comando == 'tempo':
        #return 'Está um dia de sol!'
    #if comando in ('bye', 'adeus', 'tchau'):
        #return 'Gostei de falar contigo! Até breve...'
    #if 'horas' in comando:
        #return f'São: {datetime.now():%H:%M} horas'
    #if 'data' in comando:
        #eturn f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    #return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia', 'boa noite'): 'Olá, tudo bem?',
        ('como estás'): 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau', 'até logo'): 'Gostei de falar contigo! Até breve...',
        ('como te chamas', 'qual é o teu nome', 'quem és tu'): 'O meu nome é ChatBot!',
        ('horas', 'tens horas', 'que horas são'): f'São: {datetime.now():%H:%M} horas',
        ('dia', 'hoje', 'que dia é hoje', 'data'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('piada', 'anedota', 'algo engraçado', 'rir'):  'O que diz um tomate para o outro? \n ... \n Tu matas-me!',
        ('jogo', 'vamos jogar', 'brincar', 'passatempo'): 'OK! Que tal uma adivinha? O que é que quanto mais seca, mais molhada fica?',
        ('toalha'): 'Acertaste! Muito bem!'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()