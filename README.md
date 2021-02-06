# [Raspberry Pi Pico + Python](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf)
Getting set up with the new microcontroller from the Raspberry Pi foundation

## Preparing the board
Equipment: 15" Macbook Pro 2017, 10.14.6
1. Install [Homebrew](https://brew.sh/)
    - ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
2. Install minicom
    - ```brew install minicom```
3. Plug the Pico into the computer
    - First hold down the BOOTSEL button on the Pico, then connect to computer via USB cable
    - Mine didn't work when connected via USB hub, needed to be wired directly to the USB-C port
    - Pico should show up as a drive on the desktop
4. Download [Micropython](https://micropython.org/download/rp2-pico/) and copy it to the Pico
    - When I did this the Pico automatically ejected (improperly?)

## REPL
When MicroPython boots for the first time, it will sit and wait for you to connect and tell it what to do. You can load a .pyfile from your computer onto the board, but a more immediate way to interact with it is through what is called the read-evaluate-print loop, or REPL (often pronounced similarly to "ripple").
1. Read: MicroPython waits for you to type in some text, followed by the enter key.
2. Evaluate: Whatever you typed is interpreted as Python code, and runs immediately.
3. Print: Any results of the last line you typed are printed out for you to read.
4. Loop: Go back to the start—prompt you for another line of code.

## Hello World
1. Connect to Pico via Terminal/minicom
    - ```minicom -b 115200 -o -D /dev/tty.usbmodem0000000000001```
2. From here you can run python commands like ```print("Hello World")```
3. Cntrl-D to reboot
4. Not sure how to exit without unplugging. Meta key not working for me!

## IDE
1. Download [Thonny](https://thonny.org/)
    - I did not have to install a "wheel" per Pico instructions as Thonny is v3.3.3
2. Run > Select Interpreter > Raspberry Pi Pico
3. Should autoconnect
    - Don't forget to quit minicom as this will block connection
4. Write some code and "save as"
    - pick "save to Pico"
    - this file represents the main loop, so don't use ```if __name__ == "__main__":```
    - instead, save file to Pico as "main.py"
    - if the code doesn't run, Cntrl-D to soft reset the board
    - you may also need to click the stop button in order to pause Python execution to reupload to board
3. Now you can execute blocks of code directly to the Pico
