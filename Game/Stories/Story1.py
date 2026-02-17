from Game.Ultils.Library_Text import STORY1_TEXTS, COMMON

def Story(audio_player, nome, Sujeito):
    """
    Execute the storyline for Story 1.

    Args:
        audio_player (AudioPlayer): The audio player instance to play sounds.
        nome (str): The name of the player.
        Sujeito (str): The subject pronoun for the player.
    """
    print(STORY1_TEXTS["intro"].format(Sujeito, nome))
    o1 = int(input(STORY1_TEXTS["choice1"]))
    if o1 == 1:
        print(STORY1_TEXTS["choice1_1"].format(Sujeito, nome))
        audio_player.play('souseupai.mp3')
        o111 = int(input(STORY1_TEXTS["choice1_1_1"]))
        if o111 == 1:
            print(STORY1_TEXTS["choice1_1_1_1"].format(nome))
            audio_player.play('trolei.mp3')
        else:
            print(STORY1_TEXTS["choice1_1_1_2"].format(nome))
    else:
        print(STORY1_TEXTS["choice1_2"].format(Sujeito, nome))
        o12 = int(input(STORY1_TEXTS["choice1_2_1"]))
        if o12 == 1:
            print(STORY1_TEXTS["choice1_2_1_1"].format(Sujeito, nome))
            audio_player.play('aaa.mp3')
            print(STORY1_TEXTS["choice1_2_1_1_1"].format(Sujeito, nome))
            o121 = int(input(STORY1_TEXTS["choice1_2_1_1_1_1"].format(Sujeito, nome)))
            if o121 == 1:
                print(STORY1_TEXTS["choice1_2_1_1_1_1_1"].format(Sujeito, nome))
                audio_player.play('pede.mp3')
                print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1"].format(Sujeito, nome))
                o1212 = int(input(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1"].format(Sujeito, nome)))
                if o1212 == 1:
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naoseiii.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('queropova.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1_1_1_1_1"].format(nome))
                    audio_player.play('ai.mp3')
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_1_1_1_1_1_1_1"])
                else:
                    print(COMMON["game_over"])
                    audio_player.play('cagao.mp3')
            else:
                print(STORY1_TEXTS["choice1_2_1_1_1_1_2"].format(Sujeito, nome))
                audio_player.play('pede.mp3')
                print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1"].format(Sujeito, nome))
                o122 = int(input(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1"]))
                if o122 == 1:
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naosei.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('naoseiii.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1_1_1_1_1"].format(Sujeito, nome))
                    audio_player.play('queropova.mp3')
                    input(COMMON["continue"])
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_2_1_1_1_1_1_1_1"].format(nome))
                    audio_player.play('ai.mp3')
                    print(STORY1_TEXTS["choice1_2_1_1_1_1_1_1_2_1_1_1_1_1_1"])
                else:
                    print(COMMON["game_over"])
                    audio_player.play('cagao.mp3')
        else:
            print(STORY1_TEXTS["choice1_2_2"].format(Sujeito, nome))
            audio_player.play('PegaLadrao.mp3')
            input(COMMON["continue"])
            print('\033[7mna hora vem varios policias\nconclusão voce e preso por roubo\033[m')
            audio_player.play('alo-policia-federal.mp3')
            print(COMMON["game_over"])