#!/usr/bin/env python3
from arch_wrappers import PacmanWrapper, SystemctlWrapper

class BluetoothSetup:
    def __init__(self):
        self.pacman = PacmanWrapper()
        self.systemctl = SystemctlWrapper()
    def setup(self):
        packages = ['bluez', 'bluez-tools', 'pipewire-pulse', 'pulseaudio-bluetooth']
        self.pacman.install_batch(packages)
        
        self.systemctl.enable('bluetooth.service')
        self.systemctl.start('pulseaudio-bluetooth.service')


def main():
    bluetooth_setup = BluetoothSetup()
    bluetooth_setup.setup()


if __name__ == '__main__':
    main()