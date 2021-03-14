import random

def jogar_advinhacao():
    print('*******************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('*******************************')

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000
    #rodada = 1

    print('Niveis de dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Digite o dificuldate desejada: '))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    # while(rodada <= tentativas):
    for rodada in range(1, tentativas +1):
        print( 'Tentativa {} de {}'.format(rodada, tentativas))
        numero = input('Digite um número enre 1 e 100: ')
        print('Você digitou: ', numero)
        chute = int(numero)

        if (chute < 1 or chute > 100):
            print('Digite um valor entre 1 e 100: ')
            continue

        if (numero_secreto == chute):
            print('Você acertou, seus pontos são {}'.format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print('Você errou! O número foi maior que o número certo')
            elif (chute < numero_secreto):
                print('Você errou! O número foi menor que o número certo')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim do Jogo')

if (__name__ == '__main__'):
    jogar_advinhacao()