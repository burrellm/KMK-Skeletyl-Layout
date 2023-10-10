import board
from kb import KMKKeyboard
from storage import getmount
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.lock_status import LockStatus
from kmk.modules.modtap import ModTap
from kmk.modules.holdtap import HoldTap
from kmk.modules.holdtap import HoldTapRepeat
from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()

layers = Layers()
locks = LockStatus()
modtap = ModTap()
holdtap = HoldTap()
holdtap.tap_time = 200

split = Split(
    #split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    use_pio=True,  # allows for UART to be used with PIO    
)
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=18, hue_default=135, sat_default=255, val_default=255)
keyboard.extensions.append(rgb)

# rgb
class RgbLayers(Layers):
    last_top_layer = 0
    hues = [135, 224, 64, 0, 165, 96, 100, 192, 32]
    wasdglow = [7, 5, 6, 11]
    numpadglow = [5,6,11,4,7,10,3,8,9]
    thumbglow = [15, 16, 17]
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.disable_auto_write=True
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)

            # if self.last_top_layer in [2, 3, 4, 5, 6] and side == SplitSide.LEFT:
            #     for i in self.wasdglow:
            #         rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)

            # if self.last_top_layer in [3, 4, 5] and side == SplitSide.RIGHT:
            #     for i in self.numpadglow:
            #         rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)

            # if locks.get_caps_lock():
            #     for i in self.thumbglow:
            #         rgb.set_hsv(self.hues[self.last_top_layer + 1], 255, 255, i)
            rgb.show()
#rgb

keyboard.modules = [layers, split, locks, modtap, holdtap, RgbLayers()]

keyboard.debug_enabled = True

#key shortcuts
#thumbs
TB_ESC = KC.LT(5, KC.ESC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
TB_SPC = KC.LT(3, KC.SPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
TB_TAB = KC.LT(4, KC.TAB, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
TB_ENT = KC.LT(4, KC.ENT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
TB_BSPC = KC.LT(3, KC.BSPC, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
TB_DEL = KC.LT(5, KC.DEL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)

#qwerty homes
HQ_A = KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_S = KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_D = KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_F = KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_J = KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_K = KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_L = KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HQ_SCLN = KC.HT(KC.SCLN, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)

#strdy homes
HS_S = KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_T = KC.HT(KC.T, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_R = KC.HT(KC.R, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_D = KC.HT(KC.D, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_N = KC.HT(KC.N, KC.LSFT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_A = KC.HT(KC.A, KC.LCTL, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_E = KC.HT(KC.E, KC.LALT, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
HS_I = KC.HT(KC.I, KC.LGUI, prefer_hold=False, tap_interrupted=True, repeat=HoldTapRepeat.TAP)
#key shortcuts

keyboard.keymap = [
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.A,     KC.A,     KC.A,     KC.A,     KC.A,           KC.A,     KC.A,     KC.A,     KC.A,     KC.A,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ],
    [  # QWERTY
        KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,           KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        HQ_A,     HQ_S,     HQ_D,     HQ_F,     KC.G,           KC.H,     HQ_J,     HQ_K,     HQ_L,     HQ_SCLN,
        KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,           KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
                            TB_ESC,  TB_SPC,  TB_TAB,           TB_ENT,  TB_BSPC,  TB_DEL
    ]
]

if __name__ == '__main__':
    keyboard.go()