# Ferramentas de uso TI
___
##	*Versão* *1.0*
## *Já implementados:*
___

### Pacote Sistema:

####	ComparaArquivo.py

#####	Função Completo
	Compara dois arquivos verificando hash
	
#####	Função Linhas
	Lista todas as linhas dos arquivos e compara linha por linha.
	
#####	Função Diretorios
	Compara arquivos em pasta diferente.
	Retorna três listas contendo: 
*	Arquivos correspondentes 
*	Arquivos incompatíveis 
*	Erros relacionados aos arquivos que não puderam ser comparados
	
##### Função pathArquivos
	Solicita por input os dois caminhos completos dos arquivos no computador, e retorna para ser utilizado para abrir o arquivo.
	
####	Arquivo __init__.py
#####	Função menu
	Menu recebe uma lista de itens vindo do main.py
*	É de tamanho dinâmico e numerado com 'For'
*	Envia para validaInt
*	Usa Match Case para fazer a escolha da opção
	
#####	Função validaInt
	Recebe o valor digitado pelo usuário e o número de itens do menu.
*	Valida se o número digitado é inteiro.
*	Valida se o número digitado é menor que 1 e maior que o número de itens do menu.

##### Função Linha
	Insere uma linha de - para separar a visualização da tela.
	
##### Função Final
	Insere uma linha de * para indicar o final da exibição do programa.


___

### Arquivo main.py:

*	Chama o menu para iniciar o sistema.
