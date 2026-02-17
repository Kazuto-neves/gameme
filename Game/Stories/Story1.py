def Story(audio_player, nome, Sujeito):
    print(
        '\033[7m{} {} estava voltando para sua casa quando avista uma pessoa no meio da estrada\033[m'.format(Sujeito, nome))
    o1 = int(input(
        '\033[4;33mOque voce faz\n 1 vai embora e deixa a pessoa para la\n 2 vai ver se ela esta viva\n digite: \033[m'))
    if o1 == 1:
        print('\033[7m{} {} ouviu o grito\033[m'.format(Sujeito, nome))
        audio_player.play('souseupai.mp3')
        o111 = int(input('\033[4;33mOque voce faz\n 1 volta e para onde esta a pessoa\n 2 vai embora\n digite: \033[m'))
        if o111 == 1:
            print('\033[7mFim de jogo\n {} foi trolado\033[m'.format(nome))
            audio_player.play('trolei.mp3')
        else:
            print('\033[7mFim de jogo\n {} não foi trolado\033[m'.format(nome))
    else:
        print('\033[7m{} {} ve que ele esta acordando\n\033[m'.format(Sujeito, nome))
        o12 = int(input(
            '\033[4;33mOque voce faz\n 1 pergunta se ele esta bem\n 2 rouba a carteira dele enquanto ele esta zonzo\n digite: \033[m'))
        if o12 == 1:
            print('\033[7m{} {} pergunta se esta bem e ele responde\n\033[m'.format(Sujeito, nome))
            audio_player.play('aaa.mp3')
            print('\033[7m{} {} liga para a ambulancia mas esta sem sinal\n\033[m'.format(Sujeito, nome))
            o121 = int(input(
                '\033[4;33mVoce tem duas alternativas\n 1 colocar o cara dentro do seu carro\n 2 tirar ele do meio da estrada e colocar na calsada \n digite: \033[m'))
            if o121 == 1:
                print('\033[7m Na hora que {} {} foi colocar o cara no carro ele gritou\n\033[m'.format(Sujeito, nome))
                audio_player.play('pede.mp3')
                print('\033[7m{} {} então percebe que ele esta alterado\n\033[m'.format(Sujeito, nome))
                o1212 = int(
                    input('\033[4;33mVoce faz oque\n 1 tenta conversar com ele\n 2 foje de la \n digite: \033[m'))
                if o1212 == 1:
                    print('\033[7m{} {} pergunta qual e o nome dele\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print(
                        '\033[7m{} {} pergunta se ele sabia oque aconteceu\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print('\033[7m{} {} pergunta se estava de carro\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naoseiii.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print(
                        '\033[7m{} {} então sente um cheiro de alcool e fala voce esta empreagado\n e veio a resposta\n\033[m'.format(
                            Sujeito, nome))
                    audio_player.play('queropova.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print('\033[7mA pessoa se altera e parte para cima do {} e acaba ficando inconciete\n\033[m'.format(
                        nome))
                    print('\033[7mFim de jogo\n voce não deve falar que a pessoa esta empreagada\033[m')
                else:
                    print('\033[7mFim de jogo\n\033[m')
                    audio_player.play('cagao.mp3')
            else:
                print('\033[7m Na hora que {} {} foi colocar o cara no lugar seguro\n\033[m'.format(Sujeito, nome))
                audio_player.play('pede.mp3')
                print('\033[7m{} {} então percebe que ele esta alterado\n\033[m'.format(Sujeito, nome))
                o122 = int(
                    input('\033[4;33mVoce faz oque\n 1 tenta conversar com ele\n 2 foje de la \n digite: \033[m'))
                if o122 == 1:
                    print('\033[7m{} {} pergunta qual e o nome dele\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print(
                        '\033[7m{} {} pergunta se ele sabia oque aconteceu\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print('\033[7m{} {} pergunta se estava de carro\n e veio a resposta\n\033[m'.format(Sujeito, nome))
                    audio_player.play('naoseiii.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print(
                        '\033[7m{} {} então sente um cheiro de alcool e fala voce esta empreagado\n e veio a resposta\n\033[m'.format(
                            Sujeito, nome))
                    audio_player.play('queropova.mp3')
                    print('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    print('\033[7mA pessoa se altera e parte para cima do {} e acaba ficando inconciete\n\033[m'.format(
                        nome))
                    print('\033[7mFim de jogo\n voce não deve falar que a pessoa esta empreagada\033[m')
                else:
                    print('\033[7mFim de jogo\n\033[m')
                    audio_player.play('cagao.mp3')
        else:
            print('\033[7m{} {} pega a carteira mas ouve um grito\n\033[m'.format(Sujeito, nome))
            audio_player.play('PegaLadrao.mp3')
            print('\033[7mdigite qualquer coisa para continuar\033[m')
            input("")
            print('\033[7mna hora vem varios policias\nconclusão voce e preso por roubo\nfim de jogo\033[m')