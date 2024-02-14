print("started")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide


keyboard = KMKKeyboard()

from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.holdtap import HoldTap; keyboard.modules.append(HoldTap())
from kmk.modules.mouse_keys import MouseKeys; keyboard.modules.append(MouseKeys())
from kmk.modules.power import Power; keyboard.modules.append(Power())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.extensions.media_keys import MediaKeys; keyboard.extensions.append(MediaKeys())
from kmk.modules.capsword import CapsWord; keyboard.modules.append(CapsWord())




keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7)
keyboard.row_pins = (board.GP29,board.GP28,board.GP27,board.GP26,board.GP15,board.GP14)

keyboard.diode_orientation = DiodeOrientation.ROW2COL
keyboard.debug_enabled = True
keyboard.tap_time = True


split = Split(data_pin=board.GP11, data_pin2=board.GP12, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

XXXX = KC.NO
____ = KC.TRNS

keyboard.coord_mapping = [
         5,  1,  0,  2,  3,  4,       52, 51, 50, 48, 49, 53,
    13, 14,  9,  8, 10, 11, 12,       60, 59, 58, 56, 57, 62, 61,
    22, 21, 17, 16, 18, 19, 20,       68, 67, 66, 64, 65, 69, 70,
    29, 28, 25, 24, 26, 27, 30,       78, 75, 74, 72, 73, 76, 77,
    36, 35, 32, 31, 33, 34,               82, 81, 79, 80, 83, 84,
    40, 41, 38, 37, 39,                       87, 85, 86, 89, 88,
                        42, 43,       91, 90,
                    44, 45, 46,       94, 93, 92,
                            47,       95,
    ]




keyboard.keymap = [
    
    #BASE
    [
                  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5, KC.F6,             KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,
        KC.TILDE,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.N6,      KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE,
        XXXX,KC.Q, KC.W, KC.F, KC.P, KC.B,XXXX,                             XXXX, KC.J, KC.L, KC.U, KC.Y, KC.SCLN, XXXX,
        XXXX,KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.R, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.T, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.G, XXXX,                             XXXX,KC.M, KC.HT(KC.N, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.E, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.I, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.HT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=200),XXXX,
        XXXX,KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.C, KC.HT(KC.D, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.V,             KC.K, KC.HT(KC.H, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=200), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=200), XXXX,
        XXXX,XXXX,XXXX,XXXX,KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),      KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,      XXXX,XXXX,
        KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),XXXX,                     XXXX,KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.LT(2, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
        XXXX,                           XXXX,
        ],
    #LAYER_TEMPLATE
    
       [
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                  XXXX,XXXX,XXXX,XXXX,XXXX,
                  XXXX,XXXX,                       XXXX,XXXX,
                  XXXX,XXXX,XXXX,                  XXXX,XXXX,XXXX,
                            XXXX,                  XXXX
        
        ],
    #NUMBER
    [
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,     XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,     XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.LBRC,KC.N7,KC.N8,KC.N9,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.QUOT,KC.N4,KC.N5,KC.N6,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.GRV,KC.N1,KC.N2,KC.N3,XXXX,             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                  XXXX,XXXX,XXXX,XXXX,XXXX,
                       XXXX,XXXX,                  XXXX,XXXX,
                  KC.N0,XXXX,XXXX,                  XXXX,XXXX,XXXX,
                            XXXX,                  XXXX
        
        ]
    
    ]

layer_names_list = [
"Base", "LayerTemplate", "Number",
]

if __name__ == '__main__':
    keyboard.go()
