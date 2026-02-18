from Game.Ultils.Library_Text import STORY3_TEXTS, COMMON

def Story(audio_player, nome, Sujeito):
    """
    Execute the storyline for Story 3.

    Args:
        audio_player (AudioPlayer): The audio player instance to play sounds.
        nome (str): The name of the player.
        Sujeito (str): The subject pronoun for the player.
    """
    print(STORY3_TEXTS["intro"].format(Sujeito, nome))
    o3 = int(input(STORY3_TEXTS["choice3"]))
    if o3 == 1:
        print(STORY3_TEXTS["choice3_1"].format(Sujeito, nome))
        audio_player.play('vinho.mp3')
        input(COMMON["continue"])
        print(STORY3_TEXTS["choice3_1_1"].format(Sujeito, nome))
        audio_player.play('mil8.mp3')
        input(COMMON["continue"])
        print(STORY3_TEXTS["choice3_1_2"].format(Sujeito, nome))
        print(STORY3_TEXTS["choice3_1_3"])
        audio_player.play('ha.mp3')
        print(COMMON["game_over"])
    else:
        print(STORY3_TEXTS["choice3_2"].format(Sujeito, nome))
        audio_player.play('queropova.mp3')
        input(COMMON["continue"])
        print(STORY3_TEXTS["choice3_2_1"].format(Sujeito, nome))
        audio_player.play('cafe.mp3')
        input(COMMON["continue"])
        print(STORY3_TEXTS["choice3_2_2"].format(Sujeito, nome))
        audio_player.play('mil8.mp3')
        input(COMMON["continue"])
        print(STORY3_TEXTS["choice3_2_3"].format(Sujeito, nome))
        audio_player.play('contos.mp3')
        input(COMMON["game_over"])