import pyautogui
import time

# Pause for a few seconds to give you time to switch to the monkeytype
time.sleep(5)

# The text you want to type
text = "use lead hand develop without present have since right also"

# Type the text with no interval between each character for maximum speed
pyautogui.typewrite(text, interval=0.02) ## this speend around 577