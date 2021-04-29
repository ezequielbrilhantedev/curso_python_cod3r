
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()
