# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim')

from random import randint


# def sortear_dados():
#     numero_sorteado = randint(1, 6)
#     print(numero_sorteado)

#     for numero in range(1, 7):
#         if numero % 2 != 0:
#             continue
#         elif numero % 2 == 0 and numero == numero_sorteado:
#             print('Acertou', numero)
#             break
#     else:
#         print('Não acertou o número!')


def sortear_dados():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dados() == i:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número!')

# if __name__ == '__main__':
#     sortear_dados()
