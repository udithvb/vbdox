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


tap_time = 150

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
        XXXX,KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.R, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.T, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time = tap_time), KC.G, XXXX,                             XXXX,KC.M, KC.HT(KC.N, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.E, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.I, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.HT(KC.O, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time),XXXX,
        XXXX,KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=tap_time), KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.C, KC.HT(KC.D, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.V,             KC.K, KC.HT(KC.H, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.COMM, KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time), KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=tap_time), XXXX,
        XXXX,XXXX,XXXX,XXXX,KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time),      KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=tap_time),XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,      XXXX,XXXX,
        KC.LT(3, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time), KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=tap_time),XXXX,                     XXXX,KC.LT(4, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=tap_time), KC.LT(2, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time),
        XXXX,                           XXXX,
        ],
    #LAYER_TEMPLATE
    
       [
             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,                  XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                            XXXX,XXXX,XXXX,XXXX,XXXX,
                                 XXXX,XXXX,        XXXX,XXXX,
                            XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,
                                      XXXX,        XXXX
        
        ],
    #NUMBER
    [
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,     XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,     XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.LBRC,KC.N7,KC.N8,KC.N9,KC.RBRC,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.QUOT,KC.N4,KC.N5,KC.N6,KC.EQL,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.GRV,KC.N1,KC.N2,KC.N3,KC.BSLS,             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                  XXXX,XXXX,XXXX,XXXX,XXXX,
                       XXXX,XXXX,                  XXXX,XXXX,
                  KC.N0,KC.MINUS,XXXX,                 XXXX,XXXX,XXXX,
                            XXXX,                  XXXX
        
        ],
       
       #NAV
    
       [
             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,                  KC.HOME,KC.PGDOWN,KC.PGUP,KC.END,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                            XXXX,XXXX,XXXX,XXXX,XXXX,
                                 XXXX,XXXX,        XXXX,XXXX,
                            XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,
                                      XXXX,        XXXX
        
        ],
        #SYMBOL
    
       [
             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.LCBR,KC.AMPR,KC.ASTR,KC.RPRN,KC.RCBR,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.DQT,KC.DLR,KC.PERC,KC.CIRC,KC.PLUS,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,KC.TILD,KC.EXLM,KC.AT,KC.HASH,KC.PIPE,                  XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,KC.LPRN,                            XXXX,XXXX,XXXX,XXXX,XXXX,
                                 XXXX,XXXX,        XXXX,XXXX,
                            KC.RPRN,KC.UNDS,XXXX,        XXXX,XXXX,XXXX,
                                      XXXX,        XXXX
        
        ],
     #MOUSE
    
       [
             XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,        XXXX,KC.MS_LT,KC.MS_DN,KC.MS_UP,KC.MS_RT,XXXX,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,XXXX,                  KC.MW_LT,KC.MW_DN,KC.MW_UP,KC.MW_RT,XXXX1,XXXX,
        XXXX,XXXX,XXXX,XXXX,XXXX,                            XXXX,XXXX,XXXX,XXXX,XXXX,
                                 XXXX,XXXX,        XXXX,XXXX,
                            XXXX,XXXX,XXXX,        KC.MB_RMB,KC.MB_LMB,KC.MB_MMB,
                                      XXXX,        XXXX
        
        ],

  
    
    ]

layer_names_list = [
"Base", "LayerTemplate", "Number","Nav","Symbol","Mouse",
]

if __name__ == '__main__':
    keyboard.go()

