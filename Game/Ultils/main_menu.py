def menu():
    """
    Display the main menu and collect user input.

    Returns:
        tuple: A tuple containing user details (name, gender, subject, pronoun, story choice).
    """
    nome = input('\033[4;33mDigite o nome: \033[m')
    sexo = input('\033[4;33mDigite o seu genero\n M para Homen\n F para mulher\n O outros\n Digite: \033[m')
    match sexo:
        case "M":
            Sujeito = 'O'
            Pronome = 'ele'
        case "F":
            Sujeito = 'A'
            Pronome = 'ela'
        case "O":
            Sujeito = 'E'
            Pronome = 'ele(a)'
        case _:
            Sujeito = 'O'
            Pronome = 'ele'
    print('\033[0;32mMuito bem {}\033[m\n'.format(nome))
    story = int(input('\033[4;33mQual situa\u00e7\u00e3o voce quer ver\n 1 voce encontrou uma pessoa no meio da estrada\n 2 voce esta numa fila de um banco\n 3 voce e um resepicionista/gar\u00e7om de um restalrante\n digite: \033[m'))
    return nome, sexo, Sujeito, Pronome, story
