from pynput import keyboard


def on_press(key):
    try:
        print('\n alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
i = 0
while True:
    pass
