from Game.Ultils.Library_Text import STORY2_TEXTS, COMMON

def Story(audio_player, nome, Sujeito):
    print(STORY2_TEXTS["intro"].format(Sujeito, nome))
    o2 = int(input(STORY2_TEXTS["choice2"]))
    if o2 == 1:
        print(STORY2_TEXTS["choice2_1"].format(Sujeito, nome, Sujeito, nome, nome))
        o21 = int(input(STORY2_TEXTS["choice2_1_1"]))
        if o21 == 1:
            print(STORY2_TEXTS["choice2_1_1_1"].format(Sujeito, nome))
            audio_player.play('pega.mp3')
            print(COMMON["game_over"])
        elif o21 == 2:
            print(STORY2_TEXTS["choice2_1_1_2"].format(Sujeito, nome))
            audio_player.play('come.mp3')
            print(COMMON["game_over"])
        else:
            print(STORY2_TEXTS["choice2_1_1_3"].format(Sujeito, nome))
            audio_player.play('PegaLadrao.mp3')
            input(COMMON["continue"])
            print(STORY2_TEXTS["choice2_1_1_3_1"].format(Sujeito, nome))
            audio_player.play('mil8.mp3')
            input(COMMON["game_over"])
    else:
        print(STORY2_TEXTS["choice2_2"].format(Sujeito, nome))
        audio_player.play('1.mp3')
        input(COMMON["continue"])
        print(STORY2_TEXTS["choice2_2_1"].format(Sujeito, nome))
        audio_player.play('2.mp3')
        input(COMMON["continue"])
        print(STORY2_TEXTS["choice2_2_2"].format(Sujeito, nome))
        audio_player.play('3.mp3')
        input(COMMON["continue"])
        print(STORY2_TEXTS["choice2_2_3"].format(Sujeito, nome))
        audio_player.play('2000.mp3')
        input(COMMON["continue"])
        print(STORY2_TEXTS["choice2_2_4"].format(Sujeito, nome))
        input(COMMON["continue"])
        print(STORY2_TEXTS["choice2_2_5"].format(Sujeito, nome))
        audio_player.play('caveira.mp3')
        input(COMMON["game_over"])