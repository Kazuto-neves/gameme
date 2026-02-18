import os
import sys
import pygame

def _play_with_pygame(filepath):
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

class AudioPlayer:
    def __init__(self, library="pygame"):
        self.library = library
        if getattr(sys, 'frozen', False):
            self.audio_dir = os.path.join(getattr(sys, '_MEIPASS', ''), "audio")
        else:
            self.audio_dir = os.path.join(os.path.dirname(__file__), "../audio")
        if self.library == "pygame":
            pygame.mixer.init()

    def play(self, filename):
        filepath = os.path.join(self.audio_dir, filename)
        if self.library == "pygame":
            _play_with_pygame(filepath)
        else:
            raise ValueError("Unsupported library: " + self.library)
