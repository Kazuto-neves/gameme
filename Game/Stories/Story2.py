def Story(audio_player, nome, Sujeito):
    print(
        '\033[7m{} {} esta querendo pegar o seu dinheiro na sua caderneta de polpança mas ve que a fila esta muito longa\033[m'.format(
            Sujeito, nome))
    o2 = int(input(
        '\033[4;33mOque voce faz\n 1 vai fazer outra coisa e voltar mas tarde\n 2 vai esperar na fila\n digite: \033[m'))
    if o2 == 1:
        print(
            '\033[7m{} {} voltou mas tarde e viu que a fila tinha diminuido então {} foi para a fila\nmas {} não esperava que isso ia acontecer\num ladrão estava esperando\nassim que {} saiu o ladrão ja veio falando passa tudo\n\033[m'.format(
                Sujeito, nome, Sujeito, nome, nome))
        o21 = int(input(
            '\033[4;33mOque voce faz\n 1 corre o mais rapido que puder\n 2 entrega o dinheiro\n 3 grita para chamar a atenção dos quardas\n digite: \033[m'))
        if o21 == 1:
            print(
                '\033[7m{} {} tentou fugir mas não conseguiu e acabou sendo atingido pela bala do ladrão que levou o dinheiro\nfim de jogo\n\033[m'.format(
                    Sujeito, nome))
            audio_player.play('pega.mp3')
        elif o21 == 2:
            print(
                '\033[7m{} {} entrga o dinheiro pro ladrão so que ele te mata mesmo assim\nfim de jogo\n\033[m'.format(
                    Sujeito, nome))
            audio_player.play('come.mp3')
        else:
            print('\033[7m{} {} grita\n\033[m'.format(Sujeito, nome))
            audio_player.play('PegaLadrao.mp3')
            print('\033[7mdigite qualquer coisa para continuar\033[m')
            input("")
            print(
                '\033[7mos guardas escutam e pegam o ladrão\n{} resebe uma recompença no valor de \nfim de jogo\033[m'.format(
                    nome))
            audio_player.play('mil8.mp3')
    else:
        print('\033[7m{} {} esperou\n\033[m'.format(Sujeito, nome))
        audio_player.play('1.mp3')
        print('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        print('\033[7m{} {} esperou!\n\033[m'.format(Sujeito, nome))
        audio_player.play('2.mp3')
        print('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        print('\033[7m{} {} esperou!!!!\n\033[m'.format(Sujeito, nome))
        audio_player.play('3.mp3')
        print('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        print('\033[7m{} {} esperou!!!!!!\n\033[m'.format(Sujeito, nome))
        audio_player.play('2000.mp3')
        print('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        print('\033[7mate que morreu de exastão\n\033[m'.format(nome))
        print('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        print("""\033[;31m                                .,od88888888888bo,.
                                    .d88888888888888888888888b.
                                .d88888888888888888888888888888b.
                               .d888888888888888888888888888888888b.
                             .d8888888888888888888888888888888888888b.
                            d88888888888888888888888888888888888888888b
                           d8888888888888888888888888888888888888888888b
                          d888888888888888888888888888888888888888888888
                          8888888888888888888888888888888888888888888888
                          8888888888888888888888888888888888888888888888
                          8888888888888888888888888888888888888888888888
                          Y88888888888888888888888888888888888888888888P
                          "8888888888P'   "Y8888888888P"    "Y888888888"
                           88888888P        Y88888888P        Y88888888
                           Y8888888          ]888888P          8888888P
                            Y888888          d888888b          888888P
                             Y88888b        d88888888b        d88888P
                              Y888888b.   .d88888888888b.   .d888888
                               Y8888888888888888P Y8888888888888888
                                888888888888888P   Y88888888888888
                                "8888888888888[     ]888888888888"
                                   "Y888888888888888888888888P"
                                        "Y88888888888888P"
                                     888b  Y8888888888P  d888
                                     "888b              d888"
                                      Y888bo.        .od888P
                                       Y888888888888888888P
                                        "Y88888888888888P"
                                          "Y8888888888P"
                  d8888bo.                  "Y888888P"                  .od888b
                 888888888bo.                                        .od8888888
                 "88888888888b.                                   .od888888888[
                 d8888888888888bo.                              .od888888888888
               d88888888888888888888bo.                     .od8888888888888888b
               ]888888888888888888888888bo.            .od8888888888888888888888b=
               888888888P" "Y888888888888888bo.     .od88888888888888P" "Y888888P=
                Y8888P"           "Y888888888888bd888888888888P"            "Y8P
                  ""                   "Y8888888888888888P"
                                         .od8888888888bo.
                                     .od888888888888888888bo.
                                 .od8888888888P"  "Y8888888888bo.
                              .od8888888888P"        "Y8888888888bo.
                          .od88888888888P"              "Y88888888888bo.
                .od888888888888888888P"                    "Y8888888888888888bo.
               Y8888888888888888888P"                         "Y8888888888888888b=
               888888888888888888P"                            "Y8888888888888888=
                "Y888888888888888                               "Y88888888888888P=
                     ""Y8888888P                                  "Y888888P"
                        "Y8888P                                     Y888P""

                                █▀▀ █▀▀█ ▀█░█▀ █▀▀ ░▀░ █▀▀█ █▀▀█
                                █░░ █▄▄█ ░█▄█░ █▀▀ ▀█▀ █▄▄▀ █▄▄█
                                ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀░▀▀ ▀░░▀
                \033[m""")
        audio_player.play('caveira.mp3')