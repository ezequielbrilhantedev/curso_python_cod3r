PALAVRAS_PROIBIDAS = ('religião', 'futebol', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            break

    else:
        print('Texo autorizado: ', texto)
