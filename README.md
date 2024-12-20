DIY ergonomic keyboard clone "inspired" by Ergodox.

Source code for:
  1. PCB design in Kicad
  2. Keyboard layout using KLE.
  3. 3D model using Onshape
  4. Config files for KMK for firmware.


3D model files here https://cad.onshape.com/documents/ee7b6b641733c3f6c864279a/w/8fba0d1b41314f945c99cf82/e/c87f91dc97543009856402ba?renderMode=0&uiState=66990a0e6861fb6562c59a71


![WhatsApp Image 2024-07-17 at 08 57 51](https://github.com/user-attachments/assets/803091bb-ce21-4e3a-ab89-84873e01aeb0)

![Clipped_image_20231214_193427](https://github.com/user-attachments/assets/d0fabec1-bde8-4d10-a681-528e06c8720d)


wiki:
	for flasing to rom hold bootsel before plugging -> mv to rpi folder
	for src code hold reset before plugging in + reset within 500ms -> mv to circuitpy folder

Use thonny, configure interpreter to circuipy generic device, uncomment debug to read serial console.

Rename boards for split to work:
	https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy



links for binaries:
	https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#resetting-flash-memory
	https://circuitpython.org/board/waveshare_rp2040_zero/
	https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md

Edit config:
	Hold the reset key before plugging in, keep holding for 4 seconds after (topmost key on keeb) to get into the filesystem and edit config.

# Credits

-   Keyboard parts compiled by [joe-scotto ](https://github.com/joe-scotto/scottokeebs/tree/main/Extras/ScottoKicad).
-   Reversible hotswap sockets by [LouWii ](https://github.com/LouWii/ErgoMax/tree/master/libs).
