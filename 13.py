import random

def escolher_palavra():
    palavras = ['python', 'programação', 'programar', 'computador', 'computadora']
    return random.choice(palavras)

def mostrar_palavra_secreta(palavra, letras_corretas):
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + ' '
        else:
            palavra_mostrada += '_ '
    return palavra_mostrada.strip()

def jogo_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas restantes = 6