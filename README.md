<div align="center">
    <img src="https://github.com/huterguier/s3-mini/blob/main/media/s3-mini.png" width="330">
</div>

# The Ultimate Keystroke Reward System
[![PyPI version](https://img.shields.io/badge/pypi-not_available-red.svg)](#installation)
[![License: MIT](https://img.shields.io/github/license/huterguier/s3-mini?color=yellow)](https://opensource.org/licenses/MIT)

[`s3-mini`](https://github.com/huterguier/s3-mini) is a highly sophisticated, cutting-edge background daemon masquerading as a "Samsung S3-Mini Emulator". 
Forget complex productivity apps or time-management frameworks. `s3-mini` relies on the flawless science of Pavlovian conditioning to keep you typing. It silently monitors your every keystroke in the background, keeping a meticulous tally. The moment you hit the legendary milestone of exactly 10,000 keystrokes? It violently rewards your hard work by blasting an audio file. 

## Features
- 🎧 **Pavlovian Dopamine Hits:** The system tracks your inputs and grants you an auditory reward exactly every 10,000 keystrokes. It is pure, unadulterated positive reinforcement. 

- 🥷 **Stealthy Surveillance:** Powered by `pynput`, the keylogger attaches itself to your system and quietly watches everything you type without ever getting in your way. 

- 📈 **Visceral Progress:** Why type into the void? With a state-of-the-art `tqdm` progress bar, you can literally watch a line fill up in your terminal as you march toward your next sonic reward. 

- 🪶 **Stupidly Lightweight:** Built on a hyper-optimized stack of `pygame` and basic listeners, ensuring your RAM is saved for the IDE, not the dopamine machine.

## Quick Start

### Basic Usage
To boot up your personal motivation engine, just execute the provided shell script. The script will spin up the listener and the progress bar.

```bash
$ ./boot.sh
```

If you prefer to interface with the core logic directly, you can run the python file. The moment it runs, the `keyboard.Listener` is armed and waiting for your first keystroke.

```bash
$ python s3-mini/boot.py
```

## Installation
The system requires Python 3.10+. Install it straight from the source to start earning your audio rewards today.
```bash
pip install git+https://github.com/huterguier/s3-mini
```
