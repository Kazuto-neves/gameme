generos = {
    "M": {'pronome': 'O', 'pronome2': 'ele'},
    "F": {'pronome': 'A', 'pronome2': 'ela'},
    "O": {'pronome': 'E', 'pronome2': 'ele(a)'}
}

def checkGender(opicao):
    if opicao in generos:
        genero = generos[opicao]
    return (genero['pronome'],genero['pronome2'])