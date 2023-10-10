import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP27,board.GP28,board.GP21,board.GP06,board.GP07,board.GP08)
    row_pins = (board.GP29,board.GP26,board.GP05,board.GP04,board.GP09)
    diode_orientation = DiodeOrientation.ROW2COL
    #rx = board.RX
    #tx = board.TX
    data_pin = board.RX
    rgb_pixel_pin = board.TX
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA
    coord_mapping = [
      7,  8,  9, 10, 11,    41, 40, 39, 38, 37,
     13, 14, 15, 16, 17,    47, 46, 45, 44, 43,
     19, 20, 21, 22, 23,    53, 52, 51, 50, 49,
             27, 28, 25,    55, 58, 57
    ]
    led_key_pos = [
      2,  3,  8,  9, 12,
      1,  4,  7, 10, 13,
      0,  5,  6, 11, 14,
             15, 16, 17,
    ]   