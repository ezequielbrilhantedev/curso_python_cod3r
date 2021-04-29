def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='l. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
