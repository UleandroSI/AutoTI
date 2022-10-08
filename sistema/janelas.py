# coding: utf-8
__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"


import PySimpleGUI as sg
from comparaArquivo import *


# janela inicial
def Janela_inicial():
    sg.theme("Reddit")
    layout = [
        [sg.Text("     Automatizar TI - v1.0     ")],
        [sg.Text()],
        [sg.Button("Comparar arquivos completo")],
        [sg.Button("Comparar arquivos por linhas")],
        [sg.Button("Informações")],
        [sg.Text()],
        [sg.Button("Sair")]
    ]
    window = sg.Window('AutoTI - uLeandroSP', layout, finalize=True)
    return window


def Janela_insereCaminho():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Insirir caminho dos arquivos que quer comparar:")],
        [sg.Text('Arquivo 1', size=(10, 1)), sg.InputText(key='caminho_arquivo1'), sg.FileBrowse()],
        [sg.Text('Arquivo 2', size=(10, 1)), sg.InputText(key='caminho_arquivo2'), sg.FileBrowse()],
        [sg.Button("Voltar"), sg.Submit(), sg.Button("Limpar")]
    ]
    window = sg.Window('Inserir caminho do arquivo', layout, finalize=True)
    return window


def Janela_exibiçao(retorno_da_funcao):
    sg.theme("Monokay")
    layout = [
        [sg.Text("     Automatizar TI - v1.0     ")],
        [sg.Text(size=(1,3))],
        [sg.Text(size=(400,10), key='-OUTPUT-')],
        [sg.Quit()]
    ]
    window = sg.Window('Arquivos comparados', layout, finalize=True)
    return window


# janelas iniciais
janela1, janela2, janela3 = Janela_inicial(), None, None

# loop leitura de eventos
while True:
    window, event, value = sg.read_all_windows()


    # quando  a janela for fechada
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "Comparar arquivos completo":
        escolha = 1
        janela1.hide()
        janela2 = Janela_insereCaminho()
    if event == "Comparar arquivos por linhas":
        escolha = 2
        janela1.hide()
        janela2 = Janela_insereCaminho()
    if event == "Informações":
        escolha = 3
        pass
    if window == janela2 and event == "Voltar":
        janela2.close()
        janela1.un_hide()
    if window == janela2 and event == "Limpar":
        pass
    if window == janela2 and event == "Submit":
        arquivo1 = value['caminho_arquivo1']
        arquivo2 = value['caminho_arquivo2']
        if escolha == 1:
            CompararCompleto(arquivo1, arquivo2)
        elif escolha == 2:
            CompararLinhas(arquivo1, arquivo2)
        elif escolha == 3:
            CompararDiretorios(arquivo1, arquivo2)

        # print(arquivo1)
        janela2.close()
        janela1.un_hide()

window.close()




### Referencias
# https://www.pysimplegui.org/en/latest/#getting-started-with-pysimplegui
'''
sg.popup('popup')  # Shows OK button
sg.popup_ok('popup_ok')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed
'''
