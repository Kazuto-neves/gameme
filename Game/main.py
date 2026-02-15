from Game.RunnerGame import RunnerGame

print('\033[0;32mQual motor de Audio que?\033[m')
print('\033[0;32m1. Pygame\033[m')
print('\033[0;32m2. Custom\033[m')
audio = input('\033[0;32mDigite o numero do motor de audio: \033[m')
RunnerGame("pygame" if audio == '1' else "playsound")