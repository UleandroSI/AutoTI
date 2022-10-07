# coding: utf-8
__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

from sistema import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('\033[32mAutomatizar TI v1.0\033[m'.center(42))
    print(linha())
    menu(['Comparar Arquivo Completo','Comparar Linhas do Arquivo', 'Comparar em diretorio diferente','Sair'])
    print(final())

