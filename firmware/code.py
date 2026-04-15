print("Starting")

import board
import busio

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Chord
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

# LAYER 0: SHORTCUTS (Default Layer)
L0_TL, L0_TM, L0_TR = KC.ESC, KC.LWIN(KC.V), KC.LWIN(KC.L)
L0_ML, L0_MM, L0_MR = KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.S)
L0_BL, L0_BM, L0_BR = KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X)

# LAYER 1: SYSTEM & BROWSER UTILITIES
L1_TL, L1_TM, L1_TR = KC.LWIN(KC.I), KC.LWIN(KC.R), KC.LWIN(KC.S)
L1_ML, L1_MM, L1_MR = KC.LCTL(KC.LSHIFT(KC.ESC)), KC.LWIN(KC.N), KC.LWIN(KC.L)
L1_BL, L1_BM, L1_BR = KC.LCTL(KC.H), KC.LCTL(KC.J), KC.LCTL(KC.LSHIFT(KC.R))

# LAYER 2: NAVIGATION (WASD + ARROWS)
L2_TL, L2_TM, L2_TR = KC.UP, KC.W, KC.DOWN
L2_ML, L2_MM, L2_MR = KC.A, KC.S, KC.D
L2_BL, L2_BM, L2_BR = KC.LEFT, KC.TAB, KC.RIGHT

# LAYER 3: CODING
L3_TL, L3_TM, L3_TR = KC.LCTL(KC.SLASH), KC.TAB, KC.LALT(KC.LSHIFT(KC.F))
L3_ML, L3_MM, L3_MR = KC.LCTL(KC.F), KC.LCTL(KC.H), KC.LCTL(KC.A)
L3_BL, L3_BM, L3_BR = KC.LCTL(KC.GRAVE), KC.LSHIFT(KC.TAB), KC.DQUO

# LAYER 4: MEETINGS
L4_TL, L4_TM, L4_TR = KC.LCTL(KC.LSHIFT(KC.O)), KC.LCTL(KC.LSHIFT(KC.M)), KC.LCTL(KC.LSHIFT(KC.H))
L4_ML, L4_MM, L4_MR = KC.SPC, KC.LWIN(KC.LALT(KC.R)), KC.LWIN(KC.LSHIFT(KC.S))
L4_BL, L4_BM, L4_BR = KC.LWIN(KC.DOT), KC.LCTL(KC.LSHIFT(KC.K)), KC.LCTL(KC.LSHIFT(KC.E))

# LAYER 5: NUMPAD
L5_TL, L5_TM, L5_TR = KC.N1, KC.N2, KC.N3
L5_ML, L5_MM, L5_MR = KC.N4, KC.N5, KC.N6
L5_BL, L5_BM, L5_BR = KC.N7, KC.N8, KC.N9

# LAYER 6: FUNCTION KEYS
L6_TL, L6_TM, L6_TR = KC.F1, KC.F2, KC.F3
L6_ML, L6_MM, L6_MR = KC.F4, KC.F5, KC.F6
L6_BL, L6_BM, L6_BR = KC.F7, KC.F8, KC.F9

#  EDIT DISPLAY
LINE1 = "Rainier's Hackpad"
BRIGHTNESS      = 0.8   # 0.0 to 1.0
DIM_AFTER       = 20    # seconds before dimming
DIM_TO          = 0.1   # brightness when dimmed
OFF_AFTER       = 60    # seconds before screen off
PS_DIM_AFTER    = 10    # seconds before dimming in powersave
PS_DIM_TO       = 0.1   # brightness when dimmed in powersave
PS_OFF_AFTER    = 30    # seconds before screen off in powersave

#  DO NOT EDIT BELOW THIS LINE
keyboard = KMKKeyboard()
keyboard.debounce = 20

keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

macros = Macros()
encoder_handler = EncoderHandler()
combos = Combos()
layers = Layers()
mousekeys = MouseKeys(max_speed=20, acc_interval=10, move_step=5)

keyboard.modules.append(layers)
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(combos)
keyboard.modules.append(mousekeys)
keyboard.extensions.append(MediaKeys())

# KEYMAP LAYOUT
# Physical layout (3x3 grid):
# Row 0: Col 0, Col 1, Col 2  →  TL, TM, TR
# Row 1: Col 0, Col 1, Col 2  →  ML, MM, MR
# Row 2: Col 0, Col 1, Col 2  →  BL, BM, BR
# Layer switching via TOP ROW combos
keyboard.keymap = [
    [
        L0_TL,    L0_ML,    L0_BL,
        L0_TM,    L0_MM,    L0_BM,
        L0_TR,    L0_MR,    L0_BR,
    ],
    [
        L1_TL,    L1_ML,    L1_BL,
        L1_TM,    L1_MM,    L1_BM,
        L1_TR,    L1_MR,    L1_BR,
    ],
    [
        L2_TL,    L2_ML,    L2_BL,
        L2_TM,    L2_MM,    L2_BM,
        L2_TR,    L2_MR,    L2_BR,
    ],
    [
        L3_TL,    L3_ML,    L3_BL,
        L3_TM,    L3_MM,    L3_BM,
        L3_TR,    L3_MR,    L3_BR,
    ],
    [
        L4_TL,    L4_ML,    L4_BL,
        L4_TM,    L4_MM,    L4_BM,
        L4_TR,    L4_MR,    L4_BR,
    ],
    [
        L5_TL,    L5_ML,    L5_BL,
        L5_TM,    L5_MM,    L5_BM,
        L5_TR,    L5_MR,    L5_BR,
    ],
    [
        L6_TL,    L6_ML,    L6_BL,
        L6_TM,    L6_MM,    L6_BM,
        L6_TR,    L6_MR,    L6_BR,
    ],
]

# COMBOS
combos.combos = [
    # LAYER SWITCHING COMBOS
    Chord((L0_TL, L0_TM, L0_TR), KC.TO(1)),
    Chord((L1_TL, L1_TM, L1_TR), KC.TO(2)),
    Chord((L2_TL, L2_TM, L2_TR), KC.TO(3)),
    Chord((L3_TL, L3_TM, L3_TR), KC.TO(4)),
    Chord((L4_TL, L4_TM, L4_TR), KC.TO(5)),
    Chord((L5_TL, L5_TM, L5_TR), KC.TO(6)),
    Chord((L6_TL, L6_TM, L6_TR), KC.TO(0)),

    # HARDWARE CORRECTION COMBOS
    # Layer 0 corrections
    Chord((L0_TL, L0_ML), L0_ML),
    Chord((L0_ML, L0_BL), L0_BL),
    Chord((L0_TM, L0_MM), L0_MM),
    Chord((L0_MM, L0_BM), L0_BM),
    Chord((L0_TR, L0_MR), L0_MR),
    Chord((L0_MR, L0_BR), L0_BR),

    # Layer 1 corrections
    Chord((L1_TL, L1_ML), L1_ML),
    Chord((L1_ML, L1_BL), L1_BL),
    Chord((L1_TM, L1_MM), L1_MM),
    Chord((L1_MM, L1_BM), L1_BM),
    Chord((L1_TR, L1_MR), L1_MR),
    Chord((L1_MR, L1_BR), L1_BR),

    # Layer 2 corrections
    Chord((L2_TL, L2_ML), L2_ML),
    Chord((L2_ML, L2_BL), L2_BL),
    Chord((L2_TM, L2_MM), L2_MM),
    Chord((L2_MM, L2_BM), L2_BM),
    Chord((L2_TR, L2_MR), L2_MR),
    Chord((L2_MR, L2_BR), L2_BR),
    
    # Layer 3 corrections
    Chord((L3_TL, L3_ML), L3_ML),
    Chord((L3_ML, L3_BL), L3_BL),
    Chord((L3_TM, L3_MM), L3_MM),
    Chord((L3_MM, L3_BM), L3_BM),
    Chord((L3_TR, L3_MR), L3_MR),
    Chord((L3_MR, L3_BR), L3_BR),
    
    # Layer 4 corrections
    Chord((L4_TL, L4_ML), L4_ML),
    Chord((L4_ML, L4_BL), L4_BL),
    Chord((L4_TM, L4_MM), L4_MM),
    Chord((L4_MM, L4_BM), L4_BM),
    Chord((L4_TR, L4_MR), L4_MR),
    Chord((L4_MR, L4_BR), L4_BR),

    # Layer 5 corrections
    Chord((L5_TL, L5_ML), L5_ML),
    Chord((L5_ML, L5_BL), L5_BL),
    Chord((L5_TM, L5_MM), L5_MM),
    Chord((L5_MM, L5_BM), L5_BM),
    Chord((L5_TR, L5_MR), L5_MR),
    Chord((L5_MR, L5_BR), L5_BR),

    # Layer 6 corrections
    Chord((L6_TL, L6_ML), L6_ML),
    Chord((L6_ML, L6_BL), L6_BL),
    Chord((L6_TM, L6_MM), L6_MM),
    Chord((L6_MM, L6_BM), L6_BM),
    Chord((L6_TR, L6_MR), L6_MR),
    Chord((L6_MR, L6_BR), L6_BR),
]

# ENCODER CONFIGURATION
# Pins: D3 (CLK), D6 (DT), None (no switch)
encoder_handler.pins = ((board.D3, board.D6, None),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),                             # Layer 0 - Volume
    ((KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.LWIN(KC.D)),),   # Layer 1 - Brightness
    ((KC.MW_DN, KC.MW_UP, KC.MB_MMB),),                         # Layer 2 - Scroll
    ((KC.VOLD, KC.VOLU, KC.MUTE),),                             # Layer 3 - Volume
    ((KC.VOLD, KC.VOLU, KC.MUTE),),                             # Layer 4 - Volume
    ((KC.MW_DN, KC.MW_UP, KC.MB_MMB),),                         # Layer 5 - Scroll
    ((KC.VOLD, KC.VOLU, KC.MUTE),),                             # Layer 6 - Volume
]

# DISPLAY CONFIGURATION
# SSD1306 OLED (128x32)
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
        # Header
        TextEntry(text=LINE1, x=0, y=0),
                
        TextEntry(text='Layer 0 Shortcut',   x=0, y=16, layer=0),
        TextEntry(text='Layer 1 System',   x=0, y=16, layer=1),
        TextEntry(text='Layer 2 Navigate', x=0, y=16, layer=2),
        TextEntry(text='Layer 3 Coding', x=0, y=16, layer=3),
        TextEntry(text='Layer 4 Meeting', x=0, y=16, layer=4),
        TextEntry(text='Layer 5 Numpad',    x=0, y=16, layer=5),
        TextEntry(text='Layer 6 Function',    x=0, y=16, layer=6),
    ],
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
