# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:20:46 2024

@author: Arman
"""
#pip install pygame

import pygame  
import time

def play_audio_with_pauses(file_path, play_duration=3, pause_duration=12):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(file_path)

    # Play the audio file
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(play_duration)
        pygame.mixer.music.pause()
        time.sleep(pause_duration)
        pygame.mixer.music.unpause()

    # Quit the mixer
    pygame.mixer.quit()

# Usage example
audio_file = "C:/Users/Arman/Downloads/Telegram Desktop/Why sitting is bad for health.mp3"  # Replace with your audio file path
play_audio_with_pauses(audio_file)
