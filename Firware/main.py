import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

keyboard = KMKKeyboard()

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D4)
keyboard.row_pins = (board.D0,board.D1,board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define what each key does
keyboard.keymap = [
    [KC.MFFD, KC.MPLY, KC.MRWD],
]





encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]
encoder_handler.pins = (
    (board.D3,board.D7,board.D6)
)
encoder_handler.map = [ ((KC.AUDIO_VOL_UP, KC.AUDION_VOL_DOWN, KC.MUTE),), ]


if __name__ == "__main__":
    keyboard.go()
    