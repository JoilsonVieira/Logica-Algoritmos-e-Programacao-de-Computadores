saida = ''


def adicao(a, b):
    return a+b


def subtracao(a, b):
    return a-b


def multiplicacao(a, b):
    return a*b


def divisao(a, b):
    if a == 0 or b == 0:
        return 'Não foi possivel realizar a divisão por 0.'
    else:
        return a/b


def calculadora(a, b, operador):
    resultado = 0

    if (operador == 'multiplicacao' or operador == '*'):
        resultado = multiplicacao(a, b)
        return resultado

    elif (operador == 'adicao' or operador == '+'):
        resultado = adicao(a, b)
        return resultado

    elif (operador == 'subtracao' or operador == '-'):
        resultado = subtracao(a, b)
        return resultado

    elif (operador == 'divisao' or operador == '/'):
        resultado = divisao(a, b)
        return resultado


while saida != "N":
    a = eval(input('Digite o primeiro numero:'))
    operador = input(
        'Digite o operador(+ - * / ou adicao,subtracao,multiplicacao,divisao):')
    b = eval(input('Digite o segundo numero:'))

    resultado = calculadora(a, b, operador)
    print(f'O resultado da operação {a}{operador}{b} = {resultado}')
    saida = input('Deseja continar? S(sim)/N(não)').upper()
