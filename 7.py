numeros = [10, 5, 8, 12, 3]
maior_elemento = numeros[0]
for numero in numeros:
    if numero > maior_elemento:
        maior_elemento = numero
print(f'O maior valor é {maior_elemento}')