# SignalIO Simplify Utility
Simple utility for SignalIO Development Board 
Functions:
- OTA firmware and SPIFFS image update
- Upload firmware via USB-UART
- Serial port monitor
- Erase flash

firmware folder stores firmware.bin (can be redefined in config file) image, data folder stores spiffs.bin (can be redefined in config file) image and config folder stores config.json file


This software require python 2.8^, esptool.py and some external libraries (requirements.txt)

Also this utility using external software:
- espota.py  
    Original espota.py by Ivan Grokhotkov: (https://gist.github.com/igrr/d35ab8446922179dc58c)

    Modified since 2015-09-18 from Pascal Gollor (https://github.com/pgollor)
    Modified since 2015-11-09 from Hristo Gochkov (https://github.com/me-no-dev)
    Modified since 2016-01-03 from Matthew O'Gorman (https://githumb.com/mogorman)
- esptool developed by Espressif Systems
- figlet utility (to disable it comment line 79 in __init__.py file)
 
