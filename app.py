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
        ('como estás', 'tudo bem', 'como vai tudo'): 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau', 'até logo'): 'Gostei de falar contigo! Até breve...',
        ('como te chamas', 'qual é o teu nome', 'quem és tu', 'nome'): 'O meu nome é ChatBot!',
        ('horas', 'tens horas', 'que horas são', 'dá-me as horas'): f'São: {datetime.now():%H:%M} horas',
        ('dia', 'hoje', 'que dia é hoje', 'data'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('tempo', 'lá fora', 'está bom tempo', 'está a chover'): 'Está um belo dia de sol!',
        ('piada', 'anedota', 'algo engraçado', 'rir'):  'O que diz um tomate para o outro? \n ... \n Tu matas-me!',
        ('jogo', 'vamos jogar', 'brincar', 'passatempo', 'estou aborrecido'): 'OK! Que tal uma adivinha? O que é que quanto mais seca, mais molhada fica?',
        ('toalha', 'uma toalha', 'é uma toalha'): 'Acertaste! Muito bem!',
        ('não sei', 'pista', 'dica', 'dá-me uma pista'): 'Pista: É uma coisa que encontras na casa de banho.',
        ('facto', 'algo interessante', 'curiosidade'): 'O mais longo vôo registado de uma galinha durou 13 segundos.',
        ('filosofia', 'pensamento', 'em que estás a pensar', 'diz alguma coisa'): 'O senso comum é o menos comum de todos os sensos.',
        ('contar', 'contagem', 'números', 'escondidas'): 'Ok! 1... 2... 3... 4... 5... 6... 7... 8... 9... 10...',
        ('palavra do dia', 'dicionário', 'vocabulário'): 'A palavra do dia é: Codícia. Um apetite intenso por riquezas, bens materiais ou dinheiro.',
        ('programar', 'sabes programar', 'python', 'código'): 'Eu não consigo ajudar-te a programar. Mas eu acredito que vais conseguir!',
        ('filmes', 'filme', 'recomendação', 'quero ver um filme'): 'Filmes no Top 5 do IMDB: \n - Os Condenados de Shawshank \n - O Padrinho \n - O Cavaleiro das Trevas \n - O Padrinho: Parte 2 \n - 12 Homens em Fúria',
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