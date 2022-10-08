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
from sistema import janelas

def CompararCompleto(f1, f2):
    result = filecmp.cmp(f1, f2)
    #print(result)
    janelas.Janela_exibiçao(result)
    result = filecmp.cmp(f1, f2, shallow=False)
    print(result)
    #return result


def CompararLinhas(f1, f2):
    arq1, arq2 = f1, f2
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

def CompararDiretorios(f1, f2):
    arq1, arq2 = f1, f2
    d1 = arq1
    d2 = arq2
    files = ['intro.txt']
    match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
    print('Shallow comparison')
    print("Match:", match)
    print("Mismatch:", mismatch)
    print("Errors:", errors)
    match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
    print('Deep comparison')
    print("Match:", match)
    print("Mismatch:", mismatch)
    print("Errors:", errors)
