import os
import sys
import pygame
from abc import ABC, abstractmethod

class AudioLibrary(ABC):
    @abstractmethod
    def play(self, filepath):
        pass

class PygameAudioLibrary(AudioLibrary):
    def __init__(self):
        pygame.mixer.init()

    def play(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

class AudioPlayer:
    def __init__(self, library: AudioLibrary):
        self.library = library
        if getattr(sys, 'frozen', False):
            self.audio_dir = os.path.join(getattr(sys, '_MEIPASS', ''), "audio")
        else:
            self.audio_dir = os.path.join(os.path.dirname(__file__), "../audio")

    def play(self, filename):
        filepath = os.path.join(self.audio_dir, filename)
        self.library.play(filepath)