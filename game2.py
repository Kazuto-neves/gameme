﻿from playsound import playsound
import Services.Path as path
import Services.input_output_processor as io
import Services.genres as gen

def Play(dir):
    playsound(path.GetPath(dir))

io.read('\033[0;32mBem vindo ao gameme\033[m')
nome = input('\033[4;33mDigite o nome: \033[m')
Genero = gen.checkGender(io.write('\033[4;33mDigite o seu genero\n M para Homen\n F para mulher\n O outros\n Digite: \033[m'))
io.read('\033[0;32mMuito bem {}\033[m\n'.format(nome))
o = int(input('\033[4;33mQual situação voce quer ver\n 1 voce encontrou uma pessoa no meio da estrada\n 2 voce esta numa fila de um banco\n 3 voce e um resepicionista/garçom de um restalrante\n digite: \033[m'))
if o == 1:
    io.read('\033[7m{} {} estava voltando para sua casa quando avista uma pessoa no meio da estrada\033[m'.format(Genero[0], nome))
    o1 = int(input('\033[4;33mOque voce faz\n 1 vai embora e deixa a pessoa para la\n 2 vai ver se ela esta viva\n digite: \033[m'))
    if o1 == 1:
        io.read('\033[7m{} {} ouviu o grito\033[m'.format(Genero[0], nome))
        Play("souseupai.mp3")
        o111 = int(input('\033[4;33mOque voce faz\n 1 volta e para onde esta a pessoa\n 2 vai embora\n digite: \033[m'))
        if o111 == 1:
            io.read('\033[7mFim de jogo\n {} foi trolado\033[m'.format(nome))
            Play("trolei.mp3")
        else:
            io.read('\033[7mFim de jogo\n {} não foi trolado\033[m'.format(nome))
    else:
        io.read('\033[7m{} {} ve que ele esta acordando\n\033[m'.format(Genero[0], nome))
        o12 = int(input('\033[4;33mOque voce faz\n 1 pergunta se ele esta bem\n 2 rouba a carteira dele enquanto ele esta zonzo\n digite: \033[m'))
        if o12 == 1:
            io.read('\033[7m{} {} pergunta se esta bem e ele responde\n\033[m'.format(Genero[0], nome))
            Play("aaa.mp3")
            io.read('\033[7m{} {} liga para a ambulancia mas esta sem sinal\n\033[m'.format(Genero[0], nome))
            o121 = int(input('\033[4;33mVoce tem duas alternativas\n 1 colocar o cara dentro do seu carro\n 2 tirar ele do meio da estrada e colocar na calsada \n digite: \033[m'))
            if o121 == 1:
                io.read('\033[7m Na hora que {} {} foi colocar o cara no carro ele gritou\n\033[m'.format(Genero[0], nome))
                Play("pede.mp3")
                io.read('\033[7m{} {} então percebe que ele esta alterado\n\033[m'.format(Genero[0], nome))
                o1212 = int(input('\033[4;33mVoce faz oque\n 1 tenta conversar com ele\n 2 foje de la \n digite: \033[m'))
                if o1212 == 1:
                    io.read('\033[7m{} {} pergunta qual e o nome dele\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    Play("naosei.mp3")
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} pergunta se ele sabia oque aconteceu\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    Play("naosei.mp3")
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} pergunta se estava de carro\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    Play("naoseiii.mp3")
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} então sente um cheiro de alcool e fala voce esta empreagado\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    Play("queropova.mp3")
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7mA pessoa se altera e parte para cima do {} e acaba ficando inconciete\n\033[m'.format(nome))
                    io.read('\033[7mFim de jogo\n voce não deve falar que a pessoa esta empreagada\033[m')
                else:
                    io.read('\033[7mFim de jogo\n\033[m')
                    Play("cagao.mp3")
            else:
                io.read('\033[7m Na hora que {} {} foi colocar o cara no lugar seguro\n\033[m'.format(Genero[0], nome))
                pede()
                io.read('\033[7m{} {} então percebe que ele esta alterado\n\033[m'.format(Genero[0], nome))
                o122 = int(input('\033[4;33mVoce faz oque\n 1 tenta conversar com ele\n 2 foje de la \n digite: \033[m'))
                if o122 == 1:
                    io.read('\033[7m{} {} pergunta qual e o nome dele\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    naosei()
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} pergunta se ele sabia oque aconteceu\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    naosei()
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} pergunta se estava de carro\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    naoseiii()
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7m{} {} então sente um cheiro de alcool e fala voce esta empreagado\n e veio a resposta\n\033[m'.format(Genero[0], nome))
                    Play("queropova.mp3")
                    io.read('\033[7mdigite qualquer coisa para continuar\033[m')
                    input("")
                    io.read('\033[7mA pessoa se altera e parte para cima do {} e acaba ficando inconciete\n\033[m'.format(nome))
                    io.read('\033[7mFim de jogo\n voce não deve falar que a pessoa esta empreagada\033[m')
                else:
                    io.read('\033[7mFim de jogo\n\033[m')
                    Play("cagao.mp3")
        else:
            io.read('\033[7m{} {} pega a carteira mas ouve um grito\n\033[m'.format(Genero[0], nome))
            Play("PegaLadrao.mp3")
            io.read('\033[7mdigite qualquer coisa para continuar\033[m')
            input("")
            io.read('\033[7mna hora vem varios policias\nconclusão voce e preso por roubo\nfim de jogo\033[m')
elif o == 2:
    io.read('\033[7m{} {} esta querendo pegar o seu dinheiro na sua caderneta de polpança mas ve que a fila esta muito longa\033[m'.format(Genero[0], nome))
    o2 = int(input('\033[4;33mOque voce faz\n 1 vai fazer outra coisa e voltar mas tarde\n 2 vai esperar na fila\n digite: \033[m'))
    if o2 == 1:
        io.read('\033[7m{} {} voltou mas tarde e viu que a fila tinha diminuido então {} foi para a fila\nmas {} não esperava que isso ia acontecer\num ladrão estava esperando\nassim que {} saiu o ladrão ja veio falando passa tudo\n\033[m'.format(Genero[0], nome, Genero[1]))
        o21 = int(input('\033[4;33mOque voce faz\n 1 corre o mais rapido que puder\n 2 entrega o dinheiro\n 3 grita para chamar a atenção dos quardas\n digite: \033[m'))
        if o21 == 1:
            io.read('\033[7m{} {} tentou fugir mas não conseguiu e acabou sendo atingido pela bala do ladrão que levou o dinheiro\nfim de jogo\n\033[m'.format(Genero[0], nome))
            Play("pega.mp3")
        elif o21 == 2:
            io.read('\033[7m{} {} entrga o dinheiro pro ladrão so que ele te mata mesmo assim\nfim de jogo\n\033[m'.format(Genero[0], nome))
            Play("come.mp3")
        else:
            io.read('\033[7m{} {} grita\n\033[m'.format(Genero[0], nome))
            Play("PegaLadrao.mp3")
            io.read('\033[7mdigite qualquer coisa para continuar\033[m')
            input("")
            io.read('\033[7mos guardas escutam e pegam o ladrão\n{} resebe uma recompença no valor de \nfim de jogo\033[m'.format(nome))
            Play("mil8.mp3")
    else:
        io.read('\033[7m{} {} esperou\n\033[m'.format(Genero[0], nome))
        Play("1.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} esperou!\n\033[m'.format(Genero[0], nome))
        Play("2.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} esperou!!!!\n\033[m'.format(Genero[0], nome))
        Play("3.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} esperou!!!!!!\n\033[m'.format(Genero[0], nome))
        Play("2000.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7mate que morreu de exastão\n\033[m'.format(nome))
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read("""\033[;31m                                .,od88888888888bo,.
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
        Play("caveira.mp3")
else:
    io.read('\033[7m{} {} ve a chegada de um clinte que não parece ter muito dinheiro\033[m'.format(Genero[0], nome))
    o3 = int(input('\033[4;33mOque voce faz\n 1 leva ele para uma mesa distante\n 2 coloca ele numa mesa com janela\n digite: \033[m'))
    if o3 == 1:
        io.read('\033[7m{} {} coloca ele na mesa distante e pergunta\no que voce quer para comer?\nele responde\033[m'.format(Genero[0], nome))
        Play("vinho.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} fica surpreso com o pedido mas anota mesmo assim\ndepois chega com o pedido\ndepois de comer voce fala quanto que custou\033[m'.format(Genero[0], nome))
        Play("mil8.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} fica mas surpreso ainda quando ele retira do seu boço um cartão e fala\033[m'.format(Genero[0],nome))
        io.read("""\033[0;31;44m█▀▀▄ █▀▀█   █▀▀ █▀▀█ █▀▀ █▀▀▄ ░▀░ ▀▀█▀▀ █▀▀█   █▀▀█ █▀▀█ █▀▀█   █▀▀ █▀▀█ ▀█░█▀ █▀▀█ █▀▀█\033[m
\033[0;31;44m█░░█ █░░█   █░░ █▄▄▀ █▀▀ █░░█ ▀█▀ ░░█░░ █░░█   █░░█ █░░█ █▄▄▀   █▀▀ █▄▄█ ░█▄█░ █░░█ █▄▄▀\033[m
\033[0;31;44m▀░░▀ ▀▀▀▀   ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀░ ▀▀▀ ░░▀░░ ▀▀▀▀   █▀▀▀ ▀▀▀▀ ▀░▀▀   ▀░░ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀\033[m""")
        Play("ha.mp3")
    else:
        io.read('\033[7m{} {} coloca ele na mesa com vista pela janela e pergunta\no que voce quer para comer?\nele responde\033[m'.format(Genero[0], nome))
        Play("queropova.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7m{} {} perqunta\nalgo para beber?\nele responde\033[m'.format(Genero[0], nome))
        Play("cafe.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7mdepois dele ter se alimntando {} {} fala o valor da refeição\033[m'.format(Genero[0], nome))
        Play("mil8.mp3")
        io.read('\033[7mdigite qualquer coisa para continuar\033[m')
        input("")
        io.read('\033[7me ele responde so tenho\033[m')
        Play("contos.mp3")
