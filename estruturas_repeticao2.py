# Crie uma variável chamada texto e atribua a ela o valor ‘Olá, laço for.’;
# Crie uma instrução for que itere sobre a variável texto atribuindo cada um
# de seus caracteres a uma variável chamada item;
# Imprima, na tela, dentro do escopo do laço for, o valor da variável item
# precedido do texto 'Caractere: ';

texto = 'Olá, laço for.'


for item in texto:
    print('Caractere:', item)

# Itere sobre um intervalo numérico entre 1 e 10 (dica: use a instrução range);
# Imprima, na tela, dentro do escopo do laço for, o valor de cada número no
# intervalo acima precedido do texto ‘Número do intervalo: ‘ ;
# Lembre-se de utilizar a instrução str para concatenar o valor inteiro com a
# string no momento de imprimir o valor pedido na tela.

numero = range (1,10)

for valor in numero:
    
    print('Número do intervalo:',str(valor))