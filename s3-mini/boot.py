import argparse
from pathlib import Path

from pynput import keyboard
import pygame
import threading
import tqdm

MEDIA_DIR = Path(__file__).resolve().parent.parent / "media"
SOUNDS = {
    "samsung": MEDIA_DIR / "samsung.mp3",
    "metal_pipe": MEDIA_DIR / "metal_pipe_falling.mp3",
}

pygame.mixer.init()

n = 1000
counter = 0
pbar = None
sound = None

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
    global pbar, sound
    parser = argparse.ArgumentParser()
    parser.add_argument("--sound", choices=SOUNDS.keys(), default="samsung")
    args = parser.parse_args()

    sound = pygame.mixer.Sound(str(SOUNDS[args.sound]))
    pbar = tqdm.tqdm(total=n)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
