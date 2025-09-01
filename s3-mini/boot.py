from pynput import keyboard
import pygame
import threading

pygame.mixer.init()
sound = pygame.mixer.Sound("media/samsung.mp3")

def play_sound():
    sound.play()

def on_press(key):
    threading.Thread(target=play_sound).start()

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
