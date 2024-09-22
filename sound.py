import pygame
import time

def play_sound(file_path):
    # Initialize the mixer module in pygame
    pygame.mixer.init()

    # Load the sound file
    pygame.mixer.music.load(file_path)

    # Play the sound
    pygame.mixer.music.play()

    # Wait for 4 seconds
    time.sleep(4)

    # Stop the sound after 4 seconds
    pygame.mixer.music.stop()
