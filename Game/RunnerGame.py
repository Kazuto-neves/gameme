from Game.Ultils.audio_player import AudioPlayer, PygameAudioLibrary

def RunnerGame(menu_function, story_modules):
    """
    Main function to run the game.
    """
    audio_library = PygameAudioLibrary()
    audio_player = AudioPlayer(audio_library)

    print('\033[0;32mBem vindo ao gameme\033[m')
    nome, sexo, Sujeito, pronome, story = menu_function()
    
    if story in story_modules:
        story_modules[story](audio_player, nome, Sujeito)
    else:
        print("Invalid story selection.")