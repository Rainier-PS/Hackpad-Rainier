print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.combos import Combos, Chord
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

#   EDIT KEYS
TL = KC.N1
TM = KC.N2
TR = KC.N3
ML = KC.N4
MM = KC.N5
MR = KC.N6
BL = KC.N7
BM = KC.N8
BR = KC.N9

#   EDIT DISPLAY
LINE1 = "Welcome back."
LINE2 = "Rainier P.S."

BRIGHTNESS      = 0.8   # 0.0 to 1.0
DIM_AFTER       = 20    # seconds before dimming
DIM_TO          = 0.1   # brightness when dimmed
OFF_AFTER       = 60    # seconds before screen off
PS_DIM_AFTER    = 10    # seconds before dimming in powersave
PS_DIM_TO       = 0.1   # brightness when dimmed in powersave
PS_OFF_AFTER    = 30    # seconds before screen off in powersave

#   DO NOT EDIT BELOW THIS LINE
keyboard = KMKKeyboard()
keyboard.debounce = 20

keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

macros = Macros()
encoder_handler = EncoderHandler()
combos = Combos()
layers = Layers()

keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(combos)
keyboard.modules.append(layers)
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        TL, ML, BL,
        TM, MM, BM,
        TR, MR, BR,
    ]
]

combos.combos = [
    Chord((TL, ML), ML),
    Chord((ML, BL), BL),
    Chord((TM, MM), MM),
    Chord((MM, BM), BM),
    Chord((TR, MR), MR),
    Chord((MR, BR), BR),
]

encoder_handler.pins = ((board.D3, board.D6, None),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

i2c_bus = busio.I2C(board.SCL, board.SDA)
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    brightness=BRIGHTNESS,
    dim_time=DIM_AFTER,
    dim_target=DIM_TO,
    off_time=OFF_AFTER,
    powersave_dim_time=PS_DIM_AFTER,
    powersave_dim_target=PS_DIM_TO,
    powersave_off_time=PS_OFF_AFTER,
    entries=[
        TextEntry(text=LINE1, x=0, y=0),
        TextEntry(text=LINE2, x=0, y=16),
    ],
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
