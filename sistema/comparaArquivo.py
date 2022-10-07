# coding: utf-8
__author__ = "UleandroSI"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["Leandro Barbosa"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Leandro Barbosa"
__email__ = "uleandrosp7@gmail.com"
__status__ = "Development"

import filecmp

def pathArquivos():
    arquivo1 = input("Digite o endereço completo do arquivo 1\033[31m'Inclusive extensão'\033[m:\n")
    arquivo2 = input("Digite o endereço completo do arquivo 2\033[31m'Inclusive extensão'\033[m:\n")
    return arquivo1, arquivo2


def Completo():
    f1, f2 = pathArquivos()
    #f1 = "C:/Users/lbarbosa/Documents/Git/Untitled.ipynb"
    #f2 = "C:/Users/lbarbosa/Documents/Git/Untitled1.ipynb"
    result = filecmp.cmp(f1, f2)
    print(result)
    result = filecmp.cmp(f1, f2, shallow=False)
    print(result)


def Linhas():
    arq1, arq2 = pathArquivos()
    f1 = open(arq1, "r")
    f2 = open(arq2, "r")
    
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            if line1 == line2:
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
                
            break
        
    f1.close()
    f2.close()
