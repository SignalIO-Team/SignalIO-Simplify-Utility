import serial
import os
import sys
import helper
from termcolor import colored
from prettytable import PrettyTable
import logging

log = logging.getLogger()
help = helper.help()
config = help.load_config()

Board = "SignalIO board v1.0"
SOC = "ESP32 WROOM 4mb Flash"


def on_load():
    command = PrettyTable(['Board', 'SOC'])
    command.add_row([Board, SOC])
    print("----------------BOARD--------------------------")
    print(command)


def Serial_init():
    try:
        port = serial.Serial(
                port=config["port"],
                baudrate=config["port_speed"],
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
        )
        print(colored("COM PORT INITED!", "green"))
        print("Port: " + config["port"] + "\n" + "Speed: " + config["port_speed"])

        return port
    except Exception as e:
        print(colored("COM PORT ERROR", 'red'))
        print(colored(e,'red'))
        


def flash_firmware():
    os.system("esptool.py --port " + config["port"] + " write_flash --flash_mode qio --flash_size " + config["flash"] + " " + config["start_addr"] + " " + config["firmware path"])
    pass


def serial_monitor(port):
    try:
        print(colored("Serial debuger started!\nPress Ctrl^C to return to menu","green"))
        while (True):
            val = port.readline()
            if(val > 0):
                print(val).strip("\r\n")
    except KeyboardInterrupt:
        pass


def erase_flash():
    os.system("esptool.py --chip esp32 erase_flash")
    pass


def ota():
    password = raw_input("Enter OTA password (if password not set press enter): ")
    print(colored("Updating Firmware", "green"))
    os.system("python3 OTA/espota.py -i " + config["ota_ip"] + " [-a " + password + "] -f "+ config["firmware_path"])


def ota_spiffs():
    print(colored("Updating SPIFFS", "green"))
    os.system("python3 OTA/espota.py -i " + config["ota_ip"] + " -p 8266 -f " + config["spiffs_path"] + " -s -r")


def init():
    try:
        port = Serial_init()
        os.system("clear")
        os.system("figlet SIGNALIO ESPTOOL SIMPLIFIER")
        on_load()
        print(colored("System inited", "green"))
        log.info("TEST")
        print("1. OTA update\n2. OTA update SPIFFS\n3. Serial debuger\n4. Erase flash (!!!WARNING!!! This will erase both flash and SPIFFS image)\n5. Flash firmware\n6. Exit")
        while(1):
            key = input("Choose option: ")
            if(key == 1):
                ota()
            if(key == 2):
                ota_spiffs()
            if(key == 3):
                serial_monitor(port)
            if(key == 4):
                erase_flash()
            if(key == 5):
                flash_firmware()
            if(key == 6):
                os.system("clear")
                port.close()
                sys.exit("Exit")

    except Exception as e:
        sys.exit(e)


if __name__ == "__main__":
    init()
