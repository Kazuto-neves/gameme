import os
import sys
import pygame
from playsound import playsound

class AudioPlayer:
    def __init__(self, library="pygame"):
        self.library = library
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            self.audio_dir = os.path.join(getattr(sys, '_MEIPASS', ''), "audio")
        else:
            # Running in normal Python environment
            self.audio_dir = os.path.join(os.path.dirname(__file__), "../audio")
        if self.library == "pygame":
            pygame.mixer.init()

    def play(self, filename):
        filepath = os.path.join(self.audio_dir, filename)
        if self.library == "pygame":
            self._play_with_pygame(filepath)
        elif self.library == "playsound":
            self._play_with_playsound(filepath)
        else:
            raise ValueError("Unsupported library: " + self.library)

    def _play_with_pygame(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def _play_with_playsound(self, filepath):
        playsound(filepath)
