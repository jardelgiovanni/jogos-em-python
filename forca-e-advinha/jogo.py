import adivinhacao
import forca

def escolher():
    print('*******************************')
    print('********Escolha um jogo********')
    print('*******************************')

    print('(1) Forca (2) Advinhação')
    jogo = int(input('Qual jogo você deseja: '))

    if (jogo == 1):
        print('Jogando Forca')
        forca.jogar_forca()
    else:
        print('Jogando Adivinhação')
        adivinhacao.jogar_advinhacao()

if (__name__ == '__main__'):
    escolher()