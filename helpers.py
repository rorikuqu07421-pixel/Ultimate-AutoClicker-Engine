import time
import random


def sleep_random(min_seconds, max_seconds):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
    return delay


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def click_position(x, y):
    import pyautogui
    pyautogui.click(x, y)


def is_hotkey_pressed(hotkey):
    from pynput import keyboard
    pressed = set()

    def on_press(key):
        try:
            pressed.add(key.char)
        except AttributeError:
            pressed.add(key)

    def on_release(key):
        pressed.discard(key)
        if all(k in pressed for k in hotkey):
            return False
        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    return True


def random_click(min_x, max_x, min_y, max_y):
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)
    click_position(x, y)