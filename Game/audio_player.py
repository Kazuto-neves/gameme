import os
import sys
import pygame
from playsound import playsound

class AudioPlayer:
    def __init__(self, library="pygame"):
        self.library = library
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            self.audio_dir = os.path.join(sys._MEIPASS, "audio")
        else:
            # Running in normal Python environment
            self.audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        if self.library == "pygame":
            pygame.mixer.init()

    def play(self, filename):
        filepath = os.path.join(self.audio_dir, filename)
        if self.library == "pygame":
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()
        elif self.library == "playsound":
            playsound(filepath)
        else:
            raise ValueError("Unsupported library: " + self.library)
