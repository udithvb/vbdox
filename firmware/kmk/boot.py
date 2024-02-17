import board

from kmk.bootcfg import bootcfg

# bootcfg(
#     # required:
#     sense: [microcontroller.Pin, digitalio.DigitalInOut],
#     # optional:
#     source: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
#     boot_device: int = 0,
#     cdc: bool = True,
#     consumer_control: bool = True,
#     keyboard: bool = True,
#     midi: bool = False,
#     mouse: bool = True,
#     nkro: bool = False,
#     pan: bool = True,
#     storage: bool = True,
#     usb_id: Optional[tuple[str, str]] = None,
#     **kwargs,
# ) -> bool




from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP29,
    source=board.GP0,
    midi=False,
    mouse=True,
    pan=True,
    storage=False,
    usb_id=('VBinc.', 'sakydox'),
)