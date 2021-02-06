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
