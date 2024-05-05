def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
numero = int(input('Digite um número: '))
resultado = factorial(numero)
print(f'O fatorial de {numero} é {resultado}')