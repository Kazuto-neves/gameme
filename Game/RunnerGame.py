from Game.Ultils.audio_player import AudioPlayer
from Game.Ultils.main_menu import menu

def RunnerGame(library):
    audio_player = AudioPlayer(library)

    print('\033[0;32mBem vindo ao gameme\033[m')
    nome, sexo, Sujeito, pronome, story = menu()
    match story:
        case 1:
            from Game.Stories.Story1 import Story
            Story(audio_player, nome, Sujeito)
        case 2:
            from Game.Stories.Story2 import Story
            Story(audio_player, nome, Sujeito)
        case 3:
            from Game.Stories.Story3 import Story
            Story(audio_player, nome, Sujeito)
