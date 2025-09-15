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
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()
keyboard.debounce = 50  # milliseconds

# Define pins
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

# Define safe macros per row (prevents ghosting/double-type)
SAFE_D0 = KC.MACRO(KC.D)   # row 0 version of D
SAFE_E0 = KC.MACRO(KC.E)   # row 0 version of E
SAFE_F0 = KC.MACRO(KC.F)   # row 0 version of F

SAFE_D1 = KC.MACRO(KC.J)   # row 1 version, DIFFERENT output
SAFE_E1 = KC.MACRO(KC.K)   # row 1 version, DIFFERENT output
SAFE_F1 = KC.MACRO(KC.L)   # row 1 version, DIFFERENT output

# Keymap (3x3) with 2 layers
keyboard.keymap = [
    [  # Layer 0 (default)
        KC.A   , SAFE_D1 , KC.G ,   # Col 0
        KC.B   , SAFE_E1 , KC.H ,   # Col 1
        KC.C   , SAFE_F1 , KC.I     # Col 2
    ],
    [  # Layer 1 (encoder = brightness)
        KC.TRNS, KC.TRNS, KC.TRNS,  # Col 0
        KC.TRNS, KC.TRNS, KC.TRNS,  # Col 1
        KC.TRNS, KC.TRNS, KC.TRNS   # Col 2
    ]
]

# Encoder setup (EC11, pins D3 = A, D6 = B, no button)
encoder_handler.pins = (
    (board.D3, board.D6, None),  # encoder #1
)

# Encoder mapping (2 layers defined)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),  # Layer 0: Volume + Mute
    ((KC.BRID, KC.BRIU, KC.TRNS),),  # Layer 1: Brightness
]

combos.combos = [
    Chord((6, 7, 8), KC.MUTE, match_coord=True),  # encoder button combo
]


i2c_bus = busio.I2C(board.SCL, board.SDA)

display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,  # default I2C addr
)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    dim_time=45,      # dim after 45s
    dim_target=0.2,   # faint glow, not totally dark
    off_time=90,      # fully off after 1.5 min
    brightness=0.6,   # easier on OLED lifespan
    entries=[
        TextEntry(text="Hey there!  ^_^", x=20, y=0),
	TextEntry(text="I'm finally working!", x=0, y=16),
    ],
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
