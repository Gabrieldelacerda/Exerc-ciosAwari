def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input('Digite um numero'))
if verificar_primo(numero):
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} n e')