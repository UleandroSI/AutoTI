# coding: utf-8
__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"


import time
from sistema.comparaArquivo import *

def menu(lista):
    itensMenu = len(lista)
    conteudoMenu = lista
    while True:
        cont = 1
        linha()
        print('Escolha uma das Opções: ')
        for item in conteudoMenu:
            print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
            cont += 1

        dig = input("-> ")
        opc = validaInt(dig, itensMenu)
        match opc:
            case 1:
                comparaArquivo.Completo()
            case 2:
                comparaArquivo.Linhas()
            case 3:
                print("Encerrando Obrigado!")
                time.sleep(2)
                break
            case KeyboardInterrupt:
                print("Encerrado pelo usuário. Obrigado!")
                time.sleep(2)
                break


def validaInt(entrada, itensMenu):
    try:
        entrada.isdigit()
        entrada = int(entrada)
        if entrada < 0 or entrada > itensMenu:
            print(f'{entrada} - Somente Opções do Menu!')
    except ValueError:
        print(f'{entrada} não é um valor valido!')
    return entrada


def linha(tam=42):
    print('-' * tam)


def final(tam=42):
    print('*' * tam)
