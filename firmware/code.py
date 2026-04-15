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
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.mouse_jiggler import MouseJiggler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# ========================================
# LAYER 0: NUMPAD (Default Layer)
# ========================================
# Top:    1        2        3
# Middle: 4        5        6
# Bottom: 7        8        9
# ========================================
L0_TL, L0_TM, L0_TR = KC.N1, KC.N2, KC.N3
L0_ML, L0_MM, L0_MR = KC.N4, KC.N5, KC.N6
L0_BL, L0_BM, L0_BR = KC.N7, KC.N8, KC.N9

# ========================================
# LAYER 1: SHORTCUTS & MEDIA
# ========================================
# Top:    Prev     Play     Next
# Middle: Undo     Redo     Save
# Bottom: Copy     Paste    Cut
# ========================================
L1_TL, L1_TM, L1_TR = KC.MPRV, KC.MPLY, KC.MNXT
L1_ML, L1_MM, L1_MR = KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.S)
L1_BL, L1_BM, L1_BR = KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X)

# ========================================
# LAYER 2: FUNCTION KEYS
# ========================================
# Top:    F1       F2       F3
# Middle: F4       F5       F6
# Bottom: F7       F8       F9
# ========================================
L2_TL, L2_TM, L2_TR = KC.F1, KC.F2, KC.F3
L2_ML, L2_MM, L2_MR = KC.F4, KC.F5, KC.F6
L2_BL, L2_BM, L2_BR = KC.F7, KC.F8, KC.F9

# ========================================
# LAYER 3: NAVIGATION (WASD + ARROWS)
# ========================================
# Top:    Up       W/Up     Down
# Middle: A/Left   S/Down   D/Right
# Bottom: Left     Tab      Right
# ========================================
L3_TL, L3_TM, L3_TR = KC.UP, KC.W, KC.DOWN
L3_ML, L3_MM, L3_MR = KC.A, KC.S, KC.D
L3_BL, L3_BM, L3_BR = KC.LEFT, KC.TAB, KC.RIGHT

# ========================================
# LAYER 4: MOUSE UTILITIES
# ========================================
# Top:    M.Up     LClick   RClick
# Middle: M.Left   MClick   M.Right
# Bottom: M.Down   Jiggler  Scroll
# ========================================
L4_TL, L4_TM, L4_TR = KC.MS_UP, KC.MB_LMB, KC.MB_RMB
L4_ML, L4_MM, L4_MR = KC.MS_LT, KC.MB_MMB, KC.MS_RT
L4_BL, L4_BM, L4_BR = KC.MS_DN, KC.MJ_TOGGLE, KC.MW_UP

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
mousekeys = MouseKeys(max_speed=10, acc_interval=20, move_step=2)
jiggler = MouseJiggler(period_ms=5000, move_step=1)

keyboard.modules.append(layers)
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(combos)
keyboard.modules.append(mousekeys)
keyboard.modules.append(jiggler)
keyboard.extensions.append(MediaKeys())

# ========================================
# KEYMAP LAYOUT
# Physical layout (3x3 grid):
# Row 0: Col 0, Col 1, Col 2  →  TL, TM, TR
# Row 1: Col 0, Col 1, Col 2  →  ML, MM, MR
# Row 2: Col 0, Col 1, Col 2  →  BL, BM, BR
# 
# Layer switching via TOP ROW combos
# ========================================
keyboard.keymap = [
    [   # LAYER 0 - NUMPAD
        # Top:    1          2          3
        # Middle: 4          5          6
        # Bottom: 7          8          9
        L0_TL,    L0_ML,    L0_BL,
        L0_TM,    L0_MM,    L0_BM,
        L0_TR,    L0_MR,    L0_BR,
    ],
    [   # LAYER 1 - SHORTCUTS & MEDIA
        # Top:    Prev       Play       Next
        # Middle: Undo       Redo       Save
        # Bottom: Copy       Paste      Cut
        L1_TL,    L1_ML,    L1_BL,
        L1_TM,    L1_MM,    L1_BM,
        L1_TR,    L1_MR,    L1_BR,
    ],
    [   # LAYER 2 - FUNCTION KEYS
        # Top:    F1         F2         F3
        # Middle: F4         F5         F6
        # Bottom: F7         F8         F9
        L2_TL,    L2_ML,    L2_BL,
        L2_TM,    L2_MM,    L2_BM,
        L2_TR,    L2_MR,    L2_BR,
    ],
    [   # LAYER 3 - NAVIGATION (WASD + ARROWS)
        # Top:    Up         W/Up       Down
        # Middle: A/Left     S/Down     D/Right
        # Bottom: Left       Tab        Right
        L3_TL,    L3_ML,    L3_BL,
        L3_TM,    L3_MM,    L3_BM,
        L3_TR,    L3_MR,    L3_BR,
    ],
    [   # LAYER 4 - MOUSE UTILITIES
        # Top:    M.Up       LClick     RClick
        # Middle: M.Left     MClick     M.Right
        # Bottom: M.Down     Jiggler    Scroll
        L4_TL,    L4_ML,    L4_BL,
        L4_TM,    L4_MM,    L4_BM,
        L4_TR,    L4_MR,    L4_BR,
    ],
]

# ========================================
# COMBOS
# Hardware correction combos (for PCB issues)
# + Layer switching combos (THREE-KEY combos)
# ========================================
combos.combos = [
    # ===== LAYER SWITCHING COMBOS (LISTED FIRST FOR PRIORITY) =====
    # Three-key combos using TOP ROW - cycles through all 5 layers
    
    # From Layer 0 (Numpad) → Layer 1 (Shortcuts)
    # Press ALL THREE TOP KEYS: 1 + 2 + 3
    Chord((L0_TL, L0_TM, L0_TR), KC.TO(1)),
    
    # From Layer 1 (Shortcuts) → Layer 2 (Functions)  
    # Press ALL THREE TOP KEYS: Prev + Play + Next
    Chord((L1_TL, L1_TM, L1_TR), KC.TO(2)),
    
    # From Layer 2 (Functions) → Layer 3 (Navigation)
    # Press ALL THREE TOP KEYS: F1 + F2 + F3
    Chord((L2_TL, L2_TM, L2_TR), KC.TO(3)),
    
    # From Layer 3 (Navigation) → Layer 4 (Mouse)
    # Press ALL THREE TOP KEYS: W + Up + PgUp
    Chord((L3_TL, L3_TM, L3_TR), KC.TO(4)),
    
    # From Layer 4 (Mouse) → Layer 0 (Numpad)
    # Press ALL THREE TOP KEYS: M.Up + LClick + RClick
    Chord((L4_TL, L4_TM, L4_TR), KC.TO(0)),

    # ===== HARDWARE CORRECTION COMBOS =====
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
]

# ========================================
# ENCODER CONFIGURATION
# Pins: D3 (CLK), D6 (DT), None (no switch)
# Layer 0-3: Volume Down / Volume Up / Mute
# Layer 4 (Mouse): Scroll Up / Scroll Down / Middle Click
# ========================================
encoder_handler.pins = ((board.D3, board.D6, None),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),      # Layer 0 - Volume
    ((KC.VOLD, KC.VOLU, KC.MUTE),),      # Layer 1 - Volume
    ((KC.VOLD, KC.VOLU, KC.MUTE),),      # Layer 2 - Volume
    ((KC.VOLD, KC.VOLU, KC.MUTE),),      # Layer 3 - Volume
    ((KC.MW_DN, KC.MW_UP, KC.MB_MMB),),  # Layer 4 - Scroll (reversed for natural feel)
]

# ========================================
# DISPLAY CONFIGURATION
# SSD1306 OLED (128x32)
# Shows title and current layer with visual indicator
# ========================================
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
                
        TextEntry(text='Layer 0 Numpad',   x=0, y=16, layer=0),
        TextEntry(text='Layer 1 Shortcut', x=0, y=16, layer=1),
        TextEntry(text='Layer 2 Function', x=0, y=16, layer=2),
        TextEntry(text='Layer 3 Navigate', x=0, y=16, layer=3),
        TextEntry(text='Layer 4 Mouse',    x=0, y=16, layer=4),
    ],
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
