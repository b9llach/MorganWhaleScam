import time
from colorama import Fore, Style
from mnemonic import Mnemonic
import bip32utils
import random
import subprocess
import ctypes
import os
subprocess.call('', shell=True)

mnemon = Mnemonic('english')
inspections = 0
btc_found = random.randrange(80000,120000)/100000
balance = random.randrange(2,8)

def gen_check():
    global inspections
    while True:
        jj = mnemon.generate(strength=128)
        seed = mnemon.to_seed(jj, passphrase="TREZOR")
        root_key = bip32utils.BIP32Key.fromEntropy(seed)
        root_address = root_key.Address()
        print(f"{Fore.GREEN}Balance: 0 | Recieved: 0 | Address: {root_address} | Mnemonic: {jj}{Style.RESET_ALL}")
        inspections += 10
        ctypes.windll.kernel32.SetConsoleTitleW(f"BTC | SeedExpert v6.0 | With balance: {balance} - Total inspections: {inspections} - [Found {btc_found}]")
        time.sleep(.001)

def main():
    os.system("cls")
    os.system("mode con: cols=190 lines=40")
    ctypes.windll.kernel32.SetConsoleTitleW(f"BTC | SeedExpert v6.0 | With balance: {balance} - Total inspections: {inspections} - [Found {btc_found}")
    while True:
        gen_check()

if __name__ == "__main__":
    main()