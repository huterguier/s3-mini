from pynput import keyboard
import pygame
import threading
import tqdm

pygame.mixer.init()
sound = pygame.mixer.Sound("media/moemax.mp3")

n = 10000
counter = 0
pbar = None

def play_sound():
    global counter, pbar
    if counter % n == 0:
        sound.play()
        if pbar is not None:
            pbar.reset()
    if pbar is not None:
        pbar.update(1)
    counter += 1


def on_press(key):
    threading.Thread(target=play_sound).start()

def main():
    global pbar
    pbar = tqdm.tqdm(total=n)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
