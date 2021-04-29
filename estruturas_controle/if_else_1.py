# Conceitos   Notas
# A           De 10,0 à 9,1
# A-          De 9,0 à 8,1
# B           De 8,0 à 7,1
# B-          De 7,0 à 6,1
# C           De 6,0 à 5,1
# C-          De 5,0 à 4,1
# D           De 4,0 à 3,1
# D-          De 3,0 à 2,1
# E           De 2,0 à 1,1
# E-          De 1,0 à 0,0

# Para notas maiores que 10 e menores que 0, será impresso "Nota inválida"

def notaAluno(nota):
    if float(nota) > 10.0:
        print('Nota Inválida')
    elif float(nota) > 9.1:
        print('A')
    elif float(nota) >= 8.1:
        print('A-')
    elif float(nota) >= 7.1:
        print('B')
    elif float(nota) >= 6.1:
        print('B-')
    elif float(nota) >= 5.1:
        print('C')
    elif float(nota) >= 4.1:
        print('C-')
    elif float(nota) >= 3.1:
        print('D')
    elif float(nota) >= 2.1:
        print('D-')
    elif float(nota) >= 1.1:
        print('E')
    elif float(nota) >= 0.0:
        print('E-')
    else:
        print('Nota inválida')


if __name__ == '__main__':
    nota = input('Digite a nota do aluno: ')
    notaAluno(nota)
