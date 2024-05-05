import math
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Erro'
    return a / b

def raiz_quadrada(a):
    if a < 0:
        return 'Erro'
    return math.sqrt(a)

def potenciacao(a, b):
    return a ** b

def calculadora():
    operacao = input('Digite a operação ou sair: ')

    while operacao != 'sair':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        if operacao == '+':
            print(adicao(num1, num2))
        elif operacao == '-':
            print(subtracao(num1, num2))
        elif operacao == '*':
            print(multiplicacao(num1, num2))
        elif operacao == '/':
            print(divisao(num1, num2))
        elif operacao == 'sqrt':
            print(raiz_quadrada(num1))
        elif operacao == '^':
            print(potenciacao(num1, num2))


calculadora()