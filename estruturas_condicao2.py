#Crie uma variável chamada tempoExperiencia e atribua a ela o valor 5;
#Crie uma verificação, utilizando a condição if, para checar se o valor da variável tempoExperiencia é menor que 2;
#Caso positivo, imprima na tela o texto ‘Nível de conhecimento júnior.’;
#Após as instruções acima, crie uma outra condição utilizando elif (else if) para verificar se o valor da variável tempoExperiencia é maior que 2 e
#menor que 5. Em caso positivo, imprima o texto ‘Nível de conhecimento pleno.’
#Por fim, crie uma condição else e imprima o texto ‘Nível de conhecimento sênior.’;

tempoExperiencia = 3

if(tempoExperiencia < 2):
    print('Nível de conhecimento Júnior.')

elif((tempoExperiencia >= 2) and (tempoExperiencia <= 5)):
    print('Nível de conhecimento pleno')

else:
    print('Nível de conhecimento sênior')