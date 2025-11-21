# magical paperclip's developer hackpad
# professional productivity tool for enhanced coding workflow
# custom firmware optimized for development tasks

# you import all the ios of your board
import board

# these are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# this is the main instance of your keyboard
keyboard = KMKKeyboard()

# add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# magical paperclip's pin configuration
# professional 4-key layout for development productivity
PINS = [board.D3, board.D4, board.D2, board.D1]

# tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# magical paperclip's developer macro suite
# key layout for optimal workflow:
# [copy]   [paste]
# [delete] [debug]

# core developer macros
COPY_MACRO = KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL))
PASTE_MACRO = KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)) 
DEBUG_MACRO = KC.F5  # f5 for refresh/dev tools
SMART_DELETE = KC.Macro(Press(KC.LCTRL), Tap(KC.BSPC), Release(KC.LCTRL))  # delete whole word

# professional greeting macro
SIGNATURE_MACRO = KC.Macro("magical paperclip - professional developer tools")

# magical paperclip's hackpad configuration
# pin mapping: d3=copy, d4=paste, d2=smart delete, d1=debug tools
keyboard.keymap = [
    [
        COPY_MACRO,        # pin d3 - copy selected text/code
        PASTE_MACRO,       # pin d4 - paste clipboard content
        SMART_DELETE,      # pin d2 - delete whole word (ctrl+backspace)
        DEBUG_MACRO,       # pin d1 - f5 for refresh/dev tools
    ]
]

# initialize magical paperclip's developer hackpad
if __name__ == '__main__':
    keyboard.go()
