def verificar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Digite um número: "))
resultado = verificar(numero)
print(f'O número {numero} é {resultado}')